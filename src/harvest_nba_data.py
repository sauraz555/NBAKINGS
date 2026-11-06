"""Live NBA data harvester: ESPN scoreboards, box scores, odds, BPI, official injury PDFs, and Basketball Reference."""

from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
import json
import os
import re
import shutil
import subprocess
import urllib.request


def fetch_json(url: str, retries: int = 3) -> dict | None:
    """Fetch JSON from an HTTP endpoint with retry support."""
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=20) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as exc:
            if attempt == retries - 1:
                print(f"[WARN] Failed fetching {url}: {exc}")
                return None
    return None


def convert_timezones(utc_dt: datetime) -> tuple[datetime, str, datetime, str]:
    """Convert UTC timestamp to US Eastern (`America/New_York`) and `Australia/Sydney`."""
    try:
        from zoneinfo import ZoneInfo

        et_dt = utc_dt.astimezone(ZoneInfo("America/New_York"))
        syd_dt = utc_dt.astimezone(ZoneInfo("Australia/Sydney"))
        return et_dt, et_dt.strftime("%Z"), syd_dt, syd_dt.strftime("%Z")
    except Exception:
        # Fallback for environments without tzdata package installed
        year = utc_dt.year
        # US DST ends first Sunday in November at 06:00 UTC
        nov1 = datetime(year, 11, 1, tzinfo=timezone.utc)
        days_to_sun = (6 - nov1.weekday()) % 7
        dst_end_utc = datetime(year, 11, 1 + days_to_sun, 6, 0, tzinfo=timezone.utc)
        is_est = utc_dt >= dst_end_utc
        et_dt = utc_dt.astimezone(timezone(timedelta(hours=-5 if is_est else -4)))
        syd_dt = utc_dt.astimezone(timezone(timedelta(hours=11)))
        return et_dt, ("EST" if is_est else "EDT"), syd_dt, "AEDT"


def download_file(url: str, out_path: str) -> bool:
    """Download an HTML or PDF asset using curl (preferred for TLS/HTTP2) or urllib fallback."""
    curl_bin = "curl.exe" if os.name == "nt" and shutil.which("curl.exe") else shutil.which("curl")
    if curl_bin:
        res = subprocess.run(
            [curl_bin, "-s", "-L", "--max-time", "30", "-H", "User-Agent: Mozilla/5.0", url, "-o", out_path],
            capture_output=True,
            check=False,
        )
        if res.returncode == 0 and os.path.exists(out_path) and os.path.getsize(out_path) > 500:
            return True
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=25) as resp, open(out_path, "wb") as f:
            f.write(resp.read())
        return os.path.getsize(out_path) > 500
    except Exception as exc:
        print(f"[WARN] Download failed for {url}: {exc}")
        return False


def harvest_nba_data(
    target_date: str,
    data_dir: str,
    season_start: str = "2026-10-20",
    lookahead_days: int = 4,
    bref_end_year: int = 2027,
) -> str:
    """Harvest ESPN schedule/box-score cache, Basketball Reference tables, and Official NBA Injury PDF."""
    os.makedirs(data_dir, exist_ok=True)
    inj_dir = os.path.join(data_dir, "injury_reports")
    os.makedirs(inj_dir, exist_ok=True)

    target_dt = datetime.strptime(target_date, "%Y-%m-%d")
    start_dt = datetime.strptime(season_start, "%Y-%m-%d")
    end_dt = target_dt + timedelta(days=lookahead_days)
    target_key = target_dt.strftime("%Y%m%d")
    prev_key = (target_dt - timedelta(days=1)).strftime("%Y%m%d")

    dates: list[str] = []
    curr = start_dt
    while curr <= end_dt:
        dates.append(curr.strftime("%Y%m%d"))
        curr += timedelta(days=1)

    print(f"[1/4] Fetching {len(dates)} NBA scoreboard dates ({dates[0]} -> {dates[-1]})...")
    scoreboards: dict[str, dict | None] = {}
    with ThreadPoolExecutor(max_workers=12) as ex:
        futs = {
            ex.submit(
                fetch_json,
                f"https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates={dt}",
            ): dt
            for dt in dates
        }
        for fut in as_completed(futs):
            scoreboards[futs[fut]] = fut.result()

    completed_event_ids: list[str] = []
    today_event_ids: list[str] = []
    all_schedule_games: list[dict] = []

    for dt in sorted(scoreboards.keys()):
        sb = scoreboards[dt]
        if not sb:
            continue
        for ev in sb.get("events", []):
            if ev.get("season", {}).get("type") != 2:
                continue
            comp = ev["competitions"][0]
            completed = bool(ev["status"]["type"]["completed"])
            utc_str = ev["date"]
            utc_dt = datetime.fromisoformat(utc_str.replace("Z", "+00:00"))
            et_dt, et_tz, syd_dt, syd_tz = convert_timezones(utc_dt)

            home_c = [c for c in comp["competitors"] if c["homeAway"] == "home"][0]
            away_c = [c for c in comp["competitors"] if c["homeAway"] == "away"][0]
            venue = comp.get("venue", {})
            addr = venue.get("address", {})
            notes = [n.get("headline", "") for n in comp.get("notes", [])]

            g_info = {
                "id": ev["id"],
                "espn_date_key": dt,
                "utc_iso": utc_str,
                "et_date": et_dt.strftime("%Y-%m-%d"),
                "et_time": f"{et_dt.strftime('%I:%M %p')} {et_tz}",
                "syd_date": syd_dt.strftime("%Y-%m-%d"),
                "syd_time": f"{syd_dt.strftime('%I:%M %p')} {syd_tz}",
                "completed": completed,
                "status_detail": ev["status"]["type"]["detail"],
                "periods": ev["status"].get("period", 4),
                "home_abbr": home_c["team"]["abbreviation"],
                "home_name": home_c["team"]["displayName"],
                "home_id": home_c["team"]["id"],
                "home_score": int(home_c.get("score", 0)) if completed else None,
                "home_rec": home_c.get("records", [{"summary": ""}])[0]["summary"],
                "away_abbr": away_c["team"]["abbreviation"],
                "away_name": away_c["team"]["displayName"],
                "away_id": away_c["team"]["id"],
                "away_score": int(away_c.get("score", 0)) if completed else None,
                "away_rec": away_c.get("records", [{"summary": ""}])[0]["summary"],
                "venue_name": venue.get("fullName", ""),
                "city": addr.get("city", ""),
                "state": addr.get("state", ""),
                "notes": notes,
            }
            all_schedule_games.append(g_info)
            if completed and dt <= prev_key:
                completed_event_ids.append(ev["id"])
            elif dt == target_key:
                today_event_ids.append(ev["id"])

    print(
        f"      Found {len(completed_event_ids)} completed regular-season games through {prev_key}, "
        f"and {len(today_event_ids)} fixtures on {target_date}."
    )

    all_target_ids = list(dict.fromkeys(completed_event_ids + today_event_ids))
    print(f"[2/4] Fetching {len(all_target_ids)} ESPN game box scores, odds & BPI summaries...")
    summaries: dict[str, dict | None] = {}
    with ThreadPoolExecutor(max_workers=20) as ex:
        futs = {
            ex.submit(
                fetch_json,
                f"https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event={gid}",
            ): gid
            for gid in all_target_ids
        }
        for fut in as_completed(futs):
            summaries[futs[fut]] = fut.result()

    injuries_data = fetch_json("https://site.api.espn.com/apis/site/v2/sports/basketball/nba/injuries")

    print("[3/4] Checking Official NBA Injury Report PDFs & Basketball Reference tables...")
    season_slug = f"{bref_end_year - 1}-{str(bref_end_year)[-2:]}"
    try:
        req = urllib.request.Request(
            f"https://official.nba.com/nba-injury-report-{season_slug}-season/",
            headers={"User-Agent": "Mozilla/5.0"},
        )
        html = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", errors="ignore")
        pdfs = [p for p in re.findall(r'https://[^\s"\'<>]+\.pdf', html) if "Injury-Report" in p]
        if pdfs:
            latest_pdf = pdfs[-1]
            pdf_name = os.path.basename(latest_pdf)
            pdf_out = os.path.join(inj_dir, pdf_name)
            if download_file(latest_pdf, pdf_out):
                print(f"      Saved latest Official NBA Injury PDF: {pdf_name}")
    except Exception as exc:
        print(f"[WARN] Could not index official.nba.com injury page: {exc}")

    bref_pages = [
        f"NBA_{bref_end_year}.html",
        f"NBA_{bref_end_year}_per_game.html",
        f"NBA_{bref_end_year}_advanced.html",
        f"NBA_{bref_end_year - 1}_per_game.html",
    ]
    for page in bref_pages:
        out_path = os.path.join(data_dir, page)
        ok = download_file(f"https://www.basketball-reference.com/leagues/{page}", out_path)
        size = os.path.getsize(out_path) if ok and os.path.exists(out_path) else 0
        print(f"      Downloaded {page} ({size:,} bytes)")

    print("[4/4] Aggregating player game logs, DNP records & slate metadata...")
    game_meta_map = {g["id"]: g for g in all_schedule_games}
    player_appearances: dict[str, dict] = {}

    for gid in completed_event_ids:
        s = summaries.get(gid)
        if not s or "boxscore" not in s:
            continue
        gm = game_meta_map[gid]
        for p_team in s["boxscore"].get("players", []):
            t_abbr = p_team["team"]["abbreviation"]
            is_home = t_abbr == gm["home_abbr"]
            opp_abbr = gm["away_abbr"] if is_home else gm["home_abbr"]
            t_score = gm["home_score"] if is_home else gm["away_score"]
            o_score = gm["away_score"] if is_home else gm["home_score"]
            wl = "W" if t_score > o_score else "L"
            ot_str = ""
            if gm["periods"] > 4:
                ot_str = "OT" if gm["periods"] == 5 else f"{gm['periods'] - 4}OT"

            if not p_team.get("statistics"):
                continue
            stat_block = p_team["statistics"][0]
            labels = stat_block["labels"]

            for ath_entry in stat_block.get("athletes", []):
                ath = ath_entry["athlete"]
                aid = ath["id"]
                aname = ath["displayName"]
                pos = ath.get("position", {}).get("abbreviation", "")
                if aid not in player_appearances:
                    player_appearances[aid] = {
                        "id": aid,
                        "name": aname,
                        "pos": pos,
                        "latest_team": t_abbr,
                        "latest_date": gm["et_date"],
                        "games": [],
                        "dnps": [],
                    }
                if gm["et_date"] >= player_appearances[aid]["latest_date"]:
                    player_appearances[aid]["latest_team"] = t_abbr
                    player_appearances[aid]["latest_date"] = gm["et_date"]

                if ath_entry.get("didNotPlay"):
                    player_appearances[aid]["dnps"].append(
                        {
                            "game_id": gid,
                            "date": gm["et_date"],
                            "team": t_abbr,
                            "opp": opp_abbr,
                            "home_away": "H" if is_home else "A",
                            "reason": ath_entry.get("reason", "DNP"),
                        }
                    )
                    continue

                st = dict(zip(labels, ath_entry.get("stats", [])))
                min_raw = st.get("MIN", "0")
                try:
                    if ":" in min_raw:
                        mm, ss = min_raw.split(":")
                        min_val = int(mm) + int(ss) / 60.0
                    else:
                        min_val = float(min_raw)
                except ValueError:
                    min_val = 0.0

                if (
                    min_val == 0
                    and st.get("PTS", "0") == "0"
                    and st.get("FG", "0-0") == "0-0"
                    and st.get("REB", "0") == "0"
                    and st.get("AST", "0") == "0"
                ):
                    player_appearances[aid]["dnps"].append(
                        {
                            "game_id": gid,
                            "date": gm["et_date"],
                            "team": t_abbr,
                            "opp": opp_abbr,
                            "home_away": "H" if is_home else "A",
                            "reason": ath_entry.get("reason", "0 MIN DNP"),
                        }
                    )
                    continue

                fgm, fga = map(int, st.get("FG", "0-0").split("-"))
                tpm, tpa = map(int, st.get("3PT", "0-0").split("-"))
                ftm, fta = map(int, st.get("FT", "0-0").split("-"))

                player_appearances[aid]["games"].append(
                    {
                        "game_id": gid,
                        "date": gm["et_date"],
                        "season": season_slug,
                        "team": t_abbr,
                        "opp": opp_abbr,
                        "home_away": "H" if is_home else "A",
                        "wl": wl,
                        "score": f"{wl} {t_score}-{o_score}" + (f" ({ot_str})" if ot_str else ""),
                        "margin": t_score - o_score,
                        "ot": ot_str,
                        "starter": bool(ath_entry.get("starter")),
                        "min": min_val,
                        "min_str": min_raw,
                        "pts": int(st.get("PTS", 0)),
                        "ast": int(st.get("AST", 0)),
                        "reb": int(st.get("REB", 0)),
                        "oreb": int(st.get("OREB", 0)),
                        "dreb": int(st.get("DREB", 0)),
                        "fgm": fgm,
                        "fga": fga,
                        "tpm": tpm,
                        "tpa": tpa,
                        "ftm": ftm,
                        "fta": fta,
                        "tov": int(st.get("TO", 0)),
                        "stl": int(st.get("STL", 0)),
                        "blk": int(st.get("BLK", 0)),
                        "pf": int(st.get("PF", 0)),
                        "plus_minus": st.get("+/-", "0"),
                    }
                )

    for pdata in player_appearances.values():
        pdata["games"].sort(key=lambda x: x["date"])
        pdata["dnps"].sort(key=lambda x: x["date"])

    today_details: dict[str, dict] = {}
    for gid in today_event_ids:
        s = summaries.get(gid) or {}
        gm = game_meta_map[gid]
        today_details[gid] = {
            "meta": gm,
            "pickcenter": s.get("pickcenter", []),
            "predictor": s.get("predictor", {}),
            "seasonseries": s.get("seasonseries", []),
            "injuries": s.get("injuries", []),
        }

    cache_path = os.path.join(data_dir, f"nba_data_cache_{target_date}.json")
    cache_out = {
        "target_date": target_date,
        "season_slug": season_slug,
        "bref_end_year": bref_end_year,
        "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
        "all_schedule_games": all_schedule_games,
        "player_appearances": player_appearances,
        "today_details": today_details,
        "espn_injuries": injuries_data,
    }
    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(cache_out, f)

    print(f"      Saved {cache_path} ({len(player_appearances)} active NBA players).")
    return cache_path
