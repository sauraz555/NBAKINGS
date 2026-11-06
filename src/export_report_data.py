"""Report data exporter: generates structured matchup tables, 30-team key player database, and 10-game logs."""

import json
import os

from src.bref_parser import norm_team


def _ml_to_prob(ml: float | int | str | None) -> float | None:
    if ml is None or ml == "":
        return None
    val = float(ml)
    return (-val) / (-val + 100.0) if val < 0 else 100.0 / (val + 100.0)


def export_report_sections(
    target_date: str,
    data_dir: str,
    output_dir: str,
) -> tuple[str, str]:
    """Export human-readable analytical dumps for Parts A–I into `output_dir`."""
    os.makedirs(output_dir, exist_ok=True)

    master_path = os.path.join(data_dir, f"master_analytics_{target_date}.json")
    cache_path = os.path.join(data_dir, f"nba_data_cache_{target_date}.json")
    if not os.path.exists(cache_path):
        cache_path = os.path.join(data_dir, "nba_data_cache.json")

    with open(master_path, "r", encoding="utf-8") as f:
        M = json.load(f)
    with open(cache_path, "r", encoding="utf-8") as f:
        C = json.load(f)

    team_bref = M["team_bref"]
    team_splits = M["team_splits"]
    today_details = M["today_details"]
    players_by_team = M["players_by_team"]
    merged_inj = M.get("merged_injuries", M.get("official_inj_nov6", {}))

    slate_gids = sorted(today_details.keys(), key=lambda gid: today_details[gid]["meta"]["utc_iso"])
    playing_teams: set[str] = set()
    for gid in slate_gids:
        gm = today_details[gid]["meta"]
        playing_teams.add(norm_team(gm["away_abbr"]))
        playing_teams.add(norm_team(gm["home_abbr"]))

    selected_30: dict[str, dict] = {}
    selected_playing_detailed: dict[str, list[dict]] = {}

    for t in sorted(players_by_team.keys()):
        plist = players_by_team[t]
        est = [p for p in plist if p["gp"] >= 3 and p["min"]["mean"] >= 15.0]
        small_outliers = [
            p for p in plist if (p["gp"] < 3 or p["min"]["mean"] < 15.0) and p["pts"]["mean"] >= 14.0
        ]

        by_pts = sorted(est, key=lambda x: x["season_pts"], reverse=True)
        by_ast = sorted(est, key=lambda x: x["season_ast"], reverse=True)
        by_reb = sorted(est, key=lambda x: x["season_reb"], reverse=True)

        s1 = by_pts[0] if len(by_pts) > 0 else None
        s2 = by_pts[1] if len(by_pts) > 1 else None
        s3 = by_pts[2] if len(by_pts) > 2 else None
        s4 = by_pts[3] if len(by_pts) > 3 else None
        a1 = by_ast[0] if len(by_ast) > 0 else None
        a2 = by_ast[1] if len(by_ast) > 1 else None
        r1 = by_reb[0] if len(by_reb) > 0 else None
        r2 = by_reb[1] if len(by_reb) > 1 else None

        selected_30[t] = {
            "scorers": [x for x in (s1, s2, s3) if x],
            "ast_leaders": [x for x in (a1, a2) if x],
            "reb_leaders": [x for x in (r1, r2) if x],
            "small_outliers": small_outliers,
        }

        if t in playing_teams:
            cand_list: list[dict] = []

            def add_p(px: dict | None, role_tag: str) -> None:
                if not px:
                    return
                for existing in cand_list:
                    if existing["player"]["id"] == px["id"]:
                        if role_tag not in existing["roles"]:
                            existing["roles"].append(role_tag)
                        return
                cand_list.append({"player": px, "roles": [role_tag]})

            add_p(s1, "Primary Scorer #1")
            add_p(s2, "Primary Scorer #2")
            if s1 and ("Out" in s1["status"] or "Questionable" in s1["status"]):
                add_p(s3, "Replacement/Active Scorer")
            if s2 and ("Out" in s2["status"] or "Questionable" in s2["status"]):
                add_p(s3, "Replacement/Active Scorer")
                if s1 and ("Out" in s1["status"] or "Questionable" in s1["status"]):
                    add_p(s4, "Replacement/Active Scorer")

            add_p(a1, "Primary Assist Leader")
            if a1 and ("Out" in a1["status"] or "Questionable" in a1["status"] or a1["min"]["mean"] < 22.0):
                add_p(a2, "Co-Primary/Replacement Playmaker")

            add_p(r1, "Primary Rebound Leader")
            if r1 and ("Out" in r1["status"] or "Questionable" in r1["status"] or r1["min"]["mean"] < 22.0):
                add_p(r2, "Co-Primary/Replacement Rebounder")

            active_cands = [c for c in cand_list if "Out" not in c["player"]["status"]]
            if len(active_cands) < 3 and s3:
                add_p(s3, "Secondary Scoring/Matchup Candidate")

            selected_playing_detailed[t] = cand_list

    # Export 1: Matchups + All 30 Teams Summary
    lines_abef = [f"=== PART A, E & F: {target_date} NBA SLATE MATCHUPS ===\n"]
    for gid in slate_gids:
        td = today_details[gid]
        gm = td["meta"]
        aw = norm_team(gm["away_abbr"])
        hm = norm_team(gm["home_abbr"])
        pc = td["pickcenter"][0] if td["pickcenter"] else {}
        pred = td.get("predictor", {})
        aw_ml = pc.get("awayTeamOdds", {}).get("moneyLine")
        hm_ml = pc.get("homeTeamOdds", {}).get("moneyLine")
        p_aw = _ml_to_prob(aw_ml)
        p_hm = _ml_to_prob(hm_ml)
        vig_str = ""
        if p_aw and p_hm:
            tot_p = p_aw + p_hm
            vig_str = (
                f"Vig-Free Market Win%: {aw} {100 * p_aw / tot_p:.1f}% | "
                f"{hm} {100 * p_hm / tot_p:.1f}% (ML: {aw} {aw_ml} / {hm} {hm_ml})"
            )
        bpi_aw = pred.get("awayTeam", {}).get("gameProjection", "?")
        bpi_hm = pred.get("homeTeam", {}).get("gameProjection", "?")

        lines_abef.append(f"GAME {gid}: {aw} ({gm['away_rec']}) @ {hm} ({gm['home_rec']})")
        lines_abef.append(
            f"  Time: {gm['et_date']} {gm['et_time']} | Sydney: {gm['syd_date']} {gm['syd_time']} | Notes: {gm['notes']}"
        )
        lines_abef.append(f"  Venue: {gm['venue_name']} ({gm['city']}, {gm['state']})")
        lines_abef.append(
            f"  Odds: {pc.get('details', 'N/A')} | O/U: {pc.get('overUnder', 'N/A')} | {vig_str}"
        )
        lines_abef.append(f"  ESPN BPI Predictor: {aw} {bpi_aw}% | {hm} {bpi_hm}%")

        h2h = [
            g
            for g in C["all_schedule_games"]
            if g["completed"] and {norm_team(g["home_abbr"]), norm_team(g["away_abbr"])} == {aw, hm}
        ]
        lines_abef.append(
            f"  Current-Season H2H: {[(g['et_date'], norm_team(g['away_abbr']), g['away_score'], '@', norm_team(g['home_abbr']), g['home_score']) for g in h2h]}"
        )

        for side, tcode in (("AWAY", aw), ("HOME", hm)):
            tb = team_bref.get(tcode, {})
            adv = tb.get("adv", {})
            tpg = tb.get("team_pg", {})
            opg = tb.get("opp_pg", {})
            osh = tb.get("opp_sh", {})
            sp = team_splits[tcode]
            ri = sp.get("rest_info", {})
            lines_abef.append(
                f"  [{side}: {tcode}] W-L: {sp['w']}-{sp['l']} (L5: {sp['l5']}, "
                f"H: {sp['home_rec']} [{sp['home_ppg']}/{sp['home_oppg']}], "
                f"A: {sp['away_rec']} [{sp['away_ppg']}/{sp['away_oppg']}])"
            )
            if adv:
                lines_abef.append(
                    f"    Ratings: ORtg={adv.get('off_rtg')} DRtg={adv.get('def_rtg')} "
                    f"NRtg={adv.get('net_rtg')} Pace={adv.get('pace')} SRS={adv.get('srs')}"
                )
            if opg and tpg:
                missed_fg = float(opg.get("opp_fga", 0)) - float(opg.get("opp_fg", 0))
                lines_abef.append(
                    f"    Defense: OppPTS={opg.get('opp_pts')} (L5={sp['l5_opp_ppg']}) "
                    f"OppAST={opg.get('opp_ast')} OppREB={opg.get('opp_trb')} "
                    f"DRB%={adv.get('drb_pct')} OppMissedFG={missed_fg:.1f} "
                    f"RimFG%={osh.get('opp_fg_pct_00_03')}"
                )
            if ri:
                lines_abef.append(
                    f"    Schedule: RestDays={ri['rest_days']} B2B_2nd={ri['is_b2b_second']} "
                    f"FrontB2B_Tmrw={ri['front_end_b2b']} 3in4={ri['is_3in4']} 4in6={ri['is_4in6']} | "
                    f"Prev={ri['prev_game']} | Next={ri['next_game']}"
                )
            lines_abef.append(f"    Injuries: {merged_inj.get(tcode, {})}")
        lines_abef.append("")

    lines_abef.append("\n=== PART B: ALL 30 TEAMS KEY PLAYER DATABASE ===\n")
    for t in sorted(selected_30.keys()):
        s30 = selected_30[t]
        sp = team_splits[t]
        lines_abef.append(
            f"TEAM {t} ({sp['w']}-{sp['l']}, GP={sp['gp']}) "
            f"{'[PLAYING TODAY]' if t in playing_teams else ''} | "
            f"SmallOutliers={[(x['name'], x['gp'], x['pts']['mean'], x['status']) for x in s30['small_outliers']]}"
        )
        for cat_name, arr, stat_k, th_k in (
            ("Scorers", s30["scorers"], "pts", "pts_th"),
            ("Assists", s30["ast_leaders"], "ast", "ast_th"),
            ("Rebounds", s30["reb_leaders"], "reb", "reb_th"),
        ):
            for p in arr:
                f80 = p[th_k]["f80"]
                th_map = p[th_k]["map"]
                th_str = (
                    f"{f80}+: {th_map[str(f80)]['hits']}/{p['gp']} ({th_map[str(f80)]['pct']}%)"
                    if f80
                    else "Below base thresh"
                )
                pr = p.get("prior_season") or p.get("prior_2025_26")
                pr_str = (
                    f"Prior({pr['team']},{pr['gp']}G): {pr['ppg']}p/{pr['apg']}a/{pr['rpg']}r"
                    if pr
                    else "Prior: Rookie/DNP"
                )
                lines_abef.append(
                    f"  [{cat_name}] {p['name']} ({p['pos']}) | {p['gp']}/{p['team_gp']}G ({p['starts']}S) | "
                    f"MIN={p['min']['mean']} | L10: {p['pts']['mean']}p/{p['ast']['mean']}a/{p['reb']['mean']}r | "
                    f"L5: {p['l5_pts']}p/{p['l5_ast']}a/{p['l5_reb']}r | "
                    f"Floor80%({stat_k.upper()})={th_str} | {pr_str} | Status: {p['status']}"
                )

    abef_path = os.path.join(output_dir, f"{target_date}_matchups_and_30teams.txt")
    with open(abef_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines_abef))

    # Export 2: Detailed Last-10 Chronological Logs & Floor Tables for Playing Teams
    lines_cd: list[str] = []
    for gid in slate_gids:
        gm = today_details[gid]["meta"]
        for t in (norm_team(gm["away_abbr"]), norm_team(gm["home_abbr"])):
            lines_cd.append("=" * 58)
            lines_cd.append(f"TEAM {t} DETAILED KEY PLAYERS ({norm_team(gm['away_abbr'])} @ {norm_team(gm['home_abbr'])})")
            lines_cd.append("=" * 58)
            for entry in selected_playing_detailed.get(t, []):
                p = entry["player"]
                roles = ", ".join(entry["roles"])
                pr = p.get("prior_season") or p.get("prior_2025_26")
                pr_str = (
                    f"{pr['ppg']} PPG, {pr['apg']} APG, {pr['rpg']} RPG, {pr['mpg']} MPG ({pr['gp']} GP w/ {pr['team']})"
                    if pr
                    else "Rookie / No Prior NBA Regular-Season GP"
                )
                lines_cd.append(f"\n>>> {p['name']} ({t} - {p['pos']}) | Roles: {roles} | Status: {p['status']}")
                lines_cd.append(
                    f"  Sample: L10 Window N={p['gp']} (Season {p.get('season_gp', p['gp'])}/{p['team_gp']} GP, {p['starts']} Starts) | "
                    f"DNPs: {[(d['date'], d['opp'], d['reason']) for d in p['dnps']]}"
                )
                lines_cd.append(
                    f"  Averages: PTS L10={p['pts']['mean']} / L5={p['l5_pts']} / Sea={p.get('season_pts', p['pts']['mean'])} | "
                    f"AST L10={p['ast']['mean']} / L5={p['l5_ast']} / Sea={p.get('season_ast', p['ast']['mean'])} | "
                    f"REB L10={p['reb']['mean']} / L5={p['l5_reb']} / Sea={p.get('season_reb', p['reb']['mean'])} "
                    f"(OREB={p['oreb']}/DREB={p['dreb']})"
                )
                lines_cd.append(f"  Prior-Season Context (Separate): {pr_str}")
                lines_cd.append(
                    f"  Minutes: Mean={p['min']['mean']} (L5={p['l5_min']}), Med={p['min']['median']}, "
                    f"Min={p['min']['min']}, Max={p['min']['max']}, SD={p['min']['sd']} | "
                    f"30+m={p['min_30plus']}/{p['gp']}, 35+m={p['min_35plus']}/{p['gp']} | "
                    f"CloseMin={p['close_min']}, BlowoutMin={p['blowout_min']}"
                )
                lines_cd.append(
                    f"  Consistency: PTS[Med={p['pts']['median']}, Min={p['pts']['min']}, Max={p['pts']['max']}, SD={p['pts']['sd']}] | "
                    f"AST[Med={p['ast']['median']}, Min={p['ast']['min']}, Max={p['ast']['max']}, SD={p['ast']['sd']}] | "
                    f"REB[Med={p['reb']['median']}, Min={p['reb']['min']}, Max={p['reb']['max']}, SD={p['reb']['sd']}]"
                )
                for label, tk, l5tk in (("PTS", "pts_th", "l5_pts_th"), ("AST", "ast_th", "l5_ast_th"), ("REB", "reb_th", "l5_reb_th")):
                    tmap = p[tk]["map"]
                    l5map = p[l5tk]["map"]
                    parts = [
                        f"{k}+: {v['hits']}/{v['total']} ({v['pct']}%, L5:{l5map[k]['hits']}/{l5map[k]['total']})"
                        for k, v in tmap.items()
                    ]
                    lines_cd.append(
                        f"  {label} Thresholds: "
                        + " | ".join(parts)
                        + f" --> Floor80={p[tk]['f80']}, Floor90={p[tk]['f90']}, Floor100={p[tk]['f100']}"
                    )

                lines_cd.append("  Chronological Game Log:")
                for idx, g in enumerate(p["games"], 1):
                    flags = []
                    if g["ot"]:
                        flags.append(g["ot"])
                    if abs(g["margin"]) >= 15:
                        flags.append(f"Blowout({'+' if g['margin'] > 0 else ''}{g['margin']})")
                    if g["pf"] >= 4:
                        flags.append(f"FoulTrbl({g['pf']}PF)")
                    if g["min"] < 22.0 and p["min"]["mean"] >= 26.0:
                        flags.append(f"ShortMin({g['min_str']})")
                    flag_s = ", ".join(flags) if flags else "Normal"
                    lines_cd.append(
                        f"    G{idx} | {g['date']} | {'vs' if g['home_away'] == 'H' else '@'} {g['opp']} | "
                        f"{g['score']} | {'Start' if g['starter'] else 'Bench'} | MIN:{g['min_str']} | "
                        f"PTS:{g['pts']} | AST:{g['ast']} | REB:{g['reb']}({g['oreb']}o/{g['dreb']}d) | "
                        f"FG:{g['fgm']}-{g['fga']} | 3PT:{g['tpm']}-{g['tpa']} | FT:{g['ftm']}-{g['fta']} | "
                        f"TO:{g['tov']} PF:{g['pf']} +/-:{g['plus_minus']} | {flag_s}"
                    )

    cd_path = os.path.join(output_dir, f"{target_date}_detailed_player_logs.txt")
    with open(cd_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines_cd))

    print(f"      Exported {abef_path} and {cd_path}.")
    return abef_path, cd_path
