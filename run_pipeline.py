#!/usr/bin/env python3
"""CLI entrypoint for the NBA Elite Analyst live data & prediction pipeline."""

import argparse
from datetime import datetime
import os
import sys

from src.build_analytics import build_master_analytics
from src.build_predictions import build_predictions
from src.export_report_data import export_report_sections
from src.harvest_nba_data import harvest_nba_data
from src.parse_injury_pdf import write_overrides_from_latest_pdf


def main() -> int:
    parser = argparse.ArgumentParser(
        description="NBA Elite Analyst — Daily Player Statistics, Statistical Floors & Matchup Pipeline"
    )
    parser.add_argument(
        "--date",
        default=datetime.now().strftime("%Y-%m-%d"),
        help="Target NBA slate date in YYYY-MM-DD (US Eastern Time). Defaults to today.",
    )
    parser.add_argument(
        "--season-start",
        default="2026-10-20",
        help="Regular-season start date in YYYY-MM-DD (default: 2026-10-20).",
    )
    parser.add_argument(
        "--bref-year",
        type=int,
        default=2027,
        help="Basketball Reference season end year (e.g., 2027 for 2026-27 NBA season).",
    )
    parser.add_argument(
        "--data-dir",
        default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"),
        help="Directory for cached JSON/HTML/PDF inputs.",
    )
    parser.add_argument(
        "--output-dir",
        default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "output"),
        help="Directory for exported analytical text dumps.",
    )
    parser.add_argument(
        "--skip-fetch",
        action="store_true",
        help="Skip live HTTP harvesting and rebuild analytics from existing cached files in --data-dir.",
    )
    args = parser.parse_args()

    print(f"=== NBA ELITE ANALYST PIPELINE (Slate Date: {args.date}) ===")
    if not args.skip_fetch:
        harvest_nba_data(
            target_date=args.date,
            data_dir=args.data_dir,
            season_start=args.season_start,
            bref_end_year=args.bref_year,
        )
    else:
        print("[INFO] --skip-fetch enabled; reusing cached files in", args.data_dir)

    write_overrides_from_latest_pdf(target_date=args.date, data_dir=args.data_dir)

    build_master_analytics(
        target_date=args.date,
        data_dir=args.data_dir,
        bref_end_year=args.bref_year,
    )
    export_report_sections(
        target_date=args.date,
        data_dir=args.data_dir,
        output_dir=args.output_dir,
    )
    build_predictions(
        target_date=args.date,
        data_dir=args.data_dir,
        output_dir=args.output_dir,
        reports_dir=os.path.join(os.path.dirname(os.path.abspath(__file__)), "reports"),
    )
    print("=== PIPELINE COMPLETE ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
