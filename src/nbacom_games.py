"""Pull each slate team's last N games from NBA.com game pages (box score + full play-by-play).

NBA.com's game pages embed their data as JSON (__NEXT_DATA__), so a plain HTTPS fetch is enough:
  https://www.nba.com/games?date=YYYY-MM-DD           -> the day's game links
  https://www.nba.com/game/<away>-vs-<home>-<gameId>/play-by-play -> box score + every play
                                                         (shot distance, x/y, assister, subs)

Per player, over the team's last N games, it reports:
  points / rebounds / assists / threes made and attempted, game by game (lowest game shown)
  shot mix: rim (0-4 ft), short (5-14 ft), mid-range (15 ft+ twos), threes
  fourth-quarter share of points, rebounds and assists (who loses output in a blowout)
  who his assists go to, and games missed with the reason NBA.com gives (DNP / injury)
  with/without: his averages in games a key teammate missed vs games that teammate played

Pages are cached under data/nbacom/ and fetched once, about one request a second.
Usage: python -m src.nbacom_games --date 2026-11-27 --games 6
"""

import argparse
import collections
import datetime as dt
import json
import os
import re
import statistics
import time
import unicodedata
import urllib.request

BASE = "https://www.nba.com"
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"}
_NEXT = re.compile(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', re.S)
_GAME_LINK = re.compile(r'/game/([a-z]{3})-vs-([a-z]{3})-(\d{10})')
_AST = re.compile(r"\(([A-Za-z.'\- ]+?) \d+ AST\)")


def _plain(s: str) -> str:
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


def _get(url: str) -> str:
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=40) as r:
                return r.read().decode("utf-8", "replace")
        except Exception:
            if attempt == 2:
                raise
            time.sleep(3 * (attempt + 1))
    return ""


def _page_props(html: str) -> dict:
    m = _NEXT.search(html)
    return json.loads(m.group(1))["props"]["pageProps"] if m else {}


def day_games(date: str, cache: str) -> list[dict]:
    """[{game_id, away, home, slug}] for a US-ET date, cached."""
    path = os.path.join(cache, "days", f"{date}.json")
    if os.path.exists(path) and date < dt.date.today().isoformat():
        with open(path) as f:
            return json.load(f)
    html = _get(f"{BASE}/games?date={date}")
    time.sleep(1)
    seen, out = set(), []
    for away, home, gid in _GAME_LINK.findall(html):
        if gid in seen:
            continue
        seen.add(gid)
        out.append({"game_id": gid, "away": away.upper(), "home": home.upper(), "slug": f"{away}-vs-{home}-{gid}"})
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(out, f)
    return out


def _mins(s: str) -> float:
    if not s:
        return 0.0
    m = re.match(r"(?:PT)?(\d+)[M:](\d+)", s)
    return int(m.group(1)) + int(m.group(2)) / 60 if m else 0.0


def game_detail(slug: str, cache: str) -> dict | None:
    """Compact box score + per-player play-by-play features for one finished game, cached."""
    gid = slug.rsplit("-", 1)[1]
    path = os.path.join(cache, "games", f"{gid}.json")
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    pp = _page_props(_get(f"{BASE}/game/{slug}/play-by-play"))
    time.sleep(1)
    g = pp.get("game") or {}
    if g.get("gameStatus") != 3:  # 3 = final
        return None
    actions = (pp.get("playByPlay") or {}).get("actions", [])

    teams = {}
    for side in ("homeTeam", "awayTeam"):
        t = g[side]
        players = {}
        for p in t.get("players", []):
            s = p.get("statistics", {})
            players[str(p["personId"])] = {
                "name": f"{p['firstName']} {p['familyName']}".strip(), "family": p["familyName"],
                "starter": bool(p.get("position")), "comment": p.get("comment", ""),
                "min": round(_mins(s.get("minutes", "")), 1), "pts": s.get("points", 0),
                "reb": s.get("reboundsTotal", 0), "ast": s.get("assists", 0),
                "tpm": s.get("threePointersMade", 0), "tpa": s.get("threePointersAttempted", 0),
                "fga": s.get("fieldGoalsAttempted", 0), "fta": s.get("freeThrowsAttempted", 0),
                "stl": s.get("steals", 0), "blk": s.get("blocks", 0), "pf": s.get("foulsPersonal", 0),
                "zones": {"rim": 0, "short": 0, "mid": 0, "three": 0},
                "q4": {"pts": 0, "reb": 0, "ast": 0}, "ast_to": {},
            }
        teams[t["teamTricode"]] = {"score": t.get("score"), "players": players}

    for a in actions:
        tri, pid = a.get("teamTricode"), str(a.get("personId"))
        team = teams.get(tri)
        if not team or pid not in team["players"]:
            continue
        pl = team["players"][pid]
        q4 = a.get("period", 0) >= 4
        if a.get("isFieldGoal"):
            d = a.get("shotDistance", 0) or 0
            zone = "three" if a.get("shotValue") == 3 else "rim" if d <= 4 else "short" if d <= 14 else "mid"
            pl["zones"][zone] += 1
            if a.get("shotResult") == "Made":
                if q4:
                    pl["q4"]["pts"] += a.get("shotValue", 2)
                m = _AST.search(a.get("description", ""))
                if m:
                    passer = next((p for p in team["players"].values() if _plain(p["family"]) == _plain(m.group(1))), None)
                    if passer:
                        passer["ast_to"][pl["name"]] = passer["ast_to"].get(pl["name"], 0) + 1
                        if q4:
                            passer["q4"]["ast"] += 1
        elif a.get("actionType") == "Free Throw" and q4 and not a.get("description", "").startswith("MISS"):
            pl["q4"]["pts"] += 1
        elif a.get("actionType") == "Rebound" and q4:
            pl["q4"]["reb"] += 1

    home, away = g["homeTeam"]["teamTricode"], g["awayTeam"]["teamTricode"]
    out = {"game_id": gid, "date": (g.get("gameEt") or "")[:10], "home": home, "away": away,
           "margin": abs((g["homeTeam"].get("score") or 0) - (g["awayTeam"].get("score") or 0)), "teams": teams}
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(out, f, separators=(",", ":"))
    return out


def last_n_games(target_date: str, n: int, cache: str, max_days: int = 30) -> tuple[list[str], dict[str, list[dict]]]:
    """Slate teams for target_date and each one's last n finished games (newest first)."""
    slate = day_games(target_date, cache)
    teams = sorted({t for g in slate for t in (g["home"], g["away"])})
    found = {t: [] for t in teams}
    day = dt.date.fromisoformat(target_date)
    for back in range(1, max_days + 1):
        if all(len(v) >= n for v in found.values()):
            break
        d = (day - dt.timedelta(days=back)).isoformat()
        for gm in day_games(d, cache):
            need = [t for t in (gm["home"], gm["away"]) if t in found and len(found[t]) < n]
            if not need:
                continue
            det = game_detail(gm["slug"], cache)
            if det:
                for t in need:
                    found[t].append(det)
    return teams, found


def player_report(teams: list[str], found: dict[str, list[dict]]) -> list[dict]:
    rows = []
    for t in teams:
        games = found[t]
        roster = collections.OrderedDict()
        for gm in games:
            for pid, p in gm["teams"][t]["players"].items():
                roster.setdefault(pid, p["name"])
        logs = {pid: [(gm, gm["teams"][t]["players"].get(pid)) for gm in games] for pid in roster}
        played = {pid: [(gm, p) for gm, p in lg if p and p["min"] > 0] for pid, lg in logs.items()}
        # Key teammates: averaged 28+ minutes in the games they played.
        keys = [pid for pid, lg in played.items() if lg and statistics.mean(p["min"] for _, p in lg) >= 28]
        for pid, lg in played.items():
            if len(lg) < 2 or statistics.mean(p["min"] for _, p in lg) < 18:
                continue
            ps = [p for _, p in lg]
            tot = {k: sum(p[k] for p in ps) for k in ("pts", "reb", "ast")}
            zones = collections.Counter()
            ast_to = collections.Counter()
            for p in ps:
                zones.update(p["zones"])
                ast_to.update(p["ast_to"])
            fga = sum(zones.values()) or 1
            missed = [f"{gm['date'][5:]}: {(p or {}).get('comment') or 'not on roster / inactive'}" for gm, p in logs[pid] if not p or p["min"] == 0]
            splits = []
            for k in keys:
                if k == pid:
                    continue
                without = [p for gm, p in lg if not (gm["teams"][t]["players"].get(k) or {}).get("min")]
                with_ = [p for gm, p in lg if (gm["teams"][t]["players"].get(k) or {}).get("min")]
                if without and with_:
                    splits.append({"teammate": roster[k], "games_without": len(without),
                                   **{f"{s}_with": round(statistics.mean(p[s] for p in with_), 1) for s in ("pts", "reb", "ast")},
                                   **{f"{s}_without": round(statistics.mean(p[s] for p in without), 1) for s in ("pts", "reb", "ast")}})
            rows.append({
                "team": t, "player": roster[pid], "games": len(ps),
                "min": [p["min"] for p in ps], "pts": [p["pts"] for p in ps], "reb": [p["reb"] for p in ps],
                "ast": [p["ast"] for p in ps], "tpm": [p["tpm"] for p in ps], "tpa": [p["tpa"] for p in ps],
                "dates": [gm["date"][5:] for gm, _ in lg], "margins": [gm["margin"] for gm, _ in lg],
                "shot_mix": {z: round(100 * c / fga) for z, c in zones.items()},
                "q4_share": {k: round(100 * sum(p["q4"][k] for p in ps) / tot[k]) if tot[k] else 0 for k in tot},
                "ast_to": dict(ast_to.most_common(3)), "missed": missed, "with_without": splits,
            })
    return rows


def write_outputs(target_date: str, n: int, rows: list[dict], output_dir: str) -> str:
    os.makedirs(os.path.join(output_dir, "dashboard"), exist_ok=True)
    with open(os.path.join(output_dir, "dashboard", "nbacom_lastn.json"), "w", encoding="utf-8") as f:
        json.dump({"slate": target_date, "games": n, "rows": rows}, f, separators=(",", ":"))

    def avg(v):
        return f"{statistics.mean(v):.1f}" if v else "-"

    lines = [f"# Last {n} games per player (NBA.com box scores and play-by-play) — {target_date} ET slate\n",
             "Values are newest game first. Low = lowest game in the sample. Q4 share = share of the "
             "player's output that came in the fourth quarter (high share = more exposed to blowout benching).\n"]
    for team in sorted({r["team"] for r in rows}):
        lines += [f"\n## {team}\n", "| Player | Min | PTS (low) | REB (low) | AST (low) | 3PM/3PA | Shot mix rim/short/mid/3 | Q4 share P/R/A | Assists go to |",
                  "|---|---|---|---|---|---|---|---|---|"]
        for r in sorted((r for r in rows if r["team"] == team), key=lambda r: -statistics.mean(r["min"])):
            sm, q = r["shot_mix"], r["q4_share"]
            lines.append(
                f"| {r['player']} | {avg(r['min'])} | {avg(r['pts'])} ({min(r['pts'])}) | {avg(r['reb'])} ({min(r['reb'])}) | "
                f"{avg(r['ast'])} ({min(r['ast'])}) | {sum(r['tpm'])}/{sum(r['tpa'])} | "
                f"{sm.get('rim', 0)}/{sm.get('short', 0)}/{sm.get('mid', 0)}/{sm.get('three', 0)}% | "
                f"{q['pts']}/{q['reb']}/{q['ast']}% | {', '.join(f'{k} {v}' for k, v in r['ast_to'].items()) or '-'} |")
        notes = []
        for r in rows:
            if r["team"] != team:
                continue
            if r["missed"]:
                notes.append(f"- {r['player']} missed: {'; '.join(r['missed'])}")
            for s in r["with_without"]:
                big = [k for k in ("pts", "reb", "ast") if abs(s[f"{k}_without"] - s[f"{k}_with"]) >= max(2, 0.25 * s[f"{k}_with"])]
                if big:
                    notes.append(f"- {r['player']} without {s['teammate']} ({s['games_without']} games): " + ", ".join(
                        f"{k} {s[f'{k}_with']} → {s[f'{k}_without']}" for k in big))
        if notes:
            lines += ["", *notes]
    path = os.path.join(output_dir, f"{target_date}_last{n}_nbacom.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return path


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--date", required=True, help="Slate date in US Eastern time, YYYY-MM-DD")
    ap.add_argument("--games", type=int, default=6)
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ap.add_argument("--cache", default=os.path.join(root, "data", "nbacom"))
    ap.add_argument("--output-dir", default=os.path.join(root, "output"))
    a = ap.parse_args()
    teams, found = last_n_games(a.date, a.games, a.cache)
    short = {t: len(v) for t, v in found.items() if len(v) < a.games}
    rows = player_report(teams, found)
    print(f"{len(teams)} teams, {sum(len(v) for v in found.values())} team-games, {len(rows)} players."
          + (f" Short samples: {short}" if short else ""))
    print(write_outputs(a.date, a.games, rows, a.output_dir))
