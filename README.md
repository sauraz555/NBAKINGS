# NBA Elite Analyst — Daily Player Statistics & Game Prediction System

Quantitative NBA research, statistical floor calculation, official injury tracking, matchup analysis, and game forecasting pipeline built with zero external Python package dependencies (Python 3.10+ standard library).

## Features

- **Live Multi-Source NBA Ingestion (`src/harvest_nba_data.py`)**:
  - Pulls regular-season and Emirates NBA Cup schedules, full player box scores, DraftKings spreads/totals/moneylines, and ESPN BPI win probabilities via ESPN Site v2 APIs.
  - Downloads current-season and prior-season team/player advanced & opponent-shooting tables from Basketball Reference (`ORtg`, `DRtg`, `Pace`, Four Factors, rim `0-3ft` defense, `USG%`, `TS%`, `AST%`, `ORB%`, `DRB%`).
  - Automatically indexes and downloads the latest timestamped Official NBA Injury Report PDF from `official.nba.com`.
  - Converts all fixture tip-off times across both **US Eastern Time (`EST`/`EDT`)** and **`Australia/Sydney` (`AEDT`/`AEST`)**.
- **Statistical Floor & Consistency Engine (`src/build_analytics.py`)**:
  - Evaluates each player's **10 most recent actual appearances** (strictly excluding `0:00` and `DNP` games while logging absences separately).
  - Compares **Last-10**, **Last-5**, **Current-Season**, and separate **Prior-Season** benchmarks without blending seasons.
  - Calculates exact hit fractions and percentages across Points (`10+` to `35+`), Assists (`3+` to `12+`), and Rebounds (`5+` to `15+`), isolating `>=80%`, `>=88-90%`, and `100%` observed statistical floors alongside close-game vs. blowout (`>=15` pt margin) minute splits.
  - Tracks schedule fatigue (`0`-day Back-to-Back, `3-in-4`, `4-in-6`, road-trip length, and front-end B2B lookahead).
- **Structured Report Exporter (`src/export_report_data.py`)**:
  - Produces ready-to-audit matchup sheets, a 30-team key-player database (top 2 scorers, primary assist leader, primary rebound leader, injury replacements, and small-sample outlier flags), and chronological game logs.

## Repository Structure

```text
nba-elite-analyst/
├── run_pipeline.py                              # CLI entrypoint for daily slate execution
├── pyproject.toml                               # Project metadata (Python >= 3.10, stdlib only)
├── prompts/
│   └── nba_elite_analyst_system_prompt.md       # Full 14-section NBA Elite Analyst specification
├── src/
│   ├── bref_parser.py                           # Zero-dependency Basketball Reference HTML parser
│   ├── harvest_nba_data.py                      # Live ESPN + BRef + Official NBA Injury PDF fetcher
│   ├── build_analytics.py                       # Statistical floor, rest/travel & split calculator
│   └── export_report_data.py                    # Matchup, 30-team database & game-log exporter
├── data/
│   ├── injury_overrides_2026-11-06.json         # Verified 11/06/2026 04:45 AM ET PDF injury statuses
│   └── injury_reports/
│       └── Injury-Report_2026-11-06_04_45AM.pdf # Archived official NBA injury report PDF
├── output/
│   ├── 2026-11-06_matchups_and_30teams.txt      # Generated matchup & 30-team key-player tables
│   ├── 2026-11-06_detailed_player_logs.txt      # Chronological logs & threshold hit rates (18 teams)
│   └── 2026-11-06_supplementary_logs.txt        # Secondary rotation logs & missed-game dates
└── reports/
    └── 2026-11-06_nba_elite_analyst_report.md   # Complete Parts A-I report (Nov 6, 2026 NBA Cup slate)
```

## Quick Start

### 1. Run Live Analysis for Today's NBA Slate

```powershell
python run_pipeline.py --date 2026-11-06
```

### 2. Rebuild Analytics Offline from Cached Data

```powershell
python run_pipeline.py --date 2026-11-06 --skip-fetch
```

### CLI Options

| Flag | Default | Description |
|---|---|---|
| `--date` | Current local date | Target NBA slate date in `YYYY-MM-DD` (US Eastern Time) |
| `--season-start` | `2026-10-20` | NBA regular-season opening night (`YYYY-MM-DD`) |
| `--bref-year` | `2027` | Basketball Reference season end year (`2027` = `2026-27` season) |
| `--data-dir` | `./data` | Directory for downloaded caches and official PDF injury reports |
| `--output-dir` | `./output` | Directory for exported matchup and player-floor text dumps |
| `--skip-fetch` | `False` | Reuse existing cached JSON/HTML files in `--data-dir` |

## Predictions, Report & Dashboard

`run_pipeline.py` now also:

- **Parses the Official NBA Injury Report PDF** (`src/parse_injury_pdf.py`, needs `pdftotext` from poppler-utils) into `data/injury_overrides_<date>.json`, so official Out/Doubtful/Questionable/Probable statuses override ESPN's "Day-To-Day".
- **Builds predictions** (`src/build_predictions.py`): game winner, win %, score, margin, total, confidence and blowout risk (possession model blended 50/50 with DraftKings lines, win % averaged with vig-free moneyline and ESPN BPI), plus PTS/REB/AST projections with likely ranges for every rotation player on the slate.
- **Writes the full Parts A–I report** to `reports/<date>_nba_elite_analyst_report.md`. Part I (analyst summary) is written by hand and kept when the report is regenerated.
- **Exports dashboard data** to `output/dashboard/` (`slate_games.json`, `player_projections.json`, `past_games.json`, `player_logs.json`). The dashboard page source is `dashboard/index.html`.

Network hosts needed: `site.api.espn.com`, `www.basketball-reference.com`, `official.nba.com`, `ak-static.cms.nba.com`.

## Methodology & Data Integrity Rules

1. **No Blended Seasons**: When early-season sample sizes are `< 10` games, actual current-season appearances (`N`) are evaluated transparently and prior-season averages are displayed strictly as separate reference context.
2. **Strict DNP Exclusion**: `DNP` and `0:00` appearances are excluded from per-game averages and threshold denominators, while missed games and injury interruptions are tracked separately.
3. **Observed Floors != Guarantees**: An `80%+` or `100%` historical threshold hit rate represents observed past consistency, which is always stress-tested against opponent defense, pace, foul trouble, minutes stability, and blowout risk.
