"""Analytics builder: merges ESPN game logs, Basketball Reference metrics, schedule rest/travel, and statistical floors."""

from datetime import date, datetime, timedelta
import json
import os
import statistics

from src.bref_parser import TEAM_NAME_TO_STD, norm_pname, norm_team, parse_bref_table

PTS_THRESH = [10, 15, 20, 25, 30, 35]
AST_THRESH = [3, 5, 7, 8, 10, 12]
REB_THRESH = [5, 7, 8, 10, 12, 15]


def _clean_team_name(raw_name: str) -> str:
    return raw_name.replace("*", "").strip()


def build_master_analytics(
    target_date: str,
    data_dir: str,
    bref_end_year: int = 2027,
) -> str:
    """Build `master_analytics_<date>.json` with Last-10, Last-5, Season, and Prior-Season splits."""
    cache_path = os.path.join(data_dir, f"nba_data_cache_{target_date}.json")
    if not os.path.exists(cache_path):
        legacy_cache = os.path.join(data_dir, "nba_data_cache.json")
        if os.path.exists(legacy_cache):
            cache_path = legacy_cache
        else:
            raise FileNotFoundError(f"Cache file not found: {cache_path}")

    with open(cache_path, "r", encoding="utf-8") as f:
        cache = json.load(f)

    all_sched = cache["all_schedule_games"]
    players = cache["player_appearances"]
    today_details = cache["today_details"]
    espn_inj = cache.get("espn_injuries") or {}

    target_dt = datetime.strptime(target_date, "%Y-%m-%d").date()
    target_key = target_dt.strftime("%Y%m%d")
    prev_key = (target_dt - timedelta(days=1)).strftime("%Y%m%d")

    # 1. Parse Basketball Reference team & player tables
    bref_main = os.path.join(data_dir, f"NBA_{bref_end_year}.html")
    bref_adv_path = os.path.join(data_dir, f"NBA_{bref_end_year}_advanced.html")
    bref_prior_path = os.path.join(data_dir, f"NBA_{bref_end_year - 1}_per_game.html")

    adv_team_rows = parse_bref_table(bref_main, "advanced-team") if os.path.exists(bref_main) else []
    pg_team_rows = parse_bref_table(bref_main, "per_game-team") if os.path.exists(bref_main) else []
    pg_opp_rows = parse_bref_table(bref_main, "per_game-opponent") if os.path.exists(bref_main) else []
    sh_opp_rows = parse_bref_table(bref_main, "shooting-opponent") if os.path.exists(bref_main) else []
    adv_player_rows = parse_bref_table(bref_adv_path, "advanced") if os.path.exists(bref_adv_path) else []
    pg_prior_rows = parse_bref_table(bref_prior_path, "per_game_stats") if os.path.exists(bref_prior_path) else []

    team_bref: dict[str, dict] = {}
    for rows, key in [
        (adv_team_rows, "adv"),
        (pg_team_rows, "team_pg"),
        (pg_opp_rows, "opp_pg"),
        (sh_opp_rows, "opp_sh"),
    ]:
        for r in rows:
            tn = _clean_team_name(r.get("team", ""))
            if tn in TEAM_NAME_TO_STD:
                team_bref.setdefault(TEAM_NAME_TO_STD[tn], {})[key] = r

    bref_adv_p: dict[str, dict] = {}
    for r in adv_player_rows:
        nm = norm_pname(r.get("name_display", ""))
        tm = r.get("team_name_abbr", "")
        if nm and (nm not in bref_adv_p or tm in ("2TM", "3TM")):
            bref_adv_p[nm] = r

    bref_prior_p: dict[str, dict] = {}
    for r in pg_prior_rows:
        nm = norm_pname(r.get("name_display", ""))
        tm = r.get("team_name_abbr", "")
        if nm and (nm not in bref_prior_p or tm in ("2TM", "3TM")):
            bref_prior_p[nm] = r

    # 2. Load optional official PDF injury overrides + ESPN live injury statuses
    override_path = os.path.join(data_dir, f"injury_overrides_{target_date}.json")
    official_overrides: dict[str, dict[str, list[str]]] = {}
    if os.path.exists(override_path):
        with open(override_path, "r", encoding="utf-8") as f:
            official_overrides = json.load(f)

    espn_inj_by_team: dict[str, dict[str, tuple[str, str]]] = {}
    if "injuries" in espn_inj:
        for tb in espn_inj["injuries"]:
            t_std = TEAM_NAME_TO_STD.get(tb.get("displayName", ""), "")
            if t_std:
                espn_inj_by_team[t_std] = {}
                for item in tb.get("injuries", []):
                    pn = item.get("athlete", {}).get("displayName", "")
                    st = item.get("status", "")
                    tp = f"{item.get('details', {}).get('side', '')} {item.get('details', {}).get('type', '')}".strip()
                    espn_inj_by_team[t_std][pn] = (st, tp)

    merged_injuries: dict[str, dict[str, list[str]]] = {}
    for t_std in TEAM_NAME_TO_STD.values():
        if t_std in official_overrides:
            merged_injuries[t_std] = official_overrides[t_std]
        else:
            merged_injuries[t_std] = {
                k: [v[0], v[1]] for k, v in espn_inj_by_team.get(t_std, {}).items()
            }

    def get_player_status(team_std: str, pname: str) -> str:
        npn = norm_pname(pname)
        for k, v in merged_injuries.get(team_std, {}).items():
            if norm_pname(k) == npn:
                return f"{v[0]} ({v[1]})" if v[1] else v[0]
        return "Available"

    # 3. Compute team schedule context, rest days, B2B/3-in-4/4-in-6 flags, and home/away splits
    team_sched_all: dict[str, list[dict]] = {t: [] for t in TEAM_NAME_TO_STD.values()}
    for g in sorted(all_sched, key=lambda x: x["utc_iso"]):
        h = norm_team(g["home_abbr"])
        a = norm_team(g["away_abbr"])
        if h in team_sched_all:
            team_sched_all[h].append(
                {**g, "team_ha": "H", "opp_std": a, "team_pts": g["home_score"], "opp_pts": g["away_score"]}
            )
        if a in team_sched_all:
            team_sched_all[a].append(
                {**g, "team_ha": "A", "opp_std": h, "team_pts": g["away_score"], "opp_pts": g["home_score"]}
            )

    team_splits_summary: dict[str, dict] = {}
    for t, glist in team_sched_all.items():
        comp = [g for g in glist if g["completed"] and g["espn_date_key"] <= prev_key]
        h_games = [g for g in comp if g["team_ha"] == "H"]
        a_games = [g for g in comp if g["team_ha"] == "A"]
        hw = sum(1 for g in h_games if g["team_pts"] > g["opp_pts"])
        hl = len(h_games) - hw
        aw = sum(1 for g in a_games if g["team_pts"] > g["opp_pts"])
        al = len(a_games) - aw
        l5 = comp[-5:]
        l5w = sum(1 for g in l5 if g["team_pts"] > g["opp_pts"])

        h_ppg = sum(g["team_pts"] for g in h_games) / len(h_games) if h_games else 0.0
        h_oppg = sum(g["opp_pts"] for g in h_games) / len(h_games) if h_games else 0.0
        a_ppg = sum(g["team_pts"] for g in a_games) / len(a_games) if a_games else 0.0
        a_oppg = sum(g["opp_pts"] for g in a_games) / len(a_games) if a_games else 0.0

        slate_list = [g for g in glist if g["espn_date_key"] == target_key]
        rest_info: dict = {}
        if slate_list and comp:
            ng = slate_list[0]
            ng_date = date.fromisoformat(ng["et_date"])
            prev_g = comp[-1]
            prev_date = date.fromisoformat(prev_g["et_date"])
            rest_days = (ng_date - prev_date).days - 1
            g_in_prev3 = sum(1 for g in comp if 1 <= (ng_date - date.fromisoformat(g["et_date"])).days <= 3)
            g_in_prev5 = sum(1 for g in comp if 1 <= (ng_date - date.fromisoformat(g["et_date"])).days <= 5)

            consec_away = 0
            for g in reversed(comp):
                if g["team_ha"] == "A":
                    consec_away += 1
                else:
                    break
            consec_home = 0
            for g in reversed(comp):
                if g["team_ha"] == "H":
                    consec_home += 1
                else:
                    break

            future = [g for g in glist if g["espn_date_key"] > target_key]
            next_g = future[0] if future else None
            next_b2b = bool(next_g and (date.fromisoformat(next_g["et_date"]) - ng_date).days == 1)

            rest_info = {
                "rest_days": rest_days,
                "is_b2b_second": rest_days == 0,
                "is_3in4": g_in_prev3 >= 2,
                "is_4in6": g_in_prev5 >= 3,
                "prev_game": (
                    f"{prev_g['et_date']} ({'vs' if prev_g['team_ha'] == 'H' else '@'} {prev_g['opp_std']} "
                    f"in {prev_g['city']}, {'W' if prev_g['team_pts'] > prev_g['opp_pts'] else 'L'} "
                    f"{prev_g['team_pts']}-{prev_g['opp_pts']})"
                ),
                "tonight_city": f"{ng['city']}, {ng['state']} ({ng['venue_name']})",
                "consec_away_prior": consec_away,
                "consec_home_prior": consec_home,
                "next_game": (
                    f"{next_g['et_date']} ({'vs' if next_g['team_ha'] == 'H' else '@'} {next_g['opp_std']} in {next_g['city']})"
                    if next_g
                    else "None in window"
                ),
                "front_end_b2b": next_b2b,
            }

        team_splits_summary[t] = {
            "gp": len(comp),
            "w": hw + aw,
            "l": hl + al,
            "l5": f"{l5w}-{len(l5) - l5w}",
            "home_rec": f"{hw}-{hl}",
            "away_rec": f"{aw}-{al}",
            "home_ppg": round(h_ppg, 1),
            "home_oppg": round(h_oppg, 1),
            "away_ppg": round(a_ppg, 1),
            "away_oppg": round(a_oppg, 1),
            "l5_opp_ppg": round(sum(g["opp_pts"] for g in l5) / len(l5), 1) if l5 else 0.0,
            "l5_ppg": round(sum(g["team_pts"] for g in l5) / len(l5), 1) if l5 else 0.0,
            "recent_scores": [
                f"{g['et_date'][5:]} {'vs' if g['team_ha'] == 'H' else '@'}{g['opp_std']} "
                f"{'W' if g['team_pts'] > g['opp_pts'] else 'L'}{g['team_pts']}-{g['opp_pts']}"
                for g in comp[-5:]
            ],
            "rest_info": rest_info,
        }

    # 4. Player-level statistical floor & Last-10 / Last-5 / Season engine
    def analyze_player(aid: str, team_std: str) -> dict | None:
        p = players[aid]
        g_season = [x for x in p["games"] if norm_team(x["team"]) == team_std]
        dnps_curr = [d for d in p["dnps"] if norm_team(d["team"]) == team_std]
        if not g_season:
            return None

        # Use most recent 10 actual appearances for Last-10 window (or full N if N < 10)
        g_l10 = g_season[-10:]
        n10 = len(g_l10)
        n_season = len(g_season)
        l5 = g_l10[-5:]
        n5 = len(l5)

        def stat_summary(arr: list[float | int]) -> dict:
            return {
                "mean": round(sum(arr) / len(arr), 1),
                "median": round(statistics.median(arr), 1),
                "min": round(min(arr), 1),
                "max": round(max(arr), 1),
                "sd": round(statistics.pstdev(arr), 2) if len(arr) > 1 else 0.0,
            }

        pts_l10 = [g["pts"] for g in g_l10]
        ast_l10 = [g["ast"] for g in g_l10]
        reb_l10 = [g["reb"] for g in g_l10]
        min_l10 = [g["min"] for g in g_l10]

        def thresh_hits(arr: list[int], thresholds: list[int]) -> dict:
            out = {}
            tot = len(arr)
            for th in thresholds:
                c = sum(1 for v in arr if v >= th)
                out[str(th)] = {"hits": c, "total": tot, "pct": round(100.0 * c / tot, 1)}
            f80 = max([th for th in thresholds if out[str(th)]["pct"] >= 80.0], default=None)
            f90 = max(
                [th for th in thresholds if out[str(th)]["pct"] >= 87.5 and out[str(th)]["hits"] >= max(1, tot - 1)],
                default=None,
            )
            f100 = max([th for th in thresholds if out[str(th)]["hits"] == tot], default=None)
            return {"map": out, "f80": f80, "f90": f90, "f100": f100}

        close_m = [g["min"] for g in g_l10 if abs(g["margin"]) <= 12]
        blow_m = [g["min"] for g in g_l10 if abs(g["margin"]) >= 15]
        home_pts = [g["pts"] for g in g_l10 if g["home_away"] == "H"]
        away_pts = [g["pts"] for g in g_l10 if g["home_away"] == "A"]

        nm = norm_pname(p["name"])
        adv = bref_adv_p.get(nm, {})
        prior = bref_prior_p.get(nm, {})

        return {
            "id": aid,
            "name": p["name"],
            "pos": p["pos"],
            "team": team_std,
            "status": get_player_status(team_std, p["name"]),
            "gp": n10,
            "season_gp": n_season,
            "team_gp": team_splits_summary[team_std]["gp"],
            "starts": sum(1 for g in g_l10 if g["starter"]),
            "dnps": dnps_curr,
            "pts": stat_summary(pts_l10),
            "ast": stat_summary(ast_l10),
            "reb": stat_summary(reb_l10),
            "min": stat_summary(min_l10),
            "season_pts": round(sum(g["pts"] for g in g_season) / n_season, 1),
            "season_ast": round(sum(g["ast"] for g in g_season) / n_season, 1),
            "season_reb": round(sum(g["reb"] for g in g_season) / n_season, 1),
            "season_min": round(sum(g["min"] for g in g_season) / n_season, 1),
            "l5_pts": round(sum(g["pts"] for g in l5) / n5, 1),
            "l5_ast": round(sum(g["ast"] for g in l5) / n5, 1),
            "l5_reb": round(sum(g["reb"] for g in l5) / n5, 1),
            "l5_min": round(sum(g["min"] for g in l5) / n5, 1),
            "min_30plus": sum(1 for m in min_l10 if m >= 30.0),
            "min_35plus": sum(1 for m in min_l10 if m >= 35.0),
            "close_min": round(sum(close_m) / len(close_m), 1) if close_m else None,
            "blowout_min": round(sum(blow_m) / len(blow_m), 1) if blow_m else None,
            "home_ppg": round(sum(home_pts) / len(home_pts), 1) if home_pts else None,
            "away_ppg": round(sum(away_pts) / len(away_pts), 1) if away_pts else None,
            "fga": round(sum(g["fga"] for g in g_l10) / n10, 1),
            "fgm": round(sum(g["fgm"] for g in g_l10) / n10, 1),
            "tpa": round(sum(g["tpa"] for g in g_l10) / n10, 1),
            "tpm": round(sum(g["tpm"] for g in g_l10) / n10, 1),
            "fta": round(sum(g["fta"] for g in g_l10) / n10, 1),
            "ftm": round(sum(g["ftm"] for g in g_l10) / n10, 1),
            "oreb": round(sum(g["oreb"] for g in g_l10) / n10, 1),
            "dreb": round(sum(g["dreb"] for g in g_l10) / n10, 1),
            "tov": round(sum(g["tov"] for g in g_l10) / n10, 1),
            "pf": round(sum(g["pf"] for g in g_l10) / n10, 1),
            "pts_th": thresh_hits(pts_l10, PTS_THRESH),
            "ast_th": thresh_hits(ast_l10, AST_THRESH),
            "reb_th": thresh_hits(reb_l10, REB_THRESH),
            "l5_pts_th": thresh_hits([g["pts"] for g in l5], PTS_THRESH),
            "l5_ast_th": thresh_hits([g["ast"] for g in l5], AST_THRESH),
            "l5_reb_th": thresh_hits([g["reb"] for g in l5], REB_THRESH),
            "bref_adv": {
                "usg_pct": adv.get("usg_pct", ""),
                "ts_pct": adv.get("ts_pct", ""),
                "ast_pct": adv.get("ast_pct", ""),
                "orb_pct": adv.get("orb_pct", ""),
                "drb_pct": adv.get("drb_pct", ""),
                "trb_pct": adv.get("trb_pct", ""),
                "tov_pct": adv.get("tov_pct", ""),
                "bpm": adv.get("bpm", ""),
            },
            "prior_season": (
                {
                    "gp": prior.get("games", "0"),
                    "mpg": prior.get("mp_per_g", "-"),
                    "ppg": prior.get("pts_per_g", "-"),
                    "apg": prior.get("ast_per_g", "-"),
                    "rpg": prior.get("trb_per_g", "-"),
                    "team": prior.get("team_name_abbr", "-"),
                }
                if prior
                else None
            ),
            "games": g_l10,
        }

    all_analyzed_by_team: dict[str, list[dict]] = {t: [] for t in TEAM_NAME_TO_STD.values()}
    for aid, p in players.items():
        t_std = norm_team(p["latest_team"])
        if t_std in all_analyzed_by_team:
            res = analyze_player(aid, t_std)
            if res:
                all_analyzed_by_team[t_std].append(res)

    out_path = os.path.join(data_dir, f"master_analytics_{target_date}.json")
    full_export = {
        "target_date": target_date,
        "team_bref": team_bref,
        "team_splits": team_splits_summary,
        "today_details": today_details,
        "players_by_team": all_analyzed_by_team,
        "merged_injuries": merged_injuries,
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(full_export, f, indent=2)

    print(f"      Built {out_path} across {len(all_analyzed_by_team)} teams.")
    return out_path
