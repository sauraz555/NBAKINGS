"""Review a list of player-prop picks against last-10 game logs, injuries, minutes and blowout risk.

Input:  data/picks_<date>.json   {"owner", "slate_date", "picks": [{player, game, stat, line, label}]}
        stat is one of pts, reb, ast, tpm (threes made), blk, stl.
Output: output/dashboard/sids_picks.json  ({rows, meta} for the dashboard)
        output/<date>_picks_review.md

RULES (applied in order)
  Remove      player is Out/Doubtful/Questionable/Day-To-Day on the latest official report,
              or averages under 18 minutes over the last 10 games,
              or hit the line in under 80% of the last 10 games.
  Borderline  the stat is blocks or steals (high game-to-game swing),
              or the player had a game under 16 minutes in the last 10 (unstable role).
  Keep        everything else.
A hit rate is what happened in past games, not a probability for the next one.

Usage: python -m src.review_picks --date 2026-11-13
"""

import argparse
import json
import os
import statistics

from src.bref_parser import norm_team

STAT_NAMES = {"pts": "points", "reb": "rebounds", "ast": "assists", "tpm": "threes", "blk": "blocks", "stl": "steals"}


def review_picks(target_date: str, data_dir: str, output_dir: str) -> list[dict]:
    with open(os.path.join(data_dir, f"picks_{target_date}.json"), encoding="utf-8") as f:
        spec = json.load(f)
    with open(os.path.join(data_dir, f"nba_data_cache_{target_date}.json"), encoding="utf-8") as f:
        C = json.load(f)
    with open(os.path.join(data_dir, f"predictions_{target_date}.json"), encoding="utf-8") as f:
        P = json.load(f)
    with open(os.path.join(data_dir, f"master_analytics_{target_date}.json"), encoding="utf-8") as f:
        M = json.load(f)

    by_name = {p["name"]: p for p in C["player_appearances"].values()}
    proj = {p["player"]: p for p in P["players"]}
    game_by_team = {}
    for g in P["games"]:
        game_by_team[g["home"]] = g
        game_by_team[g["away"]] = g
    status = {n: v[0] for t in M["merged_injuries"].values() for n, v in t.items()}

    rows = []
    for i, pk in enumerate(spec["picks"], 1):
        name, stat, line = pk["player"], pk["stat"], int(pk["line"])
        p = by_name.get(name)
        row = {"pick_id": i, "owner": spec.get("owner", ""), "player": name, "game": pk["game"], "pick": pk["label"],
               "stat": STAT_NAMES.get(stat, stat), "line": line}
        if not p:
            row.update({"verdict": "Remove", "reason": "No game logs found for this player this season."})
            rows.append(row)
            continue
        played = [g for g in p["games"] if g.get("season") == "2026-27" and g["min"] > 0]
        l10 = played[-10:]
        vals = [g.get(stat, 0) for g in l10]
        mins = [g["min"] for g in l10]
        hits = sum(v >= line for v in vals)
        team = norm_team(l10[-1]["team"]) if l10 else ""
        g = game_by_team.get(team, {})
        st = status.get(name, "Available")
        avg_min = statistics.mean(mins) if mins else 0.0
        misses = [f"{x['date'][5:]}: {x.get(stat, 0)} in {x['min']:.0f} min" for x in l10 if x.get(stat, 0) < line]
        pr = proj.get(name, {})
        proj_key = {"pts": "proj_pts", "reb": "proj_reb", "ast": "proj_ast"}.get(stat)

        rate = hits / len(l10) if l10 else 0
        if st.lower() in ("out", "doubtful", "questionable", "day-to-day", "suspension"):
            verdict, reason = "Remove", f"{st} on the official injury report."
        elif avg_min < 18:
            verdict, reason = "Remove", f"Bench role: averages {avg_min:.1f} minutes."
        elif rate < 0.8:
            verdict, reason = "Remove", f"Hit in only {hits} of {len(l10)} recent games."
        elif stat in ("blk", "stl"):
            verdict, reason = "Borderline", f"{STAT_NAMES[stat].capitalize()} swing a lot from game to game."
        elif min(mins) < 16:
            verdict, reason = "Borderline", f"Minutes are unstable ({min(mins):.0f} to {max(mins):.0f})."
        else:
            verdict, reason = "Keep", "Steady minutes and a strong recent hit rate."
        starter = sum(1 for x in l10 if x.get("starter")) >= len(l10) / 2
        if verdict != "Remove" and starter and g.get("blowout") in ("Elevated", "Moderate") and min(mins) < 20:
            reason += f" {g['blowout']} blowout risk could cut late minutes."
        if misses and verdict != "Remove":
            reason += " Misses: " + "; ".join(misses) + "."

        row.update({
            "team": team, "opp": (g.get("home") if g.get("away") == team else g.get("away")) or "",
            "syd_time": g.get("syd_time", ""), "game_id": g.get("game_id", ""),
            "status": st, "l10_hits": hits, "l10_games": len(l10),
            "l10_hit_pct": round(100 * rate, 1),
            "l10_low": min(vals) if vals else None, "l10_avg": round(statistics.mean(vals), 1) if vals else None,
            "l10_values": ", ".join(str(v) for v in vals),
            "season_hits": sum(x.get(stat, 0) >= line for x in played), "season_games": len(played),
            "min_low": round(min(mins)), "min_high": round(max(mins)), "min_avg": round(avg_min, 1),
            "projection": pr.get(proj_key) if proj_key else None,
            "blowout": g.get("blowout", ""),
            "verdict": verdict, "reason": reason,
        })
        rows.append(row)

    _write(rows, spec, C, output_dir, target_date)
    return rows


def _write(rows, spec, C, output_dir, target_date):
    os.makedirs(os.path.join(output_dir, "dashboard"), exist_ok=True)
    with open(os.path.abspath(__file__), encoding="utf-8") as f:
        code = f.read()
    meta = [
        {"label": "review_picks.py", "value": code, "type": "code", "lang": "python"},
        {"label": "Input", "value": f"picks_{target_date}.json ({len(rows)} picks), ESPN game logs fetched {C.get('fetched_at_utc')}, "
                                     "Official NBA injury report"},
    ]
    with open(os.path.join(output_dir, "dashboard", "sids_picks.json"), "w", encoding="utf-8") as f:
        json.dump({"rows": rows, "meta": meta}, f, separators=(",", ":"))

    lines = [f"# {spec.get('owner', '')}'s picks — {target_date} (US ET) slate\n",
             "| Verdict | Player | Pick | L10 hits | L10 low | Min range | Status | Reason |", "|---|---|---|---|---|---|---|---|"]
    order = {"Remove": 0, "Borderline": 1, "Keep": 2}
    for r in sorted(rows, key=lambda r: (order[r["verdict"]], r["pick_id"])):
        lines.append(f"| {r['verdict']} | {r['player']} | {r['pick']} | {r.get('l10_hits', '-')}/{r.get('l10_games', '-')} | "
                     f"{r.get('l10_low', '-')} | {r.get('min_low', '-')}-{r.get('min_high', '-')} | {r.get('status', '-')} | {r['reason']} |")
    lines.append("\n" + __doc__.split("RULES", 1)[1].split("Usage:", 1)[0].strip())
    with open(os.path.join(output_dir, f"{target_date}_picks_review.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Review player-prop picks against recent game logs.")
    ap.add_argument("--date", required=True)
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ap.add_argument("--data-dir", default=os.path.join(root, "data"))
    ap.add_argument("--output-dir", default=os.path.join(root, "output"))
    a = ap.parse_args()
    out = review_picks(a.date, a.data_dir, a.output_dir)
    from collections import Counter
    print(Counter(r["verdict"] for r in out))
