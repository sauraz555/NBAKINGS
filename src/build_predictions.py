"""Prediction engine: game forecasts, player PTS/REB/AST projections, rankings and dashboard exports.

Reads `master_analytics_<date>.json` and `nba_data_cache_<date>.json` (built by the pipeline) and writes:
  - data/predictions_<date>.json            full machine-readable predictions
  - output/dashboard/*.json                 {rows, meta} files for the dashboard
  - reports/<date>_nba_elite_analyst_report.md   Parts A-I report

Every number is reproducible from the inputs with the documented formulas below.

GAME MODEL
  Possession model: game pace = mean(home pace, away pace).
  Team expected points = pace/100 * (team ORtg + opponent DRtg)/2, home +HCA/2, away -HCA/2 (HCA = 2.0).
  Blend: margin and total = 50% possession model + 50% DraftKings line (model only when no line).
  Win probability = mean of (a) Normal(blended margin, SD 12) model probability, (b) vig-free
  moneyline probability, (c) ESPN BPI; any missing component is dropped from the mean.

PLAYER MODEL
  Per-minute rate = 0.60 * last-10 rate + 0.25 * season rate + 0.15 * last-5 rate.
  Expected minutes = 0.60 * last-10 MIN + 0.40 * last-5 MIN, + share of minutes vacated by teammates
  who played in the team's last 3 games but are Out/Doubtful now, x0.95 for starters when the
  blended spread is >= 10 (elevated blowout concern), capped at the L10 maximum and 112% of the L10 mean.
  Matchup multiplier (half-strength): PTS by opponent DRtg vs league and game pace vs team pace;
  AST by opponent assists allowed; REB by opponent rebounds allowed.
  Range = projection +/- 0.8 * last-10 standard deviation (scaled to expected minutes).
  Doubtful players are treated as out; Questionable players are projected "if active" and flagged.
"""

import json
import math
import os
import statistics

from src.bref_parser import norm_team

HCA = 2.0
MARGIN_SD = 12.0
BLOWOUT_ELEVATED = 10.0
BLOWOUT_MODERATE = 6.0
ROTATION_MIN = 18.0


def _f(x, default=None):
    try:
        if x in (None, ""):
            return default
        return float(x)
    except (TypeError, ValueError):
        return default


def _ml_prob(ml):
    v = _f(ml)
    if v is None:
        return None
    return (-v) / (-v + 100.0) if v < 0 else 100.0 / (v + 100.0)


def _phi(z: float) -> float:
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def _status_kind(status: str) -> str:
    s = status.split(" (")[0].strip().lower()
    if s in ("out", "suspension"):
        return "out"
    if s == "doubtful":
        return "doubtful"
    if s in ("questionable", "day-to-day"):
        return "questionable"
    if s == "probable":
        return "probable"
    return "available"


def _thr(th: dict) -> dict:
    """Return the 80/90/100% thresholds with exact hit fractions."""
    out = {}
    for key in ("f80", "f90", "f100"):
        t = th.get(key)
        if t is None:
            out[key] = None
            continue
        h = th["map"][str(t)]
        out[key] = {"line": t, "hits": h["hits"], "total": h["total"]}
    return out


def _thr_text(t: dict | None, unit: str) -> str:
    if not t:
        return "-"
    return f"{t['line']}+ {unit} ({t['hits']}/{t['total']})"


def _game_model(gid: str, M: dict) -> dict:
    td = M["today_details"][gid]
    gm = td["meta"]
    home, away = norm_team(gm["home_abbr"]), norm_team(gm["away_abbr"])
    tb = M["team_bref"]
    adv_h, adv_a = tb[home]["adv"], tb[away]["adv"]
    pace = (_f(adv_h["pace"]) + _f(adv_a["pace"])) / 2.0
    exp_h = pace / 100.0 * (_f(adv_h["off_rtg"]) + _f(adv_a["def_rtg"])) / 2.0 + HCA / 2.0
    exp_a = pace / 100.0 * (_f(adv_a["off_rtg"]) + _f(adv_h["def_rtg"])) / 2.0 - HCA / 2.0
    model_margin = exp_h - exp_a
    model_total = exp_h + exp_a

    pc = (td.get("pickcenter") or [{}])[0] if td.get("pickcenter") else {}
    mkt_margin = mkt_total = mkt_prob_h = None
    spread_txt = pc.get("details")
    if pc.get("spread") is not None:
        sp = abs(_f(pc["spread"]))
        home_fav = bool(pc.get("homeTeamOdds", {}).get("favorite"))
        mkt_margin = sp if home_fav else -sp
    if pc.get("overUnder") is not None:
        mkt_total = _f(pc["overUnder"])
    ph = _ml_prob(pc.get("homeTeamOdds", {}).get("moneyLine"))
    pa = _ml_prob(pc.get("awayTeamOdds", {}).get("moneyLine"))
    if ph and pa:
        mkt_prob_h = ph / (ph + pa)

    bpi_h = _f(td.get("predictor", {}).get("homeTeam", {}).get("gameProjection"))
    bpi_h = bpi_h / 100.0 if bpi_h is not None else None

    margin = model_margin if mkt_margin is None else 0.5 * model_margin + 0.5 * mkt_margin
    total = model_total if mkt_total is None else 0.5 * model_total + 0.5 * mkt_total
    model_prob_h = _phi(margin / MARGIN_SD)
    comps = [p for p in (model_prob_h, mkt_prob_h, bpi_h) if p is not None]
    prob_h = sum(comps) / len(comps)

    winner, loser = (home, away) if prob_h >= 0.5 else (away, home)
    win_prob = max(prob_h, 1 - prob_h)
    score_h, score_a = (total + margin) / 2.0, (total - margin) / 2.0
    fav_sides = {
        "model": "H" if model_prob_h >= 0.5 else "A",
        "market": None if mkt_prob_h is None else ("H" if mkt_prob_h >= 0.5 else "A"),
        "bpi": None if bpi_h is None else ("H" if bpi_h >= 0.5 else "A"),
    }
    agree = len({v for v in fav_sides.values() if v}) == 1
    if win_prob >= 0.75 and agree:
        conf = "High"
    elif win_prob >= 0.60 and agree:
        conf = "Medium"
    else:
        conf = "Low"
    am = abs(margin)
    blow = "Elevated" if am >= BLOWOUT_ELEVATED else ("Moderate" if am >= BLOWOUT_MODERATE else "Low")

    return {
        "game_id": gid,
        "et_date": gm["et_date"], "et_time": gm["et_time"],
        "syd_date": gm["syd_date"], "syd_time": gm["syd_time"],
        "home": home, "away": away, "home_name": gm["home_name"], "away_name": gm["away_name"],
        "home_rec": gm["home_rec"], "away_rec": gm["away_rec"],
        "venue": f"{gm['venue_name']} ({gm['city']}, {gm['state']})",
        "notes": ", ".join(gm.get("notes") or []),
        "pace": round(pace, 1),
        "model_home_pts": round(exp_h, 1), "model_away_pts": round(exp_a, 1),
        "model_margin_home": round(model_margin, 1), "model_total": round(model_total, 1),
        "market_spread": spread_txt, "market_margin_home": mkt_margin, "market_total": mkt_total,
        "market_prob_home": None if mkt_prob_h is None else round(mkt_prob_h, 3),
        "bpi_prob_home": bpi_h,
        "model_prob_home": round(model_prob_h, 3),
        "prob_home": round(prob_h, 3),
        "pred_margin_home": round(margin, 1), "pred_total": round(total, 1),
        "pred_home_pts": round(score_h), "pred_away_pts": round(score_a),
        "winner": winner, "loser": loser, "win_prob": round(win_prob, 3),
        "pred_margin": round(am, 1),
        "margin_leader": home if margin >= 0 else away,
        "sources_agree": agree, "confidence": conf, "blowout": blow,
        "home_nrtg": _f(adv_h["net_rtg"]), "away_nrtg": _f(adv_a["net_rtg"]),
        "home_ortg": _f(adv_h["off_rtg"]), "away_ortg": _f(adv_a["off_rtg"]),
        "home_drtg": _f(adv_h["def_rtg"]), "away_drtg": _f(adv_a["def_rtg"]),
        "home_pace": _f(adv_h["pace"]), "away_pace": _f(adv_a["pace"]),
        "home_efg": _f(adv_h["efg_pct"]), "away_efg": _f(adv_a["efg_pct"]),
        "home_tov": _f(adv_h["tov_pct"]), "away_tov": _f(adv_a["tov_pct"]),
        "home_orb": _f(adv_h["orb_pct"]), "away_orb": _f(adv_a["orb_pct"]),
        "home_ftr": _f(adv_h["ft_rate"]), "away_ftr": _f(adv_a["ft_rate"]),
    }


def _league_avgs(M: dict) -> dict:
    tb = M["team_bref"]
    teams = [t for t in tb if "adv" in tb[t] and "opp_pg" in tb[t]]
    drtg = statistics.mean(_f(tb[t]["adv"]["def_rtg"]) for t in teams)
    ast = statistics.mean(_f(tb[t]["opp_pg"]["opp_ast"]) for t in teams)
    trb = statistics.mean(_f(tb[t]["opp_pg"]["opp_trb"]) for t in teams)
    return {"drtg": drtg, "opp_ast": ast, "opp_trb": trb}


def _recent_team_dates(M: dict, C: dict, team: str, n: int = 3) -> set[str]:
    dates = []
    for g in C["all_schedule_games"]:
        if not g.get("completed"):
            continue
        if team in (norm_team(g["home_abbr"]), norm_team(g["away_abbr"])):
            dates.append(g["et_date"])
    return set(sorted(dates)[-n:])


def _project_team(team: str, opp: str, game: dict, M: dict, C: dict, lg: dict) -> list[dict]:
    plist = M["players_by_team"].get(team, [])
    tb = M["team_bref"]
    is_home = team == game["home"]
    recent = _recent_team_dates(M, C, team)

    def recently_active(p):
        return any(g["date"] in recent and g["min"] > 0 for g in p.get("games", []))

    # Minutes vacated by players who were in the rotation in the last 3 games but are now out/doubtful.
    vac_min = vac_pts = 0.0
    vacated_names = []
    for p in plist:
        if _status_kind(p["status"]) in ("out", "doubtful") and recently_active(p) and p["gp"] >= 1:
            vac_min += p["l5_min"] or p["min"]["mean"]
            vac_pts += p["l5_pts"] or p["pts"]["mean"]
            vacated_names.append(p["name"])

    rot = [
        p for p in plist
        if _status_kind(p["status"]) not in ("out", "doubtful") and p["gp"] >= 3 and p["min"]["mean"] >= ROTATION_MIN
    ]
    tot_min = sum(p["min"]["mean"] for p in rot) or 1.0
    tot_pts = sum(p["pts"]["mean"] for p in rot) or 1.0

    opp_adv, opp_pg = tb[opp]["adv"], tb[opp]["opp_pg"]
    team_pace = _f(tb[team]["adv"]["pace"])
    pace_x = game["pace"] / team_pace
    m_pts = 1 + 0.5 * ((_f(opp_adv["def_rtg"]) / lg["drtg"]) * pace_x - 1)
    m_ast = 1 + 0.5 * ((_f(opp_pg["opp_ast"]) / lg["opp_ast"]) * pace_x - 1)
    m_reb = 1 + 0.5 * ((_f(opp_pg["opp_trb"]) / lg["opp_trb"]) * pace_x - 1)
    elevated = game["blowout"] == "Elevated"

    out = []
    for p in rot:
        l10m, l5m = p["min"]["mean"], p["l5_min"] or p["min"]["mean"]
        smin = p["season_min"] or l10m
        exp_min = 0.6 * l10m + 0.4 * l5m
        exp_min += 0.5 * vac_min * (l10m / tot_min)
        starter = p["starts"] >= p["gp"] / 2
        if elevated:
            exp_min *= 0.95 if starter else 1.03
        exp_min = min(exp_min, max(p["min"]["max"], l10m), 1.12 * l10m)

        proj = {}
        for stat, mult, l5k, sk in (("pts", m_pts, "l5_pts", "season_pts"), ("ast", m_ast, "l5_ast", "season_ast"), ("reb", m_reb, "l5_reb", "season_reb")):
            r10 = p[stat]["mean"] / l10m if l10m else 0
            r5 = (p[l5k] / l5m) if (p[l5k] is not None and l5m) else r10
            rs = (p[sk] / smin) if (p[sk] is not None and smin) else r10
            rate = 0.6 * r10 + 0.25 * rs + 0.15 * r5
            v = rate * exp_min * mult
            if stat == "pts":
                v += 0.25 * vac_pts * (p["pts"]["mean"] / tot_pts)
            sd = p[stat]["sd"] * (exp_min / l10m if l10m else 1)
            proj[stat] = (round(v, 1), round(max(0.0, v - 0.8 * sd), 1), round(v + 0.8 * sd, 1))

        kind = _status_kind(p["status"])
        min_cv = p["min"]["sd"] / l10m if l10m else 1
        if kind == "questionable" or min_cv > 0.25 or p["gp"] < 5:
            conf = "Low"
        elif min_cv < 0.15 and p["gp"] >= 8 and kind in ("available", "probable") and not elevated:
            conf = "High"
        else:
            conf = "Medium"
        trend_d = (p["l5_pts"] or 0) - p["pts"]["mean"]
        trend = "Rising" if trend_d >= 2.5 else ("Falling" if trend_d <= -2.5 else "Stable")
        risk = []
        if kind == "questionable":
            risk.append("Questionable: projection assumes the player is active")
        if kind == "probable":
            risk.append("Probable on injury report")
        if elevated:
            risk.append("Elevated blowout risk could cut 4th-quarter minutes")
        if p["min"]["min"] < 0.7 * l10m:
            risk.append(f"Had a {p['min']['min']:.0f}-minute game in last {p['gp']}")
        if (p["pf"] or 0) >= 3.5:
            risk.append(f"Foul-prone ({p['pf']:.1f} PF/g)")
        out.append({
            "game_id": game["game_id"], "player_id": p["id"], "player": p["name"], "pos": p["pos"],
            "team": team, "opp": opp, "home_away": "H" if is_home else "A",
            "status": p["status"], "status_kind": kind, "starter": starter,
            "gp_l10": p["gp"], "season_gp": p["season_gp"], "dnps": len(p.get("dnps") or []),
            "exp_min": round(exp_min, 1), "l10_min": l10m, "l5_min": l5m, "min_sd": p["min"]["sd"],
            "min_lo": p["min"]["min"], "min_hi": p["min"]["max"],
            "proj_pts": proj["pts"][0], "pts_lo": proj["pts"][1], "pts_hi": proj["pts"][2],
            "proj_ast": proj["ast"][0], "ast_lo": proj["ast"][1], "ast_hi": proj["ast"][2],
            "proj_reb": proj["reb"][0], "reb_lo": proj["reb"][1], "reb_hi": proj["reb"][2],
            "l10_pts": p["pts"]["mean"], "l10_ast": p["ast"]["mean"], "l10_reb": p["reb"]["mean"],
            "l5_pts": p["l5_pts"], "l5_ast": p["l5_ast"], "l5_reb": p["l5_reb"],
            "season_pts": p["season_pts"], "season_ast": p["season_ast"], "season_reb": p["season_reb"],
            "pts_med": p["pts"]["median"], "pts_min": p["pts"]["min"], "pts_max": p["pts"]["max"], "pts_sd": p["pts"]["sd"],
            "ast_med": p["ast"]["median"], "ast_min": p["ast"]["min"], "ast_max": p["ast"]["max"], "ast_sd": p["ast"]["sd"],
            "reb_med": p["reb"]["median"], "reb_min": p["reb"]["min"], "reb_max": p["reb"]["max"], "reb_sd": p["reb"]["sd"],
            "pts_floor": _thr(p["pts_th"]), "ast_floor": _thr(p["ast_th"]), "reb_floor": _thr(p["reb_th"]),
            "pts_floor80": _thr_text(_thr(p["pts_th"])["f80"], "PTS"),
            "ast_floor80": _thr_text(_thr(p["ast_th"])["f80"], "AST"),
            "reb_floor80": _thr_text(_thr(p["reb_th"])["f80"], "REB"),
            "fga": p["fga"], "tpa": p["tpa"], "fta": p["fta"], "usg": _f((p.get("bref_adv") or {}).get("usg_pct")),
            "ts": _f((p.get("bref_adv") or {}).get("ts_pct")),
            "trend": trend, "confidence": conf, "risks": "; ".join(risk) or "None flagged",
            "mult_pts": round(m_pts, 3), "mult_ast": round(m_ast, 3), "mult_reb": round(m_reb, 3),
            "vacated_by": ", ".join(vacated_names),
            "prior": p.get("prior_season") or {},
            "games": p.get("games", [])[-10:],
        })
    return out


def _key_roles(team_rows: list[dict]) -> dict[str, list[str]]:
    roles: dict[str, list[str]] = {}
    by_pts = sorted(team_rows, key=lambda r: r["season_pts"] or 0, reverse=True)
    by_ast = sorted(team_rows, key=lambda r: r["season_ast"] or 0, reverse=True)
    by_reb = sorted(team_rows, key=lambda r: r["season_reb"] or 0, reverse=True)
    for i, r in enumerate(by_pts[:2]):
        roles.setdefault(r["player_id"], []).append(f"Scorer #{i + 1}")
    if by_ast:
        roles.setdefault(by_ast[0]["player_id"], []).append("Assist leader")
    if by_reb:
        roles.setdefault(by_reb[0]["player_id"], []).append("Rebound leader")
    return roles


def build_predictions(target_date: str, data_dir: str, output_dir: str, reports_dir: str) -> dict:
    with open(os.path.join(data_dir, f"master_analytics_{target_date}.json"), encoding="utf-8") as f:
        M = json.load(f)
    with open(os.path.join(data_dir, f"nba_data_cache_{target_date}.json"), encoding="utf-8") as f:
        C = json.load(f)
    lg = _league_avgs(M)

    gids = sorted(M["today_details"], key=lambda g: M["today_details"][g]["meta"]["utc_iso"])
    games = [_game_model(g, M) for g in gids]
    players = []
    for g in games:
        for team, opp in ((g["away"], g["home"]), (g["home"], g["away"])):
            rows = _project_team(team, opp, g, M, C, lg)
            roles = _key_roles(rows)
            for r in rows:
                r["roles"] = ", ".join(roles.get(r["player_id"], []))
                r["matchup"] = f"{g['away']} @ {g['home']}"
                r["syd_time"] = g["syd_time"]
            players.extend(rows)

    injuries = {}
    for g in games:
        for t in (g["away"], g["home"]):
            injuries[t] = M["merged_injuries"].get(t, {})

    result = {
        "target_date": target_date,
        "fetched_at_utc": C.get("fetched_at_utc"),
        "league": lg,
        "games": games,
        "players": players,
        "injuries": injuries,
        "team_splits": {t: M["team_splits"][t] for g in games for t in (g["away"], g["home"])},
        "team_bref": {t: M["team_bref"][t] for g in games for t in (g["away"], g["home"])},
        "players_by_team": M["players_by_team"],
    }
    pred_path = os.path.join(data_dir, f"predictions_{target_date}.json")
    with open(pred_path, "w", encoding="utf-8") as f:
        json.dump({k: v for k, v in result.items() if k != "players_by_team"}, f, indent=1, default=str)

    _export_dashboard(result, C, output_dir)
    rpt = _write_report(result, C, reports_dir)
    print(f"      Wrote {pred_path}, dashboard files in {os.path.join(output_dir, 'dashboard')} and {rpt}.")
    return result


# ---------------------------------------------------------------- dashboard exports

def _export_dashboard(R: dict, C: dict, output_dir: str) -> None:
    out = os.path.join(output_dir, "dashboard")
    os.makedirs(out, exist_ok=True)
    code_path = os.path.abspath(__file__)
    with open(code_path, encoding="utf-8") as f:
        code = f.read()
    meta = [
        {"label": "build_predictions.py", "value": code, "type": "code", "lang": "python"},
        {"label": "Input", "value": f"master_analytics_{R['target_date']}.json, nba_data_cache_{R['target_date']}.json "
                                     f"(ESPN, Basketball Reference, Official NBA injury report), fetched {R['fetched_at_utc']}"},
    ]

    def dump(name, rows):
        with open(os.path.join(out, name), "w", encoding="utf-8") as f:
            json.dump({"rows": rows, "meta": meta}, f, separators=(",", ":"), default=str)

    games_rows = []
    for g in R["games"]:
        row = {k: v for k, v in g.items()}
        inj = []
        for t in (g["away"], g["home"]):
            for nm, (st, why) in R["injuries"].get(t, {}).items():
                if st.lower() in ("available",) or "G League" in why:
                    continue
                inj.append(f"{t} {nm} ({st})")
        row["injuries"] = "; ".join(inj)
        row["matchup"] = f"{g['away']} @ {g['home']}"
        row["winner_pct"] = round(g["win_prob"] * 100, 1)
        w_home = g["winner"] == g["home"]
        for src, key in (("model", "model_prob_home"), ("market", "market_prob_home"), ("bpi", "bpi_prob_home")):
            v = g[key]
            row[f"winner_{src}_pct"] = None if v is None else round((v if w_home else 1 - v) * 100, 1)
        row["model_away_pts"], row["model_home_pts"] = g["model_away_pts"], g["model_home_pts"]
        games_rows.append(row)
    dump("slate_games.json", games_rows)

    prow = []
    for p in R["players"]:
        prow.append({k: v for k, v in p.items() if k not in ("games", "prior", "pts_floor", "ast_floor", "reb_floor")})
    dump("player_projections.json", prow)

    past = []
    for g in sorted(C["all_schedule_games"], key=lambda x: x["utc_iso"]):
        if not g.get("completed") or g.get("home_score") is None:
            continue
        h, a = norm_team(g["home_abbr"]), norm_team(g["away_abbr"])
        hs, as_ = int(g["home_score"]), int(g["away_score"])
        past.append({
            "game_id": g["id"], "et_date": g["et_date"], "syd_date": g["syd_date"], "syd_time": g["syd_time"],
            "away": a, "home": h, "away_score": as_, "home_score": hs,
            "winner": h if hs > as_ else a, "margin": abs(hs - as_),
            "ot": "OT" if (g.get("periods") or 4) > 4 else "",
            "matchup": f"{a} @ {h}", "notes": ", ".join(g.get("notes") or []),
        })
    dump("past_games.json", past)

    logs = []
    for p in C["player_appearances"].values():
        for g in p["games"]:
            if g.get("season") != "2026-27":
                continue
            logs.append({
                "game_id": g["game_id"], "date": g["date"], "player": p["name"], "team": norm_team(g["team"]),
                "opp": norm_team(g["opp"]), "ha": g["home_away"], "starter": 1 if g["starter"] else 0,
                "min": g["min"], "pts": g["pts"], "reb": g["reb"], "ast": g["ast"],
                "fg": f"{g['fgm']}-{g['fga']}", "tp": f"{g['tpm']}-{g['tpa']}", "ft": f"{g['ftm']}-{g['fta']}",
                "pm": g.get("plus_minus", ""),
            })
    dump("player_logs.json", logs)


# ---------------------------------------------------------------- markdown report

def _pct(x):
    return "-" if x is None else f"{x * 100:.1f}%"


def _write_report(R: dict, C: dict, reports_dir: str) -> str:
    os.makedirs(reports_dir, exist_ok=True)
    d = R["target_date"]
    G, P = R["games"], R["players"]
    L: list[str] = []
    w = L.append
    w(f"# NBA Elite Analyst Report — {d} (US ET) slate / {G[0]['syd_date']} Sydney\n")
    w(f"*Data fetched {R['fetched_at_utc']} UTC. Sources: ESPN scoreboard/box scores/odds (DraftKings)/BPI, "
      "Basketball Reference team & player tables, Official NBA Injury Report (official.nba.com). "
      "All times shown in Australia/Sydney (AEDT) with US Eastern in brackets.*\n")
    w("> Historical figures are facts from completed games. Projections are model outputs (method at the end) "
      "and are not guarantees. An 8/10 hit rate is an observed frequency, not an 80% probability.\n")

    # PART A
    w("## PART A — Fixtures (Sydney time)\n")
    w("| Sydney (AEDT) | US ET | Away | Home | Venue | Event |\n|---|---|---|---|---|---|")
    for g in G:
        w(f"| {g['syd_date']} {g['syd_time']} | {g['et_time']} | {g['away_name']} ({g['away_rec']}) | "
          f"{g['home_name']} ({g['home_rec']}) | {g['venue']} | {g['notes']} |")
    w("")

    # PART B — 30 teams compact
    w("## PART B — All 30 Teams Key-Player Database\n")
    w("Top two scorers, assist leader and rebound leader by current-season average (players with 3+ games and 15+ MIN). "
      "L10 = last 10 actual appearances (DNPs excluded).\n")
    w("| Team | Role | Player | Season P/A/R | L10 P/A/R | L10 MIN | 80% floor (L10) | Status |\n|---|---|---|---|---|---|---|---|")
    for t in sorted(R["players_by_team"]):
        pl = [p for p in R["players_by_team"][t] if p["gp"] >= 3 and p["min"]["mean"] >= 15]
        if not pl:
            continue
        picks = []
        for i, p in enumerate(sorted(pl, key=lambda x: x["season_pts"] or 0, reverse=True)[:2]):
            picks.append((f"Scorer {i + 1}", p, "pts_th", "PTS"))
        picks.append(("Assists", max(pl, key=lambda x: x["season_ast"] or 0), "ast_th", "AST"))
        picks.append(("Rebounds", max(pl, key=lambda x: x["season_reb"] or 0), "reb_th", "REB"))
        for role, p, th, unit in picks:
            w(f"| {t} | {role} | {p['name']} | {p['season_pts']}/{p['season_ast']}/{p['season_reb']} | "
              f"{p['pts']['mean']}/{p['ast']['mean']}/{p['reb']['mean']} | {p['min']['mean']} | "
              f"{_thr_text(_thr(p[th])['f80'], unit)} | {p['status']} |")
    w("")

    # PART C — logs for key players
    w("## PART C — Last-10 Game Logs (key players on this slate)\n")
    w("Chronological, oldest first. Full logs for every rotation player are in "
      f"`output/{d}_detailed_player_logs.txt`.\n")
    keyp = [p for p in P if p["roles"]]
    for g in G:
        w(f"### {g['away']} @ {g['home']}\n")
        for p in [x for x in keyp if x["game_id"] == g["game_id"]]:
            w(f"**{p['player']}** ({p['team']}, {p['roles']}) — {p['status']} · {p['gp_l10']} apps in sample, "
              f"{p['dnps']} DNP/absences logged")
            w("\n| Date | Opp | H/A | Result | MIN | PTS | AST | REB | FG | 3P | FTA | GS |\n|---|---|---|---|---|---|---|---|---|---|---|---|")
            for x in p["games"]:
                w(f"| {x['date']} | {norm_team(x['opp'])} | {x['home_away']} | {x['score']}{' ' + x['ot'] if x['ot'] else ''} | "
                  f"{x['min_str']} | {x['pts']} | {x['ast']} | {x['reb']} | {x['fgm']}-{x['fga']} | {x['tpm']}-{x['tpa']} | "
                  f"{x['fta']} | {'Y' if x['starter'] else 'N'} |")
            w(f"\nL10 {p['l10_pts']}/{p['l10_ast']}/{p['l10_reb']} · L5 {p['l5_pts']}/{p['l5_ast']}/{p['l5_reb']} · "
              f"Season {p['season_pts']}/{p['season_ast']}/{p['season_reb']} (P/A/R) · MIN mean {p['l10_min']} "
              f"(range {p['min_lo']:.0f}-{p['min_hi']:.0f}, SD {p['min_sd']}) · Trend: {p['trend']}\n")
    # PART D
    w("## PART D — Consistency Tables (slate players, L10)\n")
    for stat, unit in (("pts", "PTS"), ("ast", "AST"), ("reb", "REB")):
        rows = sorted(P, key=lambda r: (((r[f"{stat}_floor"]["f80"] or {}).get("line") or 0), r[f"{stat}_min"]), reverse=True)[:20]
        w(f"### {unit}\n")
        w("| Player | Team | Avg | Median | Min | Max | SD | 80% floor | 90% floor | 100% floor |\n|---|---|---|---|---|---|---|---|---|---|")
        for r in rows:
            fl = r[f"{stat}_floor"]
            w(f"| {r['player']} | {r['team']} | {r[f'l10_{stat}']} | {r[f'{stat}_med']} | {r[f'{stat}_min']} | {r[f'{stat}_max']} | "
              f"{r[f'{stat}_sd']} | {_thr_text(fl['f80'], unit)} | {_thr_text(fl['f90'], unit)} | {_thr_text(fl['f100'], unit)} |")
        w("")

    # PART E
    w("## PART E — Matchup, Injuries and Schedule\n")
    for g in G:
        w(f"### {g['away']} @ {g['home']} — {g['syd_time']} Sydney\n")
        for t in (g["away"], g["home"]):
            sp = R["team_splits"][t]
            ri = sp["rest_info"]
            inj = R["injuries"].get(t, {})
            real = [f"{n} ({s[0]}{', ' + s[1] if s[1] else ''})" for n, s in inj.items() if s[0].lower() != "available" and "G League" not in s[1]]
            flags = [k for k, v in (("back-to-back", ri["is_b2b_second"]), ("3-in-4", ri["is_3in4"]), ("4-in-6", ri["is_4in6"]), ("plays again tomorrow", ri["front_end_b2b"])) if v]
            nrt = g["home_nrtg"] if t == g["home"] else g["away_nrtg"]
            w(f"- **{t}** ({sp['w']}-{sp['l']}, L5 {sp['l5']}, home {sp['home_rec']}, away {sp['away_rec']}; NRtg {nrt:+.1f}). "
              f"Rest: {ri['rest_days']} day(s){' — ' + ', '.join(flags) if flags else ''}. Prev: {ri['prev_game']}. Next: {ri['next_game']}.")
            w(f"  - Injuries: {'; '.join(real) if real else 'none listed'}")
        w(f"- Expected pace {g['pace']} · Blowout concern: **{g['blowout']}** (blended margin {g['pred_margin']}).\n")

    # PART F
    w("## PART F — Match Predictions\n")
    w("| Sydney | Game | Pick | Win % | Model / Market / BPI (home) | Pred. score | Margin | Total | Confidence | Blowout |\n|---|---|---|---|---|---|---|---|---|---|")
    for g in G:
        w(f"| {g['syd_time']} | {g['away']} @ {g['home']} | **{g['winner']}** | {g['win_prob'] * 100:.0f}% | "
          f"{_pct(g['model_prob_home'])} / {_pct(g['market_prob_home'])} / {_pct(g['bpi_prob_home'])} | "
          f"{g['away']} {g['pred_away_pts']} – {g['home']} {g['pred_home_pts']} | {g['margin_leader']} by {g['pred_margin']} | "
          f"{g['pred_total']} (line {g['market_total']}) | {g['confidence']} | {g['blowout']} |")
    w("\nPick = side with the higher blended win probability. Margin and score come from the blended margin, so in a "
      "close game where the sources disagree (Low confidence) they can point to different sides; treat those as toss-ups.")
    w("\nScore range: about ±6 points per team around the predicted score covers most outcomes for games like these.\n")

    # PART G
    w("## PART G — Player Projections (PTS / AST / REB)\n")
    w("Expected projection with a likely range in brackets. Rotation players only (18+ L10 MIN). "
      "Doubtful players are treated as out; Questionable players are shown *if active*.\n")
    for g in G:
        w(f"### {g['away']} @ {g['home']}\n")
        w("| Player | Team | Status | Exp MIN | PTS | AST | REB | Reliable floors (L10) | Conf | Main risk |\n|---|---|---|---|---|---|---|---|---|---|")
        for p in sorted([x for x in P if x["game_id"] == g["game_id"]], key=lambda r: (r["team"], -r["proj_pts"])):
            w(f"| {p['player']}{' *' + p['roles'] + '*' if p['roles'] else ''} | {p['team']} | {p['status'].split(' (')[0]} | {p['exp_min']} | "
              f"{p['proj_pts']} ({p['pts_lo']}-{p['pts_hi']}) | {p['proj_ast']} ({p['ast_lo']}-{p['ast_hi']}) | "
              f"{p['proj_reb']} ({p['reb_lo']}-{p['reb_hi']}) | {p['pts_floor80']}; {p['ast_floor80']}; {p['reb_floor80']} | "
              f"{p['confidence']} | {p['risks']} |")
        w("")

    # PART H
    w("## PART H — Top Reliable Statistical Selections\n")
    elig = [p for p in P if p["confidence"] != "Low" and p["status_kind"] in ("available", "probable")]
    for stat, unit in (("pts", "PTS"), ("ast", "AST"), ("reb", "REB")):
        w(f"### Top 10 {unit}\n")
        w(f"| # | Player | Team | Opp | Floor (L10 hits) | Proj (range) | Exp MIN | Why |\n|---|---|---|---|---|---|---|---|")
        cand = [p for p in elig if p[f"{stat}_floor"]["f80"]]
        cand.sort(key=lambda r: (r[f"{stat}_lo"], r[f"{stat}_floor"]["f80"]["line"]), reverse=True)
        for i, p in enumerate(cand[:10], 1):
            fl = p[f"{stat}_floor"]["f80"]
            why = f"L10 low {p[f'{stat}_min']}, median {p[f'{stat}_med']}; matchup x{p['mult_' + stat]}"
            w(f"| {i} | {p['player']} | {p['team']} | {p['opp']} | {fl['line']}+ ({fl['hits']}/{fl['total']}) | "
              f"{p[f'proj_{stat}']} ({p[f'{stat}_lo']}-{p[f'{stat}_hi']}) | {p['exp_min']} | {why} |")
        w("")
    w("### Top 5 overall matchup and minutes outlook\n")
    top5 = sorted(elig, key=lambda r: r["pts_lo"] + 1.5 * r["ast_lo"] + 1.2 * r["reb_lo"], reverse=True)[:5]
    w("| # | Player | Team | Opp | Proj P/A/R | Exp MIN | Conf |\n|---|---|---|---|---|---|---|")
    for i, p in enumerate(top5, 1):
        w(f"| {i} | {p['player']} | {p['team']} | {p['opp']} | {p['proj_pts']}/{p['proj_ast']}/{p['proj_reb']} | {p['exp_min']} | {p['confidence']} |")
    w("")
    w("<!-- PART I is written by the analyst after reviewing these tables. -->\n")
    w("## PART I — Final Analyst Summary\n\nSEE_ANALYST_SUMMARY\n")

    w("## Method\n")
    w("```\n" + __doc__.strip() + "\n```\n")
    path = os.path.join(reports_dir, f"{d}_nba_elite_analyst_report.md")
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            old = f.read()
        if "## PART I — Final Analyst Summary" in old and "SEE_ANALYST_SUMMARY" not in old:
            # keep the analyst-written Part I when regenerating
            part_i = old.split("## PART I — Final Analyst Summary", 1)[1].split("\n## Method", 1)[0]
            L = [x.replace("\n\nSEE_ANALYST_SUMMARY\n", part_i) if x.startswith("## PART I") else x for x in L]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    return path
