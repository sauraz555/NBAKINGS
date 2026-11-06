# NBA ELITE ANALYST — DAILY PLAYER STATISTICS & GAME PREDICTION REPORT

### Live Research Metadata & Verification Disclosure
- **Analysis Date & Timezone**:
  - **NBA Slate Calendar Date (US Eastern)**: **Friday, November 6, 2026** (`EST`, `UTC-5` — US Daylight Saving Time ended Nov 1, 2026).
  - **Local Australian Conversion (`Australia/Sydney`)**: **Saturday, November 7, 2026** (`AEDT`, `UTC+11` — 16 hours ahead of `EST`; non-DST `AEST` `UTC+10` also noted where helpful).
  - **Research Cut & Verification Timestamp**: `2026-11-06 20:10 AEST (UTC+10)` / `21:10 AEDT (Australia/Sydney)` / **`05:10 AM EST (America/New_York)`**.
- **Current NBA Season & Completed Sample**: **2026–27 NBA Regular Season** (tipped off October 20, 2026; **123 regular-season games completed** across the league).
- **Most Recently Completed NBA Games**: **Thursday, November 5, 2026 (US EST)** — Orlando Magic at Phoenix Suns (`Final`) and Miami Heat at Golden State Warriors (`Final`).
- **Official Injury Report Timestamp**: **November 6, 2026 at 04:45 AM ET** (cross-checked against the `04:30 AM ET` edition via official NBA league PDFs: [Injury-Report_2026-11-06_04_45AM.pdf](../data/injury_reports/Injury-Report_2026-11-06_04_45AM.pdf) and `Injury-Report_2026-11-06_04_30AM.pdf`).
- **Early-Season Sample-Size Protocol (`N < 10`)**: Because today is Day 18 of the 2026–27 regular season, every NBA team has completed **7, 8, or 9 games** (`0` teams have reached 10 games). Following **Section 1**, every player's **entire completed 2026–27 game log (`N = 4` to `9` actual appearances)** is analysed in chronological order (`Last-N = Current-Season Sample`), compared against their **Last-5** appearances, with **2025–26 prior-season averages** displayed strictly separately and never blended into 2026–27 figures. DNP games are excluded from all averages and itemized separately; injury-shortened appearances (e.g., Jarrett Allen `7 MIN` on Nov 4; Lauri Markkanen `6 MIN` on Oct 26) are retained inside actual game logs and explicitly flagged.
- **Data Completeness & Source Disclosure**:
  - **Verified Primary Sources Used**: Official NBA Injury Reports ([official.nba.com](https://official.nba.com/nba-injury-report-2026-27-season/)), ESPN Official Box Scores, Schedules, BPI Matchup Predictor & DraftKings Sportsbook Odds ([espn.com/nba](https://www.espn.com/nba/schedule/_/date/20261106)), and Basketball Reference 2026–27 & 2025–26 Team/Player Advanced, Four Factors & Shooting Distance Tables ([basketball-reference.com](https://www.basketball-reference.com/leagues/NBA_2027.html)). Full parsed datasets are archived locally in `data/nba_data_cache_2026-11-06.json` and `data/master_analytics_2026-11-06.json`.
  - **Disclosed Unavailable Sub-Metrics**: Direct `stats.nba.com` / Second Spectrum optical player-tracking endpoints (`Potential Assists`, `Time of Possession`, `Contested/Uncontested Rebound Chances`, and individual play-type synergy splits) block automated cloud queries via Akamai (`HTTP 403`/timeout). Per **Section 1.9 & Section 14**, those optical tracking sub-fields are explicitly disclosed as unavailable rather than estimated; verified box-score and possession equivalents (`AST%`, `USG%`, `FGA/3PA/FTA`, `ORB%/DRB%/TRB%`, `Opponent Missed FG`, and `Opponent Rim [0–3 ft] / Short-Paint [3–10 ft] FG%`) are used throughout.

---

## PART A — TODAY'S NBA FIXTURES

All **9 fixtures** scheduled for **Friday, November 6, 2026 (US EST)** are **Emirates NBA Cup — Group Play** games. Because NBA Cup tiebreakers weight **Group Play point differential** immediately after head-to-head record, coaches frequently keep starters on the floor slightly longer in 12–18 point 4Q leads than in ordinary regular-season games—though 25+ point blowouts still trigger bench clearings.

| # | Tip-Off (US EST, Fri Nov 6) | Tip-Off (`Australia/Sydney` AEDT, Sat Nov 7) | Away Team (Record) | Home Team (Record) | Venue | DraftKings Line & Total | Key Official Injury & Availability Concerns (`04:45 AM ET` Report) |
|---|---|---|---|---|---|---|---|
| **1** | 7:00 PM EST | **11:00 AM AEDT** *(10:00 AM AEST)* | **Washington Wizards** (`4-4`) | **Atlanta Hawks** (`5-4`) | State Farm Arena (Atlanta, GA) | **ATL -6.5** \| O/U **229.5** | **WAS**: Anthony Davis (*Questionable* — R Ankle), Justin Champagnie (*Out* — R Foot), Tristan Vukcevic (*Out*). **ATL**: Jalen Johnson (*Questionable* — L Ankle, missed L2), Jock Landale (*Out*), Mouhamed Gueye (*Out*). |
| **2** | 7:00 PM EST | **11:00 AM AEDT** *(10:00 AM AEST)* | **Boston Celtics** (`6-2`) | **Charlotte Hornets** (`3-6`) | Spectrum Center (Charlotte, NC) | **BOS -8.5** \| O/U **209.5** | **BOS**: Payton Pritchard (*Questionable* — R Eye Abrasion); Tatum & PG13 *Available*. **CHA**: Moussa Diabate (*Questionable* — R Quad), Dennis Schroder (*Questionable* — L Thigh Soreness), Kon Knueppel (*Out* — L Hamstring), Grant Williams (*Out*). |
| **3** | 7:30 PM EST | **11:30 AM AEDT** *(10:30 AM AEST)* | **Philadelphia 76ers** (`8-1`) | **Cleveland Cavaliers** (`4-4`) | Rocket Arena (Cleveland, OH) | **PHI -2.5** \| O/U **228.5** | **PHI**: Adem Bona (*Doubtful* — Cervical Sprain), Dominick Barlow (*Out*); Maxey/Brown/Embiid/LeBron all *Available*. **CLE**: Jarrett Allen (*Questionable* — R Knee Contusion, exited after 7 MIN Nov 4), Jaylon Tyson (*Out*), Peyton Watson (*Questionable*). |
| **4** | 8:00 PM EST | **12:00 PM AEDT** *(11:00 AM AEST)* | **Utah Jazz** (`1-7`) | **Dallas Mavericks** (`4-4`) | American Airlines Center (Dallas, TX) | **DAL -7.5** \| O/U **225.5** | **UTA**: Jaren Jackson Jr. (*Out* — R MCL Tear), Jusuf Nurkic (*Out* — R Plantar Plate Tear). **DAL**: Dereck Lively II (*Out* — R Foot Surgery), Santi Aldama (*Probable*), Max Christie (*Probable*). |
| **5** | 8:00 PM EST | **12:00 PM AEDT** *(11:00 AM AEST)* | **Oklahoma City Thunder** (`6-2`) | **Memphis Grizzlies** (`6-2`) | FedExForum (Memphis, TN) | **OKC -3.5** \| O/U **225.5** | **OKC**: Chet Holmgren (*Out* — R Knee), Jalen Williams (*Out* — L Ankle Surgery), Cason Wallace (*Out* — L Shoulder), Jaylin Williams (*Out*), Nikola Topic (*Out*). **MEM**: Scotty Pippen Jr. (*Out* — Lumbar Disc), Isaiah Stewart (*Out* — R Knee Bone Bruise). |
| **6** | 8:00 PM EST | **12:00 PM AEDT** *(11:00 AM AEST)* | **Toronto Raptors** (`4-4`) | **Milwaukee Bucks** (`1-7`) | Fiserv Forum (Milwaukee, WI) | **TOR -6.5** \| O/U **230.5** | **TOR**: Scottie Barnes (*Questionable* — L Adductor/Groin Soreness), Kawhi Leonard (*Out* — L Knee Injury Mgmt), Nate Bittle (*Out*). **MIL**: Core rotation clean (only Two-Way/G-League assignments *Out*). |
| **7** | 8:00 PM EST | **12:00 PM AEDT** *(11:00 AM AEST)* | **Minnesota Timberwolves** (`6-3`) | **New Orleans Pelicans** (`4-4`) | Smoothie King Center (New Orleans, LA) | **MIN -4.5** \| O/U **231.5** | **MIN**: Anthony Edwards (*Out* — R Knee Arthroscopy), Donte DiVincenzo (*Out* — R Achilles), Terrence Shannon Jr. (*Questionable* — L Hip). **NOP**: Trey Murphy III (*Probable* — Patella Tendinopathy), Yves Missi (*Out* — L Knee). |
| **8** | 10:00 PM EST | **2:00 PM AEDT** *(1:00 PM AEST)* | **Portland Trail Blazers** (`6-1`) | **Los Angeles Lakers** (`7-2`) | crypto.com Arena (Los Angeles, CA) | **LAL -2.5** \| O/U **232.5** | **POR**: Ja Morant (*Out* — L Hamstring Strain), Shaedon Sharpe (*Out* — R Meniscus Surgery), Vit Krejci (*Out*). **LAL**: Walker Kessler (*Available* — L Finger Splint), Sandro Mamukelashvili (*Questionable* — Illness). |
| **9** | 10:00 PM EST | **2:00 PM AEDT** *(1:00 PM AEST)* | **San Antonio Spurs** (`6-2`) | **Sacramento Kings** (`1-7`) | Golden 1 Center (Sacramento, CA) | **SAS -15.5** \| O/U **229.5** | **SAS**: Tobias Harris (*Out* — L Calf Strain), Jayden Quaintance (*Out* — R Knee). **SAC**: Keegan Murray (*Out* — L Ankle Capsulitis), Maxime Raynaud (*Out* — R Patella), Ben Simmons (*Out* — R Achilles). |

---

## PART B — ALL 30 NBA TEAM KEY PLAYER DATABASE

- **Methodology Note**: Because all 30 teams have played between `7` and `9` games in `2026–27`, each player's **Current-Season (`26–27`)** average equals their **Last-`N` (`N <= 9`)** active-game average. **Last-5 (`L5`)** is shown alongside to capture immediate form, while **Prior-Season (`25–26`)** is strictly isolated in its own column. Teams playing today are marked **`[NOV 6]`**. Where a top leader is `Out` or `Questionable`, the active replacement is included immediately underneath. Small-sample PPG leaders (`<5 GP`) are explicitly flagged.

| Team (Rec, GP) | Role Category | Player (Pos) | GP/Tm (Starts) | 26–27 MIN | 26–27 Season (= Last-N) PPG / APG / RPG | Last-5 PPG / APG / RPG | Separate 2025–26 Context | Relevant >=80% Observed Floor (Hits, %) | Official Availability Status |
|---|---|---|---|---|---|---|---|---|---|
| **ATL** (`5-4`, 9G) **`[NOV 6]`** | Scorer #1 | Nickeil Alexander-Walker (G) | 9/9 (9S) | 30.3 | **21.7** / 2.7 / 3.3 | 24.0 / 1.8 / 3.2 | 20.8p/3.7a/3.4r (78G, ATL) | **10+ PTS**: 9/9 (100%) | Available |
| **ATL** | Scorer #2 / AST #1 / REB #1 | Jalen Johnson (F) | 7/9 (7S) | 32.7 | **18.3** / **7.9** / **9.0** | 17.8 / 8.2 / 8.4 | 22.5p/7.9a/10.3r (72G, ATL) | **10+ PTS**, **3+ AST**, **7+ REB**: 7/7 (100%) | **Questionable** (L Ankle) |
| **ATL** | Active Scorer Repl. | CJ McCollum (G) | 9/9 (8S) | 26.6 | **14.3** / 4.0 / 3.0 | 12.0 / 5.6 / 4.2 | 18.7p/3.9a/3.3r (76G, 2TM) | **10+ PTS**: 8/9 (88.9%) | Available |
| **ATL** | Active AST Repl. | Dyson Daniels (G) | 9/9 (9S) | 29.7 | 9.6 / **4.7** / 6.7 | 6.6 / 5.4 / 7.8 | 11.9p/5.9a/6.8r (76G, ATL) | **3+ AST**: 9/9 (100%) | Available |
| **ATL** | Active REB Repl. | Onyeka Okongwu (F/C) | 9/9 (9S) | 29.1 | 12.2 / 2.8 / **8.4** | 14.6 / 2.8 / 10.4 | 15.2p/3.1a/7.6r (74G, ATL) | *5+ REB: 7/9 (77.8%, L5 4/5)* | Available |
| **BKN** (`2-6`, 8G) | Scorer #1 / REB #1 | Michael Porter Jr. (F) | 8/8 (8S) | 33.1 | **21.4** / 1.2 / **7.4** | 21.4 / 1.6 / 8.6 | 24.2p/3.0a/7.1r (52G, BKN) | **10+ PTS**: 8/8 (100%) \| **5+ REB**: 7/8 (87.5%) | Off Nov 6 (Available) |
| **BKN** | Scorer #2 / AST #1 | Julius Randle (F) | 8/8 (8S) | 33.8 | **21.0** / **4.8** / 7.1 | 20.4 / 3.8 / 7.2 | 21.1p/5.0a/6.7r (79G, MIN) | **15+ PTS**: 7/8 (87.5%) \| **3+ AST**: 7/8 (87.5%) | Off Nov 6 (Available) |
| **BOS** (`6-2`, 8G) **`[NOV 6]`** | Scorer #1 / AST #1 | Jayson Tatum (F) | 7/8 (7S) | 35.1 | **27.0** / **7.9** / 6.0 | 28.0 / 7.4 / 5.8 | 21.8p/5.3a/10.0r (16G, BOS) | **15+ PTS**: 6/7 (85.7%) \| **7+ AST**: 6/7 (85.7%) | Available |
| **BOS** | Scorer #2 | Paul George (F) | 7/8 (7S) | 31.6 | **21.3** / 5.0 / 5.6 | 19.2 / 6.0 / 5.4 | 17.3p/3.6a/5.3r (37G, PHI) | **15+ PTS**: 7/7 (100%) \| **5+ REB**: 6/7 (85.7%) | Available |
| **BOS** | Secondary AST | Derrick White (G) | 8/8 (8S) | 30.8 | 12.8 / **5.1** / 3.2 | 13.6 / 4.6 / 3.0 | 16.5p/5.4a/4.4r (77G, BOS) | **3+ AST**: 7/8 (87.5%) | Available |
| **BOS** | REB #1 | Neemias Queta (C) | 8/8 (3S) | 22.5 | 9.8 / 1.4 / **6.2** | 10.6 / 1.4 / 7.0 | 10.2p/1.7a/8.4r (76G, BOS) | *5+ REB: 6/8 (75.0%, L4 4/4 as starter/20+m)* | Available |
| **CHA** (`3-6`, 9G) **`[NOV 6]`** | Scorer #1 | Brandon Miller (F) | 9/9 (9S) | 32.9 | **22.0** / 2.3 / 5.3 | 20.2 / 3.0 / 5.8 | 20.2p/3.3a/4.9r (65G, CHA) | **10+ PTS**: 8/9 (88.9%) | Available |
| **CHA** | Scorer #2 / Active REB | Naz Reid (C) | 9/9 (9S) | 29.7 | **16.9** / 1.9 / **8.3** | 14.8 / 1.4 / 7.4 | 13.6p/2.2a/6.2r (77G, MIN) | **10+ PTS**: 8/9 (88.9%) \| **5+ REB**: 9/9 (100%) | Available |
| **CHA** | AST #1 | Dennis Schroder (G) | 9/9 (7S) | 30.0 | 10.2 / **4.9** / 3.6 | 7.2 / 5.0 / 3.2 | 10.8p/4.9a/2.7r (70G, 2TM) | **3+ AST**: 8/9 (88.9%) | **Questionable** (L Soreness) |
| **CHA** | Active AST / 6th Man | Sion James / Grayson Allen | 9/9 | 25.3 / 26.4 | 5.2p/**2.8a** \| **15.7p**/2.7a | 7.2p/2.4a \| 14.8p/2.2a | James 5.4p/2.0a \| Allen 16.5p/3.8a | James *3+ AST: 6/9* \| Allen *10+ PTS: 7/9* | Available |
| **CHA** | REB #1 | Moussa Diabate (F/C) | 9/9 (9S) | 28.8 | 8.9 / 2.0 / **9.1** | 8.6 / 2.0 / 8.8 | 7.9p/1.9a/8.7r (73G, CHA) | **5+ REB**: 9/9 (100%) *(7+ REB: 7/9, 77.8%)* | **Questionable** (R Quad) |
| **CHI** (`1-7`, 8G) | Scorer #1 | Caleb Wilson (F) | 8/8 (8S) | 32.5 | **19.5** / 2.4 / 6.5 | 17.8 / 3.0 / 5.6 | 2026–27 NBA Rookie | **15+ PTS**: 7/8 (87.5%) \| **5+ REB**: 7/8 (87.5%) | Off Nov 6 (Available) |
| **CHI** | Scorer #2 | Norman Powell (G) | 8/8 (8S) | 28.9 | **19.2** / 1.6 / 2.5 | 19.2 / 1.6 / 1.8 | 21.7p/2.5a/3.5r (58G, MIA) | **15+ PTS**: 7/8 (87.5%) | Off Nov 6 (Available) |
| **CHI** | AST #1 / REB #1 | Josh Giddey (G) / Jalen Smith (F) | 8/8 (8S) | 27.2 / 22.4 | Giddey **7.6a** \| Smith **7.8r** | Giddey 7.2a \| Smith 7.6r | Giddey 17.0p/9.1a \| Smith 10.2p/6.7r | Giddey **5+ AST**: 7/8 (87.5%) \| Smith *5+ REB: 6/8* | Off Nov 6 (Smith DTD) |
| **CLE** (`4-4`, 8G) **`[NOV 6]`** | Scorer #1 | Donovan Mitchell (G) | 8/8 (8S) | 33.1 | **22.5** / 5.5 / 5.0 | 20.0 / 6.0 / 4.0 | 27.9p/5.7a/4.5r (70G, CLE) | **15+ PTS**: 8/8 (100%) \| **3+ AST**: 8/8 (100%) | Available |
| **CLE** | Scorer #2 / REB #1 | Evan Mobley (C) | 8/8 (8S) | 32.9 | **18.8** / 3.5 / **8.2** | 18.8 / 3.8 / 7.6 | 18.2p/3.6a/9.0r (65G, CLE) | **15+ PTS**: 7/8 (87.5%) \| **5+ REB**: 7/8 (87.5%) | Available |
| **CLE** | AST #1 / Scorer #3 | James Harden (G) | 8/8 (8S) | 33.6 | 16.6 / **6.2** / 5.2 | 17.2 / 5.8 / 5.2 | 23.6p/8.0a/4.8r (70G, 2TM) | **5+ AST**: 7/8 (87.5%) \| **10+ PTS**: 8/8 (100%) | Available |
| **CLE** | Co-REB #2 | Jarrett Allen (C) | 8/8 (8S) | 25.1 | 13.2 / 1.2 / **7.8** | 12.2 / 1.6 / 7.6 | 15.4p/1.8a/8.5r (56G, CLE) | **5+ REB**: 7/8 (87.5%, only miss = 7-min inj exit) | **Questionable** (R Knee) |
| **DAL** (`4-4`, 8G) **`[NOV 6]`** | Scorer #1 / AST #1 | Cooper Flagg (F) | 7/8 (7S) | 34.6 | **24.3** / **6.3** / 6.3 | 24.8 / 7.2 / 6.8 | 21.0p/4.5a/6.7r (70G, DAL) | **15+ PTS**: 6/7 (85.7%) \| **5+ AST**: 6/7 (85.7%) | Available |
| **DAL** | Scorer #2 | Kyrie Irving (G) | 6/8 (6S) | 30.0 | **22.7** / 4.8 / 4.0 | 24.2 / 5.4 / 4.0 | Missed 2025–26 (Injury Recovery) | **15+ PTS**: 6/6 (100%) \| **3+ AST**: 5/6 (83.3%) | Available |
| **DAL** | REB #1 / Scorer #3 | P.J. Washington (F) | 8/8 (8S) | 34.9 | 14.5 / 1.4 / **8.0** | 14.8 / 1.4 / 8.6 | 14.2p/1.8a/7.0r (56G, DAL) | **10+ PTS**: 7/8 (87.5%) \| *5+ REB: 6/8 (L5 5/5)* | Available |
| **DEN** (`4-3`, 7G) | Scorer #1 | Jamal Murray (G) | 7/7 (7S) | 36.9 | **25.4** / 5.9 / 5.4 | 26.0 / 6.4 / 5.0 | 25.4p/7.1a/4.4r (75G, DEN) | **10+ PTS**: 6/7 (85.7%) \| **5+ AST**: 6/7 (85.7%) | Off Nov 6 (Available) |
| **DEN** | Scorer #2 / AST #1 / REB #1 | Nikola Jokic (C) | 7/7 (7S) | 35.9 | **23.4** / **9.3** / **9.7** | 23.2 / 10.0 / 9.2 | 27.7p/10.7a/12.9r (65G, DEN) | **15+ PTS**: 6/7 \| **8+ AST**: 6/7 \| **7+ REB**: 7/7 | Off Nov 6 (Available) |
| **DET** (`6-2`, 8G) | Scorer #1 / AST #1 | Cade Cunningham (G) | 8/8 (8S) | 33.5 | **24.0** / **7.6** / 5.6 | 25.6 / 7.4 / 6.2 | 23.9p/9.9a/5.5r (64G, DET) | **15+ PTS**: 8/8 (100%) \| **7+ AST**: 7/8 (87.5%) | Off Nov 6 (Available) |
| **DET** | Scorer #2 / REB #1 | Duncan Robinson (F) / Ausar Thompson (G) | 8/8 \| 7/8 | 31.0 / 27.4 | Robinson **19.0p** \| Ausar **8.6r** | Robinson 18.6p \| Ausar 9.2r | Robinson 12.2p \| Ausar 9.9p/5.7r | Robinson **10+ PTS**: 8/8 \| Ausar **5+ REB**: 6/7 | Off Nov 6 (Available) |
| **GSW** (`6-3`, 9G) | Scorer #1 | Stephen Curry (G) | 7/9 (7S) | 28.9 | **29.9** / 4.4 / 3.7 | 32.4 / 5.2 / 4.4 | 26.6p/4.7a/3.6r (43G, GSW) | **20+ PTS**: 7/7 (100%) | Off Nov 6 (Available) |
| **GSW** | Scorer #2 / REB #1 / AST #1 | Yaxel Lendeborg (F) / Draymond Green (F) | 9/9 \| 7/9 | 31.7 / 26.7 | Lendeborg **21.0p**/**7.1r** \| Green **7.0a** | Lendeborg 20.4p/5.4r \| Green 7.0a | Lendeborg Rookie \| Green 8.4p/5.5a | Lendeborg **10+ PTS**: 8/9 \| Green **5+ AST**: 6/7 | Off Nov 6 (Available) |
| **HOU** (`7-2`, 9G) | Scorer #1 / AST #1 / REB #1 | Alperen Sengun (C) | 7/9 (7S) | 35.1 | **22.4** / **8.1** / **9.1** | 21.0 / 9.0 / 9.4 | 20.4p/6.2a/8.9r (72G, HOU) | **15+ PTS**: 7/7 \| **7+ AST**: 6/7 \| **7+ REB**: 7/7 | Off Nov 6 (Available) |
| **HOU** | Scorer #2 | Kevin Durant (F) | 9/9 (9S) | 33.8 | **20.8** / 3.0 / 5.2 | 18.6 / 2.8 / 4.2 | 26.0p/4.8a/5.5r (78G, HOU) | **10+ PTS**: 9/9 (100%) | Off Nov 6 (Available) |
| **IND** (`3-6`, 9G) | *Small-Sample Leader* | *Tyrese Haliburton (G) [Flag: 4G]* | 4/9 (4S) | 33.0 | *21.8* / *9.5* / 4.5 | 21.8 / 9.5 / 4.5 | Missed 2025–26 (Injury Recovery) | **15+ PTS**, **7+ AST**: 4/4 (100%) | **Out** (L Hamstring) |
| **IND** | Active Scorer #1 & #2 / AST / REB | Pascal Siakam (F) / Andrew Nembhard (G) / Ivica Zubac (C) | 8/9 \| 7/9 \| 4/9 | 32.0 / 33.4 / 21.0 | Siakam **21.2p**/**7.0r** \| Nembhard **19.0p**/**7.0a** \| Zubac **7.8r** | Siakam 19.2p/7.6r \| Nembhard 19.8p/7.0a | Siakam 24.0p \| Nembhard 16.9p/7.7a \| Zubac 14.1p/10.6r | Siakam **15+ PTS**: 7/8 \| Nembhard **15+ PTS**: 6/7, **3+ AST**: 7/7 | Off Nov 6 (Available) |
| **LAC** (`1-7`, 8G) | Scorer #1 / AST #1 | Darius Garland (G) | 8/8 (8S) | 33.8 | **20.9** / **6.6** / 1.6 | 19.0 / 6.4 / 1.6 | 18.8p/6.7a/2.4r (45G, 2TM) | **15+ PTS**: 7/8 (87.5%) \| **5+ AST**: 7/8 (87.5%) | Off Nov 6 (Available) |
| **LAC** | Scorer #2 / REB #1 | Rui Hachimura (F) | 6/8 (6S) | 31.2 | **14.7** / 1.7 / **6.5** | 15.6 / 1.6 / 6.2 | 11.5p/0.8a/3.3r (68G, LAL) | **10+ PTS**: 5/6 (83.3%) \| **5+ REB**: 5/6 (83.3%) | Off Nov 6 (Available) |
| **LAL** (`7-2`, 9G) **`[NOV 6]`** | Scorer #1 / AST #1 | Luka Doncic (G) | 8/9 (8S) | 35.6 | **38.5** / **8.0** / 8.1 | 41.0 / 8.0 / 8.6 | 33.5p/8.3a/7.7r (64G, LAL) | **25+ PTS**: 7/8 (87.5%) \| **5+ AST & 5+ REB**: 8/8 (100%) | Available |
| **LAL** | Scorer #2 | Austin Reaves (G) | 9/9 (9S) | 35.9 | **23.3** / 5.0 / 3.2 | 20.8 / 3.8 / 3.6 | 23.3p/5.5a/4.7r (51G, LAL) | **15+ PTS**: 9/9 (100%) \| **3+ AST**: 8/9 (88.9%) | Available |
| **LAL** | REB #1 | Walker Kessler (C) | 9/9 (9S) | 30.6 | 14.4 / 1.1 / **10.2** | 13.4 / 1.2 / 12.0 | 14.4p/3.0a/10.8r (5G, UTA) | **8+ REB**: 8/9 (88.9%) \| **7+ REB**: 9/9 (100%) | Available (L Finger Splint) |
| **MEM** (`6-2`, 8G) **`[NOV 6]`** | Scorer #1 | Ty Jerome (G) | 7/8 (7S) | 30.9 | **27.4** / 5.3 / 3.6 | 23.8 / 5.2 / 3.2 | 19.7p/5.7a/2.8r (15G, MEM) | **15+ PTS**: 6/7 (85.7%) \| **3+ AST**: 7/7 (100%) | Available |
| **MEM** | Scorer #2 / REB #1 / Co-AST | Cameron Boozer (F) | 8/8 (8S) | 32.1 | **16.5** / **5.4** / **9.8** | 17.2 / 5.6 / 8.6 | 2026–27 NBA Rookie | **10+ PTS**: 7/8 \| **3+ AST**: 8/8 \| **7+ REB**: 7/8 (87.5%) | Available |
| **MEM** | AST #1 (Bench) / REB #2 | Cam Spencer (G) / Cedric Coward (F) | 8/8 \| 7/8 | 19.8 / 29.3 | Spencer **5.8a** \| Coward 14.3p/**8.7r** | Spencer 8.4a \| Coward 15.2p/8.6r | Spencer 11.1p/5.6a \| Coward 13.6p/5.9r | Spencer *5+ AST: 5/8 (L5 5/5)* \| Coward **7+ REB**: 7/7 (100%) | Available |
| **MIA** (`3-6`, 9G) | Scorer #1 / REB #1 | Giannis Antetokounmpo (F) | 9/9 (9S) | 32.8 | **27.3** / 5.6 / **12.7** | 26.4 / 6.0 / 15.2 | 27.6p/5.4a/9.8r (36G, MIL) | **20+ PTS**: 8/9 (88.9%) \| **5+ REB**: 9/9 (100%) | Off Nov 6 (Available) |
| **MIA** | Scorer #2 / AST #1 | Bam Adebayo (C) / Davion Mitchell (G) | 9/9 (9S) | 32.7 / 35.0 | Bam **18.6p**/8.4r \| Mitchell **8.2a** | Bam 24.0p \| Mitchell 9.2a | Bam 20.1p/10.0r \| Mitchell 9.3p/6.5a | Bam **7+ REB**: 8/9 \| Mitchell **5+ AST**: 8/9 (88.9%) | Off Nov 6 (Available) |
| **MIL** (`1-7`, 8G) **`[NOV 6]`** | Scorer #1 | Tyler Herro (G) | 8/8 (8S) | 30.6 | **22.2** / 3.9 / 5.0 | 21.4 / 3.0 / 5.4 | 20.5p/4.1a/4.8r (33G, MIA) | **15+ PTS**: 7/8 (87.5%) \| **10+ PTS**: 8/8 (100%) | Available |
| **MIL** | Scorer #2 / Starter REB | Jaime Jaquez Jr. (F) | 8/8 (8S) | 28.4 | **16.8** / 2.8 / **6.6** | 14.4 / 2.2 / 5.4 | 15.4p/4.7a/5.0r (75G, MIA) | *15+ PTS: 6/8 (75%)* \| *5+ REB: 6/8 (75%)* | Available |
| **MIL** | AST #1 | Ryan Rollins (G) | 8/8 (6S) | 24.9 | 11.2 / **4.5** / 4.8 | 11.0 / 4.6 / 4.2 | 17.3p/5.6a/4.6r (74G, MIL) | **3+ AST**: 7/8 (87.5%) | Available |
| **MIL** | REB #1 (Bench) | Kel'el Ware (C) | 8/8 (0S) | 18.9 | 10.2 / 0.8 / **8.2** | 9.0 / 0.8 / 9.2 | 11.1p/0.7a/9.0r (77G, MIA) | *5+ REB: 6/8 (75%, L5 5/5)* | Available |
| **MIN** (`6-3`, 9G) **`[NOV 6]`** | *Scorer #1 [Small-Sample Out]* | *Anthony Edwards (G) [Flag: 4G]* | 4/9 (4S) | 33.8 | *33.2* / 3.5 / 4.8 | 33.2 / 3.5 / 4.8 | 28.8p/3.7a/5.0r (61G, MIN) | **15+ PTS**: 4/4 (100%) | **Out** (R Knee Arthroscopy) |
| **MIN** | Active Scorer #1 / AST #1 | LaMelo Ball (G) | 9/9 (9S) | 26.8 | **17.2** / **5.9** / 3.4 | 19.2 / 5.6 / 4.6 | 20.1p/7.1a/4.8r (72G, CHA) | **10+ PTS**: 8/9 (88.9%) \| **3+ AST**: 9/9 (100%) | Available |
| **MIN** | Active Scorer #2 & #3 | Jaden McDaniels (F) / Ayo Dosunmu (G) | 9/9 (9S\|5S) | 33.3 / 30.7 | McDaniels **16.4p** \| Dosunmu **16.3p**/4.3a | McDaniels 17.6p \| Dosunmu **19.8p**/4.6a | McDaniels 14.8p \| Dosunmu 14.8p/3.6a | McDaniels **10+ PTS**: 9/9, **5+ REB**: 8/9 \| Dosunmu *15+ PTS: L5 5/5* | Available |
| **MIN** | REB #1 | Rudy Gobert (C) | 8/9 (8S) | 30.5 | 7.5 / 1.5 / **11.9** | 6.6 / 2.0 / 11.6 | 10.9p/1.7a/11.5r (76G, MIN) | **8+ REB**: 7/8 (87.5%) | Available |
| **NOP** (`4-4`, 8G) **`[NOV 6]`** | Scorer #1 | Zion Williamson (F) | 8/8 (8S) | 33.0 | **21.5** / 2.6 / 5.1 | 22.0 / 2.8 / 6.4 | 21.0p/3.2a/5.7r (62G, NOP) | **15+ PTS**: 8/8 (100%) | Available |
| **NOP** | Scorer #2 / AST #1 | Dejounte Murray (G) | 5/8 (5S) | 34.8 | **18.2** / **5.6** / 6.2 | 18.2 / 5.6 / 6.2 | 16.7p/6.4a/5.4r (14G, NOP) | **15+ PTS**, **5+ AST**, **5+ REB**: 4/5 (80%) | Available |
| **NOP** | REB #1 / Scorer #3 | Derik Queen (C) / Saddiq Bey (F) | 8/8 (0S) | 24.1 / 26.5 | Queen 13.4p/**7.9r** \| Bey **16.4p** | Queen 13.6p/7.6r \| Bey 16.8p | Queen 11.7p/7.1r \| Bey 17.7p/5.6r | Queen **7+ REB**: 7/8 (87.5%) \| Bey **10+ PTS**: 7/8 | Available |
| **NYK** (`4-4`, 8G) | Scorer #1 / AST #1 | Jalen Brunson (G) | 8/8 (8S) | 33.9 | **25.6** / **5.1** / 2.6 | 27.4 / 6.0 / 2.2 | 26.0p/6.8a/3.3r (74G, NYK) | **15+ PTS**: 8/8 (100%) \| **3+ AST**: 8/8 (100%) | Off Nov 6 (Available) |
| **NYK** | Scorer #2 / REB #1 | Karl-Anthony Towns (C) | 8/8 (8S) | 31.2 | **19.9** / 3.1 / **13.6** | 19.2 / 3.4 / 14.6 | 20.1p/3.0a/11.9r (75G, NYK) | **15+ PTS**: 7/8 (87.5%) \| **12+ REB**: 7/8 (87.5%) | Off Nov 6 (Available) |
| **OKC** (`6-2`, 8G) **`[NOV 6]`** | Scorer #1 / AST #1 | Shai Gilgeous-Alexander (G) | 8/8 (8S) | 33.8 | **30.1** / **4.5** / 4.2 | 31.6 / 4.8 / 4.0 | 31.1p/6.6a/4.3r (68G, OKC) | **20+ PTS**: 7/8 (87.5%) \| **3+ AST**: 7/8 (87.5%) | Available |
| **OKC** | Scorer #2 *(w/ J-Dub & Chet Out)* | Ajay Mitchell (G) | 8/8 (5S) | 27.5 | **17.8** / 3.5 / 4.0 | **21.6** / 3.6 / 4.2 | 13.6p/3.6a/3.3r (57G, OKC) | *10+ PTS: 6/8 (75%, 4/5 as starter)* | Available |
| **OKC** | REB #1 | Isaiah Hartenstein (C) | 8/8 (8S) | 24.8 | 8.1 / 2.5 / **10.1** | 8.6 / 2.8 / **12.0** | 9.2p/3.5a/9.4r (47G, OKC) | **5+ REB**: 7/8 (87.5%, L5 **7+ REB**: 5/5) | Available |
| **ORL** (`2-6`, 8G) | Scorer #1 / AST #1 *(Banchero 2G Out)* | Franz Wagner (F) | 8/8 (8S) | 36.0 | **19.6** / **8.5** / 6.4 | 18.8 / 9.8 / 5.2 | 20.6p/3.3a/5.2r (34G, ORL) | **15+ PTS**: 7/8 (87.5%) \| **5+ AST**: 8/8 (100%) | Off Nov 6 (Available) |
| **ORL** | Scorer #2 / REB #1 | Desmond Bane (G) / Wendell Carter Jr. (C) | 8/8 (8S) | 34.5 / 32.6 | Bane **17.5p** \| Carter 14.2p/**9.4r** | Bane 19.0p \| Carter 12.6p/9.8r | Bane 20.1p \| Carter 11.8p/7.4r | Bane **10+ PTS**: 7/8 \| Carter **7+ REB**: 8/8 (100%) | Off Nov 6 (Available) |
| **PHI** (`8-1`, 9G) **`[NOV 6]`** | Scorer #1 | Tyrese Maxey (G) | 9/9 (9S) | 37.1 | **28.0** / 5.4 / 3.8 | 27.4 / 6.0 / 3.6 | 28.3p/6.6a/4.1r (70G, PHI) | **25+ PTS**: 8/9 (88.9%) \| **3+ AST**: 9/9 (100%) | Available |
| **PHI** | Scorer #2 | Jaylen Brown (G/F) | 8/9 (8S) | 36.2 | **21.8** / 3.9 / 6.9 | 21.4 / 3.2 / 7.2 | 28.7p/5.1a/6.9r (71G, BOS) | **15+ PTS**: 8/8 (100%) | Available |
| **PHI** | REB #1 / Scorer #3 | Joel Embiid (C) | 7/9 (7S) | 33.3 | **19.6** / 4.4 / **10.0** | 20.0 / 4.8 / 10.4 | 26.9p/3.9a/7.7r (38G, PHI) | **10+ PTS**: 7/7 (100%) \| **7+ REB**: 7/7 (100%) | Available |
| **PHI** | AST #1 | LeBron James (F) | 7/9 (7S) | 33.0 | 15.7 / **7.4** / 7.4 | 15.8 / 8.0 / 6.6 | 20.9p/7.2a/6.1r (60G, LAL) | **5+ AST**: 7/7 (100%) \| **5+ REB**: 6/7 (85.7%) | Available |
| **PHX** (`2-5`, 7G) | Scorer #1 / AST #1 | Devin Booker (G) | 7/7 (7S) | 34.4 | **25.4** / **5.1** / 2.9 | 22.4 / 5.4 / 1.8 | 26.1p/6.0a/3.9r (64G, PHX) | **20+ PTS**: 6/7 (85.7%) | Off Nov 6 (Available) |
| **PHX** | Scorer #2 / REB #1 | Dillon Brooks (F) / Miles Bridges (F) | 7/7 (7S) | 30.4 / 32.6 | Brooks **17.6p** \| Bridges 17.4p/**7.9r** | Brooks 19.6p \| Bridges 19.6p/8.8r | Brooks 20.2p \| Bridges 17.1p/5.8r | Both **15+ PTS**: 6/7 \| Bridges **5+ REB**: 6/7 | Off Nov 6 (Available) |
| **POR** (`6-1`, 7G) **`[NOV 6]`** | Scorer #1 / AST #1 | Deni Avdija (F) | 7/7 (7S) | 32.3 | **23.4** / **6.4** / 6.4 | 24.0 / 7.0 / 5.6 | 24.2p/6.7a/6.9r (66G, POR) | **20+ PTS**: 6/7 (85.7%) \| **3+ AST**: 6/7 (85.7%) | Available |
| **POR** | Scorer #2 *(Ja Morant 4G Out)* | Damian Lillard (G) | 7/7 (7S) | 29.7 | **20.1** / 4.1 / 4.1 | 19.4 / 4.2 / 4.2 | Missed 2025–26 (Injury Recovery) | **15+ PTS**: 6/7 (85.7%) | Available |
| **POR** | REB #1 | Donovan Clingan (C) | 7/7 (7S) | 24.7 | 12.0 / 1.6 / **10.6** | 13.0 / 1.2 / 11.2 | 12.1p/2.1a/11.6r (77G, POR) | **8+ REB**: 6/7 (85.7%) \| **7+ REB**: 7/7 (100%) | Available |
| **SAC** (`1-7`, 8G) **`[NOV 6]`** | Scorer #1 / AST #1 | Darius Acuff Jr. (G) | 8/8 (8S) | 37.2 | **25.6** / **7.0** / 3.8 | 27.6 / 8.4 / 4.4 | 2026–27 NBA Rookie | **15+ PTS**: 7/8 (87.5%) \| **3+ AST**: 8/8 (100%) | Available |
| **SAC** | Scorer #2 | Zach LaVine (G) | 8/8 (8S) | 33.4 | **23.1** / 2.6 / 3.1 | 19.6 / 2.2 / 2.8 | 19.2p/2.3a/2.8r (39G, SAC) | **20+ PTS**: 7/8 (87.5%) | Available |
| **SAC** | REB #1 / Co-AST | Domantas Sabonis (F/C) | 8/8 (8S) | 36.1 | 15.1 / **6.1** / **14.9** | 13.0 / 5.6 / 13.4 | 15.8p/4.1a/11.4r (19G, SAC) | **12+ REB**: 7/8 (87.5%) \| **3+ AST**: 7/8 (87.5%) | Available |
| **SAS** (`6-2`, 8G) **`[NOV 6]`** | Scorer #1 / REB #1 | Victor Wembanyama (F/C) | 8/8 (8S) | 31.6 | **29.0** / 3.1 / **12.4** | 34.4 / 3.6 / 13.2 | 25.0p/3.1a/11.5r (64G, SAS) | **10+ PTS**: 8/8 \| **7+ REB**: 8/8 (100%) | Available |
| **SAS** | Scorer #2 | Dylan Harper (G) | 8/8 (8S) | 32.9 | **18.6** / 4.6 / 5.6 | 17.8 / 5.6 / 6.0 | 11.8p/3.9a/3.4r (69G, SAS) | **10+ PTS**: 8/8 (100%) \| **5+ REB**: 7/8 (87.5%) | Available |
| **SAS** | AST #1 | De'Aaron Fox (G) | 8/8 (8S) | 30.9 | 15.1 / **6.1** / 4.2 | 13.8 / 4.8 / 4.0 | 18.6p/6.2a/3.8r (72G, SAS) | **10+ PTS**: 8/8 (100%) \| **3+ AST**: 8/8 (100%) | Available |
| **TOR** (`4-4`, 8G) **`[NOV 6]`** | Scorer #1 / REB #1 *(Kawhi 2G Out)* | Scottie Barnes (F) | 8/8 (8S) | 33.4 | **23.5** / 5.1 / **7.6** | 27.4 / 5.6 / 7.6 | 18.1p/5.9a/7.5r (80G, TOR) | **15+ PTS**: 7/8 \| **3+ AST**: 8/8 \| **5+ REB**: 7/8 | **Questionable** (L Adductor) |
| **TOR** | Scorer #2 / Active REB | RJ Barrett (F) | 8/8 (8S) | 32.5 | **20.9** / 3.9 / **6.0** | 20.8 / 4.4 / 6.6 | 19.3p/3.3a/5.3r (57G, TOR) | **20+ PTS**: 7/8 (87.5%) \| **3+ AST**: 7/8 (87.5%) | Available |
| **TOR** | AST #1 & #2 / Active Scorer | Immanuel Quickley (G) / Jamal Shead (G) | 8/8 (8S\|0S) | 31.8 / 21.5 | Quickley **17.4p**/**5.8a** \| Shead 5.5p/**5.4a** | Quickley 17.0p/6.2a \| Shead 6.6p/6.6a | Quickley 16.4p/5.9a \| Shead 6.6p/5.4a | Quickley **10+ PTS**: 8/8 \| Shead **5+ AST**: 7/8 (87.5%) | Available |
| **UTA** (`1-7`, 8G) **`[NOV 6]`** | Scorer #1 / AST #1 | Keyonte George (G) | 8/8 (8S) | 32.4 | **22.0** / **5.9** / 4.0 | 22.2 / 4.4 / 3.8 | 23.6p/6.1a/3.7r (54G, UTA) | **3+ AST**: 7/8 (87.5%) *(PTS 15+: 6/8, 75%)* | Available |
| **UTA** | Scorer #2 *(JJJ 4G Out)* | Lauri Markkanen (F) | 7/8 (7S) | 30.4 | **17.1** / 2.1 / 6.6 | 17.2 / 1.8 / 6.2 | 26.7p/2.1a/6.9r (42G, UTA) | **10+ PTS**: 6/7 (85.7%) \| **5+ REB**: 6/7 (only miss = 6m exit) | Available |
| **UTA** | REB #1 | Ace Bailey (G/F) | 8/8 (7S) | 30.6 | 12.5 / 2.0 / **7.2** | 13.0 / 1.4 / 6.8 | 13.8p/1.8a/4.2r (72G, UTA) | **5+ REB**: 8/8 (100%) | Available |
| **WAS** (`4-4`, 8G) **`[NOV 6]`** | Scorer #1 / REB #1 | Anthony Davis (F/C) | 8/8 (8S) | 33.1 | **23.4** / 2.1 / **9.2** | 25.0 / 1.6 / 9.4 | 20.4p/2.8a/11.1r (20G, DAL) | **15+ PTS**: 7/8 (87.5%) \| **5+ REB**: 8/8 (100%) | **Questionable** (R Ankle) |
| **WAS** | Scorer #2 / AST #1 | Trae Young (G) | 8/8 (8S) | 35.9 | **19.6** / **9.5** / 3.4 | 18.0 / 8.4 / 4.4 | 17.9p/8.0a/2.0r (15G, 2TM) | **15+ PTS**: 7/8 (87.5%) \| **8+ AST**: 7/8 (87.5%) | Available |
| **WAS** | Active Scorer / Active C REB | Kyshawn George (F) / Alex Sarr (C) | 8/8 \| 7/8 | 32.8 / 25.1 | George **17.2p**/4.8a \| Sarr 9.6p/**6.0r** | George 17.4p/5.6a \| Sarr 10.8p/5.8r | George 14.8p/4.5a \| Sarr 16.3p/7.4r | George **10+ PTS & 3+ AST**: 7/8 (87.5%) | Available *(Champagnie Out)* |

---

## PART C — PLAYER LAST-10-GAME REPORT (TODAY'S 9 FIXTURES)

Every selected rotation leader across tonight's **18 competing teams** is profiled below in exact chronological order (`G1` -> `GN` of 2026–27). Because all teams have played `7–9` games so far in `2026–27`, `Last-N` equals `2026–27 Season`. All DNP dates are explicitly reported and excluded from averages.

### Fixture 1: Washington Wizards (`4-4`) @ Atlanta Hawks (`5-4`)

#### 1. Anthony Davis (`WAS` — F/C) | Primary Scorer #1 & Rebound Leader | **Questionable (Right Ankle Sprain)**
- **2026–27 Chronological Log (`N = 8/8 GP`, 8 Starts, 0 DNPs)**:
  - `G1 10-21` vs MIL (`W 128-116`, Start): **34 MIN** | **34 PTS**, **4 AST**, **12 REB** (3o/9d) | FG `11-20`, 3P `1-3`, FT `11-14` | PF:2 | Normal
  - `G2 10-23` vs TOR (`L 102-112`, Start): **32 MIN** | **9 PTS**, **0 AST**, **9 REB** (0o/9d) | FG `3-12`, 3P `0-2`, FT `3-4` | PF:2 | Cold shooting
  - `G3 10-24` @ CHI (`W 124-120`, Start): **31 MIN** | **19 PTS**, **5 AST**, **6 REB** (2o/4d) | FG `8-21`, 3P `0-1`, FT `3-5` | PF:3 | B2B 2nd night
  - `G4 10-26` @ CHA (`L 103-110`, Start): **36 MIN** | **29 PTS**, **0 AST**, **10 REB** (0o/10d) | FG `11-22`, 3P `3-6`, FT `4-4` | PF:2 | Normal
  - `G5 10-28` @ CLE (`L 111-121`, Start): **34 MIN** | **18 PTS**, **3 AST**, **5 REB** (1o/4d) | FG `8-18`, 3P `2-5`, FT `0-0` | PF:2 | Normal
  - `G6 10-30` vs CHA (`W 95-79`, Start): **34 MIN** | **25 PTS**, **1 AST**, **13 REB** (3o/10d) | FG `8-17`, 3P `0-1`, FT `9-10` | PF:1 | Blowout (+16)
  - `G7 11-02` @ ORL (`W 103-94`, Start): **34 MIN** | **27 PTS**, **1 AST**, **9 REB** (1o/8d) | FG `12-17`, 3P `1-1`, FT `2-2` | PF:2 | Normal
  - `G8 11-04` vs ATL (`L 105-120`, Start): **30 MIN** | **26 PTS**, **3 AST**, **10 REB** (2o/8d) | FG `12-19`, 3P `0-1`, FT `2-2` | PF:0 | Blowout (-15), ankle tweak
- **Required Summary Metrics**:
  - **PTS / AST / REB**: Last-8 (`26–27`): **23.4 / 2.1 / 9.2** | Last-5: **25.0 / 1.6 / 9.4** | Separate `25–26` (DAL, 20G): `20.4 / 2.8 / 11.1` (`31.3` MIN).
  - **Minutes**: Mean **33.1** (L5 `33.6`), Med **34.0**, Min `30`, Max `36`, SD `1.83` (`30+m`: 8/8, `35+m`: 1/8; Close `33.5`, Blowout `32.0`).
  - **Consistency**: PTS `[Med 25.5, Min 9, Max 34, SD 7.26]` | AST `[Med 2.0, Min 0, Max 5, SD 1.76]` | REB `[Med 9.5, Min 5, Max 13, SD 2.54]`.
  - **Opportunities & Trend**: `18.2` FGA, `2.5` 3PA, `5.1` FTA | `USG% 30.1%`, `TS% .570`, `ORB% 5.3%`, `DRB% 23.7%`, `TRB% 15.1%`. **Trend**: **Improving** (25+ PTS in 4 of L5, including `26p/10r` on `12-19` FG vs ATL two nights ago), but **Availability** is **Questionable (Right Ankle Sprain)** ahead of a Sat `@ OKC` B2B (`32–34` MIN if cleared; `0` if held out).

#### 2. Trae Young (`WAS` — G) | Primary Scorer #2 & Assist Leader | **Available**
- **2026–27 Chronological Log (`N = 8/8 GP`, 8 Starts, 0 DNPs)**:
  - `G1 10-21` vs MIL (`W 128-116`, Start): **38 MIN** | **20 PTS**, **13 AST**, **0 REB** | FG `4-13`, 3P `0-6`, FT `12-16` | PF:4 | FoulTrbl (4PF)
  - `G2 10-23` vs TOR (`L 102-112`, Start): **37 MIN** | **22 PTS**, **12 AST**, **1 REB** (0o/1d) | FG `5-15`, 3P `4-10`, FT `8-10` | PF:3 | Normal
  - `G3 10-24` @ CHI (`W 124-120`, Start): **34 MIN** | **25 PTS**, **9 AST**, **4 REB** (0o/4d) | FG `6-13`, 3P `4-10`, FT `9-9` | PF:3 | Normal
  - `G4 10-26` @ CHA (`L 103-110`, Start): **38 MIN** | **22 PTS**, **10 AST**, **6 REB** (0o/6d) | FG `10-20`, 3P `1-4`, FT `1-1` | PF:1 | Normal
  - `G5 10-28` @ CLE (`L 111-121`, Start): **34 MIN** | **14 PTS**, **8 AST**, **5 REB** (0o/5d) | FG `3-12`, 3P `1-7`, FT `7-7` | PF:1 | Normal
  - `G6 10-30` vs CHA (`W 95-79`, Start): **38 MIN** | **21 PTS**, **9 AST**, **6 REB** (1o/5d) | FG `4-9`, 3P `1-5`, FT `12-14` | PF:1 | Blowout (+16)
  - `G7 11-02` @ ORL (`W 103-94`, Start): **34 MIN** | **15 PTS**, **9 AST**, **3 REB** (0o/3d) | FG `5-12`, 3P `2-6`, FT `3-5` | PF:0 | Normal
  - `G8 11-04` vs ATL (`L 105-120`, Start): **34 MIN** | **18 PTS**, **6 AST**, **2 REB** (0o/2d) | FG `6-12`, 3P `2-6`, FT `4-4` | PF:4 | Blowout (-15), 4PF
- **Required Summary Metrics**:
  - **PTS / AST / REB**: Last-8 (`26–27`): **19.6 / 9.5 / 3.4** | Last-5: **18.0 / 8.4 / 4.4** | Separate `25–26` (2TM, 15G): `17.9 / 8.0 / 2.0` (`25.6` MIN).
  - **Minutes**: Mean **35.9** (L5 `35.6`), Med **35.5**, Min `34`, Max `38`, SD `1.90` (`30+m`: 8/8, `35+m`: 4/8; Close `35.8`, Blowout `36.0`).
  - **Consistency**: PTS `[Med 20.5, Min 14, Max 25, SD 3.50]` | AST `[Med 9.0, Min 6, Max 13, SD 2.06]` | REB `[Med 3.5, Min 0, Max 6, SD 2.12]`.
  - **Opportunities & Trend**: `13.2` FGA, `6.8` 3PA, `8.2` FTA | `USG% 24.5%`, `TS% .581`, `AST% 39.7%`. **Trend**: **Stable** elite floor (`34+` MIN in all 8 games; first return game in Atlanta since trade; usage jumps toward `30%+` if AD sits). Expected **35–37 MIN**.

#### 3. Kyshawn George (`WAS` — F) & Alex Sarr (`WAS` — C) | Active Replacement Scorer & Active Center Rebounder | **Available**
- **Kyshawn George (`N = 8/8 GP`, 8 Starts, 0 DNPs)**:
  - Chronological (`10-21` to `11-04`): `G1 vs MIL` (`29m, 18p/3a/5r, 8-14 FG, 4PF`), `G2 vs TOR` (`26m, 11p/3a/3r, 2-9 FG, 5PF`), `G3 @ CHI` (`36m, 22p/4a/9r, 8-17 FG`), `G4 @ CHA` (`29m, 20p/2a/4r, 8-14 FG, 5PF`), `G5 @ CLE` (`38m, 8p/11a/2r, 4-10 FG`), `G6 vs CHA` (`32m, 12p/3a/3r, 4-10 FG`), `G7 @ ORL` (`37m, 22p/5a/4r, 9-15 FG`), `G8 vs ATL` (`35m, 25p/7a/4r, 10-14 FG, 3-7 3P, 4PF`).
  - **Summary**: `26–27`: **17.2p / 4.8a / 4.2r** (L5: **17.4p / 5.6a / 3.4r**; Separate `25–26`: `14.8p/4.5a/5.1r`). MIN Mean **32.8** (Med `33.5`, Min `26`, Max `38`, SD `4.12`). Consistency: PTS `[Med 19.0, Min 8, Max 25, SD 5.76]`, AST `[Med 3.5, Min 2, Max 11, SD 2.77]`. Opp: `12.9` FGA, `5.5` 3PA, `USG% 23.4%`, `TS% .612`, `AST% 24.2%`. **Trend**: **Surging** (`23.5p / 6.0a` over L2). Expected **34–36 MIN** (primary wing scorer if AD sits).
- **Alex Sarr (`N = 7/8 GP`, 7 Starts; Missed `11-02 @ ORL` — 1 DNP; Note: Justin Champagnie `7.5 RPG` is `Out - Right Foot Surgery`)**:
  - Chronological (`10-21` to `11-04`): `G1 vs MIL` (`24m, 6p/2a/9r`), `G2 vs TOR` (`25m, 7p/5a/4r, 4PF`), `G3 @ CHI` (`23m, 10p/3a/2r, 4PF`), `G4 @ CHA` (`26m, 12p/1a/6r`), `G5 @ CLE` (`26m, 18p/2a/4r, 7-11 FG`), `G6 vs CHA` (`29m, 3p/0a/8r`), `G7 vs ATL` (`23m, 11p/1a/9r, 3-6 FG, 5-6 FT`).
  - **Summary**: `26–27`: **9.6p / 2.0a / 6.0r** (L5: `10.8p / 1.4a / 5.8r`; Separate `25–26`: `16.3p/2.7a/7.4r`). MIN Mean **25.1** (Med `25.0`, Min `23`, Max `29`, SD `1.96`). `TRB% 13.0%`. Expected **25–27 MIN** if AD plays, **30–32 MIN** as lone center if AD sits.

#### 4. Nickeil Alexander-Walker (`ATL` — G) | Primary Scorer #1 | **Available**
- **2026–27 Chronological Log (`N = 9/9 GP`, 9 Starts, 0 DNPs)**:
  - `G1 10-21` @ ORL (`W 132-125`, Start): **30 MIN** | **31 PTS**, **3 AST**, **4 REB** (3o/1d) | FG `8-15`, 3P `5-8`, FT `10-13` | PF:3 | Normal
  - `G2 10-23` @ CHA (`W 128-81`, Start): **27 MIN** | **14 PTS**, **5 AST**, **3 REB** (0o/3d) | FG `5-12`, 3P `2-7`, FT `2-2` | PF:1 | Blowout (+47)
  - `G3 10-24` vs HOU (`L 114-121`, Start): **32 MIN** | **18 PTS**, **4 AST**, **5 REB** (2o/3d) | FG `7-16`, 3P `4-12`, FT `0-1` | PF:1 | Normal
  - `G4 10-26` @ HOU (`L 110-120`, Start): **29 MIN** | **12 PTS**, **3 AST**, **2 REB** (1o/1d) | FG `5-13`, 3P `2-7`, FT `0-2` | PF:4 | FoulTrbl (4PF)
  - `G5 10-28` vs MIA (`L 117-129`, Start): **32 MIN** | **23 PTS**, **1 AST**, **3 REB** (0o/3d) | FG `8-18`, 3P `5-9`, FT `2-2` | PF:3 | Normal
  - `G6 10-29` vs CLE (`W 114-111`, Start): **31 MIN** | **25 PTS**, **1 AST**, **3 REB** (2o/1d) | FG `8-17`, 3P `4-12`, FT `5-5` | PF:3 | Normal
  - `G7 10-31` @ NOP (`L 99-121`, Start): **29 MIN** | **12 PTS**, **1 AST**, **2 REB** (2o/0d) | FG `3-12`, 3P `0-7`, FT `6-6` | PF:1 | Blowout (-22)
  - `G8 11-02` @ IND (`W 108-104`, Start): **31 MIN** | **34 PTS**, **4 AST**, **4 REB** (3o/1d) | FG `12-25`, 3P `9-15`, FT `1-1` | PF:4 | Jalen Johnson Out
  - `G9 11-04` @ WAS (`W 120-105`, Start): **32 MIN** | **26 PTS**, **2 AST**, **4 REB** (1o/3d) | FG `9-20`, 3P `6-14`, FT `2-2` | PF:3 | Jalen Johnson Out
- **Required Summary Metrics**:
  - **PTS / AST / REB**: Last-9 (`26–27`): **21.7 / 2.7 / 3.3** | Last-5: **24.0 / 1.8 / 3.2** | Separate `25–26` (ATL, 78G): `20.8 / 3.7 / 3.4` (`33.4` MIN).
  - **Minutes**: Mean **30.3** (L5 `31.0`), Med **31.0**, Min `27`, Max `32`, SD `1.63` (`30+m`: 6/9, `35+m`: 0/9; Close `30.8`, Blowout `29.3`).
  - **Consistency**: PTS `[Med 23, Min 12, Max 34, SD 7.67]` | AST `[Med 3, Min 1, Max 5, SD 1.41]` | REB `[Med 3, Min 2, Max 5, SD 0.94]`.
  - **Opportunities & Trend**: `16.4` FGA (`22.5` FGA without Jalen Johnson!), `10.1` 3PA (`14.5` 3PA without Johnson!), `3.8` FTA | `USG% 26.8%`, `TS% .598`. **Trend**: **Explosive upward surge** without Johnson (`30.0 PPG` over L2) against a WAS perimeter allowing `42.4` 3PA/g. Expected **31–32 MIN**.

#### 5. Jalen Johnson (`ATL` — F) | Scorer #2, Assist Leader & Rebound Leader | **Questionable (Left Ankle Sprain)**
- **2026–27 Chronological Log (`N = 7/9 GP`, 7 Starts; Missed `11-02 @ IND` & `11-04 @ WAS` — Left Ankle Sprain)**:
  - `G1 10-21` @ ORL (`W 132-125`, Start): **28 MIN** | **20 PTS**, **6 AST**, **14 REB** (0o/14d) | FG `7-19`, 3P `0-4`, FT `6-7` | PF:5 | FoulTrbl (5PF)
  - `G2 10-23` @ CHA (`W 128-81`, Start): **29 MIN** | **19 PTS**, **8 AST**, **7 REB** (1o/6d) | FG `9-16`, 3P `0-3`, FT `1-1` | PF:2 | Blowout (+47)
  - `G3 10-24` vs HOU (`L 114-121`, Start): **38 MIN** | **26 PTS**, **16 AST**, **9 REB** (4o/5d) | FG `8-19`, 3P `2-7`, FT `8-10` | PF:2 | Normal
  - `G4 10-26` @ HOU (`L 110-120`, Start): **36 MIN** | **21 PTS**, **3 AST**, **9 REB** (1o/8d) | FG `5-14`, 3P `1-5`, FT `10-12` | PF:5 | FoulTrbl (5PF)
  - `G5 10-28` vs MIA (`L 117-129`, Start): **36 MIN** | **12 PTS**, **11 AST**, **9 REB** (0o/9d) | FG `4-12`, 3P `2-4`, FT `2-3` | PF:3 | Normal
  - `G6 10-29` vs CLE (`W 114-111`, Start): **34 MIN** | **17 PTS**, **7 AST**, **8 REB** (1o/7d) | FG `7-16`, 3P `2-5`, FT `1-1` | PF:3 | Normal
  - `G7 10-31` @ NOP (`L 99-121`, Start): **28 MIN** | **13 PTS**, **4 AST**, **7 REB** (0o/7d) | FG `5-11`, 3P `1-3`, FT `2-2` | PF:3 | Blowout (-22), ankle sprain
- **Required Summary Metrics**:
  - **PTS / AST / REB**: Last-7 (`26–27`): **18.3 / 7.9 / 9.0** | Last-5: **17.8 / 8.2 / 8.4** | Separate `25–26` (ATL, 72G): `22.5 / 7.9 / 10.3` (`35.2` MIN).
  - **Minutes**: Mean **32.7** (L5 `34.4`), Med **34.0**, Min `28`, Max `38`, SD `3.95` (`30+m`: 4/7, `35+m`: 3/7; Close `34.4`, Blowout `28.5`).
  - **Consistency**: PTS `[Med 19, Min 12, Max 26, SD 4.46]` | AST `[Med 7, Min 3, Max 16, SD 4.12]` | REB `[Med 9, Min 7, Max 14, SD 2.20]`.
  - **Opportunities & Trend**: `15.3` FGA, `4.4` 3PA, `5.1` FTA | `USG% 25.5%`, `TS% .521`, `AST% 35.4%`, `DRB% 28.4%`. **Availability**: **Questionable** after missing 2 games (`30–33` MIN if active; ATL plays BKN tomorrow on B2B, creating minutes-cap risk on return).

#### 6. Onyeka Okongwu (`ATL` — F/C), Dyson Daniels (`ATL` — G) & CJ McCollum (`ATL` — G) | Active Replacements | **Available**
- **Onyeka Okongwu (`N = 9/9 GP`, 9 Starts, 0 DNPs)**:
  - Chronological (`10-21` to `11-04`): `G1 @ ORL` (`29m, 8p/7a/5r`), `G2 @ CHA` (`22m, 10p/1a/4r, +47 blowout`), `G3 vs HOU` (`26m, 8p/2a/6r`), `G4 @ HOU` (`29m, 11p/1a/9r`), `G5 vs MIA` (`31m, 11p/4a/4r, 5PF`), `G6 vs CLE` (`33m, 29p/2a/12r, 11-17 FG`), `G7 @ NOP` (`28m, 6p/1a/10r, 5PF`), `G8 @ IND` (`33m, 13p/3a/10r`), `G9 @ WAS` (`31m, 14p/4a/16r, 3o/13d`).
  - **Summary**: `26–27`: **12.2p / 2.8a / 8.4r** (L5: **14.6p / 2.8a / 10.4r**; `13.0 RPG` in 2G without Johnson; Separate `25–26`: `15.2p/3.1a/7.6r`). MIN Mean **29.1** (L5 `31.2`, Med `29`, Min `22`, Max `33`, SD `3.31`). REB `[Med 9, Min 4, Max 16, SD 3.83]`, `ORB% 10.2%`, `DRB% 21.7%`. **Trend**: **Strong rebounding surge** (`10+` REB in 4 straight games). Expected **31–33 MIN**.
- **Dyson Daniels (`N = 9/9 GP`, 9 Starts, 0 DNPs)**:
  - Chronological (`10-21` to `11-04`): `G1 @ ORL` (`35m, 20p/3a/4r`), `G2 @ CHA` (`23m, 11p/5a/9r`), `G3 vs HOU` (`29m, 18p/3a/8r, 6PF`), `G4 @ HOU` (`28m, 4p/4a/0r`), `G5 vs MIA` (`28m, 7p/7a/4r`), `G6 vs CLE` (`32m, 4p/5a/6r`), `G7 @ NOP` (`27m, 8p/3a/4r`), `G8 @ IND` (`31m, 6p/4a/9r`), `G9 @ WAS` (`34m, 8p/8a/16r, 7o/9d`).
  - **Summary**: `26–27`: **9.6p / 4.7a / 6.7r** (L5: `6.6p / 5.4a / 7.8r`; `6.0a / 12.5r` in 2G without Johnson; Separate `25–26`: `11.9p/5.9a/6.8r`). MIN Mean **29.7** (Med `29`, Min `23`, Max `35`, SD `3.53`). AST `[Med 4, Min 3, Max 8, SD 1.70]` (**9/9 at 3+ AST**). Expected **30–33 MIN**.
- **CJ McCollum (`N = 9/9 GP`, 8 Starts, 0 DNPs)**:
  - Chronological (`10-21` to `11-04`): `G1 @ ORL` (`25m, 19p/3a/2r`), `G2 @ CHA` (`22m, 13p/1a/1r`), `G3 vs HOU` (`30m, 17p/1a/2r`), `G4 @ HOU` (`30m, 20p/3a/1r`), `G5 vs MIA` (`20m, 13p/1a/2r`), `G6 vs CLE` (`31m, 5p/8a/3r`), `G7 @ NOP` (`24m, 14p/2a/2r`), `G8 @ IND` (`32m, 13p/12a/9r`), `G9 @ WAS` (`Bench, 25m, 15p/5a/5r`).
  - **Summary**: `26–27`: **14.3p / 4.0a / 3.0r** (L5: `12.0p / 5.6a / 4.2r`; `8.5 APG` without Johnson; Separate `25–26`: `18.7p/3.9a/3.3r`). MIN Mean **26.6** (SD `4.06`; moved to 6th-man creator role on Nov 4). Expected **26–29 MIN**.

---

### Fixture 2: Boston Celtics (`6-2`) @ Charlotte Hornets (`3-6`)

#### 7. Jayson Tatum (`BOS` — F) | Primary Scorer #1 & Assist Leader | **Available**
- **2026–27 Chronological Log (`N = 7/8 GP`, 7 Starts; Missed `11-04 vs MIL` — 1 DNP)**:
  - `G1 10-20` @ DET (`L 113-121`, Start): **38 MIN** | **13 PTS**, **11 AST**, **4 REB** (1o/3d) | FG `6-23`, 3P `0-7`, FT `1-1` | PF:3 | Cold 3PT
  - `G2 10-23` vs NYK (`W 107-103`, Start): **37 MIN** | **36 PTS**, **7 AST**, **9 REB** (1o/8d) | FG `14-26`, 3P `3-10`, FT `5-5` | PF:2 | Normal
  - `G3 10-26` vs CHI (`W 134-99`, Start): **28 MIN** | **23 PTS**, **6 AST**, **7 REB** (1o/6d) | FG `7-17`, 3P `2-5`, FT `7-8` | PF:4 | Blowout (+35)
  - `G4 10-27` vs BKN (`W 125-124 OT`, Start): **42 MIN** | **40 PTS**, **8 AST**, **5 REB** (0o/5d) | FG `10-20`, 3P `2-7`, FT `18-22` | PF:3 | OT
  - `G5 10-30` vs CHI (`W 125-111`, Start): **35 MIN** | **26 PTS**, **7 AST**, **7 REB** (0o/7d) | FG `9-20`, 3P `2-7`, FT `6-8` | PF:5 | FoulTrbl (5PF)
  - `G6 11-01` @ ORL (`W 108-97`, Start): **34 MIN** | **32 PTS**, **7 AST**, **4 REB** (1o/3d) | FG `8-19`, 3P `1-5`, FT `15-17` | PF:0 | Normal
  - `G7 11-02` @ HOU (`L 93-109`, Start): **32 MIN** | **19 PTS**, **9 AST**, **6 REB** (0o/6d) | FG `5-16`, 3P `1-7`, FT `8-8` | PF:4 | Blowout (-16), B2B
- **Required Summary Metrics**:
  - **PTS / AST / REB**: Last-7 (`26–27`): **27.0 / 7.9 / 6.0** | Last-5: **28.0 / 7.4 / 5.8** | Separate `25–26` (BOS, 16G): `21.8 / 5.3 / 10.0` (`32.6` MIN).
  - **Minutes**: Mean **35.1** (L5 `34.2`), Med **35.0**, Min `28`, Max `42`, SD `4.16` (`30+m`: 6/7, `35+m`: 4/7; Close `37.8`, Blowout `30.0`).
  - **Consistency**: PTS `[Med 26, Min 13, Max 40, SD 8.88]` | AST `[Med 7, Min 6, Max 11, SD 1.55]` | REB `[Med 6, Min 4, Max 9, SD 1.69]`.
  - **Opportunities & Trend**: `20.1` FGA, `6.9` 3PA, `9.9` FTA | `USG% 33.0%`, `TS% .551`, `AST% 39.1%`. **Trend**: **Elite point-forward playmaking** (`6+` AST in 7/7, `7+` AST in 6/7) and rested since Nov 2 (`3` full rest days). Expected **35–36 MIN** (`29–31` MIN if BOS blows out CHA).

#### 8. Paul George (`BOS` — F), Derrick White (`BOS` — G) & Neemias Queta (`BOS` — C) | **Available**
- **Paul George (`N = 7/8 GP`, 7 Starts; Missed `11-02 @ HOU` B2B rest — 1 DNP)**:
  - Chronological (`10-20` to `11-04`): `G1 @ DET` (`31m, 38p/3a/5r, 7-12 3P, 5PF`), `G2 vs NYK` (`34m, 15p/2a/7r, 4PF`), `G3 vs CHI` (`25m, 16p/2a/5r, +35 blowout`), `G4 vs BKN` (`OT, 36m, 20p/7a/7r`), `G5 vs CHI` (`27m, 18p/8a/6r`), `G6 @ ORL` (`33m, 17p/8a/6r`), `G7 vs MIL` (`35m, 25p/5a/3r, 5-9 3P, Tatum Out`).
  - **Summary**: `26–27`: **21.3p / 5.0a / 5.6r** (L5: `19.2p / 6.0a / 5.4r`; Separate `25–26` PHI, 37G: `17.3p/3.6a/5.3r`). MIN Mean **31.6** (Med `33`, Min `25`, Max `36`, SD `3.85`; Close `33.8`, Blowout `25.0`). Consistency: PTS `[Med 18, Min 15, Max 38, SD 7.48 — 38-pt G1 inflates mean above 18.0 median]`, REB `[Med 6, Min 3, Max 7, SD 1.29]`. Opp: `16.1` FGA, `8.3` 3PA, `USG% 28.3%`, `TS% .599`, `AST% 27.4%`. **Trend**: **Rock-solid 15+ PTS floor (`7/7`)** and elevated playmaking (`5+` AST in 4 straight). Expected **32–34 MIN**.
- **Derrick White (`N = 8/8 GP`, 8 Starts, 0 DNPs)**:
  - Chronological: `G1 @ DET` (`36m, 17p/8a/1r`), `G2 vs NYK` (`33m, 12p/6a/4r`), `G3 vs CHI` (`18m, 5p/4a/6r, +35 blowout`), `G4 vs BKN` (`OT, 33m, 16p/7a/5r`), `G5 vs CHI` (`26m, 9p/4a/2r`), `G6 @ ORL` (`34m, 12p/2a/2r`), `G7 @ HOU` (`30m, 7p/3a/2r`), `G8 vs MIL` (`36m, 24p/7a/4r, Tatum Out`).
  - **Summary**: `26–27`: **12.8p / 5.1a / 3.2r** (L5: `13.6p / 4.6a / 3.0r`; Separate `25–26`: `16.5p/5.4a/4.4r`). MIN Mean **30.8** (Close `34.4`, Blowout `24.0`). `AST% 25.3%`. Extra ball-handling if Payton Pritchard (`Questionable — Right Eye Abrasion`, `13.0p/3.6a` in `26.8m`) sits. Expected **32–35 MIN**.
- **Neemias Queta (`N = 8/8 GP`, 3 Starts — promoted to starter in L3, 0 DNPs)**:
  - Chronological: `G1 @ DET` (`Bench 22m, 3p/2a/4r`), `G2 vs NYK` (`Bench 22m, 15p/1a/6r`), `G3 vs CHI` (`Bench 19m, 7p/1a/5r`), `G4 vs BKN` (`Bench OT 15m, 7p/2a/3r, 6PF`), `G5 vs CHI` (`Bench 20m, 13p/0a/6r`), `G6 @ ORL` (`Start 27m, 8p/1a/8r`), `G7 @ HOU` (`Start 26m, 16p/1a/6r`), `G8 vs MIL` (`Start 29m, 9p/3a/12r`).
  - **Summary**: `26–27`: **9.8p / 1.4a / 6.2r** (L5: `10.6p / 1.4a / 7.0r`; **8.7 RPG in 27.3 MPG across 3 starts**; Separate `25–26`: `10.2p/1.7a/8.4r`). `ORB% 10.8%`, `DRB% 19.7%`. **Trend**: **Rising role security** since entering starting five Nov 1. Expected **26–28 MIN**.

#### 9. Brandon Miller (`CHA` — F) & Naz Reid (`CHA` — C) | Primary Scorers #1 & #2 / Active Rebound Leader | **Available**
- **Brandon Miller (`N = 9/9 GP`, 9 Starts, 0 DNPs)**:
  - `G1 10-21` @ BKN (`W 110-103`, Start): **36 MIN** | **18p / 1a / 3r** | FG `7-21`, 3P `3-14`, FT `1-2` | PF:3
  - `G2 10-23` vs ATL (`L 81-128`, Start): **23 MIN** | **6p / 0a / 2r** | FG `2-14`, 3P `1-11`, FT `1-1` | PF:2 | Blowout (-47)
  - `G3 10-24` vs MIA (`W 115-110`, Start): **36 MIN** | **34p / 4a / 8r** | FG `10-29`, 3P `3-10`, FT `11-12` | PF:1
  - `G4 10-26` vs WAS (`W 110-103`, Start): **36 MIN** | **39p / 1a / 6r** | FG `15-28`, 3P `5-10`, FT `4-5` | PF:3
  - `G5 10-28` @ DET (`L 89-97`, Start): **38 MIN** | **31p / 3a / 12r** | FG `12-26`, 3P `3-10`, FT `4-5` | PF:3
  - `G6 10-30` @ WAS (`L 79-95`, Start): **37 MIN** | **19p / 2a / 7r** | FG `7-24`, 3P `3-13`, FT `2-2` | PF:2 | Blowout (-16)
  - `G7 10-31` vs PHI (`L 104-109`, Start): **33 MIN** | **24p / 5a / 5r** | FG `8-20`, 3P `5-12`, FT `3-4` | PF:4
  - `G8 11-02` vs DET (`L 91-124`, Start): **31 MIN** | **17p / 4a / 1r** | FG `7-18`, 3P `3-11`, FT `0-0` | PF:1 | Blowout (-33)
  - `G9 11-04` @ BKN (`L 104-114`, Start): **26 MIN** | **10p / 1a / 4r** | FG `2-15`, 3P `1-10`, FT `5-5` | PF:5 | FoulTrbl (5PF)
  - **Summary**: `26–27`: **22.0p / 2.3a / 5.3r** (L5: `20.2p / 3.0a / 5.8r`; Separate `25–26`: `20.2p/3.3a/4.9r`). MIN Mean **32.9** (Med `36.0`, Min `23`, Max `38`, SD `4.95`). PTS `[Med 19, Min 6, Max 39, SD 10.37]`. Opp: Massive `21.7` FGA & `11.2` 3PA (`USG% 33.3%`), but poor `TS% .470`. **Trend**: **Declining efficiency** over L4, facing Tatum/PG13/White wing defense. Expected **33–35 MIN** (`27–29` in blowout).
- **Naz Reid (`N = 9/9 GP`, 9 Starts, 0 DNPs)**:
  - Chronological (`10-21` to `11-04`): `G1 @ BKN` (`33m, 20p/7a/11r, 4-10 3P`), `G2 vs ATL` (`25m, 17p/2a/6r, -47 blowout`), `G3 vs MIA` (`37m, 23p/0a/9r, 5-8 3P`), `G4 vs WAS` (`29m, 18p/1a/12r`), `G5 @ DET` (`13m, 7p/0a/6r — ShortMin 13m`), `G6 @ WAS` (`31m, 12p/1a/11r`), `G7 vs PHI` (`36m, 14p/2a/5r`), `G8 vs DET` (`27m, 13p/2a/6r, -33 blowout`), `G9 @ BKN` (`36m, 28p/2a/9r, 11-18 FG`).
  - **Summary**: `26–27`: **16.9p / 1.9a / 8.3r** (L5: `14.8p / 1.4a / 7.4r`; Separate `25–26` MIN, 77G: `13.6p/2.2a/6.2r`). MIN Mean **29.7** (Med `31`, Min `13`, Max `37`, SD `7.10`). REB `[Med 9, Min 5, Max 12, SD 2.49]` (**9/9 at 5+ REB**), `DRB% 28.0%`. Expected **31–35 MIN** (surges to `34–36` MIN at lone 5-spot if Diabate sits).

#### 10. Moussa Diabate (`CHA` — F/C) & Dennis Schroder (`CHA` — G) | Primary Rebound & Assist Leaders | **Both Questionable**
- **Moussa Diabate (`N = 9/9 GP`, 9 Starts, 0 DNPs) — Questionable (Right Quadriceps Tendinopathy)**:
  - Chronological (`10-21` to `11-04`): `G1 @ BKN` (`34m, 17p/3a/8r [5o]`), `G2 vs ATL` (`21m, 5p/1a/8r [4o], -47 blowout`), `G3 vs MIA` (`22m, 4p/1a/5r`), `G4 vs WAS` (`35m, 11p/3a/17r [11o!]`), `G5 @ DET` (`35m, 9p/2a/9r [5o]`), `G6 @ WAS` (`31m, 10p/1a/12r [7o]`), `G7 vs PHI` (`28m, 10p/3a/8r`), `G8 vs DET` (`24m, 7p/2a/9r [6o], -33 blowout`), `G9 @ BKN` (`29m, 7p/2a/6r [4o], 5PF`).
  - **Summary**: `26–27`: **8.9p / 2.0a / 9.1r** (`5.2 OREB/g!`, `ORB% 19.2%`, `TRB% 17.6%`; L5: `8.6p / 2.0a / 8.8r`; Separate `25–26`: `7.9p/1.9a/8.7r`). MIN Mean **28.8** (SD `5.16`). **9/9 at 5+ REB**, `7/9` at `7+ REB`. **Status**: **Questionable** (`27–29` MIN if active vs BOS's `69.9%` DRB%).
- **Dennis Schroder (`N = 9/9 GP`, 7 Starts — moved to bench L2, 0 DNPs) — Questionable (Left Soreness)**:
  - Chronological (`10-21` to `11-04`): `G1 @ BKN` (`Start 35m, 19p/6a/4r`), `G2 vs ATL` (`Start 20m, 4p/3a/4r, -47`), `G3 vs MIA` (`Start 38m, 25p/5a/6r`), `G4 vs WAS` (`Start 36m, 8p/5a/2r`), `G5 @ DET` (`Start 34m, 14p/5a/4r`), `G6 @ WAS` (`Start 29m, 8p/8a/2r, 6PF`), `G7 vs PHI` (`Start 35m, 4p/7a/3r`), `G8 vs DET` (`Bench 23m, 5p/1a/2r, -33`), `G9 @ BKN` (`Bench 20m, 5p/4a/5r, 5PF`).
  - **Summary**: `26–27`: **10.2p / 4.9a / 3.6r** (L5: `7.2p / 5.0a / 3.2r`; Separate `25–26`: `10.8p/4.9a/2.7r`). MIN Mean **30.0** (`21.5` MIN in L2 off bench; SD `6.80`). **Trend**: **Declining minutes & bench demotion** plus Questionable tag (`22–25` MIN if active; if Out, Sion James `25.3m, 2.8a` and Grayson Allen `26.4m, 15.7p/2.7a` absorb guard duties).

---

### Fixture 3: Philadelphia 76ers (`8-1`) @ Cleveland Cavaliers (`4-4`)

#### 11. Tyrese Maxey (`PHI` — G) | Primary Scorer #1 | **Available**
- **2026–27 Chronological Log (`N = 9/9 GP`, 9 Starts, 0 DNPs)**:
  - `G1 10-20` @ NYK (`W 106-100`, Start): **40 MIN** | **28 PTS**, **5 AST**, **4 REB** | FG `9-19`, 3P `2-9`, FT `8-9` | PF:3
  - `G2 10-22` vs CLE (`W 114-106`, Start): **42 MIN** | **32 PTS**, **6 AST**, **3 REB** | FG `12-23`, 3P `2-7`, FT `6-8` | PF:4 | H2H vs CLE
  - `G3 10-24` vs MIL (`W 127-116`, Start): **36 MIN** | **26 PTS**, **4 AST**, **4 REB** | FG `9-22`, 3P `4-9`, FT `4-4` | PF:2 | LeBron Out
  - `G4 10-25` vs DET (`L 93-106`, Start): **34 MIN** | **29 PTS**, **4 AST**, **5 REB** | FG `11-24`, 3P `1-5`, FT `6-7` | PF:4 | Embiid Out
  - `G5 10-28` @ IND (`W 114-109`, Start): **36 MIN** | **27 PTS**, **4 AST**, **5 REB** | FG `8-18`, 3P `3-7`, FT `8-9` | PF:3
  - `G6 10-30` vs NYK (`W 98-93`, Start): **38 MIN** | **27 PTS**, **4 AST**, **4 REB** | FG `10-19`, 3P `3-8`, FT `4-7` | PF:1 | Brown Out
  - `G7 10-31` @ CHA (`W 109-104`, Start): **38 MIN** | **38 PTS**, **4 AST**, **4 REB** | FG `13-23`, 3P `4-9`, FT `8-9` | PF:1 | Embiid & LeBron Out
  - `G8 11-02` vs CHI (`W 126-107`, Start): **36 MIN** | **26 PTS**, **11 AST**, **4 REB** | FG `10-15`, 3P `1-5`, FT `5-6` | PF:3 | Blowout (+19)
  - `G9 11-04` @ DET (`W 112-106`, Start): **34 MIN** | **19 PTS**, **7 AST**, **1 REB** | FG `5-16`, 3P `3-7`, FT `6-6` | PF:3
- **Required Summary Metrics**:
  - **PTS / AST / REB**: Last-9 (`26–27`): **28.0 / 5.4 / 3.8** | Last-5: **27.4 / 6.0 / 3.6** | Separate `25–26` (PHI, 70G): `28.3 / 6.6 / 4.1` (`38.0` MIN).
  - **Minutes**: Mean **37.1** (L5 `36.4`), Med **36.0**, Min `34`, Max `42`, SD `2.51` (`30+m`: 9/9, `35+m`: 7/9; Close `37.7`, Blowout `36.0`).
  - **Consistency**: PTS `[Med 27, Min 19, Max 38, SD 4.81]` | AST `[Med 4, Min 4, Max 11, SD 2.22]` | REB `[Med 4, Min 1, Max 5, SD 1.13]`.
  - **Opportunities & Trend**: `19.9` FGA, `7.3` 3PA, `7.2` FTA | `USG% 29.3%`, `TS% .607`, `AST% 25.8%`. **Trend**: **Ultra-stable** (`25+` PTS in `8/9`, `4+` AST in `9/9`, dropped `32p/6a` in `42m` vs CLE on Oct 22). Expected **37–39 MIN**.

#### 12. Jaylen Brown (`PHI` — G/F), Joel Embiid (`PHI` — C) & LeBron James (`PHI` — F) | **All Available**
- **Jaylen Brown (`N = 8/9 GP`, 8 Starts; Missed `10-30 vs NYK` — 1 DNP)**:
  - Chronological (`10-20` to `11-04`): `G1 @ NYK` (`35m, 19p/6a/8r`), `G2 vs CLE` (`38m, 21p/4a/8r, 10-20 FG`), `G3 vs MIL` (`35m, 27p/5a/3r`), `G4 vs DET` (`40m, 16p/4a/4r, 5-20 FG, 5PF`), `G5 @ IND` (`34m, 20p/2a/10r`), `G6 @ CHA` (`38m, 16p/4a/4r`), `G7 vs CHI` (`33m, 25p/5a/11r, +19`), `G8 @ DET` (`37m, 30p/1a/7r, 11-19 FG`).
  - **Summary**: `26–27`: **21.8p / 3.9a / 6.9r** (L5: `21.4p / 3.2a / 7.2r`; Separate `25–26` BOS, 71G: `28.7p/5.1a/6.9r`). MIN Mean **36.2** (Min `33`, Max `40`, SD `2.22`, `30+m`: 8/8). PTS `[Med 20.5, Min 16, Max 30, SD 4.79]` (**8/8 at 15+ PTS**). `16.9` FGA, `USG% 25.2%`, `TS% .568`. Expected **36–37 MIN**.
- **Joel Embiid (`N = 7/9 GP`, 7 Starts; Missed `10-25 vs DET` & `10-31 @ CHA` [B2B 2nd nights] — 2 DNPs)**:
  - Chronological (`10-20` to `11-04`): `G1 @ NYK` (`33m, 13p/6a/11r`), `G2 vs CLE` (`34m, 24p/1a/7r, 8-16 FG, 7-9 FT`), `G3 vs MIL` (`36m, 28p/10a/11r, 12-14 FT, 5PF`), `G4 @ IND` (`39m, 21p/2a/11r`), `G5 vs NYK` (`33m, 10p/7a/7r`), `G6 vs CHI` (`25m, 15p/3a/8r, +19 blowout`), `G7 @ DET` (`33m, 26p/2a/15r, 10-10 FT`).
  - **Summary**: `26–27`: **19.6p / 4.4a / 10.0r** (L5: `20.0p / 4.8a / 10.4r`; Separate `25–26` PHI, 38G: `26.9p/3.9a/7.7r`). MIN Mean **33.3** (Close `34.7`, Blowout `25.0`, SD `3.95`). REB `[Med 11, Min 7, Max 15, SD 2.67]` (**7/7 at 7+ REB**). `15.6` FGA, `7.1` FTA, `USG% 28.2%`, `DRB% 25.5%`. Non-B2B spot tonight (`1` rest day, next game Nov 8); massive interior edge if CLE's Jarrett Allen sits. Expected **33–35 MIN**.
- **LeBron James (`N = 7/9 GP`, 7 Starts; Missed `10-24 vs MIL` & `10-31 @ CHA` — 2 DNPs)**:
  - Chronological (`10-20` to `11-04`): `G1 @ NYK` (`34m, 14p/7a/9r`), `G2 vs CLE` (`33m, 17p/5a/10r`), `G3 vs DET` (`33m, 18p/5a/2r`), `G4 @ IND` (`33m, 13p/10a/5r`), `G5 vs NYK` (`34m, 20p/8a/9r`), `G6 vs CHI` (`31m, 15p/9a/7r, +19`), `G7 @ DET` (`33m, 13p/8a/10r`).
  - **Summary**: `26–27`: **15.7p / 7.4a / 7.4r** (L5: `15.8p / 8.0a / 6.6r`; Separate `25–26` LAL, 60G: `20.9p/7.2a/6.1r`). MIN Mean **33.0** (`Min 31, Max 34, SD 0.93!` — most surgical minute stability in the NBA). PTS `[Med 15, Min 13, Max 20, SD 2.49]`, AST `[Med 8, Min 5, Max 10, SD 1.76]` (**7/7 at 5+ AST**, L4 all `8+ AST`). Homecoming game in Cleveland. Expected **33–34 MIN**.

#### 13. Donovan Mitchell (`CLE` — G), Evan Mobley (`CLE` — C), James Harden (`CLE` — G) & Jarrett Allen (`CLE` — C)
- **Donovan Mitchell (`N = 8/8 GP`, 8 Starts, 0 DNPs) — Available**:
  - Chronological (`10-22` to `11-04`): `G1 @ PHI` (`35m, 32p/3a/10r, 11-19 FG`), `G2 vs BKN` (`35m, 22p/4a/5r`), `G3 vs MIN` (`OT, 38m, 26p/7a/5r`), `G4 vs WAS` (`31m, 19p/7a/5r`), `G5 @ ATL` (`33m, 22p/3a/3r`), `G6 @ MIL` (`24m, 15p/3a/4r, +25 blowout, 5PF`), `G7 vs OKC` (`36m, 17p/11a/5r`), `G8 @ OKC` (`33m, 27p/6a/3r, 5PF`).
  - **Summary**: `26–27`: **22.5p / 5.5a / 5.0r** (L5: `20.0p / 6.0a / 4.0r`; Separate `25–26`: `27.9p/5.7a/4.5r`). MIN Mean **33.1** (Close `34.4`, Blowout `24.0`, SD `3.98`). PTS `[Med 22.0, Min 15, Max 32, SD 5.27]` (**8/8 at 15+ PTS**, **8/8 at 3+ AST**). `16.0` FGA, `7.0` 3PA, `USG% 26.6%`, `TS% .618`. Scored `32 PTS` vs PHI in G1. Expected **34–36 MIN**.
- **Evan Mobley (`N = 8/8 GP`, 8 Starts, 0 DNPs) — Available**:
  - Chronological (`10-22` to `11-04`): `G1 @ PHI` (`34m, 18p/2a/8r`), `G2 vs BKN` (`35m, 20p/4a/10r`), `G3 vs MIN` (`OT, 38m, 18p/3a/10r`), `G4 vs WAS` (`32m, 24p/2a/12r, 5-6 3P`), `G5 @ ATL` (`33m, 11p/7a/4r`), `G6 @ MIL` (`25m, 27p/3a/5r, +25 blowout`), `G7 vs OKC` (`33m, 16p/4a/7r`), `G8 @ OKC` (`33m, 16p/3a/10r — played lone C after Allen exited at 7m`).
  - **Summary**: `26–27`: **18.8p / 3.5a / 8.2r** (L5: `18.8p / 3.8a / 7.6r`; Separate `25–26`: `18.2p/3.6a/9.0r`). MIN Mean **32.9** (Close `34.0`, SD `3.44`). PTS `[Med 18.0, Min 11, Max 27, SD 4.66]`, REB `[Med 9.0, Min 4, Max 12, SD 2.59]`. `12.5` FGA, `4.4` 3PA (`48.6% 3P!`), `TS% .655`. Expected **34–36 MIN** (rebound ceiling jumps to `10–12+` if Jarrett Allen sits).
- **James Harden (`N = 8/8 GP`, 8 Starts, 0 DNPs) — Available**:
  - Chronological (`10-22` to `11-04`): `G1 @ PHI` (`33m, 16p/5a/3r`), `G2 vs BKN` (`33m, 12p/7a/8r, 9-11 FT`), `G3 vs MIN` (`OT, 39m, 19p/9a/5r, 5PF`), `G4 vs WAS` (`34m, 16p/6a/2r`), `G5 @ ATL` (`36m, 24p/4a/5r`), `G6 @ MIL` (`26m, 13p/7a/6r, +25 blowout`), `G7 vs OKC` (`33m, 14p/6a/4r`), `G8 @ OKC` (`35m, 19p/6a/9r`).
  - **Summary**: `26–27`: **16.6p / 6.2a / 5.2r** (L5: `17.2p / 5.8a / 5.2r`; Separate `25–26` 2TM, 70G: `23.6p/8.0a/4.8r`). MIN Mean **33.6** (Close `34.7`, SD `3.46`). AST `[Med 6.0, Min 4, Max 9, SD 1.39]` (**7/8 at 5+ AST**, **8/8 at 4+ AST & 10+ PTS**). Expected **34–35 MIN**.
- **Jarrett Allen (`N = 8/8 GP`, 8 Starts, 0 DNPs) — Questionable (Right Knee Contusion)**:
  - Chronological (`10-22` to `11-04`): `G1 @ PHI` (`28m, 14p/0a/7r`), `G2 vs BKN` (`27m, 21p/0a/8r`), `G3 vs MIN` (`OT, 27m, 10p/2a/9r`), `G4 vs WAS` (`30m, 8p/2a/12r`), `G5 @ ATL` (`30m, 14p/1a/8r`), `G6 @ MIL` (`24m, 25p/4a/11r, +25`), `G7 vs OKC` (`28m, 14p/1a/6r`), `G8 @ OKC` (`7m, 0p/0a/1r — INJURY EXIT: Right Knee Contusion`).
  - **Summary**: `26–27`: **13.2p / 1.2a / 7.8r** (`15.1p / 8.7r` in 7 healthy games before the `7-min` injury exit!). **Status**: **Questionable** (`0` MIN if held out ahead of Sat `vs NYK` B2B; `25–28` MIN if cleared).

---

### Fixture 4: Utah Jazz (`1-7`) @ Dallas Mavericks (`4-4`)

#### 14. Keyonte George (`UTA` — G), Lauri Markkanen (`UTA` — F) & Ace Bailey (`UTA` — G/F) | **All Available**
- **Keyonte George (`N = 8/8 GP`, 8 Starts, 0 DNPs)**:
  - `G1 10-21` @ MEM (`L 103-123`, Start): **29m** | **22p / 5a / 3r** | FG `7-12`, 3P `4-6`, FT `4-7` | PF:4 | Blowout (-20)
  - `G2 10-23` vs NOP (`W 120-119`, Start): **32m** | **19p / 10a / 1r** | FG `6-12`, 3P `3-7`, FT `4-6` | PF:2
  - `G3 10-25` vs LAL (`L 123-132`, Start): **33m** | **24p / 10a / 9r** | FG `7-13`, 3P `2-6`, FT `8-10` | PF:4
  - `G4 10-26` vs MEM (`L 105-110`, Start): **33m** | **26p / 6a / 3r** | FG `9-17`, 3P `0-3`, FT `8-9` | PF:4
  - `G5 10-28` vs SAS (`L 111-117 OT`, Start): **37m** | **31p / 3a / 4r** | FG `11-27`, 3P `5-12`, FT `4-4` | PF:2 | OT, JJJ & Lauri Out
  - `G6 10-31` vs POR (`L 90-112`, Start): **29m** | **8p / 4a / 3r** | FG `2-10`, 3P `0-4`, FT `4-4` | PF:3 | Blowout (-22)
  - `G7 11-02` @ SAS (`L 97-119`, Start): **22m** | **7p / 0a / 7r** | FG `3-12`, 3P `1-5`, FT `0-0` | PF:0 | Blowout (-22)
  - `G8 11-04` @ NOP (`L 113-120 OT`, Start): **44m** | **39p / 9a / 2r** | FG `14-26`, 3P `2-9`, FT `9-13` | PF:3 | OT
  - **Summary**: `26–27`: **22.0p / 5.9a / 4.0r** (L5: `22.2p / 4.4a / 3.8r`; Separate `25–26`: `23.6p/6.1a/3.7r`). MIN Mean **32.4** (Close `35.8`, Blowout `26.7`, SD `6.00`). PTS `[Med 23.0, Min 7, Max 39, SD 10.12]` — high blowout sensitivity (`7` & `8` PTS in back-to-back 22-pt losses vs `19+` in all 6 competitive/early games). `16.1` FGA (`18.8` FGA without JJJ), `USG% 29.7%`, `AST% 33.5%`. Expected **33–35 MIN** (`26–28` in blowout).
- **Lauri Markkanen (`N = 7/8 GP`, 7 Starts; Missed `10-28 vs SAS` after `6-min` injury exit on `10-26 vs MEM`)**:
  - Chronological: `G1 @ MEM` (`36m, 18p/3a/9r`), `G2 vs NOP` (`34m, 16p/3a/6r`), `G3 vs LAL` (`38m, 28p/1a/7r, 5-11 3P`), `G4 vs MEM` (`6m, 2p/0a/0r — INJURY EXIT [Back spasms]`), `G5 vs POR` (`29m, 13p/1a/6r, 6PF, -22`), `G6 @ SAS` (`31m, 22p/3a/8r`), `G7 @ NOP` (`OT, 39m, 21p/4a/10r, 5-12 3P`).
  - **Summary**: `26–27`: **17.1p / 2.1a / 6.6r** (`19.7p / 7.7r` in `34.5m` excluding the `6-min` injury exit!; Separate `25–26`: `26.7p/2.1a/6.9r`). `13.3` FGA (`15.0` FGA without JJJ), `8.3` 3PA, `TS% .560`. **Trend**: **Fully ramped back up** (`21.5p / 9.0r` over L2). Expected **33–35 MIN**.
- **Ace Bailey (`N = 8/8 GP`, 7 Starts, 0 DNPs)**:
  - Chronological: `G1 @ MEM` (`Bench 24m, 12p/3a/5r`), `G2 vs NOP` (`Start 22m, 6p/2a/7r`), `G3 vs LAL` (`29m, 17p/4a/12r [6o]`), `G4 vs MEM` (`34m, 17p/3a/10r [4o]`), `G5 vs SAS` (`OT, 40m, 19p/0a/6r`), `G6 vs POR` (`37m, 9p/1a/7r, -22`), `G7 @ SAS` (`24m, 5p/2a/6r, -22`), `G8 @ NOP` (`OT, 35m, 15p/1a/5r, 6PF`).
  - **Summary**: `26–27`: **12.5p / 2.0a / 7.2r** (L5: `13.0p / 1.4a / 6.8r`; Separate `25–26`: `13.8p/1.8a/4.2r`). MIN Mean **30.6** (L5 `34.0`). **8/8 at 5+ REB** (`ORB% 7.0%`, `DRB% 18.8%`) facing a DAL defense ranked **29th in DRB% (`67.9%`)**. Expected **32–34 MIN**.

#### 15. Cooper Flagg (`DAL` — F), Kyrie Irving (`DAL` — G), P.J. Washington (`DAL` — F) & Daniel Gafford (`DAL` — C) | **All Available**
- **Cooper Flagg (`N = 7/8 GP`, 7 Starts; Missed `10-24 vs SAS` — 1 DNP)**:
  - `G1 10-21` @ HOU (`L 110-128`, Start): **33m** | **32p / 2a / 5r** | FG `10-17`, 3P `1-4`, FT `11-13` | PF:4 | Blowout (-18)
  - `G2 10-23` @ IND (`W 121-105`, Start): **17m** | **14p / 6a / 5r** | FG `4-6`, 3P `2-2`, FT `4-4` | PF:1 | ShortMin (17m, +34 +/-, minor knock)
  - `G3 10-26` @ MIA (`W 113-109`, Start): **40m** | **29p / 11a / 6r** | FG `12-23`, 3P `2-8`, FT `3-3` | PF:3
  - `G4 10-28` vs OKC (`W 120-96`, Start): **33m** | **26p / 8a / 5r** | FG `10-23`, 3P `2-8`, FT `4-4` | PF:1 | Blowout (+24)
  - `G5 10-30` vs HOU (`W 116-111`, Start): **39m** | **33p / 6a / 9r** | FG `13-19`, 3P `0-4`, FT `7-10` | PF:3
  - `G6 11-02` vs SAC (`L 100-115`, Start): **40m** | **17p / 6a / 4r** | FG `3-19`, 3P `0-4`, FT `11-11` | PF:2 | Kyrie Out
  - `G7 11-04` @ SAS (`L 111-112`, Start): **40m** | **19p / 5a / 10r** | FG `7-19`, 3P `0-3`, FT `5-7` | PF:3
  - **Summary**: `26–27`: **24.3p / 6.3a / 6.3r** (L5: **24.8p / 7.2a / 6.8r**; Separate `25–26` DAL, 70G: `21.0p/4.5a/6.7r`). MIN Mean **34.6** (`38.4` MIN in L5, `39.7` in close games!). PTS `[Med 26, Min 14, Max 33, SD 7.05]`, AST `[Med 6, Min 2, Max 11, SD 2.55]` (`5+` AST in 6 straight!). `18.0` FGA, `7.4` FTA, `USG% 29.9%`, `AST% 29.5%`. Expected **36–38 MIN** (`31–33` in blowout).
- **Kyrie Irving (`N = 6/8 GP`, 6 Starts; Missed `10-24 vs SAS` & `11-02 vs SAC` [rest/load mgmt] — 2 DNPs)**:
  - Chronological: `G1 @ HOU` (`24m, 15p/2a/4r, -18`), `G2 @ IND` (`25m, 24p/3a/1r, 5-10 3P, 6PF`), `G3 @ MIA` (`33m, 18p/6a/6r`), `G4 vs OKC` (`27m, 15p/4a/2r, +24`), `G5 vs HOU` (`35m, 35p/9a/4r, 12-19 FG`), `G6 @ SAS` (`36m, 29p/5a/7r, 9-27 FG, 5-14 3P`).
  - **Summary**: `26–27`: **22.7p / 4.8a / 4.0r** (L5: `24.2p / 5.4a / 4.0r`; Missed `2025–26` due to injury recovery). MIN Mean **30.0** (`35.5` MIN over L2!). **6/6 at 15+ PTS**, `5/5` in L5 at `3+ AST`. `16.8` FGA, `9.2` 3PA, `TS% .617`. Expected **33–35 MIN**.
- **P.J. Washington (`N = 8/8 GP`, 8 Starts, 0 DNPs) & Daniel Gafford (`N = 8/8 GP`, 8 Starts, 0 DNPs)**:
  - **Washington**: `G1 @ HOU` (`31m, 10p/2a/4r`), `G2 @ IND` (`33m, 20p/0a/13r`), `G3 vs SAS` (`36m, 12p/2a/4r`), `G4 @ MIA` (`41m, 20p/2a/9r`), `G5 vs OKC` (`27m, 18p/0a/9r`), `G6 vs HOU` (`34m, 3p/1a/10r`), `G7 vs SAC` (`38m, 12p/1a/5r`), `G8 @ SAS` (`39m, 21p/3a/10r`). `26–27`: **14.5p / 1.4a / 8.0r** (L5: `14.8p / 8.6r`, `5+` REB in 5/5 L5; Separate `25–26`: `14.2p/1.8a/7.0r`). MIN Mean **34.9** (Close `38.0`). Expected **34–36 MIN**.
  - **Gafford**: `26–27`: **9.1p / 2.0a / 6.6r** in **23.2 MIN** (L5: `11.0p / 7.6r` in `25.2m`, Dereck Lively II `Out`; Separate `25–26`: `9.5p/6.9r`). Home/Away split: `14.2 PPG` at home vs `4.0 PPG` away. Expected **24–26 MIN**.

---

### Fixture 5: Oklahoma City Thunder (`6-2`) @ Memphis Grizzlies (`6-2`)

#### 16. Shai Gilgeous-Alexander (`OKC` — G), Ajay Mitchell (`OKC` — G) & Isaiah Hartenstein (`OKC` — C) | **All Available**
- **Shai Gilgeous-Alexander (`N = 8/8 GP`, 8 Starts, 0 DNPs)**:
  - `G1 10-20` @ SAS (`W 116-104`, Start): **36m** | **32p / 4a / 6r** | FG `13-27`, 3P `3-7`, FT `3-4` | PF:2
  - `G2 10-22` vs DEN (`W 96-84`, Start): **35m** | **17p / 3a / 2r** | FG `6-19`, 3P `3-11`, FT `2-2` | PF:0
  - `G3 10-25` vs LAC (`W 108-101`, Start): **36m** | **34p / 5a / 6r** | FG `13-26`, 3P `1-5`, FT `7-8` | PF:2
  - `G4 10-26` vs PHX (`W 125-114`, Start): **30m** | **26p / 3a / 3r** | FG `11-18`, 3P `1-5`, FT `3-4` | PF:5 | 5PF; Chet & J-Dub Out begins
  - `G5 10-28` @ DAL (`L 96-120`, Start): **28m** | **21p / 2a / 6r** | FG `7-19`, 3P `1-6`, FT `6-6` | PF:3 | Blowout (-24)
  - `G6 10-31` @ HOU (`L 98-119`, Start): **31m** | **26p / 3a / 4r** | FG `10-20`, 3P `3-6`, FT `3-4` | PF:1 | Blowout (-21)
  - `G7 11-02` @ CLE (`W 117-112`, Start): **39m** | **43p / 8a / 3r** | FG `14-35`, 3P `4-8`, FT `11-12` | PF:2
  - `G8 11-04` vs CLE (`W 124-116`, Start): **35m** | **42p / 8a / 4r** | FG `11-26`, 3P `5-11`, FT `15-19` | PF:2
  - **Summary**: `26–27`: **30.1p / 4.5a / 4.2r** (L5 without Holmgren & Jalen Williams: **31.6p / 4.8a / 4.0r**; L2: **42.5p / 8.0a**; Separate `25–26`: `31.1p/6.6a/4.3r`). MIN Mean **33.8** (Close `35.2`, Blowout `29.5`). PTS `[Med 29.0, Min 17, Max 43, SD 8.77]`. Massive `23.8` FGA & `7.4` FTA (`USG% 36.2%`). Expected **35–37 MIN**.
- **Ajay Mitchell (`N = 8/8 GP`, 5 Starts — promoted to starter since `10-26`, 0 DNPs)**:
  - Chronological: `G1 @ SAS` (`Bench 23m, 4p/6a/5r`), `G2 vs DEN` (`Bench 23m, 12p/0a/0r`), `G3 vs LAC` (`Bench 28m, 18p/4a/6r`), `G4 vs PHX` (`Start 25m, 30p/5a/2r, 10-16 FG`), `G5 @ DAL` (`Start 28m, 29p/3a/4r, 12-20 FG`), `G6 @ HOU` (`Start 26m, 6p/5a/3r, -21 blowout, 4PF`), `G7 @ CLE` (`Start 35m, 20p/1a/5r`), `G8 vs CLE` (`Start 32m, 23p/4a/7r`).
  - **Summary**: `26–27`: **17.8p / 3.5a / 4.0r** (**21.6p / 3.6a / 4.2r in 29.2 MIN across 5 starts** without J-Dub/Wallace/Chet; Separate `25–26`: `13.6p/3.6a/3.3r`). `15.6` FGA as starter, `TS% .576`. Expected **31–33 MIN**.
- **Isaiah Hartenstein (`N = 8/8 GP`, 8 Starts, 0 DNPs)**:
  - Chronological: `G1 @ SAS` (`17m, 4p/3a/3r, 5PF`), `G2 vs DEN` (`23m, 6p/2a/6r`), `G3 vs LAC` (`27m, 12p/1a/12r`), `G4 vs PHX` (`26m, 15p/3a/13r [6o]`), `G5 @ DAL` (`26m, 10p/3a/14r [4o]`), `G6 @ HOU` (`25m, 10p/0a/7r`), `G7 @ CLE` (`28m, 5p/4a/14r [7o]`), `G8 vs CLE` (`26m, 3p/4a/12r [11d]`).
  - **Summary**: `26–27`: **8.1p / 2.5a / 10.1r** (**12.0 RPG in 26.2 MIN over L5** as sole healthy center with Holmgren & Jaylin Williams Out; Separate `25–26`: `9.2p/3.5a/9.4r`). REB `[Med 12.0, Min 3, Max 14, SD 3.92]`, `ORB% 14.8%`, `DRB% 28.1%`, `TRB% 21.6%`. Expected **26–29 MIN**.

#### 17. Ty Jerome (`MEM` — G), Cameron Boozer (`MEM` — F), Cedric Coward (`MEM` — F) & Cam Spencer (`MEM` — G) | **All Available**
- **Ty Jerome (`N = 7/8 GP`, 7 Starts; Missed `10-31 vs SAC` — 1 DNP)**:
  - `G1 10-21` vs UTA (`W 123-103`, Start): **32m** | **45p / 6a / 7r** | FG `17-25`, 3P `5-10`, FT `6-7` | PF:4 | Blowout (+20)
  - `G2 10-23` @ GSW (`W 111-108`, Start): **32m** | **28p / 5a / 2r** | FG `11-22`, 3P `3-5`, FT `3-5` | PF:1
  - `G3 10-25` @ SAC (`W 123-112`, Start): **32m** | **31p / 7a / 4r** | FG `8-17`, 3P `1-6`, FT `14-14` | PF:1
  - `G4 10-26` @ UTA (`W 110-105`, Start): **30m** | **15p / 8a / 1r** | FG `4-15`, 3P `1-6`, FT `6-7` | PF:4
  - `G5 10-29` @ POR (`W 124-103`, Start): **24m** | **10p / 3a / 2r** | FG `3-12`, 3P `1-5`, FT `3-3` | PF:1 | Blowout (+21)
  - `G6 11-02` vs NOP (`L 134-135 OT`, Start): **37m** | **40p / 5a / 5r** | FG `14-22`, 3P `5-6`, FT `7-8` | PF:0 | OT
  - `G7 11-04` vs IND (`L 103-107`, Start): **29m** | **23p / 3a / 4r** | FG `10-20`, 3P `2-10`, FT `1-2` | PF:2
  - **Summary**: `26–27`: **27.4p / 5.3a / 3.6r** (L5: `23.8p / 5.2a / 3.2r`; Separate `25–26` MEM, 15G: `19.7p/5.7a/2.8r`). MIN Mean **30.9** (Close `32.0`, Blowout `28.0`, SD `3.64`). PTS `[Med 28, Min 10, Max 45, SD 11.70 — two 40+ explosions inflate mean slightly, though median is 28.0]`. `19.0` FGA, `6.6` FTA, `USG% 32.8%`, `TS% .626`, `AST% 29.9%`. Expected **32–34 MIN**.
- **Cameron Boozer (`N = 8/8 GP`, 8 Starts, 0 DNPs)**:
  - Chronological: `G1 vs UTA` (`33m, 7p/5a/11r, 2-15 FG`), `G2 @ GSW` (`37m, 25p/6a/13r`), `G3 @ SAC` (`31m, 14p/4a/11r`), `G4 @ UTA` (`31m, 13p/4a/7r`), `G5 @ POR` (`28m, 18p/12a/12r, +21`), `G6 vs SAC` (`26m, 27p/3a/9r, +31, Jerome Out`), `G7 vs NOP` (`OT, 38m, 18p/5a/9r, 5PF`), `G8 vs IND` (`33m, 10p/4a/6r`).
  - **Summary**: `26–27`: **16.5p / 5.4a / 9.8r** (L5: `17.2p / 5.6a / 8.6r`; `2026–27 NBA Rookie`). MIN Mean **32.1** (Close `34.0`, Blowout `29.0`, SD `3.82`). REB `[Med 10.0, Min 6, Max 13, SD 2.28]`, AST `[Med 4.5, Min 3, Max 12, SD 2.64]`. **8/8 at 3+ AST & 5+ REB**, **7/8 at 7+ REB & 10+ PTS**. With Isaiah Stewart (`Out — Right Knee Bone Bruise`), Boozer's frontcourt load expands. Expected **33–35 MIN**.
- **Cedric Coward (`N = 7/8 GP`, 7 Starts; Missed `10-23 @ GSW`) & Cam Spencer (`N = 8/8 GP`, 1 Start)**:
  - **Coward**: `G1 vs UTA` (`28m, 7p/2a/7r`), `G2 @ SAC` (`32m, 17p/1a/11r`), `G3 @ UTA` (`31m, 16p/3a/11r`), `G4 @ POR` (`27m, 17p/4a/7r`), `G5 vs SAC` (`23m, 10p/2a/7r`), `G6 vs NOP` (`OT, 31m, 10p/3a/9r`), `G7 vs IND` (`33m, 23p/4a/9r`). `26–27`: **14.3p / 2.7a / 8.7r** (**7/7 at 7+ REB!**; Separate `25–26`: `13.6p/5.9r`). Expected **30–32 MIN**.
  - **Spencer**: `G1–G8` (`16m–25m`; `2a, 1a, 1a, 5a, 8a, 13a [Start], 7a, 9a`). `26–27`: **9.1p / 5.8a / 3.8r** in **19.8 MIN** (L5: **8.4 APG** in `21.8m`, `5/5` at `5+ AST`, `AST% 40.7%`; Separate `25–26`: `11.1p/5.6a`). Bench minutes cap (`20–23` MIN) limits floor security vs starters, though Pippen Jr. remains `Out`.

---

### Fixture 6: Toronto Raptors (`4-4`) @ Milwaukee Bucks (`1-7`)

#### 18. Scottie Barnes (`TOR` — F), RJ Barrett (`TOR` — F), Immanuel Quickley (`TOR` — G) & Jamal Shead (`TOR` — G)
- **Scottie Barnes (`N = 8/8 GP`, 8 Starts, 0 DNPs) — Questionable (Left Adductor / Groin Soreness)**:
  - `G1 10-21` vs CHI (`W 135-92`, Start): **26m** | **23p / 5a / 6r** | FG `8-19`, 3P `1-3`, FT `6-6` | PF:2 | Blowout (+43)
  - `G2 10-23` @ WAS (`W 112-102`, Start): **37m** | **28p / 5a / 14r** | FG `12-26`, 3P `1-6`, FT `3-3` | PF:3 | Kawhi last game
  - `G3 10-25` @ MIN (`L 94-117`, Start): **28m** | **0p / 3a / 3r** | FG `0-12`, 3P `0-5`, FT `0-0` | PF:1 | Blowout (-23), outlier 0-12 FG
  - `G4 10-28` vs ORL (`W 129-99`, Start): **31m** | **28p / 4a / 6r** | FG `11-17`, 3P `0-2`, FT `6-6` | PF:3 | Blowout (+30)
  - `G5 10-30` vs ORL (`L 114-121`, Start): **39m** | **41p / 5a / 5r** | FG `19-34`, 3P `1-2`, FT `2-3` | PF:6 | 6PF
  - `G6 11-01` @ LAL (`L 125-131`, Start): **36m** | **29p / 5a / 6r** | FG `11-20`, 3P `0-3`, FT `7-13` | PF:3
  - `G7 11-02` @ LAC (`W 125-118`, Start): **38m** | **22p / 8a / 15r** | FG `7-15`, 3P `0-3`, FT `8-15` | PF:2
  - `G8 11-04` @ DEN (`L 109-128`, Start): **32m** | **17p / 6a / 6r** | FG `7-15`, 3P `1-2`, FT `2-4` | PF:1 | Blowout (-19), adductor soreness
  - **Summary**: `26–27`: **23.5p / 5.1a / 7.6r** (L5: **27.4p / 5.6a / 7.6r**; Separate `25–26`: `18.1p/5.9a/7.5r`). MIN Mean **33.4** (Close `37.5`, Blowout `29.2`, SD `4.53`). `19.8` FGA, `6.2` FTA, `USG% 32.0%`. **Availability**: **Questionable** (`Left Adductor/Groin Soreness`) on the 4th game in 6 nights (`34–36` MIN if active; `0` if held out).
- **RJ Barrett (`N = 8/8 GP`, 8 Starts, 0 DNPs) — Available**:
  - Chronological (`10-21` to `11-04`): `G1 vs CHI` (`26m, 20p/3a/4r, +43`), `G2 @ WAS` (`34m, 23p/4a/9r`), `G3 @ MIN` (`32m, 20p/2a/2r, -23`), `G4 vs ORL` (`32m, 25p/6a/9r, +30`), `G5 vs ORL` (`34m, 9p/5a/3r, 3-10 FG, 4PF`), `G6 @ LAL` (`32m, 22p/5a/10r`), `G7 @ LAC` (`37m, 26p/3a/6r`), `G8 @ DEN` (`33m, 22p/3a/5r`).
  - **Summary**: `26–27`: **20.9p / 3.9a / 6.0r** (L5: `20.8p / 4.4a / 6.6r`; Separate `25–26`: `19.3p/3.3a/5.3r`). MIN Mean **32.5** (Close `34.2`, SD `2.92`, `30+m`: 7/8). PTS `[Med 22.0, Min 9, Max 26, SD 4.91]` (**7/8 at 20+ PTS!**). `16.6` FGA, `USG% 25.1%` (jumps toward `30%+` if Barnes sits). Expected **33–36 MIN**.
- **Immanuel Quickley (`N = 8/8 GP`, 8 Starts, 0 DNPs) & Jamal Shead (`N = 8/8 GP`, 0 Starts, 0 DNPs) — Available**:
  - **Quickley**: `G1 vs CHI` (`28m, 23p/7a/4r`), `G2 @ WAS` (`29m, 12p/6a/1r`), `G3 @ MIN` (`28m, 19p/2a/3r`), `G4 vs ORL` (`29m, 16p/7a/3r`), `G5 vs ORL` (`37m, 17p/8a/6r`), `G6 @ LAL` (`33m, 12p/7a/6r`), `G7 @ LAC` (`38m, 27p/2a/4r, 10-11 FT`), `G8 @ DEN` (`32m, 13p/7a/1r`). `26–27`: **17.4p / 5.8a / 3.5r** (L5: `17.0p / 6.2a`; Separate `25–26`: `16.4p/5.9a/4.0r`). MIN Mean **31.8** (L5 `33.8`). **8/8 at 10+ PTS**, `6/8` at `6+ AST`. Expected **33–35 MIN**.
  - **Shead**: `G1–G8` (`16m–25m`; `5a, 5a, 0a, 7a, 8a, 6a, 6a, 6a`). `26–27`: **5.5p / 5.4a / 2.0r** in **21.5 MIN** (L5: `6.6p / 6.6a`, **7/8 at 5+ AST**, `AST% 30.7%`; Separate `25–26`: `6.6p/5.4a`). Expected **21–24 MIN**.

#### 19. Tyler Herro (`MIL` — G), Jaime Jaquez Jr. (`MIL` — F), Ryan Rollins (`MIL` — G) & Kel'el Ware (`MIL` — C) | **All Available**
- **Tyler Herro (`N = 8/8 GP`, 8 Starts, 0 DNPs)**:
  - `G1 10-21` @ WAS (`L 116-128`, Start): **32m** | **24p / 9a / 2r** | FG `9-21`, 3P `4-11`, FT `2-2` | PF:1
  - `G2 10-23` vs CHI (`L 125-132`, Start): **32m** | **34p / 4a / 5r** | FG `12-24`, 3P `5-10`, FT `5-7` | PF:0
  - `G3 10-24` @ PHI (`L 116-127`, Start): **31m** | **13p / 3a / 6r** | FG `6-14`, 3P `1-3`, FT `0-0` | PF:0 | B2B
  - `G4 10-26` vs IND (`W 110-102`, Start): **32m** | **23p / 7a / 10r** | FG `7-14`, 3P `3-6`, FT `6-10` | PF:3
  - `G5 10-28` vs HOU (`L 100-132`, Start): **27m** | **23p / 0a / 3r** | FG `9-13`, 3P `4-6`, FT `1-1` | PF:0 | Blowout (-32)
  - `G6 10-31` vs CLE (`L 111-136`, Start): **27m** | **15p / 2a / 3r** | FG `5-18`, 3P `4-11`, FT `1-1` | PF:0 | Blowout (-25)
  - `G7 11-02` @ MIN (`L 100-112`, Start): **31m** | **21p / 3a / 6r** | FG `8-18`, 3P `4-11`, FT `1-2` | PF:0
  - `G8 11-04` @ BOS (`L 102-109`, Start): **33m** | **25p / 3a / 5r** | FG `8-17`, 3P `4-10`, FT `5-5` | PF:0
  - **Summary**: `26–27`: **22.2p / 3.9a / 5.0r** (L5: `21.4p / 3.0a / 5.4r`; Separate `25–26` MIA, 33G: `20.5p/4.1a/4.8r`). MIN Mean **30.6** (Close `31.8`, Blowout `27.0`, SD `2.18`). PTS `[Med 23.0, Min 13, Max 34, SD 6.02]` (**7/8 at 15+ PTS**, `6/8` at `21+ PTS`). `17.4` FGA, `8.5` 3PA, `USG% 27.8%`, `TS% .588`, virtually zero foul risk (`0.5 PF/g!`). Expected **32–34 MIN**.
- **Jaime Jaquez Jr. (`N = 8/8 GP`, 8 Starts, 0 DNPs)**:
  - Chronological: `G1 @ WAS` (`31m, 22p/2a/7r`), `G2 vs CHI` (`35m, 19p/5a/11r`), `G3 @ PHI` (`27m, 21p/4a/8r`), `G4 vs IND` (`25m, 8p/0a/6r`), `G5 vs HOU` (`27m, 19p/2a/4r, -32`), `G6 vs CLE` (`23m, 8p/5a/7r, -25`), `G7 @ MIN` (`28m, 19p/2a/8r, 4PF`), `G8 @ BOS` (`31m, 18p/2a/2r`).
  - **Summary**: `26–27`: **16.8p / 2.8a / 6.6r** (L5: `14.4p / 2.2a / 5.4r`; Separate `25–26` MIA, 75G: `15.4p/4.7a/5.0r`). MIN Mean **28.4** (Close `29.5`, Blowout `25.0`, SD `3.57`). `12.9` FGA, `TS% .585`. Expected **29–31 MIN**.
- **Ryan Rollins (`N = 8/8 GP`, 6 Starts — moved to bench L2, 0 DNPs) & Kel'el Ware (`N = 8/8 GP`, 0 Starts, 0 DNPs)**:
  - **Rollins**: `G1–G6` Starts (`24m, 34m, 25m, 32m, 17m, 26m`; `3a, 6a, 4a, 4a, 5a, 7a`), `G7 @ MIN` (`Bench 17m, 10p/2a/3r`), `G8 @ BOS` (`Bench 24m, 13p/5a/9r`). `26–27`: **11.2p / 4.5a / 4.8r** in **24.9 MIN** (**7/8 at 3+ AST**, Separate `25–26`: `17.3p/5.6a/4.6r`). Bench role shift caps minutes (`22–25` MIN).
  - **Ware**: `G1–G8` Bench (`14m, 15m, 29m, 19m, 17m, 24m, 17m, 16m`; `3r, 4r, 13r, 14r, 8r, 10r, 9r, 5r`). `26–27`: **10.2p / 0.8a / 8.2r** in **18.9 MIN** (L5: `9.2 RPG`, `5/5` at `5+ REB`, elite `TRB% 21.5%`; Separate `25–26` MIA, 77G: `11.1p/0.7a/9.0r`). High per-minute rebounding, but `17–21` MIN bench cap is a major floor hazard.

---

### Fixture 7: Minnesota Timberwolves (`6-3`) @ New Orleans Pelicans (`4-4`)

#### 20. LaMelo Ball (`MIN` — G), Jaden McDaniels (`MIN` — F), Ayo Dosunmu (`MIN` — G) & Rudy Gobert (`MIN` — C) | **All Available** *(Anthony Edwards `Out — Right Knee Arthroscopy`, `33.2 PPG` in `4 GP`)*
- **LaMelo Ball (`N = 9/9 GP`, 9 Starts, 0 DNPs)**:
  - `G1 10-21` @ MIA (`W 131-106`, Start): **29m** | **21p / 6a / 2r** | FG `7-17`, 3P `5-13`, FT `2-3` | PF:4 | Blowout (+25)
  - `G2 10-23` @ ORL (`W 115-93`, Start): **23m** | **12p / 5a / 5r** | FG `4-13`, 3P `2-8`, FT `2-2` | PF:4 | Blowout (+22)
  - `G3 10-25` vs TOR (`W 117-94`, Start): **17m** | **15p / 8a / 1r** | FG `5-8`, 3P `4-5`, FT `1-2` | PF:4 | Blowout (+23), 4PF
  - `G4 10-26` @ CLE (`L 125-127 OT`, Start): **31m** | **11p / 6a / 0r** | FG `5-11`, 3P `1-6`, FT `0-2` | PF:4 | OT, 4PF (Ant last game)
  - `G5 10-28` vs GSW (`L 114-119`, Start): **28m** | **8p / 8a / 3r** | FG `3-11`, 3P `2-8`, FT `0-0` | PF:5 | 5PF (Ant Out begins)
  - `G6 10-30` vs LAC (`W 127-101`, Start): **29m** | **24p / 7a / 4r** | FG `9-19`, 3P `6-14`, FT `0-0` | PF:3 | Blowout (+26)
  - `G7 10-31` @ SAS (`L 111-121`, Start): **20m** | **10p / 4a / 8r** | FG `2-10`, 3P `0-4`, FT `6-6` | PF:6 | Fouled out (6PF in 20m!)
  - `G8 11-02` vs MIL (`W 112-100`, Start): **33m** | **34p / 3a / 6r** | FG `12-21`, 3P `6-13`, FT `4-5` | PF:4 | 4PF
  - `G9 11-04` @ HOU (`W 117-107`, Start): **31m** | **20p / 6a / 2r** | FG `6-11`, 3P `4-7`, FT `4-5` | PF:4 | 4PF
  - **Summary**: `26–27`: **17.2p / 5.9a / 3.4r** (L5 without Edwards: **19.2p / 5.6a / 4.6r**; Separate `25–26` CHA, 72G: `20.1p/7.1a/4.8r`). MIN Mean **26.8** (`28.2` L5, Max `33`, SD `5.18` — **chronic foul trouble: `4+ PF` in 8 of 9 games!**). `13.4` FGA (`14.4` without Ant), `8.7` 3PA, `USG% 28.6%`, `AST% 32.0%`. Expected **29–32 MIN** if fouls stay `<=4`.
- **Jaden McDaniels (`N = 9/9 GP`, 9 Starts, 0 DNPs)**:
  - Chronological (`10-21` to `11-04`): `G1 @ MIA` (`29m, 17p/1a/8r`), `G2 @ ORL` (`30m, 15p/3a/6r`), `G3 vs TOR` (`31m, 14p/3a/6r`), `G4 @ CLE` (`OT, 37m, 14p/4a/6r, 6PF`), `G5 vs GSW` (`35m, 19p/4a/7r, 5PF`), `G6 vs LAC` (`33m, 23p/7a/6r`), `G7 @ SAS` (`39m, 19p/3a/3r`), `G8 vs MIL` (`29m, 13p/3a/6r, 4PF`), `G9 @ HOU` (`37m, 14p/4a/8r, 4PF`).
  - **Summary**: `26–27`: **16.4p / 3.6a / 6.2r** (L5 without Ant: **17.6p / 4.2a / 6.0r** on `15.6` FGA vs `11.0` FGA with Ant!; Separate `25–26`: `14.8p/2.7a/4.2r`). MIN Mean **33.3** (Close `35.4`, SD `3.59`). PTS `[Med 15, Min 13, Max 23, SD 3.13]` (**9/9 at 13+ PTS**, **8/9 at 3+ AST & 5+ REB**). Expected **34–36 MIN**.
- **Ayo Dosunmu (`N = 9/9 GP`, 5 Starts — promoted to starter in all 5 games without Edwards, 0 DNPs)**:
  - Chronological: `G1–G4` Bench (`29m 16p/3a/5r`, `27m 14p/10a/7r`, `23m 9p/3a/3r`, `26m 9p/0a/1r`), `G5 vs GSW` (`Start 32m, 17p/4a/3r`), `G6 vs LAC` (`Start 30m, 15p/2a/7r`), `G7 @ SAS` (`Start 38m, 27p/3a/9r`), `G8 vs MIL` (`Start 37m, 19p/8a/12r`), `G9 @ HOU` (`Start 34m, 21p/6a/1r`).
  - **Summary**: `26–27`: **16.3p / 4.3a / 5.3r** (**19.8p / 4.6a / 6.4r in 34.2 MIN across 5 starts without Edwards — 5/5 at 15+ PTS!**; Separate `25–26`: `14.8p/3.6a/3.4r`). `15.6` FGA as starter, `TS% .585`. Expected **34–36 MIN**.
- **Rudy Gobert (`N = 8/9 GP`, 8 Starts; Missed `10-31 @ SAS` — 1 DNP)**:
  - Chronological: `G1 @ MIA` (`33m, 5p/1a/15r`), `G2 @ ORL` (`30m, 14p/1a/9r`), `G3 vs TOR` (`31m, 8p/0a/13r`), `G4 @ CLE` (`OT, 36m, 5p/2a/20r [8o/12d]`), `G5 vs GSW` (`20m, 1p/1a/4r — ShortMin 20m vs small-ball`), `G6 vs LAC` (`30m, 9p/4a/13r`), `G7 vs MIL` (`31m, 10p/1a/10r`), `G8 @ HOU` (`33m, 8p/2a/11r`).
  - **Summary**: `26–27`: **7.5p / 1.5a / 11.9r** (`4.2 OREB/g`, L5: `11.6 RPG`; Separate `25–26`: `10.9p/1.7a/11.5r`). MIN Mean **30.5** (`30+m`: 7/8). **7/8 at 9+ REB** (only miss was the `20-min` GSW small-ball game). `ORB% 14.5%`, `DRB% 26.0%`. Expected **31–33 MIN**.

#### 21. Zion Williamson (`NOP` — F), Dejounte Murray (`NOP` — G), Derik Queen (`NOP` — C) & Trey Murphy III (`NOP` — F)
- **Zion Williamson (`N = 8/8 GP`, 8 Starts, 0 DNPs) — Available**:
  - `G1 10-21` vs IND (`L 120-123`, Start): **32m** | **22p / 3a / 3r** | FG `7-16`, 3P `2-4`, FT `6-6` | PF:3
  - `G2 10-23` @ UTA (`L 119-120`, Start): **33m** | **23p / 2a / 5r** | FG `8-12`, 3P `0-1`, FT `7-8` | PF:5 | 5PF
  - `G3 10-24` @ DEN (`L 135-141 OT`, Start): **33m** | **17p / 2a / 1r** | FG `7-11`, 3P `0-1`, FT `3-5` | PF:5 | OT, 5PF
  - `G4 10-28` vs DEN (`L 91-104`, Start): **32m** | **25p / 2a / 5r** | FG `10-14`, 3P `1-1`, FT `4-6` | PF:3
  - `G5 10-29` vs SAC (`W 132-120`, Start): **31m** | **22p / 2a / 6r** | FG `10-12`, 3P `0-0`, FT `2-4` | PF:0
  - `G6 10-31` vs ATL (`W 121-99`, Start): **30m** | **15p / 4a / 6r** | FG `5-8`, 3P `0-0`, FT `5-8` | PF:2 | Blowout (+22)
  - `G7 11-02` @ MEM (`W 135-134 OT`, Start): **35m** | **25p / 4a / 11r** | FG `9-15`, 3P `0-0`, FT `7-9` | PF:4 | OT
  - `G8 11-04` vs UTA (`W 120-113 OT`, Start): **38m** | **23p / 2a / 4r** | FG `6-14`, 3P `0-0`, FT `11-13` | PF:4 | OT
  - **Summary**: `26–27`: **21.5p / 2.6a / 5.1r** (L5: `22.0p / 2.8a / 6.4r`; Separate `25–26`: `21.0p/3.2a/5.7r`). MIN Mean **33.0** (`30+m`: 8/8, SD `2.35`). PTS `[Med 22.5, Min 15, Max 25, SD 3.39]` (**8/8 at 15+ PTS!**). `12.8` FGA, `7.4` FTA, elite `TS% .672`, but tonight faces Rudy Gobert & Jaden McDaniels (`MIN #2 DRtg 105.9`). Expected **33–35 MIN**.
- **Dejounte Murray (`N = 5/8 GP`, 5 Starts; Missed `10-29 vs SAC`, `10-31 vs ATL`, `11-02 @ MEM` — 3 DNPs) — Available**:
  - Chronological: `G1 vs IND` (`34m, 23p/7a/3r`), `G2 @ UTA` (`30m, 16p/6a/6r`), `G3 @ DEN` (`OT, 35m, 22p/6a/6r`), `G4 vs DEN` (`30m, 10p/5a/8r`), `G5 11-04 vs UTA` (`OT return, 45m!, 20p/4a/8r, 11-11 FT`).
  - **Summary**: `26–27`: **18.2p / 5.6a / 6.2r** (Separate `25–26` NOP, 14G: `16.7p/6.4a/5.4r`). MIN Mean **34.8** (`30+m`: 5/5; played `45` MIN in OT return Nov 4, confirming zero minutes restriction!). **4/5 at 15+ PTS, 5+ AST & 5+ REB**. Expected **34–36 MIN**.
- **Derik Queen (`N = 8/8 GP`, 0 Starts, 0 DNPs) — Available & Trey Murphy III (`N = 7/8 GP`, 7 Starts; Missed `11-04 vs UTA`) — Probable**:
  - **Queen**: `G1–G8` Bench (`18m 10p/10r`, `29m 12p/7r`, `25m 17p/8r`, `25m 11p/12r`, `22m 9p/2r`, `23m 8p/8r`, `24m 20p/5a/7r`, `27m 20p/6a/9r`). `26–27`: **13.4p / 3.0a / 7.9r** in **24.1 MIN** (**7/8 at 7+ REB**, `DRB% 29.8%`; Yves Missi `Out`). Expected **24–27 MIN**.
  - **Murphy III (`Probable — Bilateral Patella Tendinopathy`)**: `26–27`: **14.9p / 3.4a / 4.6r** in **33.0 MIN** (L5: `16.8p / 4.0a / 4.4r`, **6/7 at 3+ AST**, `5/5` L5; Separate `25–26`: `21.5p/3.8a/5.7r`). Meanwhile 6th man **Saddiq Bey** (`8/8 GP`, `26.5m`, `16.4 PPG`, **7/8 at 10+ PTS**) provides bench scoring punch.

---

### Fixture 8: Portland Trail Blazers (`6-1`) @ Los Angeles Lakers (`7-2`)

#### 22. Deni Avdija (`POR` — F), Damian Lillard (`POR` — G) & Donovan Clingan (`POR` — C) | **All Available** *(Ja Morant `Out — Left Hamstring Strain`, `4 GP`)*
- **Deni Avdija (`N = 7/7 GP`, 7 Starts, 0 DNPs)**:
  - `G1 10-21` vs PHX (`W 124-83`, Start): **23m** | **18p / 4a / 10r** | FG `7-16`, 3P `2-4`, FT `2-4` | PF:1 | Blowout (+41)
  - `G2 10-23` @ SAC (`W 128-120`, Start): **38m** | **26p / 6a / 7r** | FG `8-16`, 3P `1-5`, FT `9-12` | PF:2
  - `G3 10-27` @ LAL (`W 136-129`, Start): **33m** | **23p / 9a / 4r** | FG `8-15`, 3P `4-7`, FT `3-7` | PF:4 | H2H @ LAL, 4PF
  - `G4 10-29` vs MEM (`L 103-124`, Start): **32m** | **24p / 7a / 9r** | FG `8-16`, 3P `0-4`, FT `8-12` | PF:1 | Blowout (-21), Morant last game
  - `G5 10-31` @ UTA (`W 112-90`, Start): **30m** | **24p / 2a / 5r** | FG `6-12`, 3P `2-4`, FT `10-13` | PF:3 | Blowout (+22), Morant Out
  - `G6 11-02` @ DEN (`W 118-110`, Start): **35m** | **28p / 5a / 3r** | FG `10-22`, 3P `2-9`, FT `6-9` | PF:3 | Morant Out
  - `G7 11-04` @ PHX (`W 132-119`, Start): **35m** | **21p / 12a / 7r** | FG `7-16`, 3P `1-5`, FT `6-9` | PF:1 | Morant Out
  - **Summary**: `26–27`: **23.4p / 6.4a / 6.4r** (L5: **24.0p / 7.0a / 5.6r**; `24.3 PPG` in 3G without Morant; Separate `25–26` POR, 66G: `24.2p/6.7a/6.9r`). MIN Mean **32.3** (Close `35.3`, Blowout `28.3`, SD `4.46`). PTS `[Med 24, Min 18, Max 28, SD 3.02!]` — **6/7 at 20+ PTS** (only miss was `18 PTS` in `23 MIN` during a 41-pt opener blowout!). `16.1` FGA, huge `9.4` FTA, `USG% 28.6%`, `AST% 31.4%`. Had `23p/9a` @ LAL on Oct 27. Expected **35–36 MIN**.
- **Damian Lillard (`N = 7/7 GP`, 7 Starts, 0 DNPs)**:
  - Chronological (`10-21` to `11-04`): `G1 vs PHX` (`24m, 25p/6a/3r, +41`), `G2 @ SAC` (`33m, 19p/2a/5r`), `G3 @ LAL` (`31m, 21p/4a/5r, 4-8 3P`), `G4 vs MEM` (`30m, 9p/2a/2r, -21`), `G5 @ UTA` (`27m, 22p/4a/5r, +22`), `G6 @ DEN` (`30m, 20p/6a/6r`), `G7 @ PHX` (`33m, 25p/5a/3r`).
  - **Summary**: `26–27`: **20.1p / 4.1a / 4.1r** (**22.3p / 5.0a / 4.7r in 3G without Ja Morant — 3/3 at 20+ PTS & 4+ AST!**; Missed `2025–26` due to injury recovery). MIN Mean **29.7** (Close `31.3`, SD `3.01`; note POR plays Sat vs SAS on B2B). `14.3` FGA, `8.6` 3PA, `6.6` FTA, `TS% .586`. Expected **31–33 MIN**.
- **Donovan Clingan (`N = 7/7 GP`, 7 Starts, 0 DNPs)**:
  - Chronological (`10-21` to `11-04`): `G1 vs PHX` (`21m, 11p/2a/7r, +41`), `G2 @ SAC` (`21m, 8p/3a/11r [5o], 4PF`), `G3 @ LAL` (`26m, 9p/1a/10r [9d]`), `G4 vs MEM` (`29m, 11p/1a/8r`), `G5 @ UTA` (`15m, 4p/0a/9r, 5PF, +22`), `G6 @ DEN` (`32m, 17p/3a/18r [9o/9d!], 4PF`), `G7 @ PHX` (`29m, 24p/1a/11r, 9-12 FG`).
  - **Summary**: `26–27`: **12.0p / 1.6a / 10.6r** (L5: `13.0p / 11.2r`; `12.7 RPG` in L3; Separate `25–26`: `12.1p/2.1a/11.6r`). MIN Mean **24.7** (`30.5` MIN over L2; Robert Williams III `16.5m, 7.2r` backs him up). **7/7 at 7+ REB**, **6/7 at 8+ REB** (`ORB% 18.2%`, `TRB% 23.3%`) facing LAL (`28th in DRB% at 68.4%`). Expected **27–29 MIN**.

#### 23. Luka Doncic (`LAL` — G), Austin Reaves (`LAL` — G) & Walker Kessler (`LAL` — C) | **All Available**
- **Luka Doncic (`N = 8/9 GP`, 8 Starts; Missed `10-28 @ LAC` [B2B 2nd night rest] — 1 DNP)**:
  - `G1 10-21` vs GSW (`W 127-105`, Start): **30m** | **28p / 7a / 8r** | FG `7-18`, 3P `5-12`, FT `9-9` | PF:1 | Blowout (+22)
  - `G2 10-23` vs LAC (`W 125-117`, Start): **37m** | **23p / 7a / 6r** | FG `8-21`, 3P `2-8`, FT `5-7` | PF:2 | 11 TOV
  - `G3 10-25` @ UTA (`W 132-123`, Start): **38m** | **52p / 10a / 8r** | FG `17-30`, 3P `8-18`, FT `10-11` | PF:4
  - `G4 10-27` vs POR (`L 129-136`, Start): **37m** | **41p / 9a / 5r** | FG `12-22`, 3P `6-15`, FT `11-13` | PF:3 | H2H vs POR
  - `G5 10-30` @ GSW (`L 95-112`, Start): **37m** | **37p / 5a / 7r** | FG `12-27`, 3P `6-16`, FT `7-8` | PF:2 | Blowout (-17)
  - `G6 11-01` vs TOR (`W 131-125`, Start): **35m** | **45p / 6a / 15r** | FG `12-23`, 3P `8-12`, FT `13-13` | PF:5 | 5PF
  - `G7 11-02` vs MIA (`W 138-117`, Start): **36m** | **42p / 13a / 7r** | FG `14-24`, 3P `6-15`, FT `8-10` | PF:2 | Blowout (+21)
  - `G8 11-04` @ SAC (`W 116-103`, Start): **35m** | **40p / 7a / 9r** | FG `11-23`, 3P `6-13`, FT `12-13` | PF:1
  - **Summary**: `26–27`: **38.5p / 8.0a / 8.1r** (L5: **41.0p / 8.0a / 8.6r** — **6 consecutive 37+ point games!**; Separate `25–26` LAL, 64G: `33.5p/8.3a/7.7r`). MIN Mean **35.6** (`30+m`: 8/8, `35+m`: 7/8, SD `2.34`). PTS `[Med 40.5, Min 23, Max 52, SD 8.65]`, AST `[Med 7.0, Min 5, Max 13, SD 2.40]`, REB `[Med 7.5, Min 5, Max 15, SD 2.85]`. League-high `23.5` FGA, `13.6` 3PA (`43.1% 3P`), `10.5` FTA, `USG% 40.0%`, `TS% .685`, `AST% 41.6%`. Scored `41p/9a/5r` vs POR on Oct 27. Expected **36–38 MIN**.
- **Austin Reaves (`N = 9/9 GP`, 9 Starts, 0 DNPs)**:
  - Chronological (`10-21` to `11-04`): `G1 vs GSW` (`32m, 23p/6a/4r`), `G2 vs LAC` (`38m, 28p/9a/2r`), `G3 @ UTA` (`36m, 29p/4a/1r, 5PF`), `G4 vs POR` (`39m, 26p/7a/4r, 5PF`), `G5 @ LAC` (`31m, 16p/1a/6r, Luka Out`), `G6 @ GSW` (`37m, 21p/5a/4r`), `G7 vs TOR` (`39m, 19p/4a/3r`), `G8 vs MIA` (`34m, 27p/5a/2r`), `G9 @ SAC` (`37m, 21p/4a/3r`).
  - **Summary**: `26–27`: **23.3p / 5.0a / 3.2r** (L5: `20.8p / 3.8a / 3.6r`; Separate `25–26`: `23.3p/5.5a/4.7r`). MIN Mean **35.9** (Close `38.0`, SD `2.77`, `30+m`: 9/9). PTS `[Med 23, Min 16, Max 29, SD 4.19]` (**9/9 at 16+ PTS**, **8/9 at 3+ AST**). `14.4` FGA, `6.4` FTA, elite `TS% .675`. Had `26p/7a` vs POR on Oct 27. Expected **36–38 MIN**.
- **Walker Kessler (`N = 9/9 GP`, 9 Starts, 0 DNPs) — Available (Left Finger Splint)**:
  - Chronological (`10-21` to `11-04`): `G1 vs GSW` (`30m, 26p/1a/9r, 12-12 FG!`), `G2 vs LAC` (`35m, 22p/3a/8r`), `G3 @ UTA` (`28m, 2p/0a/7r, 4PF`), `G4 vs POR` (`33m, 13p/0a/8r, 4PF`), `G5 @ LAC` (`26m, 11p/1a/9r`), `G6 @ GSW` (`31m, 10p/2a/13r`), `G7 vs TOR` (`31m, 16p/1a/15r`), `G8 vs MIA` (`32m, 15p/2a/15r`), `G9 @ SAC` (`29m, 15p/0a/8r, 6PF`).
  - **Summary**: `26–27`: **14.4p / 1.1a / 10.2r** (L5: `13.4p / 12.0r`; Separate `25–26` UTA, 5G: `14.4p/3.0a/10.8r`). MIN Mean **30.6** (`SD 2.54`). **9/9 at 7+ REB**, **8/9 at 8+ REB**, **8/9 at 10+ PTS** (`TS% .706`, `TRB% 19.8%`). Expected **31–33 MIN**.

---

### Fixture 9: San Antonio Spurs (`6-2`) @ Sacramento Kings (`1-7`)

#### 24. Victor Wembanyama (`SAS` — F/C), Dylan Harper (`SAS` — G), De'Aaron Fox (`SAS` — G) & Stephon Castle (`SAS` — G) | **All Available**
- **Victor Wembanyama (`N = 8/8 GP`, 8 Starts, 0 DNPs)**:
  - `G1 10-20` vs OKC (`L 104-116`, Start): **34m** | **12p / 3a / 13r** (2o/11d) | FG `1-13`, 3P `0-4`, FT `10-12` | PF:3
  - `G2 10-23` vs HOU (`L 110-114`, Start): **32m** | **25p / 2a / 13r** (4o/9d) | FG `9-21`, 3P `2-6`, FT `5-8` | PF:4
  - `G3 10-24` @ DAL (`W 122-106`, Start): **29m** | **23p / 2a / 7r** (1o/6d) | FG `9-18`, 3P `2-6`, FT `3-5` | PF:0 | Blowout (+16)
  - `G4 10-27` vs SAC (`W 130-103`, Start): **27m** | **29p / 2a / 10r** (3o/7d) | FG `14-21`, 3P `0-3`, FT `1-1` | PF:0 | Blowout (+27) vs SAC!
  - `G5 10-28` @ UTA (`W 117-111 OT`, Start): **39m** | **36p / 5a / 14r** (2o/12d) | FG `14-25`, 3P `4-10`, FT `4-4` | PF:4 | OT
  - `G6 10-31` vs MIN (`W 121-111`, Start): **34m** | **43p / 4a / 7r** (3o/4d) | FG `17-34`, 3P `3-8`, FT `6-9` | PF:2
  - `G7 11-02` vs UTA (`W 119-97`, Start): **24m** | **12p / 5a / 11r** (1o/10d) | FG `5-15`, 3P `0-5`, FT `2-3` | PF:2 | Blowout (+22)
  - `G8 11-04` vs DAL (`W 112-111`, Start): **34m** | **52p / 2a / 24r** (9o/15d!) | FG `16-28`, 3P `1-8`, FT `19-23` | PF:2
  - **Summary**: `26–27`: **29.0p / 3.1a / 12.4r** (L5: **34.4p / 3.6a / 13.2r**; Separate `25–26`: `25.0p/3.1a/11.5r`). MIN Mean **31.6** (**Close `34.6` vs Blowout `26.7`!**). PTS `[Med 27.0, Min 12, Max 52, SD 13.25 — 52p/24r monster G8 inflates mean]`, REB `[Med 12.0, Min 7, Max 24, SD 5.05]` (**8/8 at 10+ PTS & 7+ REB**). Against SAC on Oct 27 (`W 130-103`), he posted `29p/10r` on `14-21` FG in just `27 MIN` before sitting the 4th quarter. With SAS `-15.5` tonight and `@ POR` tomorrow on a B2B, expect **27–31 MIN** (`33–35` only if SAC keeps it close).
- **Dylan Harper (`N = 8/8 GP`, 8 Starts, 0 DNPs)**:
  - Chronological (`10-20` to `11-04`): `G1 vs OKC` (`32m, 18p/5a/7r, 5PF`), `G2 vs HOU` (`34m, 20p/2a/3r`), `G3 @ DAL` (`28m, 22p/2a/5r, +16`), `G4 vs SAC` (`30m, 13p/6a/6r, +27`), `G5 @ UTA` (`OT, 37m, 13p/8a/5r`), `G6 vs MIN` (`39m, 25p/6a/7r`), `G7 vs UTA` (`27m, 17p/8a/7r, +22`), `G8 vs DAL` (`36m, 21p/0a/5r`).
  - **Summary**: `26–27`: **18.6p / 4.6a / 5.6r** (L5: `17.8p / 5.6a / 6.0r`; Separate `25–26`: `11.8p/3.9a/3.4r`). MIN Mean **32.9** (Close `35.6`, Blowout `28.3`, SD `4.08`). PTS `[Med 19.0, Min 13, Max 25, SD 3.97]` (**8/8 at 13+ PTS**, **7/8 at 5+ REB**). `14.5` FGA, `TS% .585`. Expected **30–33 MIN**.
- **De'Aaron Fox (`N = 8/8 GP`, 8 Starts, 0 DNPs) & Stephon Castle (`N = 8/8 GP`, 8 Starts, 0 DNPs)**:
  - **Fox**: `G1 vs OKC` (`32m, 14p/7a/7r`), `G2 vs HOU` (`32m, 19p/9a/4r`), `G3 @ DAL` (`28m, 19p/9a/3r, +16`), `G4 vs SAC` (`26m, 11p/6a/4r, +27`), `G5 @ UTA` (`OT, 39m, 14p/4a/3r`), `G6 vs MIN` (`35m, 22p/7a/8r`), `G7 vs UTA` (`22m, 12p/3a/2r, +22, 5PF`), `G8 vs DAL` (`33m, 10p/4a/3r`). `26–27`: **15.1p / 6.1a / 4.2r** (Separate `25–26`: `18.6p/6.2a/3.8r`). MIN Mean **30.9** (Close `34.2`, Blowout `25.3`). **8/8 at 10+ PTS & 3+ AST** (`TS% .652`, revenge game in Sacramento). Expected **28–32 MIN**.
  - **Castle**: `26–27`: **15.0p / 4.8a / 6.1r** in **29.6 MIN** (**7/8 at 10+ PTS, 3+ AST & 5+ REB**; only scoring miss = `0 PTS` in `22m` foul trouble vs MIN; Separate `25–26`: `16.7p/7.4a/5.3r`). Expected **28–30 MIN**.

#### 25. Darius Acuff Jr. (`SAC` — G), Zach LaVine (`SAC` — G) & Domantas Sabonis (`SAC` — F/C) | **All Available**
- **Darius Acuff Jr. (`N = 8/8 GP`, 8 Starts, 0 DNPs)**:
  - `G1 10-21` @ LAC (`L 96-121`, Start): **35m** | **12p / 3a / 3r** | FG `5-24`, 3P `0-7`, FT `2-5` | PF:2 | Blowout (-25)
  - `G2 10-23` vs POR (`L 120-128`, Start): **37m** | **33p / 4a / 2r** | FG `10-26`, 3P `2-11`, FT `11-12` | PF:3
  - `G3 10-25` vs MEM (`L 112-123`, Start): **36m** | **22p / 7a / 3r** | FG `9-23`, 3P `2-9`, FT `2-2` | PF:4
  - `G4 10-27` @ SAS (`L 103-130`, Start): **33m** | **19p / 5a / 3r** | FG `8-20`, 3P `3-7`, FT `0-0` | PF:2 | Blowout (-27) @ SAS
  - `G5 10-29` @ NOP (`L 120-132`, Start): **41m** | **34p / 14a / 6r** | FG `13-26`, 3P `3-11`, FT `5-5` | PF:4
  - `G6 10-31` @ MEM (`L 105-136`, Start): **37m** | **38p / 5a / 5r** | FG `12-25`, 3P `9-14`, FT `5-5` | PF:3 | Blowout (-31)
  - `G7 11-02` @ DAL (`W 115-100`, Start): **37m** | **25p / 6a / 5r** | FG `10-21`, 3P `2-8`, FT `3-4` | PF:3 | Blowout (+15)
  - `G8 11-04` vs LAL (`L 103-116`, Start): **42m** | **22p / 12a / 3r** | FG `8-24`, 3P `3-11`, FT `3-4` | PF:2
  - **Summary**: `26–27`: **25.6p / 7.0a / 3.8r** (L5: **27.6p / 8.4a / 4.4r**; `2026–27 NBA Rookie`). MIN Mean **37.2** (Close `38.0`, **Blowout `35.5`!** — SAC keeps their rookie PG on floor even in `-25` to `-31` routs!). `23.6` FGA, `9.8` 3PA, `USG% 32.5%`, `AST% 32.2%`, `TS% .499`. **7/8 at 19+ PTS**, **5/5 in L5 at 5+ AST**. Expected **36–38 MIN**.
- **Zach LaVine (`N = 8/8 GP`, 8 Starts, 0 DNPs)**:
  - Chronological (`10-21` to `11-04`): `G1 @ LAC` (`34m, 28p/4a/4r, -25`), `G2 vs POR` (`39m, 22p/1a/5r`), `G3 vs MEM` (`40m, 37p/5a/2r`), `G4 @ SAS` (`31m, 22p/3a/3r, -27`), `G5 @ NOP` (`39m, 21p/5a/3r`), `G6 @ MEM` (`21m, 11p/1a/0r, -31 blowout benching`), `G7 @ DAL` (`28m, 23p/1a/4r, +15`), `G8 vs LAL` (`35m, 21p/1a/4r, 5PF`).
  - **Summary**: `26–27`: **23.1p / 2.6a / 3.1r** (L5: `19.6p / 2.2a / 2.8r`; Separate `25–26` SAC, 39G: `19.2p/2.3a/2.8r`). MIN Mean **33.4** (Close `39.3`, Blowout `28.5` — unlike rookie Acuff, veteran LaVine lost 4Q minutes in the `-31` MEM blowout). **7/8 at 20+ PTS!** `15.4` FGA, `7.6` 3PA, `TS% .642`. Expected **32–36 MIN** (`26–29` in 25+ pt blowout).
- **Domantas Sabonis (`N = 8/8 GP`, 8 Starts, 0 DNPs)**:
  - Chronological (`10-21` to `11-04`): `G1 @ LAC` (`34m, 14p/8a/18r, -25`), `G2 vs POR` (`39m, 27p/10a/19r, 5PF`), `G3 vs MEM` (`35m, 15p/3a/15r, 5PF`), `G4 @ SAS` (`37m, 20p/8a/14r, 10-16 FG, -27`), `G5 @ NOP` (`40m, 9p/7a/15r`), `G6 @ MEM` (`38m, 11p/8a/14r, -31`), `G7 @ DAL` (`31m, 9p/4a/7r, +15, 4PF`), `G8 vs LAL` (`35m, 16p/1a/17r`).
  - **Summary**: `26–27`: **15.1p / 6.1a / 14.9r** (L5: `13.0p / 5.6a / 13.4r`; Separate `25–26` SAC, 19G: `15.8p/4.1a/11.4r`). MIN Mean **36.1** (Close `38.0`, **Blowout `35.0`!** — logged `37m` in `-27` @ SAS and `38m` in `-31` @ MEM!). **7/8 at 14+ REB** (hits `12+ REB` in `7/8`, `87.5%`), `DRB% 34.1%`, `TRB% 23.4%`, `TS% .721`. Expected **35–37 MIN**.

---

## PART D — CONSISTENCY TABLES

> [!IMPORTANT]
> **Historical Floor vs Future Probability**: In an early-season sample of `N = 6` to `9` games, a `100%` (`8/8` or `9/9`) or `>=85%` (`7/8`, `8/9`, `6/7`) hit rate identifies an **observed historical floor**, **not** a guaranteed outcome. Matchup difficulty, injury uncertainty, foul trouble, and blowout minute-loss (`SAS -15.5 @ SAC`, `BOS -8.5 @ CHA`, `DAL -7.5 vs UTA`) must always discount raw hit rates. Note that for `N = 8`, `7/8 = 87.5%` satisfies **both** the `80%` (`8/10`) and `~88%` (`9/10` nearest-integer) thresholds; for `N = 9`, `8/9 = 88.9%` satisfies `80%` and `~90%` (`9/10` nearest-integer); for `N = 7`, `6/7 = 85.7%` satisfies `80%+`.

### 1. Points Consistency Table (`10+, 15+, 20+, 25+, 30+, 35+`)

| Rank | Player (Team, Status) | GP | Mean | Med | Min–Max (SD) | 10+ | 15+ | 20+ | 25+ | 30+ | 35+ | L5 Form | >=80% Floor | >=88–90% Floor | 100% Floor | Miss Context & Outlier Inflation Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **1** | **Luka Doncic** (`LAL`, Avail) | 8 | 38.5 | 40.5 | 23–52 (8.65) | 8/8 (100%) | 8/8 (100%) | **8/8 (100%)** | **7/8 (87.5%)** | 6/8 (75%) | 6/8 (75%) | 5/5 at 35+ | **25+ PTS** | **25+ PTS** | **20+ PTS** | Only miss `<25` was `23 PTS` in G2 (`8-21 FG`); 6 straight `37+` PTS games. |
| **2** | **Tyrese Maxey** (`PHI`, Avail) | 9 | 28.0 | 27.0 | 19–38 (4.81) | 9/9 (100%) | **9/9 (100%)** | 8/9 (88.9%) | **8/9 (88.9%)** | 2/9 (22.2%) | 1/9 (11.1%) | 4/5 at 25+ | **25+ PTS** | **25+ PTS** | **15+ PTS** | Tight `4.81` SD; sole miss `<25` was `19 PTS` on `5-16 FG` @ DET (`11-04`). |
| **3** | **Shai Gilgeous-Alexander** (`OKC`, Avail) | 8 | 30.1 | 29.0 | 17–43 (8.77) | 8/8 (100%) | **8/8 (100%)** | **7/8 (87.5%)** | 6/8 (75%) | 4/8 (50%) | 2/8 (25%) | 5/5 at 20+ | **20+ PTS** | **20+ PTS** | **15+ PTS** | Sole miss `<20` was `17 PTS` (`6-19 FG`) vs DEN slow-pace grinder (`96-84`). |
| **4** | **Deni Avdija** (`POR`, Avail) | 7 | 23.4 | 24.0 | 18–28 (3.02) | 7/7 (100%) | **7/7 (100%)** | **6/7 (85.7%)** | 2/7 (28.6%) | 0/7 (0%) | 0/7 (0%) | 5/5 at 20+ | **20+ PTS** | *15+ PTS* | **15+ PTS** | Elite `3.02` SD; sole miss `<20` was `18 PTS` in `23 MIN` (`+41` blowout vs PHX). |
| **5** | **RJ Barrett** (`TOR`, Avail) | 8 | 20.9 | 22.0 | 9–26 (4.91) | 7/8 (87.5%) | 7/8 (87.5%) | **7/8 (87.5%)** | 2/8 (25%) | 0/8 (0%) | 0/8 (0%) | 4/5 at 20+ | **20+ PTS** | **20+ PTS** | None | Sole miss `<20` was `9 PTS` (`3-10 FG`, `4 PF`) vs ORL (`10-30`). |
| **6** | **Zach LaVine** (`SAC`, Avail) | 8 | 23.1 | 22.0 | 11–37 (6.85) | **8/8 (100%)** | 7/8 (87.5%) | **7/8 (87.5%)** | 2/8 (25%) | 1/8 (12.5%) | 1/8 (12.5%) | 4/5 at 20+ | **20+ PTS** | **20+ PTS** | **10+ PTS** | Sole miss `<20` was `11 PTS` in `21 MIN` (`-31` blowout @ MEM); **high blowout risk tonight**. |
| **7** | **Austin Reaves** (`LAL`, Avail) | 9 | 23.3 | 23.0 | 16–29 (4.19) | 9/9 (100%) | **9/9 (100%)** | 7/9 (77.8%) | 4/9 (44.4%) | 0/9 (0%) | 0/9 (0%) | 5/5 at 15+ | **15+ PTS** | **15+ PTS** | **15+ PTS** | `16+ PTS` in all 9 games (`4.19` SD); `7/9` (`77.8%`) at `20+`. |
| **8** | **Donovan Mitchell** (`CLE`, Avail) | 8 | 22.5 | 22.0 | 15–32 (5.27) | 8/8 (100%) | **8/8 (100%)** | 5/8 (62.5%) | 3/8 (37.5%) | 1/8 (12.5%) | 0/8 (0%) | 5/5 at 15+ | **15+ PTS** | **15+ PTS** | **15+ PTS** | Hit `15+` even in `24 MIN` (`+25` blowout, `5 PF`) @ MIL. |
| **9** | **Jaylen Brown** (`PHI`, Avail) | 8 | 21.8 | 20.5 | 16–30 (4.79) | 8/8 (100%) | **8/8 (100%)** | 5/8 (62.5%) | 3/8 (37.5%) | 1/8 (12.5%) | 0/8 (0%) | 5/5 at 15+ | **15+ PTS** | **15+ PTS** | **15+ PTS** | `16+ PTS` in all 8 games (`33–40` MIN every night). |
| **10** | **Zion Williamson** (`NOP`, Avail) | 8 | 21.5 | 22.5 | 15–25 (3.39) | 8/8 (100%) | **8/8 (100%)** | 6/8 (75%) | 2/8 (25%) | 0/8 (0%) | 0/8 (0%) | 5/5 at 15+ | **15+ PTS** | **15+ PTS** | **15+ PTS** | Tight `3.39` SD, `15+` in `8/8`, but toughest interior test yet vs Gobert/MIN. |
| **11** | **Paul George** (`BOS`, Avail) | 7 | 21.3 | 18.0 | 15–38 (7.48) | 7/7 (100%) | **7/7 (100%)** | 3/7 (42.9%) | 2/7 (28.6%) | 1/7 (14.3%) | 1/7 (14.3%) | 5/5 at 15+ | **15+ PTS** | **15+ PTS** | **15+ PTS** | **Outlier Flag**: `38 PTS` G1 inflates `21.3` mean above `18.0` median, but `15+` is `7/7`. |
| **12** | **Kyrie Irving** (`DAL`, Avail) | 6 | 22.7 | 21.0 | 15–35 (7.45) | 6/6 (100%) | **6/6 (100%)** | 3/6 (50%) | 2/6 (33.3%) | 1/6 (16.7%) | 1/6 (16.7%) | 5/5 at 15+ | **15+ PTS** | **15+ PTS** | **15+ PTS** | Hit `15+` even in two `24–27` MIN blowouts; `64 PTS` combined over L2. |
| **13** | **Darius Acuff Jr.** (`SAC`, Avail) | 8 | 25.6 | 23.5 | 12–38 (8.17) | **8/8 (100%)** | **7/8 (87.5%)** | 6/8 (75%) | 4/8 (50%) | 3/8 (37.5%) | 1/8 (12.5%) | 5/5 at 15+ | **15+ PTS** | **15+ PTS** | **10+ PTS** | Sole miss `<15` was NBA debut (`12 PTS`, `5-24 FG`); `19+` in 7 straight since! |
| **14** | **Tyler Herro** (`MIL`, Avail) | 8 | 22.2 | 23.0 | 13–34 (6.02) | **8/8 (100%)** | **7/8 (87.5%)** | 6/8 (75%) | 2/8 (25%) | 1/8 (12.5%) | 0/8 (0%) | 5/5 at 15+ | **15+ PTS** | **15+ PTS** | **10+ PTS** | Sole miss `<15` was `13 PTS` on road B2B @ PHI (`10-24`). |
| **15** | **Trae Young** (`WAS`, Avail) | 8 | 19.6 | 20.5 | 14–25 (3.50) | **8/8 (100%)** | **7/8 (87.5%)** | 5/8 (62.5%) | 1/8 (12.5%) | 0/8 (0%) | 0/8 (0%) | 4/5 at 15+ | **15+ PTS** | **15+ PTS** | **10+ PTS** | Very tight `3.50` SD; sole miss `<15` was `14 PTS` (`3-12 FG`) @ CLE. |
| **16** | **Evan Mobley** (`CLE`, Avail) | 8 | 18.8 | 18.0 | 11–27 (4.66) | **8/8 (100%)** | **7/8 (87.5%)** | 3/8 (37.5%) | 1/8 (12.5%) | 0/8 (0%) | 0/8 (0%) | 4/5 at 15+ | **15+ PTS** | **15+ PTS** | **10+ PTS** | Sole miss `<15` was `11 PTS` (`4-9 FG`) @ ATL (`10-29`). |
| **17** | **Anthony Davis** (`WAS`, **Quest**) | 8 | 23.4 | 25.5 | 9–34 (7.26) | 7/8 (87.5%) | **7/8 (87.5%)** | 5/8 (62.5%) | 5/8 (62.5%) | 1/8 (12.5%) | 0/8 (0%) | 5/5 at 15+ | **15+ PTS** | **15+ PTS** | None | Sole miss was `9 PTS` vs TOR in G2; **Questionable (R Ankle)**. |
| **18** | **Scottie Barnes** (`TOR`, **Quest**) | 8 | 23.5 | 25.5 | 0–41 (11.03) | 7/8 (87.5%) | **7/8 (87.5%)** | 6/8 (75%) | 4/8 (50%) | 1/8 (12.5%) | 1/8 (12.5%) | 5/5 at 15+ | **15+ PTS** | **15+ PTS** | None | `0-12 FG` blowout @ MIN (`0 PTS`) vs `41 PTS` vs ORL; **Questionable (Groin)**. |
| **19** | **Jayson Tatum** (`BOS`, Avail) | 7 | 27.0 | 26.0 | 13–40 (8.88) | **7/7 (100%)** | **6/7 (85.7%)** | 5/7 (71.4%) | 4/7 (57.1%) | 3/7 (42.9%) | 2/7 (28.6%) | 5/5 at 15+ | **15+ PTS** | *10+ PTS* | **10+ PTS** | Sole miss `<15` was `13 PTS` (`6-23 FG`) @ DET opener; `19+` in 6 straight since. |
| **20** | **Ty Jerome** (`MEM`, Avail) | 7 | 27.4 | 28.0 | 10–45 (11.70) | **7/7 (100%)** | **6/7 (85.7%)** | 5/7 (71.4%) | 4/7 (57.1%) | 3/7 (42.9%) | 2/7 (28.6%) | 4/5 at 15+ | **15+ PTS** | *10+ PTS* | **10+ PTS** | **Outlier Flag**: `45` & `40` PTS games widen SD (`11.70`); miss `<15` = `10p` in `24m` blowout. |
| **21** | **Cooper Flagg** (`DAL`, Avail) | 7 | 24.3 | 26.0 | 14–33 (7.05) | **7/7 (100%)** | **6/7 (85.7%)** | 4/7 (57.1%) | 4/7 (57.1%) | 2/7 (28.6%) | 0/7 (0%) | 5/5 at 15+ | **15+ PTS** | *10+ PTS* | **10+ PTS** | Sole miss `<15` was `14 PTS` in `17 MIN` short appearance @ IND (`10-23`). |
| **22** | **Damian Lillard** (`POR`, Avail) | 7 | 20.1 | 21.0 | 9–25 (5.03) | 6/7 (85.7%) | **6/7 (85.7%)** | 5/7 (71.4%) | 2/7 (28.6%) | 0/7 (0%) | 0/7 (0%) | 4/5 at 20+ | **15+ PTS** | None | None | Sole miss was `9 PTS` (`3-13 FG`) in `-21` blowout vs MEM; `20+` in all 3G without Morant. |
| **23** | **Dejounte Murray** (`NOP`, Avail) | 5 | 18.2 | 20.0 | 10–23 (4.75) | **5/5 (100%)** | **4/5 (80.0%)** | 3/5 (60%) | 0/5 (0%) | 0/5 (0%) | 0/5 (0%) | 4/5 at 15+ | **15+ PTS** | *10+ PTS* | **10+ PTS** | `N=5` sample; sole miss `<15` was `10 PTS` vs DEN (`10-28`). |
| **24** | **Victor Wembanyama** (`SAS`, Avail) | 8 | 29.0 | 27.0 | 12–52 (13.25) | **8/8 (100%)** | 6/8 (75%) | 6/8 (75%) | 5/8 (62.5%) | 3/8 (37.5%) | 3/8 (37.5%) | 4/5 at 25+ | **10+ PTS** | **10+ PTS** | **10+ PTS** | **Outlier Flag**: `52 PTS` G8 inflates `29.0` mean; two `12-PT` games (`1-13 FG` vs OKC; `24m` blowout vs UTA). |
| **25** | **Nickeil Alexander-Walker** (`ATL`, Avail) | 9 | 21.7 | 23.0 | 12–34 (7.67) | **9/9 (100%)** | 6/9 (66.7%) | 5/9 (55.6%) | 4/9 (44.4%) | 2/9 (22.2%) | 0/9 (0%) | 4/5 at 20+ | **10+ PTS** | **10+ PTS** | **10+ PTS** | `12+ PTS` in `9/9`; `30.0 PPG` over L2 without Jalen Johnson. |
| **26** | **Jaden McDaniels** (`MIN`, Avail) | 9 | 16.4 | 15.0 | 13–23 (3.13) | **9/9 (100%)** | 5/9 (55.6%) | 1/9 (11.1%) | 0/9 (0%) | 0/9 (0%) | 0/9 (0%) | 5/5 at 13+ | **10+ PTS** | **10+ PTS** | **10+ PTS** | Custom `13+` floor is `9/9` (`100%`) with ultra-low `3.13` SD! *(Ayo Dosunmu: `5/5` at `15+` as starter)*. |

*(Other notable `10+ PTS` `>=85%` floors from tonight's slate: **Dylan Harper** `8/8 [100%]`, **Immanuel Quickley** `8/8 [100%]`, **James Harden** `8/8 [100%]`, **De'Aaron Fox** `8/8 [100%]`, **Joel Embiid** `7/7 [100%]`, **LeBron James** `7/7 [100%]`, **Jalen Johnson** `7/7 [100%, Quest]`, **Brandon Miller** `8/9 [88.9%]`, **Naz Reid** `8/9 [88.9%]`, **LaMelo Ball** `8/9 [88.9%]`, **Walker Kessler** `8/9 [88.9%]`, **CJ McCollum** `8/9 [88.9%]`, **Kyshawn George** `7/8 [87.5%]`, **Cameron Boozer** `7/8 [87.5%]`, **P.J. Washington** `7/8 [87.5%]`, **Saddiq Bey** `7/8 [87.5%]`, **Stephon Castle** `7/8 [87.5%]`, **Lauri Markkanen** `6/7 [85.7% — only miss was 6m injury exit]`.)*

---

### 2. Assists Consistency Table (`3+, 5+, 7+, 8+, 10+, 12+`)

| Rank | Player (Team, Status) | GP | Mean | Med | Min–Max (SD) | 3+ | 5+ | 7+ | 8+ | 10+ | 12+ | L5 Form | >=80% Floor | >=88–90% Floor | 100% Floor | Miss Context & Outlier Inflation Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **1** | **Trae Young** (`WAS`, Avail) | 8 | 9.5 | 9.0 | 6–13 (2.06) | 8/8 (100%) | **8/8 (100%)** | 7/8 (87.5%) | **7/8 (87.5%)** | 3/8 (37.5%) | 2/8 (25%) | 4/5 at 8+ | **8+ AST** | **8+ AST** | **5+ AST** | `6+ AST` in `8/8`; sole miss `<8` was `6 AST` (`4 PF`, `-15` blowout vs ATL `11-04`). |
| **2** | **Jayson Tatum** (`BOS`, Avail) | 7 | 7.9 | 7.0 | 6–11 (1.55) | 7/7 (100%) | **7/7 (100%)** | **6/7 (85.7%)** | 3/7 (42.9%) | 1/7 (14.3%) | 0/7 (0%) | 4/5 at 7+ | **7+ AST** | *5+ AST* | **5+ AST** | `6+ AST` in `7/7` (`1.55` SD!); sole miss `<7` was `6 AST` in `28 MIN` (`+35` blowout vs CHI). |
| **3** | **Luka Doncic** (`LAL`, Avail) | 8 | 8.0 | 7.0 | 5–13 (2.40) | 8/8 (100%) | **8/8 (100%)** | 6/8 (75%) | 3/8 (37.5%) | 2/8 (25%) | 1/8 (12.5%) | 5/5 at 5+ | **5+ AST** | **5+ AST** | **5+ AST** | `5+ AST` in `8/8`; `7+ AST` in `6/8` (had `9 AST` vs POR on Oct 27). |
| **4** | **LeBron James** (`PHI`, Avail) | 7 | 7.4 | 8.0 | 5–10 (1.76) | 7/7 (100%) | **7/7 (100%)** | 5/7 (71.4%) | 4/7 (57.1%) | 1/7 (14.3%) | 0/7 (0%) | 4/5 at 8+ | **5+ AST** | **5+ AST** | **5+ AST** | `5+ AST` in `7/7`; `8+ AST` in 4 straight (`10, 8, 9, 8`). |
| **5** | **James Harden** (`CLE`, Avail) | 8 | 6.2 | 6.0 | 4–9 (1.39) | **8/8 (100%)** | **7/8 (87.5%)** | 3/8 (37.5%) | 1/8 (12.5%) | 0/8 (0%) | 0/8 (0%) | 4/5 at 5+ | **5+ AST** | **5+ AST** | **3+ AST** | Ultra-tight `1.39` SD; sole miss `<5` was `4 AST` (`4 PF`) @ ATL (`10-29`). |
| **6** | **Jamal Shead** (`TOR`, Avail) | 8 | 5.4 | 6.0 | 0–8 (2.23) | 7/8 (87.5%) | **7/8 (87.5%)** | 2/8 (25%) | 1/8 (12.5%) | 0/8 (0%) | 0/8 (0%) | 5/5 at 6+ | **5+ AST** | **5+ AST** | None | Remarkable `5+ AST` in `7/8` despite `21.5` bench MPG; sole miss = `-23` blowout @ MIN. |
| **7** | **Cooper Flagg** (`DAL`, Avail) | 7 | 6.3 | 6.0 | 2–11 (2.55) | 6/7 (85.7%) | **6/7 (85.7%)** | 2/7 (28.6%) | 2/7 (28.6%) | 1/7 (14.3%) | 0/7 (0%) | 5/5 at 5+ | **5+ AST** | None | None | `5+ AST` in 6 straight games (`6, 11, 8, 6, 6, 5`); only miss was NBA opener @ HOU (`2 AST`). |
| **8** | **Dejounte Murray** (`NOP`, Avail) | 5 | 5.6 | 6.0 | 4–7 (1.02) | **5/5 (100%)** | **4/5 (80.0%)** | 1/5 (20%) | 0/5 (0%) | 0/5 (0%) | 0/5 (0%) | 4/5 at 5+ | **5+ AST** | *3+ AST* | **3+ AST** | `4+ AST` in `5/5` (`1.02` SD!). |
| **9** | **Darius Acuff Jr.** (`SAC`, Avail) | 8 | 7.0 | 5.5 | 3–14 (3.67) | **8/8 (100%)** | 6/8 (75%) | 3/8 (37.5%) | 2/8 (25%) | 2/8 (25%) | 2/8 (25%) | **5/5 at 5+** | **3+ AST** | **3+ AST** | **3+ AST** | **Outlier Flag**: `14` & `12` AST games lift `7.0` mean above `5.5` median, but `5+` in 6 straight! |
| **10** | **LaMelo Ball** (`MIN`, Avail) | 9 | 5.9 | 6.0 | 3–8 (1.59) | **9/9 (100%)** | 7/9 (77.8%) | 3/9 (33.3%) | 2/9 (22.2%) | 0/9 (0%) | 0/9 (0%) | 3/5 at 5+ | **3+ AST** | **3+ AST** | **3+ AST** | `3+ AST` in `9/9`, `5+` in `7/9` (one miss was `20-min` 6PF foul-out @ SAS). |
| **11** | **Tyrese Maxey** (`PHI`, Avail) | 9 | 5.4 | 4.0 | 4–11 (2.22) | **9/9 (100%)** | 4/9 (44.4%) | 2/9 (22.2%) | 1/9 (11.1%) | 1/9 (11.1%) | 0/9 (0%) | 2/5 at 5+ | **3+ AST** | **3+ AST** | **3+ AST** | Custom `4+ AST` floor is **9/9 (`100%`)** (`11 AST` & `7 AST` in L2!). |
| **12** | **Dyson Daniels** (`ATL`, Avail) | 9 | 4.7 | 4.0 | 3–8 (1.70) | **9/9 (100%)** | 4/9 (44.4%) | 2/9 (22.2%) | 1/9 (11.1%) | 0/9 (0%) | 0/9 (0%) | 3/5 at 5+ | **3+ AST** | **3+ AST** | **3+ AST** | `3+ AST` in `9/9`; `6.0 APG` without Jalen Johnson (`8 AST` @ WAS Nov 4). |
| **13** | **De'Aaron Fox** (`SAS`, Avail) | 8 | 6.1 | 6.5 | 3–9 (2.15) | **8/8 (100%)** | 5/8 (62.5%) | 4/8 (50%) | 2/8 (25%) | 0/8 (0%) | 0/8 (0%) | 2/5 at 5+ | **3+ AST** | **3+ AST** | **3+ AST** | `3+ AST` in `8/8`, though blowout risk at SAC (`25.3m` avg in blowouts) tempers `7+`. |
| **14** | **Donovan Mitchell** (`CLE`, Avail) | 8 | 5.5 | 5.0 | 3–11 (2.65) | **8/8 (100%)** | 4/8 (50%) | 3/8 (37.5%) | 1/8 (12.5%) | 1/8 (12.5%) | 0/8 (0%) | 3/5 at 5+ | **3+ AST** | **3+ AST** | **3+ AST** | `3+ AST` in `8/8`; `17 AST` combined over L2 vs OKC. |
| **15** | **Cameron Boozer** (`MEM`, Avail) | 8 | 5.4 | 4.5 | 3–12 (2.64) | **8/8 (100%)** | 4/8 (50%) | 1/8 (12.5%) | 1/8 (12.5%) | 1/8 (12.5%) | 1/8 (12.5%) | 2/5 at 5+ | **3+ AST** | **3+ AST** | **3+ AST** | `4+ AST` in `7/8`; `12-AST` game @ POR inflates mean slightly over `4.5` median. |
| **16** | **Jalen Johnson** (`ATL`, **Quest**) | 7 | 7.9 | 7.0 | 3–16 (4.12) | **7/7 (100%)** | 5/7 (71.4%) | 4/7 (57.1%) | 3/7 (42.9%) | 2/7 (28.6%) | 1/7 (14.3%) | 3/5 at 7+ | **3+ AST** | **3+ AST** | **3+ AST** | `16-AST` game vs HOU inflates mean; **Questionable (L Ankle)**. |
| **17** | **Deni Avdija** (`POR`, Avail) | 7 | 6.4 | 6.0 | 2–12 (3.06) | **6/7 (85.7%)** | 5/7 (71.4%) | 3/7 (42.9%) | 2/7 (28.6%) | 1/7 (14.3%) | 1/7 (14.3%) | 4/5 at 5+ | **3+ AST** | None | None | `5+ AST` in `5/7` (`12 AST` @ PHX Nov 4; `9 AST` @ LAL Oct 27). |

*(Note on **Immanuel Quickley** `TOR`: `5.8 APG`, median `7.0`, hit `6+ AST` in `6/8` [`75%`], with two `2-AST` games pulling his `3+` rate to `75%`. Note on **Cam Spencer** `MEM`: `8.4 APG` in L5 [`5/5` at `5+ AST`], `62.5%` full-season due to `16m` G1–G3 roles. Additional `3+ AST` `>=85%` floors: **Scottie Barnes** `8/8 [Quest]`, **Ty Jerome** `7/7`, **Austin Reaves** `8/9`, **Jaden McDaniels** `8/9`, **Dennis Schroder** `8/9 [Quest]`, **Domantas Sabonis** `7/8`, **Keyonte George** `7/8`, **Derrick White** `7/8`, **Kyshawn George** `7/8`, **Stephon Castle** `7/8`, **RJ Barrett** `7/8`, **Ryan Rollins** `7/8`, **Trey Murphy III** `6/7 [Prob]`, **Kyrie Irving** `5/6 [83.3%]`.)*

---

### 3. Rebounds Consistency Table (`5+, 7+, 8+, 10+, 12+, 15+`)

| Rank | Player (Team, Status) | GP | Mean | Med | Min–Max (SD) | 5+ | 7+ | 8+ | 10+ | 12+ | 15+ | L5 Form | >=80% Floor | >=88–90% Floor | 100% Floor | Miss Context & Outlier Inflation Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **1** | **Domantas Sabonis** (`SAC`, Avail) | 8 | 14.9 | 15.0 | 7–19 (3.44) | 8/8 (100%) | **8/8 (100%)** | 7/8 (87.5%) | 7/8 (87.5%) | **7/8 (87.5%)** | 5/8 (62.5%) | 4/5 at 14+ | **12+ REB** | **12+ REB** | **7+ REB** | `14+ REB` in `7/8` (even in `-27` & `-31` blowouts!); sole miss = `7 REB` (`4 PF`, `+15` @ DAL). |
| **2** | **Walker Kessler** (`LAL`, Avail) | 9 | 10.2 | 9.0 | 7–15 (3.01) | 9/9 (100%) | **9/9 (100%)** | **8/9 (88.9%)** | 3/9 (33.3%) | 3/9 (33.3%) | 2/9 (22.2%) | **5/5 at 8+** | **8+ REB** | **8+ REB** | **7+ REB** | Sole miss `<8` was `7 REB` (`4 PF`, `28 MIN` @ UTA); `12.0 RPG` over L5. |
| **3** | **Rudy Gobert** (`MIN`, Avail) | 8 | 11.9 | 12.0 | 4–20 (4.37) | 7/8 (87.5%) | 7/8 (87.5%) | **7/8 (87.5%)** | 6/8 (75%) | 4/8 (50%) | 2/8 (25%) | 4/5 at 10+ | **8+ REB** | **8+ REB** | None | `9+ REB` in `7/8`; sole miss was `4 REB` in `20 MIN` small-ball matchup vs GSW. |
| **4** | **Donovan Clingan** (`POR`, Avail) | 7 | 10.6 | 10.0 | 7–18 (3.33) | 7/7 (100%) | **7/7 (100%)** | **6/7 (85.7%)** | 4/7 (57.1%) | 1/7 (14.3%) | 1/7 (14.3%) | **5/5 at 8+** | **8+ REB** | *7+ REB* | **7+ REB** | Sole miss `<8` was `7 REB` in `21 MIN` (`+41` opener blowout); `10 REB` @ LAL Oct 27. |
| **5** | **Victor Wembanyama** (`SAS`, Avail) | 8 | 12.4 | 12.0 | 7–24 (5.05) | 8/8 (100%) | **8/8 (100%)** | 6/8 (75%) | 6/8 (75%) | 4/8 (50%) | 1/8 (12.5%) | 4/5 at 10+ | **7+ REB** | **7+ REB** | **7+ REB** | **Outlier Flag**: `24 REB` G8 lifts mean; hit `10 REB` in `27m` vs SAC Oct 27. |
| **6** | **Joel Embiid** (`PHI`, Avail) | 7 | 10.0 | 11.0 | 7–15 (2.67) | 7/7 (100%) | **7/7 (100%)** | 5/7 (71.4%) | 4/7 (57.1%) | 1/7 (14.3%) | 1/7 (14.3%) | 4/5 at 8+ | **7+ REB** | **7+ REB** | **7+ REB** | `7+ REB` in `7/7`, `11+ REB` in `4/7` (`15 REB` @ DET Nov 4). |
| **7** | **Cedric Coward** (`MEM`, Avail) | 7 | 8.7 | 9.0 | 7–11 (1.67) | 7/7 (100%) | **7/7 (100%)** | 4/7 (57.1%) | 2/7 (28.6%) | 0/7 (0%) | 0/7 (0%) | 5/5 at 7+ | **7+ REB** | **7+ REB** | **7+ REB** | Lowest REB SD (`1.67`) on slate; `7+ REB` even in `23m` & `27m` blowouts. |
| **8** | **Jalen Johnson** (`ATL`, **Quest**) | 7 | 9.0 | 9.0 | 7–14 (2.20) | 7/7 (100%) | **7/7 (100%)** | 5/7 (71.4%) | 1/7 (14.3%) | 1/7 (14.3%) | 0/7 (0%) | 5/5 at 7+ | **7+ REB** | **7+ REB** | **7+ REB** | `7+ REB` in `7/7`; **Questionable (Left Ankle Sprain)**. |
| **9** | **Cameron Boozer** (`MEM`, Avail) | 8 | 9.8 | 10.0 | 6–13 (2.28) | **8/8 (100%)** | **7/8 (87.5%)** | 6/8 (75%) | 4/8 (50%) | 2/8 (25%) | 0/8 (0%) | 4/5 at 7+ | **7+ REB** | **7+ REB** | **5+ REB** | `6+ REB` in `8/8`; sole miss `<7` was `6 REB` vs IND (`11-04`). |
| **10** | **Derik Queen** (`NOP`, Avail) | 8 | 7.9 | 8.0 | 2–12 (2.71) | 7/8 (87.5%) | **7/8 (87.5%)** | 5/8 (62.5%) | 2/8 (25%) | 1/8 (12.5%) | 0/8 (0%) | 4/5 at 7+ | **7+ REB** | **7+ REB** | None | Hit `7+` in `7/8` despite `24.1` bench MPG; sole miss = `2 REB` vs SAC (`10-29`). |
| **11** | **Moussa Diabate** (`CHA`, **Quest**) | 9 | 9.1 | 8.0 | 5–17 (3.35) | **9/9 (100%)** | 7/9 (77.8%) | 7/9 (77.8%) | 2/9 (22.2%) | 2/9 (22.2%) | 1/9 (11.1%) | 4/5 at 8+ | **5+ REB** | **5+ REB** | **5+ REB** | `5.2 OREB/g` (`17 REB` outlier vs WAS); **Questionable (R Quad)**. |
| **12** | **Anthony Davis** (`WAS`, **Quest**) | 8 | 9.2 | 9.5 | 5–13 (2.54) | **8/8 (100%)** | 6/8 (75%) | 6/8 (75%) | 4/8 (50%) | 2/8 (25%) | 0/8 (0%) | 4/5 at 8+ | **5+ REB** | **5+ REB** | **5+ REB** | `5+ REB` in `8/8` (`10 REB` vs ATL Nov 4); **Questionable (R Ankle)**. |
| **13** | **Naz Reid** (`CHA`, Avail) | 9 | 8.3 | 9.0 | 5–12 (2.49) | **9/9 (100%)** | 5/9 (55.6%) | 5/9 (55.6%) | 3/9 (33.3%) | 1/9 (11.1%) | 0/9 (0%) | 5/5 at 5+ | **5+ REB** | **5+ REB** | **5+ REB** | `5+ REB` in `9/9` (even in `13-min` short game @ DET). |
| **14** | **Luka Doncic** (`LAL`, Avail) | 8 | 8.1 | 7.5 | 5–15 (2.85) | **8/8 (100%)** | 6/8 (75%) | 4/8 (50%) | 1/8 (12.5%) | 1/8 (12.5%) | 1/8 (12.5%) | 4/5 at 7+ | **5+ REB** | **5+ REB** | **5+ REB** | `5+ REB` in `8/8` (`15 REB` outlier vs TOR lifts mean above `7.5` median). |
| **15** | **Ace Bailey** (`UTA`, Avail) | 8 | 7.2 | 6.5 | 5–12 (2.33) | **8/8 (100%)** | 4/8 (50%) | 2/8 (25%) | 2/8 (25%) | 1/8 (12.5%) | 0/8 (0%) | 5/5 at 5+ | **5+ REB** | **5+ REB** | **5+ REB** | `5+ REB` in `8/8` (`2.1 OREB/g`) vs DAL (`#29 DRB%`). |
| **16** | **Isaiah Hartenstein** (`OKC`, Avail) | 8 | 10.1 | 12.0 | 3–14 (3.92) | **7/8 (87.5%)** | 6/8 (75%) | 5/8 (62.5%) | 5/8 (62.5%) | 5/8 (62.5%) | 0/8 (0%) | **5/5 at 7+** | **5+ REB** | **5+ REB** | None | Sole miss `<6` was `3 REB` in `17 MIN` (`5 PF`) G1; **12.0 RPG (`4/5` at `12+`) over L5**. |
| **17** | **Evan Mobley** (`CLE`, Avail) | 8 | 8.2 | 9.0 | 4–12 (2.59) | **7/8 (87.5%)** | 6/8 (75%) | 5/8 (62.5%) | 4/8 (50%) | 1/8 (12.5%) | 0/8 (0%) | 4/5 at 5+ | **5+ REB** | **5+ REB** | None | Sole miss `<5` was `4 REB` @ ATL; lone-big upside if Jarrett Allen sits. |
| **18** | **Onyeka Okongwu** (`ATL`, Avail) | 9 | 8.4 | 9.0 | 4–16 (3.83) | 7/9 (77.8%) | 5/9 (55.6%) | 5/9 (55.6%) | 4/9 (44.4%) | 2/9 (22.2%) | 1/9 (11.1%) | **4/5 at 10+** | *Below (`77.8%`)* | None | None | **L4 Streak**: `12, 10, 10, 16 REB` (`13.0 RPG` without Johnson); two early `4-REB` games (`+47` blowout & `5 PF`). |

*(Additional `5+ REB` `>=80%` floors on tonight's slate: **Jaden McDaniels** `8/9 [88.9%]`, **Jarrett Allen** `7/8 [87.5%, Quest — only miss was 7m injury exit]`, **Scottie Barnes** `7/8 [87.5%, Quest]`, **Dylan Harper** `7/8 [87.5%]`, **Stephon Castle** `7/8 [87.5%]`, **Paul George** `6/7 [85.7%]`, **LeBron James** `6/7 [85.7%]`, **Lauri Markkanen** `6/7 [85.7% — only miss was 6m injury exit]`, **Cooper Flagg** `6/7 [85.7%]`, **Dejounte Murray** `4/5 [80%]`; **P.J. Washington** & **Kel'el Ware** are both `6/8 [75%]` overall and `5/5 [100%]` in L5.)*

---

## PART E — MATCHUP, INJURIES AND SCHEDULE (ALL 9 FIXTURES)

*(Official Injury Report verified as of **11/06/2026 04:45 AM ET** via [Injury-Report_2026-11-06_04_45AM.pdf](../data/injury_reports/Injury-Report_2026-11-06_04_45AM.pdf). All 18 teams enter tonight on **1 rest day** [all last played Wednesday, Nov 4], so **zero teams are on the 2nd night of a B2B**, though **6 teams play tomorrow [Sat Nov 7] on the front end of a B2B** and **3 teams are on 4-games-in-6-nights**.)*

### 1. `WAS (4-4)` @ `ATL (5-4)` — 7:00 PM EST / 11:00 AM AEDT
- **Confirmed Out / Doubtful**: **WAS**: Justin Champagnie (*Out — R Foot*), Reece Beekman (*Out*), Tristan Vukcevic (*Out*), Jamir Watkins (*Out*), Felix Okpara (*Doubtful*). **ATL**: Jock Landale (*Out — L Hip*), Mouhamed Gueye (*Out — L Foot*), Asa Newell (*Out*), Keshon Gilbert (*Out*), Henri Veesaar (*Out*).
- **Uncertain Availability & Dual Scenarios**:
  - **Anthony Davis (`WAS`, Questionable — R Ankle)** & **Jalen Johnson (`ATL`, Questionable — L Ankle, missed L2)**:
  - *If Johnson is Out (as in L2)*: Verified 2026–27 on/off splits show **Alexander-Walker** jumps from `19.3 PPG (14.7 FGA)` -> **`30.0 PPG (22.5 FGA)`**, **Okongwu** jumps from `7.1 RPG` -> **`13.0 RPG`** (`32.0m`), **Daniels** jumps from `4.3a/5.0r` -> **`6.0a/12.5r`**, and **McCollum** jumps from `2.7 APG` -> **`8.5 APG`**. *If Johnson plays*: Expect `30–32m` (possible cap with Sat `vs BKN` B2B), trimming NAW's FGA back to `~16` and Okongwu's REB to `8–9`.
  - *If AD is Out*: **Alex Sarr** shifts to lone five (`30–32m`, `8+ REB` outlook), **Trae Young** (`USG%` `24.5%` -> `~31%`) and **Kyshawn George** (`23.5p/6.0a` L2) absorb `+18` vacated FGA, and WAS loses its interior anchor.
- **Defensive Matchup & Pace**: Projected Pace **~100.3** (`WAS 98.2`, `ATL 102.0`). WAS ranks **28th in DRB% (`68.5%`, `15.0` Opp OREB/g — Okongwu & Daniels combined for `32 REB [10 OREB]` vs WAS on Nov 4!)** and allows `42.4` Opp 3PA/g (ideal for ATL's league-high `44.0` 3PA/g). ATL ranks weak at the rim (**`74.5%` Opp FG at `0–3 ft`**, `27.2` Opp AST/g), favoring Trae Young PnR lobs/drives, though ATL forces `18.4` TOV/g (`16.0%` TOV%).
- **Schedule, Travel & Blowout Risk**: Rematch of Nov 4 in Washington (`ATL W 120-105`); both teams flew together from DC to Atlanta (`1` rest day, no TZ change). **Both face a B2B tomorrow** (`WAS @ OKC`, `ATL vs BKN`). **Blowout Risk**: **Moderate** (`ATL -6.5`; escalates to **Elevated** if AD sits while Johnson plays).

### 2. `BOS (6-2)` @ `CHA (3-6)` — 7:00 PM EST / 11:00 AM AEDT
- **Confirmed Out**: **BOS**: Two-Way/G-League assignments only. **CHA**: Kon Knueppel (*Out — L Hamstring*), Grant Williams (*Out — R Hamstring*).
- **Uncertain Availability**: **BOS**: Payton Pritchard (*Questionable — R Eye Abrasion*; if Out, Derrick White & Jayson Tatum absorb backup PG creation). **CHA**: Moussa Diabate (*Questionable — R Quad*) & Dennis Schroder (*Questionable — L Thigh Soreness*). *If Diabate sits*, **Naz Reid** plays `34–36 MIN` as lone stretch-5. *If Schroder sits*, **Sion James** & **Grayson Allen** (`26.4m`, `71.5% TS`) handle secondary initiation.
- **Defensive Matchup & Pace**: Projected Pace **~96.0** (slowest game on slate: `BOS 96.4`, `CHA 95.6`; O/U `209.5`). CHA ranks **25th in DRtg (`114.2`)** and allows **`.555` Opp eFG% (`38.9%` Opp 3P%)**, giving Tatum and Paul George (`8.3` 3PA/g) clean perimeter looks, though CHA is #1 in DRB% (`78.1%`). BOS (`110.9` DRtg) forces `17.4` TOV/g (`15.3%` TOV%) against CHA's league-worst ball security (**`17.1%` TOV%, `102.6` ORtg**), while BOS's `69.9%` DRB% gives Diabate/Reid second-chance windows.
- **Schedule, Travel & Blowout Risk**: BOS is on **4-games-in-6-nights** (flew Boston -> Charlotte, `1` rest day; Tatum rested Wed vs MIL so he has `3` days rest). CHA flew Brooklyn -> Charlotte (`1` rest day, 0-5 L5 skid). **Blowout Risk**: **Elevated** (`BOS -8.5`; CHA lost two of L8 home/road games by `33` and `47` pts; Tatum drops from `37.8m` close to `30.0m` in blowouts, PG13 drops from `33.8m` to `25.0m`).

### 3. `PHI (8-1)` @ `CLE (4-4)` — 7:30 PM EST / 11:30 AM AEDT
- **Confirmed Out / Doubtful**: **PHI**: Dominick Barlow (*Out*), Ariel Hukporti (*Out*), Adem Bona (*Doubtful — Cervical Sprain*). **CLE**: Jaylon Tyson (*Out — R Ankle*), Nae'Qwan Tomlin (*Out*).
- **Uncertain Availability**: **CLE**: **Jarrett Allen (*Questionable — R Knee Contusion***, exited after `7 MIN` @ OKC Nov 4), Tyrese Proctor (*Questionable*), Peyton Watson (*Questionable — R Hamstring*). *If Allen sits* (strong possibility with CLE hosting NYK tomorrow on a B2B), **Evan Mobley** anchors center solo (`35–37m`, `+2.5` REB boost) while CLE loses double-big rim deterrence vs Embiid.
- **Defensive Matchup & Pace**: Projected Pace **~100.5** (`PHI 99.8`, `CLE 101.1`). PHI owns the **#1 Defense in the NBA (`105.4` DRtg, `.500` Opp eFG%, `23.8` Opp AST/g)**. CLE owns a top-6 offense (`116.4` ORtg, `.549` eFG%, `37.2%` 3P) but ranks **26th in DRtg (`114.3`, `117.1` Opp PPG, `35.2%` Opp 3P, only `11.2%` Opp TOV forced)**—ideal for Maxey (`32p` vs CLE Oct 22), Brown, LeBron, and Embiid.
- **Schedule, Travel & Blowout Risk**: PHI (`5-0` L5, `4-0` Away) hopped Detroit -> Cleveland (`1` rest day, next game Nov 8). CLE (`2-3` L5) flew Oklahoma City -> Cleveland (`1` rest day, **front end of B2B** vs NYK tomorrow). **Blowout Risk**: **Low** (`PHI -2.5`; premier competitive heavyweight clash; full `34–39m` starter workloads expected).

### 4. `UTA (1-7)` @ `DAL (4-4)` — 8:00 PM EST / 12:00 PM AEDT
- **Confirmed Out & Probable**: **UTA**: Jaren Jackson Jr. (*Out — R MCL Tear*), Jusuf Nurkic (*Out — R Plantar Plate*). **DAL**: Dereck Lively II (*Out — R Foot*), Tarik Biberovic (*Out*), Sergio de Larrea (*Out*); Santi Aldama & Max Christie (*Probable*), Caleb Martin (*Available*).
- **Lineup & On/Off Effects**: Without JJJ & Nurkic (`0-4` since JJJ's injury), UTA starts smaller/thinner up front; **Markkanen** (`18.7p / 8.0r` in 3 full games w/o JJJ) and **Keyonte George** (`18.8` FGA w/o JJJ) carry the offense. Without Lively, **Gafford** (`25.2m` L5) and **P.J. Washington** (`35.8m` L5) absorb DAL's center/PF minutes, while **Cooper Flagg** (`38.4m` L5) and **Kyrie Irving** (`35.5m` L2) run all half-court offense.
- **Defensive Matchup & Pace**: Projected Pace **~99.5** (`UTA 99.8`, `DAL 99.1`). UTA ranks **28th in DRtg (`116.2`, `119.0` Opp PPG)** and allows **`48.9%` FG in the short paint (`3–10 ft`)** and `36.3%` Opp 3P—tailor-made for Flagg drives and Kyrie pull-ups. Conversely, DAL ranks **29th in DRB% (`67.9%`, `14.9` Opp OREB/g)**, boosting Markkanen and Ace Bailey on the glass.
- **Schedule, Travel & Blowout Risk**: UTA (`0-5` L5, `3rd` consecutive road game: San Antonio -> New Orleans -> Dallas, `1` rest day after OT loss). DAL (`1` rest day, short hop San Antonio -> Dallas, next game Nov 8). **Blowout Risk**: **Moderate-to-Elevated** (`DAL -7.5`; UTA lost 3 of L5 by `20+`, where Keyonte George's minutes fell to `22–29m`).

### 5. `OKC (6-2)` @ `MEM (6-2)` — 8:00 PM EST / 12:00 PM AEDT
- **Confirmed Out**: **OKC**: Chet Holmgren (*Out — R Knee*), Jalen Williams (*Out — L Ankle*), Cason Wallace (*Out — L Shoulder*), Jaylin Williams (*Out — Back*), Nikola Topic (*Out*), Thomas Sorber (*Out*). **MEM**: Scotty Pippen Jr. (*Out — Lumbar Disc*), Isaiah Stewart (*Out — R Knee Bone Bruise*). *(No Questionable starters on either team!)*
- **Lineup & On/Off Effects**: In 5 games without Holmgren & J-Dub, **SGA** averages `31.6 PPG` (`42.5p / 8.0a` L2), **Ajay Mitchell** starts and jumps from `11.3 PPG` -> **`21.6 PPG` (`15.6` FGA)**, and **Hartenstein** jumps from `7.0 RPG` -> **`12.0 RPG` (`26.2m`)**. For MEM, with Stewart Out, rookie **Cameron Boozer** (`32.1m`) and **Zach Edey** anchor the paint while **Cam Spencer** (`8.4 APG` L5) backs up **Ty Jerome** (`32.8% USG`).
- **Defensive Matchup & Pace**: Projected Pace **~99.2** (`OKC 98.2`, `MEM 100.1`). MEM boasts the **#4 Offense (`118.9` ORtg, `40.0%` 3P)** and **#4 Defense (`108.3` DRtg, `23.8` Opp AST/g, `.647` Rim FG%)**, but allows **`50.0%` FG in the `3–10 ft` short-paint/floater zone**—SGA's exact signature scoring zone! OKC (`110.7` DRtg, `116.2` Opp PPG over L5 without Chet) surrenders **`42.4` Opp 3PA/g at `36.0%`**, feeding MEM's elite `15.8` 3PM/g spacing.
- **Schedule, Travel & Blowout Risk**: OKC flew OKC -> Memphis (`1` rest day, **front end of B2B** vs WAS tomorrow). MEM is on its **4th consecutive home game** (`1` rest day, next game Nov 9). **Blowout Risk**: **Low** (`OKC -3.5`; two `6-2` West contenders).

### 6. `TOR (4-4)` @ `MIL (1-7)` — 8:00 PM EST / 12:00 PM AEDT
- **Confirmed Out**: **TOR**: Kawhi Leonard (*Out — L Knee Mgmt*), Nate Bittle (*Out*). **MIL**: Two-Way/G-League assignments only.
- **Uncertain Availability**: **TOR**: **Scottie Barnes (*Questionable — L Adductor/Groin Soreness***). *If Barnes plays*: Expect `34–36m` against MIL's porous frontcourt. *If Barnes sits*: **RJ Barrett** (`20.9 PPG`) and **Immanuel Quickley** (`17.4p/5.8a`) become undisputed 1A/1B creators (`+4–5` FGA each), **Jamal Shead** (`5.4 APG`) sees `25–27m`, and TOR's `-6.5` spread compresses sharply.
- **Defensive Matchup & Pace**: Projected Pace **~101.5** (`TOR 101.3`, `MIL 101.4`; O/U `230.5`). MIL ranks **29th in DRtg (`120.6`, `122.3` Opp PPG)**, **30th in Opp AST (`28.1/g`)**, **30th in Opp REB (`48.6/g`, `71.1%` DRB%)**, and **30th in Opp TOV% (`10.7%`)**—an A+ statistical environment for Quickley/Shead assists and TOR wings/rebounders. TOR (`112.1` DRtg, `119.4` Opp PPG L5) allows **`.550` Opp eFG% (`36.9%` 3P)** while forcing a league-high `20.1` TOV/g (`17.6%` TOV%), giving low-turnover shooter **Tyler Herro** (`8.5` 3PA/g) high volume while pressuring MIL's young guards.
- **Schedule, Travel & Blowout Risk**: TOR is on **4th consecutive road game & 4-in-6** (`LA -> LA -> Denver [altitude] -> Milwaukee`, `1` rest day). MIL returned home from Boston (`1` rest day). **Blowout Risk**: **Moderate** (`TOR -6.5`; TOR road fatigue + Barnes' groin tag temper runaway risk).

### 7. `MIN (6-3)` @ `NOP (4-4)` — 8:00 PM EST / 12:00 PM AEDT
- **Confirmed Out & Questionable/Probable**: **MIN**: Anthony Edwards (*Out — R Knee Arthroscopy*), Donte DiVincenzo (*Out — R Achilles*), Terrence Shannon Jr. (*Questionable — L Hip*). **NOP**: Yves Missi (*Out — L Knee*); Trey Murphy III (*Probable — Bilateral Patella Tendinopathy*).
- **Lineup & On/Off Effects**: Across 5 games without Edwards (`3-2`), **Ayo Dosunmu** moved into the starting lineup (`34.2m`, **`19.8 PPG`, `5/5` at `15+ PTS`**), **LaMelo Ball** rose to `19.2p / 5.6a`, and **Jaden McDaniels** climbed to `17.6p / 4.2a` (`15.6` FGA). For NOP, **Dejounte Murray** logged `45 MIN` in his Nov 4 OT return (`20p/4a/8r`), joining **Zion Williamson**, **Murphy III**, **Jeremiah Fears**, and **Derik Queen** (`24.1m` C with Missi Out).
- **Defensive Matchup & Pace**: Projected Pace **~101.5** (`MIN 100.4`, `NOP 102.4` [#1 Pace on slate]; O/U `231.5`). Contrast of styles: NOP attacks the paint relentlessly (**#1 FT/FGA `.298`, `32.0` FTA/g**, fewest 3PM `9.0`), but runs into **#2 DRtg MIN (`105.9` DRtg, `.499` Opp eFG%)** anchored by Gobert & McDaniels. Conversely, NOP's defense (`112.1` DRtg, `119.3` Opp PPG, **`.737` Rim FG%, `.517` Short-Paint FG%, `27.6` Opp AST/g**) bleeds efficient looks toDosunmu/McDaniels cuts and LaMelo/Gobert PnRs.
- **Schedule, Travel & Blowout Risk**: MIN flew Houston -> New Orleans (`1` rest day, short flight, no TZ change). NOP is on its 2nd straight home game (`1` rest day after OT win vs UTA; `4-1` L5). **Blowout Risk**: **Low-to-Moderate** (`MIN -4.5`).

### 8. `POR (6-1)` @ `LAL (7-2)` — 10:00 PM EST / 2:00 PM AEDT
- **Confirmed Out & Questionable**: **POR**: Ja Morant (*Out — L Hamstring*), Shaedon Sharpe (*Out — R Meniscus*), Vit Krejci (*Out*). **LAL**: Walker Kessler (*Available — Finger Splint*), Sandro Mamukelashvili (*Questionable — Illness*).
- **Lineup & On/Off Effects**: Without Morant (`3-0` record), **Damian Lillard** (`22.3p / 5.0a`) and **Deni Avdija** (`24.3p / 6.3a`, `31.4% AST%`) split all primary creation while **Donovan Clingan** (`12.7 RPG` w/o Morant) dominates the paint. LAL's core (**Luka Doncic** `40.0% USG`, **Austin Reaves**, **Walker Kessler**) is 100% intact.
- **Defensive Matchup & Pace**: Projected Pace **~100.0** (`POR 99.6`, `LAL 99.9`; highest O/U **`232.5`** because **POR is #1 ORtg [`122.3`]** and **LAL is #2 ORtg [`121.9`, `.602` eFG%]**!). LAL ranks **24th in DRtg (`114.0`, `26.9` Opp AST/g, `36.4%` Opp 3P)** and **28th in DRB% (`68.4%`, `13.8` Opp OREB/g)**—fueling Clingan (`18.2% ORB%`), Avdija (`23p/9a` @ LAL Oct 27), and Lillard (`21p` @ LAL Oct 27). POR (`111.1` DRtg, `#2 DRB% 76.2%`) forces Luka into tough pull-ups (`52.5%` Opp FG at `3–10 ft`), which Luka still torched for `41p/9a` on Oct 27.
- **Schedule, Travel & Blowout Risk**: POR (`5-0` Away!) is on its **4th consecutive road game** (`Utah -> Denver -> Phoenix -> LA`, `1` rest day, **front end of B2B** vs SAS tomorrow). LAL is on **4-in-6** (`Sacramento -> LA`, `1` rest day, `4-1` Home averaging `130.0 PPG`). **Blowout Risk**: **Low** (`LAL -2.5`; game of the night).

### 9. `SAS (6-2)` @ `SAC (1-7)` — 10:00 PM EST / 2:00 PM AEDT
- **Confirmed Out**: **SAS**: Tobias Harris (*Out — L Calf*), Jayden Quaintance (*Out*). **SAC**: Keegan Murray (*Out — L Ankle Capsulitis*), Maxime Raynaud (*Out*), Ben Simmons (*Out*).
- **Defensive Matchup & Pace**: Projected Pace **~100.8** (`SAS 99.5`, `SAC 101.8`). **Biggest mismatch on the board**: SAC ranks **30th (Dead Last) in DRtg (`121.1`, `123.3` Opp PPG, `.577` Opp eFG%)** and surrenders an astonishing **`80.9%` Opp FG at the rim (`0–3 ft`)** and **`53.4%` at `3–10 ft`** with zero shot-blocking alongside Sabonis! Wembanyama shot `14-21 FG` (`29p/10r` in `27m`) vs SAC on Oct 27. Meanwhile SAS ranks **#3 in DRtg (`107.8`, `.498` Opp eFG%, `.640` Rim FG%, `.338` Short-Paint FG%)**, suffocating SAC's `107.3` ORtg (`TS% .499` for rookie Darius Acuff Jr.).
- **Schedule, Travel & Blowout Risk**: SAS (`5-0` L5) flew San Antonio -> Sacramento (`2` time zones West, `1` rest day, **front end of B2B** `@ POR` tomorrow!). SAC (`0-3` Home, `-14.0` MOV) is on its 2nd straight home game (`1` rest day). **Blowout Risk**: **Elevated (Extreme — `SAS -15.5`)**. Wembanyama (`26.7m` in blowouts), Fox (`25.3m`), Harper (`28.3m`), and LaVine (`28.5m`) all carry severe 4Q benching risk; notably, SAC leaves **Acuff (`35.5m` in blowouts)** and **Sabonis (`35.0m` in blowouts)** on the court regardless of margin.

---

## PART F — MATCH PREDICTIONS

| Matchup | Key Net Rating & Four-Factors Edge | Expected Winner | Expected Pace & Score Range (Margin) | Sourced Win Probabilities (BPI \| Vig-Free Market) | Confidence | Main Upset / Reversal Scenario |
|---|---|---|---|---|---|---|
| **1. WAS @ ATL** | ATL `+2.8` NRtg vs WAS `-0.1`; ATL `29.1%` ORB% vs WAS `68.5%` DRB%; ATL `15.4` 3PM vs WAS `8.8` 3PM; ATL won H2H `120-105` on Nov 4. | **Atlanta Hawks** | Pace `~100.3` **ATL 116–121, WAS 109–114** *(ATL by 5–8)* | ESPN BPI: **71.3%** Market: **69.1%** | **Medium-High** *(High if AD Out)* | AD plays unhindered while Jalen Johnson sits again, and Trae Young catches fire (`30+p/12+a`) in his Atlanta return while ATL shoots `<32%` on 44+ 3PA. |
| **2. BOS @ CHA** | BOS `+6.1` NRtg (`117.0` ORtg) vs CHA `-11.6` NRtg (`102.6` ORtg, `0-5` L5); CHA `17.1%` TOV% vs BOS `15.3%` Opp TOV%; Tatum & PG13 both active. | **Boston Celtics** | Pace `~96.0` **BOS 110–116, CHA 98–104** *(BOS by 9–13)* | ESPN BPI: **77.2%** Market: **74.4%** | **High** | BOS (`1-2` Away, 4-in-6) shoots cold from three (`<31%`) while Diabate plays and dominates BOS's `69.9%` DRB% alongside a `35+` PT Brandon Miller eruption. |
| **3. PHI @ CLE** | PHI `8-1` (`+5.8` NRtg, `#1` DRtg `105.4`, `4-0` Away, won Oct 22 H2H `114-106`) vs CLE `4-4` (`26th` DRtg `114.3`, Jarrett Allen Questionable, B2B tmrw). | **Philadelphia 76ers** | Pace `~100.5` **PHI 114–119, CLE 110–115** *(PHI by 2–5)* | ESPN BPI: **56.7%** Market: **57.2%** | **Medium** *(Competitive)* | Jarrett Allen plays healthy minutes and CLE replicates its elite home shooting (`121.2` Home PPG, `.549` eFG%, `15.6` 3PM/g) to outgun PHI's half-court offense. |
| **4. UTA @ DAL** | DAL `-0.1` NRtg (`+5.08` SRS, `.540` eFG%) vs UTA `-11.0` NRtg (`1-7`, `0-5` L5, `28th` DRtg `116.2`, missing JJJ & Nurkic on 3rd straight road game). | **Dallas Mavericks** | Pace `~99.5` **DAL 116–122, UTA 106–112** *(DAL by 7–11)* | ESPN BPI: **66.0%** Market: **70.6%** | **High** | UTA exploits DAL's `29th`-ranked DRB% (`67.9%`) for `16+` OREBs while Markkanen & Keyonte George combine for `60+` PTS and `15+` threes. |
| **5. OKC @ MEM** | **Contrarian Data Edge**: Full-strength MEM (`+10.6` NRtg, `#2` SRS `+11.34`, `.560` eFG%, `40.0%` 3P, 4th straight home game) vs depleted OKC (`+1.3` NRtg, missing Chet, J-Dub & Wallace, `116.2` Opp PPG L5, B2B tmrw). | **Memphis Grizzlies** *(Value Upset Pick)* | Pace `~99.2` **MEM 114–119, OKC 111–116** *(MEM by 1–4)* | Market favors OKC (`58.3%` / BPI `67.0%`); **Qualitative lean: MEM** | **Low-Medium** *(Coin-Flip)* | SGA (`85 PTS` over L2) exploits MEM's `50.0%` short-paint defense for another `40+` PT masterclass while MEM's `40%` 3P shooting regresses (as in `103-107` loss vs IND). |
| **6. TOR @ MIL** | TOR `+4.3` NRtg (`116.4` ORtg, `32.0%` ORB%, `17.6%` Opp TOV%) vs MIL `-12.1` NRtg (`1-7`, `29th` DRtg `120.6`, `1-3` Home allowing `125.5` PPG). | **Toronto Raptors** | Pace `~101.5` **TOR 118–124, MIL 110–116** *(TOR by 5–9)* | ESPN BPI: **60.1%** Market: **68.6%** | **Medium-High** *(Low-Med if Barnes Out)* | Scottie Barnes (`Questionable — Groin`) is ruled out on TOR's 4th road game in 6 nights (post-Denver altitude), allowing Tyler Herro (`30+` PTS) to steal it at home. |
| **7. MIN @ NOP** | MIN `+11.1` NRtg (`#1` SRS `+12.07`, `#2` DRtg `105.9`, `.557` eFG%) vs NOP `+2.2` NRtg (`119.3` Opp PPG); Gobert/McDaniels wall neutralizes NOP's rim-reliant offense (`9.0` 3PM/g). | **Minnesota Timberwolves** | Pace `~101.5` **MIN 116–121, NOP 111–116** *(MIN by 4–7)* | ESPN BPI: **73.4%** Market: **62.2%** | **Medium-High** | LaMelo Ball & Rudy Gobert hit early foul trouble against NOP's #1 free-throw rate (`.298` FT/FGA, `32` FTA/g), extending NOP's 4-game win streak with Murray & Murphy back. |
| **8. POR @ LAL** | LAL `7-2` (`4-1` Home scoring `130.0` PPG, `.602` eFG%, Luka averaging `41.0` PPG L5) in revenge spot vs POR (`6-1`, `#1` ORtg `122.3`, missing Ja Morant & Sharpe on 4th straight road game + B2B tmrw). | **Los Angeles Lakers** | Pace `~100.0` **LAL 119–125, POR 115–121** *(LAL by 2–5)* | ESPN BPI: **54.7%** Market: **57.2%** | **Medium** *(Competitive)* | POR (`5-0` Away, beat LAL `136-129` on Oct 27) crushes LAL's `68.4%` DRB% via Donovan Clingan (`15+` REB) while Lillard & Avdija punish LAL's `24th`-ranked defense. |
| **9. SAS @ SAC** | SAS `+8.2` NRtg (`#3` DRtg `107.8`, `5-0` L5, beat SAC `130-103` Oct 27) vs SAC `-13.8` NRtg (`1-7`, `30th` DRtg `121.1`, **`80.9%` Rim FG% allowed** vs Wembanyama). | **San Antonio Spurs** | Pace `~100.8` **SAS 121–127, SAC 104–111** *(SAS by 13–18)* | ESPN BPI: **90.4%** Market: **87.2%** | **Very High** | Extreme 3-point variance (`SAC 18+ 3PM` from LaVine/Acuff while SAS looks ahead to tomorrow's `@ POR` B2B and rests starters early). |

---

## PART G — PLAYER STATISTICAL PROJECTIONS

- **Methodology Note**: Projections weight verified **expected minutes**, **active/inactive lineup scenarios**, **usage/rebound share**, **opponent defensive profile**, and **blowout minute-loss risk** rather than double-counting overlapping `L5` and `26–27` samples. **Threshold Probability Caution**: An observed `7/8 (87.5%)` or `8/8 (100%)` early-season hit rate corresponds to an empirical Laplace-smoothed baseline of roughly `78%–89%` (`(k+1)/(N+2)`), which is then adjusted upward or downward for tonight's matchup, pace, and blowout risk—**never** treated as a `100%` certainty.

| Player | Team (Opp) | Expected MIN *(Blowout / Alt)* | Projected PTS *(Range)* | Projected AST *(Range)* | Projected REB *(Range)* | Reliable Historical Thresholds *(26–27 Hits)* | Confidence & Key Driver / Main Threat |
|---|---|---|---|---|---|---|---|
| **Trae Young** | `WAS` (@ ATL) | **36** *(33 blow)* | **20.5** *(16–27)* *(24.5 if AD Out)* | **9.8** *(7–13)* | **3.5** *(2–6)* | **8+ AST** (`7/8`, 87.5%) \| **15+ PTS** (`7/8`, 87.5%) | **High** — `35.9` MPG floor, Atlanta return, ATL allows `27.2` AST/g & `74.5%` rim FG%; *Threat*: ATL `16%` TOV% pressure. |
| **Anthony Davis** *(Q)* | `WAS` (@ ATL) | **33** *(if active; 0 if Out)* | **24.5** *(18–31)* | **2.2** *(1–4)* | **9.8** *(7–13)* | **15+ PTS** (`7/8`, 87.5%) \| **5+ REB** (`8/8`, 100%) | **Low-Med (Injury)** — `26p/10r` vs ATL Nov 4; *Threat*: **Questionable (R Ankle)** ahead of Sat `@ OKC` B2B. |
| **Kyshawn George** | `WAS` (@ ATL) | **34** *(36 if AD Out)* | **17.5** *(12–24)* *(20.5 if AD Out)* | **5.0** *(3–8)* | **4.2** *(2–7)* | **10+ PTS** (`7/8`, 87.5%) \| **3+ AST** (`7/8`, 87.5%) | **Med-High** — `23.5p/6.0a` L2; *Threat*: Foul trouble (`4+ PF` in 4/8 games). |
| **Nickeil Alexander-Walker** | `ATL` (vs WAS) | **31** *(32 if JJ Out)* | **22.5** *(16–30)* *(26.5 if JJ Out)* | **2.5** *(1–4)* | **3.5** *(2–5)* | **10+ PTS** (`9/9`, 100%) *(20+ in 4/5 L5)* | **High (if JJ Out) / Med (if JJ In)** — WAS allows `42.4` 3PA/g; `30.0` PPG w/o Johnson; *Threat*: Shot drop if Johnson returns. |
| **Jalen Johnson** *(Q)* | `ATL` (vs WAS) | **31** *(if active; 0 if Out)* | **17.5** *(13–23)* | **7.2** *(4–10)* | **8.8** *(7–12)* | **7+ REB**, **10+ PTS**, **3+ AST** (`7/7`, 100%) | **Low-Med (Injury)** — Elitevs WAS `68.5%` DRB%; *Threat*: **Questionable (L Ankle)** + Sat B2B minutes cap. |
| **Onyeka Okongwu** | `ATL` (vs WAS) | **31** *(33 if JJ Out)* | **13.5** *(9–19)* | **3.0** *(1–5)* | **10.2** *(7–14)* *(12.0 if JJ Out)* | *5+ REB (`7/9`, 77.8%; **10+ in 4/4 L4**)* | **High** — `16 REB` vs WAS (`#28 DRB%`) two nights ago; *Threat*: Foul trouble (`4+ PF` in 3 of L5). |
| **Dyson Daniels** | `ATL` (vs WAS) | **31** *(33 if JJ Out)* | **8.5** *(5–13)* | **5.2** *(3–8)* | **7.8** *(5–12)* | **3+ AST** (`9/9`, 100%) | **High (3+ AST)** — `8a/16r` vs WAS Nov 4; *Threat*: Low `15.5%` USG limits scoring. |
| **Jayson Tatum** | `BOS` (@ CHA) | **35** *(29 blow)* | **26.5** *(20–34)* | **7.6** *(6–10)* | **6.2** *(4–9)* | **7+ AST** (`6/7`, 85.7%) \| **15+ PTS** (`6/7`, 85.7%) | **High** — `3` days rest, `39.1%` AST% vs CHA `.555` Opp eFG%; *Threat*: `BOS -8.5` blowout (`30m`) + `96.0` slow pace. |
| **Paul George** | `BOS` (@ CHA) | **32** *(26 blow)* | **19.5** *(15–26)* | **5.2** *(3–8)* | **5.5** *(4–8)* | **15+ PTS** (`7/7`, 100%) \| **5+ REB** (`6/7`, 85.7%) | **High (15+ PTS)** — CHA allows `38.9%` 3P; *Threat*: Slow pace & blowout (`25m` in G3 rout). |
| **Derrick White** | `BOS` (@ CHA) | **33** *(26 blow)* | **14.0** *(9–20)* | **5.4** *(3–8)* | **3.4** *(2–5)* | **3+ AST** (`7/8`, 87.5%) | **Med-High** — `+2–3m` & extra on-ball reps if Pritchard (*Quest*) sits; *Threat*: Blowout benching. |
| **Neemias Queta** | `BOS` (@ CHA) | **27** *(24 blow)* | **10.5** *(6–15)* | **1.5** *(0–3)* | **7.8** *(5–11)* | *5+ REB (`6/8`, 75%; **8.7 RPG in 3 starts**)* | **Medium** — Promoted starter (`26–29m` L3); *Threat*: CHA `#1 DRB% (78.1%)` + foul trouble. |
| **Brandon Miller** | `CHA` (vs BOS) | **34** *(28 blow)* | **20.5** *(13–28)* | **2.6** *(1–5)* | **5.2** *(3–8)* | **10+ PTS** (`8/9`, 88.9%) | **Low-Med** — Huge `21.7` FGA volume, but `.470` TS% vs Tatum/PG13/White + blowout/foul risk. |
| **Naz Reid** | `CHA` (vs BOS) | **32** *(35 if Diabate Out)* | **16.5** *(11–23)* *(19.0 if Diabate Out)* | **1.8** *(0–4)* | **8.5** *(6–12)* *(10.2 if Diabate Out)* | **5+ REB** (`9/9`, 100%) \| **10+ PTS** (`8/9`, 88.9%) | **High (5+ REB)** — BOS `#27 DRB% (69.9%)`; huge bump if Diabate sits; *Threat*: CHA blowout. |
| **Moussa Diabate** *(Q)* | `CHA` (vs BOS) | **28** *(if active; 0 if Out)* | **8.5** *(5–13)* | **2.0** *(1–3)* | **8.8** *(6–13)* | **5+ REB** (`9/9`, 100%) *(7+ in 7/9)* | **Low-Med (Injury)** — Elite `19.2%` ORB% vs BOS glass; *Threat*: **Questionable (R Quad)**. |
| **Tyrese Maxey** | `PHI` (@ CLE) | **38** *(35 blow)* | **28.5** *(23–35)* | **5.8** *(4–9)* | **3.8** *(2–6)* | **25+ PTS** (`8/9`, 88.9%) \| **3+ AST** (`9/9`, 100%) | **Very High** — `37.1` MPG, low blowout risk, `32p/6a` vs CLE (`26th` DRtg) Oct 22; *Threat*: Cold 3P night. |
| **Jaylen Brown** | `PHI` (@ CLE) | **36** *(33 blow)* | **22.0** *(17–28)* | **3.8** *(2–6)* | **6.8** *(4–10)* | **15+ PTS** (`8/8`, 100%) | **Very High (15+ PTS)** — `36.2` MPG (`33+` in all 8G), `21p/8r` vs CLE G2; *Threat*: Shared usage w/ Big 4. |
| **Joel Embiid** | `PHI` (@ CLE) | **34** *(27 blow)* | **21.5** *(15–28)* *(24.0 if Allen Out)* | **4.2** *(2–7)* | **10.2** *(7–14)* *(11.5 if Allen Out)* | **7+ REB** (`7/7`, 100%) \| **10+ PTS** (`7/7`, 100%) | **High** — Non-B2B full workload; feasts if Jarrett Allen (*Quest*) sits; *Threat*: Mobley length. |
| **LeBron James** | `PHI` (@ CLE) | **33** *(31 blow)* | **16.0** *(13–21)* | **7.8** *(5–10)* | **7.5** *(5–10)* | **5+ AST** (`7/7`, 100%) \| **10+ PTS** (`7/7`, 100%) | **Very High** — `0.93` MIN SD (`31–34m` every game), Cleveland homecoming, `8+` AST in L4; *Threat*: Low FGA (`13.1`). |
| **Donovan Mitchell** | `CLE` (vs PHI) | **35** *(30 blow)* | **23.5** *(17–31)* | **5.6** *(3–9)* | **4.6** *(3–7)* | **15+ PTS** (`8/8`, 100%) \| **3+ AST** (`8/8`, 100%) | **High** — `32 PTS` vs PHI Oct 22, Rocket Arena home boost; *Threat*: PHI `#1 DRtg (105.4)`. |
| **Evan Mobley** | `CLE` (vs PHI) | **34** *(36 if Allen Out)* | **18.5** *(14–24)* *(20.5 if Allen Out)* | **3.6** *(2–6)* | **8.8** *(6–12)* *(10.8 if Allen Out)* | **15+ PTS** (`7/8`, 87.5%) \| **5+ REB** (`7/8`, 87.5%) | **High** — `.655` TS%; solo-5 rebound surge if Allen sits; *Threat*: Foul trouble guarding Embiid. |
| **James Harden** | `CLE` (vs PHI) | **34** *(29 blow)* | **16.5** *(12–22)* | **6.4** *(5–9)* | **5.2** *(3–8)* | **5+ AST** (`7/8`, 87.5%) \| **10+ PTS** (`8/8`, 100%) | **High (5+ AST)** — `1.39` AST SD in `33.6` MPG; *Threat*: PHI `#1` Opp AST defense (`23.8/g`). |
| **Jarrett Allen** *(Q)* | `CLE` (vs PHI) | **26** *(if active; 0 if Out)* | **13.0** *(8–18)* | **1.2** *(0–3)* | **8.0** *(5–11)* | **5+ REB** (`7/8`, 87.5% — only miss 7m inj) | **Low (Injury)** — Exited after `7m` Nov 4 (`R Knee Contusion`) + Sat B2B vs NYK; **Wait for confirmation**. |
| **Keyonte George** | `UTA` (@ DAL) | **34** *(26 blow)* | **22.5** *(14–31)* | **5.6** *(3–9)* | **3.8** *(2–6)* | **3+ AST** (`7/8`, 87.5%) *(19+ PTS in 6/6 non-routs)* | **Medium** — `29.7%` USG (`39p/9a` Nov 4); *Threat*: `DAL -7.5` blowout (`7p` & `8p` in `-22` blowouts). |
| **Lauri Markkanen** | `UTA` (@ DAL) | **34** *(29 blow)* | **20.0** *(14–27)* | **2.2** *(1–4)* | **7.6** *(5–11)* | **10+ PTS** & **5+ REB** (`6/7`, 85.7% — `6/6` healthy) | **High (10+ PTS & 5+ REB)** — `21.5p/9.0r` L2, DAL `#29 DRB% (67.9%)`; *Threat*: UTA road blowout. |
| **Ace Bailey** | `UTA` (@ DAL) | **32** *(27 blow)* | **13.0** *(8–18)* | **1.8** *(0–4)* | **7.4** *(5–11)* | **5+ REB** (`8/8`, 100%) | **High (5+ REB)** — `8/8` hit rate + DAL allows `14.9` OREB/g; *Threat*: Foul trouble (`6 PF` Nov 4). |
| **Cooper Flagg** | `DAL` (vs UTA) | **36** *(31 blow)* | **25.5** *(19–33)* | **6.6** *(5–10)* | **6.8** *(5–10)* | **15+ PTS**, **5+ AST**, **5+ REB** (`6/7`, 85.7%) | **High** — `38.4` MPG L5 vs UTA `28th` DRtg (`116.2`) & `48.9%` short-paint FG%; *Threat*: Early DAL rout. |
| **Kyrie Irving** | `DAL` (vs UTA) | **33** *(26 blow)* | **24.0** *(17–32)* | **5.2** *(3–8)* | **4.2** *(2–7)* | **15+ PTS** (`6/6`, 100%) \| **3+ AST** (`5/6`, 83.3%) | **High** — `64 PTS` over L2 (`35.5m`), elite `.617` TS% vs UTA perimeter; *Threat*: Blowout (`25m` avg in routs). |
| **P.J. Washington** | `DAL` (vs UTA) | **35** *(31 blow)* | **15.0** *(10–21)* | **1.5** *(0–3)* | **8.4** *(5–12)* | **10+ PTS** (`7/8`, 87.5%) *(5+ REB in 5/5 L5)* | **Med-High** — `34.9` MPG workhorse w/ Lively Out; *Threat*: Occasional low-shot night (`3 PTS` vs HOU). |
| **Shai Gilgeous-Alexander** | `OKC` (@ MEM) | **36** *(31 blow)* | **31.5** *(24–40)* | **5.5** *(3–8)* | **4.4** *(3–7)* | **20+ PTS** (`7/8`, 87.5%) \| **3+ AST** (`7/8`, 87.5%) | **Very High** — `36.2%` USG w/o J-Dub/Chet (`85 PTS` L2) vs MEM `50%` `3–10 ft` FG%; *Threat*: MEM `#4 DRtg`. |
| **Ajay Mitchell** | `OKC` (@ MEM) | **31** *(27 blow)* | **19.0** *(12–26)* | **3.6** *(2–6)* | **4.2** *(2–7)* | *15+ PTS in 4/5 starts (`21.6 PPG` w/o J-Dub)* | **Medium** — Locked-in #2 scorer (`15.6` FGA as starter); *Threat*: Tough MEM perimeter defense (`6p` @ HOU). |
| **Isaiah Hartenstein** | `OKC` (@ MEM) | **27** *(25 blow)* | **8.5** *(5–13)* | **2.8** *(1–5)* | **11.2** *(8–15)* | **5+ REB** (`7/8`, 87.5%; **7+ REB in 5/5 L5**, `12.0` RPG) | **High** — Sole healthy C (`21.6%` TRB%) vs high-volume 3PT MEM team (`50.0` missed FG/g); *Threat*: Foul trouble vs Edey/Boozer. |
| **Ty Jerome** | `MEM` (vs OKC) | **33** *(28 blow)* | **25.5** *(17–35)* | **5.4** *(3–8)* | **3.6** *(2–6)* | **15+ PTS** (`6/7`, 85.7%) \| **3+ AST** (`7/7`, 100%) | **High (15+ PTS / 3+ AST)** — `36.0` Home PPG, OKC allows `42.4` 3PA/g; *Threat*: Dort/Caruso ball pressure. |
| **Cameron Boozer** | `MEM` (vs OKC) | **34** *(29 blow)* | **17.0** *(11–24)* | **5.2** *(3–8)* | **9.8** *(7–13)* | **7+ REB** (`7/8`, 87.5%) \| **3+ AST** (`8/8`, 100%) | **High** — Stewart Out locks in `33–35m` vs undersized OKC frontcourt (Holmgren Out); *Threat*: Rookie FG% variance. |
| **Cedric Coward** | `MEM` (vs OKC) | **31** *(26 blow)* | **14.5** *(10–20)* | **3.0** *(1–5)* | **8.6** *(7–11)* | **7+ REB** (`7/7`, 100%) \| **10+ PTS** (`6/7`, 85.7%) | **High (7+ REB)** — `7+ REB` in every game (`1.67` SD) vs small OKC wings; *Threat*: Foul trouble (`4+ PF` in 5/7). |
| **Scottie Barnes** *(Q)* | `TOR` (@ MIL) | **35** *(if active; 0 if Out)* | **25.5** *(18–34)* | **5.8** *(4–8)* | **8.5** *(6–13)* | **15+ PTS** & **5+ REB** (`7/8`, 87.5%) \| **3+ AST** (`8/8`) | **Low-Med (Injury)** — Smash spot vs MIL `29th` DRtg & `30th` Opp REB, **IF** active; *Threat*: **Questionable (L Groin)** + 4-in-6. |
| **RJ Barrett** | `TOR` (@ MIL) | **34** *(36 if Barnes Out)* | **22.5** *(17–28)* *(25.5 if Barnes Out)* | **4.2** *(3–7)* | **6.4** *(4–10)* | **20+ PTS** (`7/8`, 87.5%) \| **3+ AST** (`7/8`, 87.5%) | **High** — `20+` in `7/8`, MIL allows `122.3` PPG (`29th` DRtg), huge usage ceiling if Barnes sits; *Threat*: 4-in-6 legs. |
| **Immanuel Quickley** | `TOR` (@ MIL) | **34** *(36 if Barnes Out)* | **18.5** *(13–25)* *(21.5 if Barnes Out)* | **6.8** *(4–10)* | **3.8** *(2–6)* | **10+ PTS** (`8/8`, 100%) *(7+ AST in 5/8)* | **High** — MIL allows league-high `28.1` AST/g & `14.9` 3PM/g; *Threat*: Two `2-AST` score-first outliers. |
| **Jamal Shead** | `TOR` (@ MIL) | **22** *(26 if Barnes Out)* | **6.5** *(3–11)* | **6.0** *(4–9)* | **2.2** *(1–4)* | **5+ AST** (`7/8`, 87.5% — `5/5` at `6+` in L5) | **Med-High** — `30.7%` AST% vs MIL `#30` Opp AST defense; *Threat*: `21.5` bench MPG ceiling. |
| **Tyler Herro** | `MIL` (vs TOR) | **33** *(28 blow)* | **23.5** *(17–31)* | **3.6** *(2–6)* | **5.0** *(3–8)* | **15+ PTS** (`7/8`, 87.5%) \| **10+ PTS** (`8/8`, 100%) | **High** — Zero foul risk (`0.5` PF/g), `23.8` Home PPG vs TOR `.550` Opp eFG% (`36.9%` 3P); *Threat*: TOR `17.6%` TOV% blitzes. |
| **Jaime Jaquez Jr.** | `MIL` (vs TOR) | **30** *(25 blow)* | **16.5** *(11–22)* | **2.8** *(1–5)* | **6.4** *(4–9)* | *15+ PTS & 5+ REB (`6/8`, 75% each)* | **Medium** — Solid `.585` TS% slasher; *Threat*: `8-PT` dips in blowouts/low-FGA games. |
| **LaMelo Ball** | `MIN` (@ NOP) | **30** *(24 if foul trbl)* | **19.5** *(13–28)* | **6.4** *(4–9)* | **4.2** *(2–7)* | **3+ AST** (`9/9`, 100%) \| **10+ PTS** (`8/9`, 88.9%) | **Med-High** — Edwards Out + `101.5` pace + NOP allows `27.6` AST/g; *Threat*: **Severe foul trouble (`4+ PF` in 8/9G!)**. |
| **Ayo Dosunmu** | `MIN` (@ NOP) | **35** *(29 blow)* | **19.5** *(15–25)* | **4.8** *(3–8)* | **5.8** *(3–9)* | *15+ PTS in **5/5 starts** (`19.8 PPG` w/o Ant)* | **High** — `34.2` MPG starter w/ Edwards Out vs NOP `.737` Rim / `.517` Short-Paint FG%; *Threat*: Shot share if LaMelo/Randle-type usage spikes. |
| **Jaden McDaniels** | `MIN` (@ NOP) | **35** *(31 blow)* | **17.5** *(13–23)* | **4.0** *(3–6)* | **6.2** *(5–9)* | **10+ PTS** (`9/9`, 100% — `13+` in `9/9`) \| **5+ REB** & **3+ AST** (`8/9`) | **High** — Ultra-consistent `3.13` PTS SD, `15.6` FGA w/o Edwards; *Threat*: Guarding Zion foul risk (`3.6` PF/g). |
| **Rudy Gobert** | `MIN` (@ NOP) | **32** *(28 blow)* | **8.5** *(5–13)* | **1.6** *(0–3)* | **11.8** *(8–16)* | **8+ REB** (`7/8`, 87.5% — `9+` in `7/8`) | **High** — NOP attacks paint (`62` 2PA/g, Missi Out), keeping Gobert in drop coverage `32m`; *Threat*: Zion drawing fouls. |
| **Zion Williamson** | `NOP` (vs MIN) | **34** *(30 blow)* | **20.5** *(15–26)* | **2.8** *(2–5)* | **5.8** *(4–9)* | **15+ PTS** (`8/8`, 100%) | **Med-High (15+ PTS)** — `8/8` at `15+` (`7.4` FTA/g), **but** faces Gobert/McDaniels (`#2 DRtg 105.9`); *Threat*: Fouls & rim wall. |
| **Dejounte Murray** | `NOP` (vs MIN) | **35** *(31 blow)* | **18.0** *(13–24)* | **5.8** *(4–8)* | **6.2** *(4–9)* | **15+ PTS**, **5+ AST**, **5+ REB** (`4/5`, 80%) | **Med-High** — `45m` in Nov 4 OT proves full conditioning; *Threat*: MIN `#2` DRtg & `14.6%` TOV% pressure. |
| **Derik Queen** | `NOP` (vs MIN) | **25** *(22 blow)* | **13.0** *(8–18)* | **3.2** *(1–5)* | **7.8** *(5–11)* | **7+ REB** (`7/8`, 87.5%) | **Medium** — Missi Out secures `24–27` C minutes (`29.8%` DRB%); *Threat*: Gobert (`14.5%` ORB%) physical battle. |
| **Deni Avdija** | `POR` (@ LAL) | **35** *(30 blow)* | **24.0** *(19–30)* | **6.8** *(4–10)* | **6.4** *(4–9)* | **20+ PTS** (`6/7`, 85.7%) \| **3+ AST** (`6/7`, 85.7%) | **Very High** — `3.02` PTS SD, Morant Out, `23p/9a` @ LAL Oct 27 (`24th` DRtg, `232.5` O/U); *Threat*: 4th road game legs. |
| **Damian Lillard** | `POR` (@ LAL) | **32** *(27 blow)* | **22.0** *(16–29)* | **4.8** *(3–7)* | **4.2** *(2–6)* | **15+ PTS** (`6/7`, 85.7% — `20+` in `3/3` w/o Morant) | **High** — `22.3p/5.0a` w/o Morant, LAL allows `36.4%` 3P (`14.3` 3PM/g); *Threat*: Possible `~32m` cap ahead of Sat B2B. |
| **Donovan Clingan** | `POR` (@ LAL) | **28** *(23 blow)* | **13.0** *(8–19)* | **1.5** *(0–3)* | **11.4** *(8–16)* | **8+ REB** (`6/7`, 85.7%) \| **7+ REB** (`7/7`, 100%) | **High** — `23.3%` TRB% (`18.2%` ORB%) vs LAL `#28 DRB% (68.4%)`, `10r` @ LAL Oct 27; *Threat*: Foul trouble (`4+ PF` in 4/7) + Rob Williams split. |
| **Luka Doncic** | `LAL` (vs POR) | **37** *(33 blow)* | **37.5** *(29–46)* | **8.4** *(6–12)* | **8.2** *(6–12)* | **25+ PTS** (`7/8`, 87.5%) \| **5+ AST & 5+ REB** (`8/8`, 100%) | **Very High** — `40.0%` USG, `6` straight `37+` PT games (`41p/9a` vs POR Oct 27), `-2.5` spread; *Threat*: High `5.1` TOV/g. |
| **Austin Reaves** | `LAL` (vs POR) | **37** *(33 blow)* | **23.0** *(17–29)* | **4.8** *(3–7)* | **3.5** *(2–6)* | **15+ PTS** (`9/9`, 100%) \| **3+ AST** (`8/9`, 88.9%) | **Very High (15+ PTS)** — `38.0` close-game MPG, `.675` TS%, `26p/7a` vs POR Oct 27; *Threat*: Secondary to Luka's `40%` USG. |
| **Walker Kessler** | `LAL` (vs POR) | **32** *(29 blow)* | **14.5** *(10–20)* | **1.2** *(0–3)* | **10.6** *(8–14)* | **8+ REB** (`8/9`, 88.9%) \| **7+ REB** (`9/9`, 100%) | **High** — Needed `32+m` to counter Clingan/Williams size; `12.0` RPG L5; *Threat*: Foul trouble (`6 PF` @ SAC Nov 4). |
| **Victor Wembanyama** | `SAS` (@ SAC) | **29** *(25–27 blow / 34 close)* | **28.5** *(20–38)* *(24.0 in 26m blow)* | **3.2** *(2–5)* | **11.8** *(8–16)* *(10.0 in 26m blow)* | **7+ REB** (`8/8`, 100%) \| **10+ PTS** (`8/8`, 100%) | **High (Per-Min) / Med (Blowout Cap)** — SAC allows **`80.9%` Rim FG%** (`29p/10r` in `27m` vs SAC Oct 27!); *Threat*: **`SAS -15.5` blowout + Sat `@ POR` B2B (`26.7m` blowout avg)**. |
| **Dylan Harper** | `SAS` (@ SAC) | **31** *(27 blow)* | **18.0** *(13–24)* | **5.0** *(3–8)* | **5.6** *(4–8)* | **10+ PTS** (`8/8`, 100%) \| **5+ REB** (`7/8`, 87.5%) | **Med-High** — `13+ PTS` in `8/8` vs SAC `#30 DRtg`; *Threat*: Blowout 4Q rest (`28.3m` avg in routs). |
| **De'Aaron Fox** | `SAS` (@ SAC) | **29** *(25 blow)* | **15.5** *(11–22)* | **6.0** *(4–9)* | **4.0** *(2–6)* | **10+ PTS** & **3+ AST** (`8/8`, 100%) | **Med-High (Floors)** — Sacramento revenge spot vs `#30` DRtg (`27.4` Opp AST/g); *Threat*: `25.3m` blowout avg. |
| **Darius Acuff Jr.** | `SAC` (vs SAS) | **37** *(35.5 blow)* | **23.5** *(16–31)* | **6.8** *(4–10)* | **3.8** *(2–6)* | **15+ PTS** (`7/8`, 87.5%) \| **3+ AST** (`8/8`, 100% — `5+` in `6/6` L6) | **High (Volume)** — **Blowout-proof rookie (`35.5m` in blowouts**, `23.6` FGA/g); *Threat*: SAS `#3 DRtg (107.8)` (`19p/5a` @ SAS Oct 27). |
| **Zach LaVine** | `SAC` (vs SAS) | **32** *(27 blow)* | **20.5** *(13–27)* | **2.4** *(1–4)* | **3.0** *(1–5)* | **20+ PTS** (`7/8`, 87.5%) \| **15+ PTS** (`7/8`, 87.5%) | **Low-Med (20+) / Med-High (15+)** — Elite `.642` TS%, **but** lost 4Q minutes (`21m, 11p`) in `-31` blowout @ MEM and faces SAS `#3` DRtg (`SAS -15.5`). |
| **Domantas Sabonis** | `SAC` (vs SAS) | **36** *(35 blow)* | **15.0** *(10–21)* | **5.8** *(3–9)* | **14.2** *(11–18)* | **12+ REB** (`7/8`, 87.5% — `14+` in `7/8`) \| **3+ AST** (`7/8`) | **Very High** — **Blowout-proof (`37m, 20p/8a/14r` in `-27` loss @ SAS Oct 27!)**, `34.1%` DRB% vs `52.3` SAS missed FG/g; *Threat*: Foul trouble vs Wemby. |

---

## PART H — TOP RELIABLE STATISTICAL SELECTIONS

*(Rankings prioritise **floor reliability, confirmed availability, role/minute security, matchup alignment, and low blowout exposure**—deliberately discounting Questionable players and `-15.5` blowout-exposed stars from top floor slots even when their raw PPG is high.)*

### 1. Top 10 Most Consistent Points Options
1. **Tyrese Maxey (`PHI` @ CLE) — `25+ PTS` (`8/9`, 88.9% | `15+ PTS`: `9/9`, 100%) | Exp `38 MIN`**: Tight `4.81` SD, `37.1` MPG, `-2.5` tight spread, dropped `32 PTS` vs `26th`-ranked CLE defense on Oct 22.
2. **Luka Doncic (`LAL` vs POR) — `25+ PTS` (`7/8`, 87.5% | `20+ PTS`: `8/8`, 100%) | Exp `37 MIN`**: `40.0%` USG, `6` straight `37+` PT games (`41 PTS` vs POR Oct 27), `-2.5` spread in `232.5` O/U shootout.
3. **Shai Gilgeous-Alexander (`OKC` @ MEM) — `20+ PTS` (`7/8`, 87.5% | `15+ PTS`: `8/8`, 100%) | Exp `36 MIN`**: `36.2%` USG (`85 PTS` L2) with J-Dub & Chet Out; `-3.5` competitive game vs MEM's `50%` short-paint FG% allowed.
4. **Deni Avdija (`POR` @ LAL) — `20+ PTS` (`6/7`, 85.7% | `15+ PTS`: `7/7`, 100%) | Exp `35 MIN`**: Lowest scorer SD (`3.02`), `5/5` at `20+` in L5, Morant Out, `9.4` FTA/g vs LAL `24th` DRtg (`23p` @ LAL Oct 27).
5. **Austin Reaves (`LAL` vs POR) — `15+ PTS` (`9/9`, 100%) | Exp `37 MIN`**: Hit `16+` in every game (`4.19` SD, `38.0` close-game MPG, `.675` TS%, `26 PTS` vs POR Oct 27).
6. **Jaylen Brown (`PHI` @ CLE) — `15+ PTS` (`8/8`, 100%) | Exp `36 MIN`**: `16+ PTS` in all 8 appearances (`33–40` MIN every game) in a tight `-2.5` matchup against CLE (`117.1` Opp PPG).
7. **Donovan Mitchell (`CLE` vs PHI) — `15+ PTS` (`8/8`, 100%) | Exp `35 MIN`**: `8/8` at `15+` (even in `24m` blowout), scored `32 PTS` @ PHI in opener, home court in low-blowout spot.
8. **RJ Barrett (`TOR` @ MIL) — `20+ PTS` (`7/8`, 87.5%) | Exp `34–36 MIN`**: `20+` in `7/8` (`4.91` SD) facing MIL's `29th`-ranked defense (`122.3` Opp PPG), with massive upside if Scottie Barnes (*Quest*) sits.
9. **Tyler Herro (`MIL` vs TOR) — `15+ PTS` (`7/8`, 87.5% | `L5: 5/5`) | Exp `33 MIN`**: `17.4` FGA (`8.5` 3PA), `0.5` PF/g, home underdog vs TOR's `.550` Opp eFG% (`36.9%` Opp 3P).
10. **Paul George (`BOS` @ CHA) — `15+ PTS` (`7/7`, 100%) | Exp `32 MIN`** *(Tie w/ **Cooper Flagg** `DAL` `15+ PTS: 6/7, L5 5/5`)*: Hit `15+` even in `25m` blowout; faces CHA's `.555` Opp eFG% (`38.9%` Opp 3P).

### 2. Top 10 Most Consistent Assists Options
1. **Trae Young (`WAS` @ ATL) — `8+ AST` (`7/8`, 87.5% | `5+ AST`: `8/8`, 100%) | Exp `36 MIN`**: `39.7%` AST% in `35.9` MPG (`6+` in `8/8`), Atlanta homecoming against a Hawks defense allowing `27.2` AST/g.
2. **Luka Doncic (`LAL` vs POR) — `5+ AST` (`8/8`, 100% | `7+ AST`: `6/8`, 75%) | Exp `37 MIN`**: `41.6%` AST% in `232.5` O/U game (`9 AST` vs POR Oct 27).
3. **LeBron James (`PHI` @ CLE) — `5+ AST` (`7/7`, 100% | `L4: 4/4 at 8+ AST`) | Exp `33 MIN`**: `33.0` MPG (`0.93` SD), `34.5%` AST%, Cleveland return vs CLE `26.6` Opp AST/g.
4. **Jayson Tatum (`BOS` @ CHA) — `7+ AST` (`6/7`, 85.7% | `5+ AST`: `7/7`, 100%) | Exp `35 MIN`**: `6+ AST` in `7/7` (`1.55` SD, `39.1%` AST%), extra ball-handling if Pritchard (*Quest*) sits.
5. **James Harden (`CLE` vs PHI) — `5+ AST` (`7/8`, 87.5% | `3+ AST`: `8/8`, 100%) | Exp `34 MIN`**: Lowest AST SD (`1.39`, `4+` in `8/8`) in competitive `-2.5` home game (even more pick-and-pop reps w/ Mobley if Allen sits).
6. **Cooper Flagg (`DAL` vs UTA) — `5+ AST` (`6/7`, 85.7% | `L5: 5/5`) | Exp `36 MIN`**: `5+ AST` in `6` consecutive games (`38.4` MPG L5) vs `28th`-ranked UTA defense.
7. **Darius Acuff Jr. (`SAC` vs SAS) — `5+ AST` (`6/8`, 75% | `L6: 6/6 at 5+` | `3+ AST`: `8/8`, 100%) | Exp `37 MIN`**: Blowout-proof `37.2` MPG (`32.2%` AST%).
8. **Dyson Daniels (`ATL` vs WAS) — `3+ AST` (`9/9`, 100% | `6.0 APG w/o Johnson`) | Exp `31–33 MIN`**: Perfect `9/9` at `3+` (`8 AST` vs WAS Nov 4); primary wing facilitator if Johnson (*Quest*) remains Out.
9. **Tyrese Maxey (`PHI` @ CLE) — `3+ AST` (`9/9`, 100% — `4+ AST` in `9/9`!) | Exp `38 MIN`**: `4+ AST` in every game (`18 AST` combined L2; `6 AST` vs CLE Oct 22).
10. **LaMelo Ball (`MIN` @ NOP) — `3+ AST` (`9/9`, 100% | `5+ AST`: `7/9`, 77.8%) | Exp `30 MIN`**: Edwards Out + `101.5` pace vs NOP (`27.6` Opp AST/g); ranked 10th rather than higher solely due to chronic foul trouble.

### 3. Top 10 Most Consistent Rebounds Options
1. **Domantas Sabonis (`SAC` vs SAS) — `12+ REB` (`7/8`, 87.5% | `7+ REB`: `8/8`, 100%) | Exp `36 MIN`**: `14+ REB` in `7/8`, blowout-immune (`37m, 14r` in `-27` loss @ SAS Oct 27), league-best `34.1%` DRB%.
2. **Walker Kessler (`LAL` vs POR) — `8+ REB` (`8/9`, 88.9% | `7+ REB`: `9/9`, 100%) | Exp `32 MIN`**: `12.0` RPG over L5 (`5/5` at `8+`), guaranteed heavy center minutes against Clingan/Williams.
3. **Donovan Clingan (`POR` @ LAL) — `8+ REB` (`6/7`, 85.7% | `7+ REB`: `7/7`, 100%) | Exp `28 MIN`**: Elite `23.3%` TRB% (`18.2%` ORB%) attacking LAL's `28th`-ranked DRB% (`68.4%`; grabbed `10 REB` @ LAL Oct 27).
4. **Rudy Gobert (`MIN` @ NOP) — `8+ REB` (`7/8`, 87.5% — `9+` in `7/8`) | Exp `32 MIN`**: `20.2%` TRB% (`4.2` OREB/g); NOP's paint-heavy offense keeps Gobert on the court `31–33` MIN (Missi Out).
5. **Joel Embiid (`PHI` @ CLE) — `7+ REB` (`7/7`, 100%) | Exp `34 MIN`**: Non-B2B full minutes (`15 REB` @ DET Nov 4), with massive ceiling if Jarrett Allen (*Quest*) sits.
6. **Cameron Boozer (`MEM` vs OKC) — `7+ REB` (`7/8`, 87.5% | `5+ REB`: `8/8`, 100%) | Exp `34 MIN`**: Stewart Out + Holmgren/Jaylin Williams Out for OKC gives Boozer (`16.0%` TRB%) clear interior control.
7. **Cedric Coward (`MEM` vs OKC) — `7+ REB` (`7/7`, 100%) | Exp `31 MIN`**: `1.67` SD (`7–11` REB in every game) against OKC's `50.8` missed FG/g and depleted frontcourt.
8. **Victor Wembanyama (`SAS` @ SAC) — `7+ REB` (`8/8`, 100% | `10+`: `6/8`) | Exp `29 MIN`**: `7+ REB` in `8/8` (`10 REB` in `27m` vs SAC Oct 27); capped at `7+`/`8+` tier rather than `12+` strictly due to `-15.5` blowout minute risk.
9. **Isaiah Hartenstein (`OKC` @ MEM) — `5+ REB` (`7/8`, 87.5% | `7+ REB`: `5/5` in L5, `12.0` RPG) | Exp `27 MIN`**: Sole healthy OKC center facing MEM's `39.4` 3PA/g (`50.0` missed FG/g).
10. **Luka Doncic (`LAL` vs POR) — `5+ REB` (`8/8`, 100% | `7+ REB`: `6/8`, 75%) | Exp `37 MIN`** *(Alongside **Naz Reid** `CHA` `5+ REB: 9/9` & **Onyeka Okongwu** `ATL` `10+ REB in 4/4 L4`)*: `24.4%` DRB% in `37` competitive minutes.

### 4. Top 5 Players — Strongest Overall Matchup & Playing-Time Outlook
1. **Luka Doncic (`LAL` vs POR)**: `37` expected competitive minutes (`LAL -2.5`, `232.5` O/U), `40.0%` USG, `6` straight `37+` PT games (`41p/9a` vs POR Oct 27), `100%` floor across `20+ PTS / 5+ AST / 5+ REB`.
2. **Tyrese Maxey (`PHI` @ CLE)**: League-elite `38` expected minutes (`PHI -2.5`), `8/9` at `25+ PTS` & `9/9` at `4+ AST`, attacking CLE's `26th`-ranked defense (`114.3` DRtg; `32p/6a` in G2 H2H).
3. **Shai Gilgeous-Alexander (`OKC` @ MEM)**: `36` expected minutes (`OKC -3.5`), `36.2%` USG without Holmgren & Jalen Williams (`85 PTS / 16 AST` over L2), attacking MEM's one defensive soft spot (`50.0%` short-paint FG%).
4. **Deni Avdija (`POR` @ LAL)**: `35` expected minutes with Ja Morant & Shaedon Sharpe Out, `3.02` PTS SD (`6/7` at `20+`), `9.4` FTA/g + `31.4%` AST% against LAL's `24th`-ranked defense (`23p/9a` @ LAL Oct 27).
5. **Domantas Sabonis (`SAC` vs SAS)**: Blowout-proof `36` expected minutes (`35.0m` avg even in `15+` pt blowouts), `14.9` RPG (`7/8` at `12+ REB`) & `6.1` APG (`7/8` at `3+ AST`), already proved immunity (`20p/8a/14r` in `37m`) in a `-27` loss @ SAS on Oct 27.

---

## PART I — FINAL ANALYST SUMMARY

1. **Games Most Likely to Remain Competitive**:
   - **`POR @ LAL` (`LAL -2.5`, O/U `232.5`)**: `#1` vs `#2` offenses in the NBA; Oct 27 H2H was decided by `7` points (`136-129`).
   - **`PHI @ CLE` (`PHI -2.5`, O/U `228.5`)**: `8-1` road-tested Sixers (`#1` DRtg) vs desperate `4-4` Cavs (`121.2` Home PPG); Oct 22 H2H was `114-106`.
   - **`OKC @ MEM` (`OKC -3.5`, O/U `225.5`)**: Two `6-2` West squads; MEM's `#4` ORtg/`#4` DRtg offsets SGA's individual brilliance for shorthanded OKC.
   - **`MIN @ NOP` (`MIN -4.5`, O/U `231.5`)**: MIN (`#2` DRtg, missing Edwards) visits a surging `4-1` L5 Pelicans squad with Murray back.
2. **Games with Elevated Blowout Risk**:
   - **`SAS @ SAC` (`SAS -15.5`) — Extreme Risk**: `+8.2` NRtg SAS (`#3` DRtg) vs `-13.8` NRtg SAC (`#30` DRtg, `80.9%` Rim FG% allowed); SAS won Oct 27 H2H by `27` and plays `@ POR` tomorrow on a B2B (expect Wembanyama/Fox/Harper to sit the 4Q if up `20+`).
   - **`BOS @ CHA` (`BOS -8.5`) — Elevated Risk**: `+6.1` NRtg BOS vs `-11.6` NRtg CHA (`0-5` L5, two `33+` pt losses); Tatum (`30.0m`) & PG13 (`25.0m`) lose 4Q minutes in routs.
   - **`UTA @ DAL` (`DAL -7.5`) — Moderate-to-Elevated Risk**: `1-7` UTA (missing JJJ & Nurkic on 3rd straight road stop) has three `20+` pt losses in L8, compressing Keyonte George's 4Q minutes when trailing big.
3. **Players with the Most Stable Minutes & Output**:
   - **LeBron James (`PHI`)**: `33.0` MPG (`SD 0.93`, `31–34m` in `7/7`), `7/7` at `10+ PTS & 5+ AST`.
   - **Tyrese Maxey (`PHI`)**: `37.1` MPG (`34–42m` in `9/9`), `8/9` at `25+ PTS`, `9/9` at `4+ AST`.
   - **Austin Reaves (`LAL`)**: `35.9` MPG (`31–39m` in `9/9`), `9/9` at `16+ PTS`.
   - **Luka Doncic (`LAL`)**: `35.6` MPG (`35–38m` in `7/8`), `8/8` at `20+ PTS / 5+ AST / 5+ REB`.
   - **Jaden McDaniels (`MIN`)**: `33.3` MPG (`29–39m` in `9/9`), `9/9` at `13+ PTS` (`SD 3.13`).
   - **Domantas Sabonis (`SAC`)**: `36.1` MPG (`31–40m` in `8/8`, blowout-immune), `7/8` at `14+ REB`.
4. **Players Whose Recent Averages Are Misleading (Outliers, Injury Exits, or Role Shifts)**:
   - **Small-Sample Inactive Leaders**: **Anthony Edwards** (`MIN`, `33.2 PPG` in `4G`), **Kawhi Leonard** (`TOR`, `19.5 PPG` in `2G`), **Tyrese Haliburton** (`IND`, `21.8p/9.5a` in `4G`), and **Paolo Banchero** (`ORL`, `24.5 PPG` in `2G`) are all `Out`.
   - **Injury-Exit Deflated Season Averages**: **Jarrett Allen** (`CLE`, `13.2p/7.8r` includes a `7-min, 0p/1r` injury exit Nov 4; healthy `7G` avg is `15.1p/8.7r`) and **Lauri Markkanen** (`UTA`, `17.1p/6.6r` includes a `6-min, 2p/0r` injury exit Oct 26; healthy `6G` avg is `19.7p/7.7r`).
   - **Single-Game Outlier Mean Inflation**: **Paul George** (`BOS`, `21.3` mean vs `18.0` median due to `38-PT` G1), **Victor Wembanyama** (`SAS`, `29.0p/12.4r` lifted by `52p/24r` Nov 4 while facing `26.7m` blowout risk tonight), and **Ty Jerome** (`MEM`, `27.4` mean with `11.70` SD from `45` & `40` PT spikes vs `10` & `15` PT lows).
   - **Bench Minutes Caps Masking Per-Minute Rates**: **Kel'el Ware** (`MIL`, `8.2 RPG` in just `18.9` bench MPG) and **Cam Spencer** (`MEM`, `8.4 APG` L5 in `21.8` bench MPG), while **Dennis Schroder** (`CHA`) and **Ryan Rollins** (`MIL`) were both demoted to the bench over their last 2 games.
5. **Players Benefiting Materially from Confirmed Injuries**:
   - **OKC (`Holmgren, Jalen Williams & Wallace Out`)**: **Shai Gilgeous-Alexander** (`36.2%` USG, `42.5 PPG` L2), **Ajay Mitchell** (`21.6 PPG` in `5` starts), and **Isaiah Hartenstein** (`12.0 RPG` L5).
   - **MIN (`Anthony Edwards & DiVincenzo Out`)**: **Ayo Dosunmu** (`19.8 PPG` in `34.2` MPG across `5` starts, `5/5` at `15+`), **Jaden McDaniels** (`+4.6` FGA/g), and **LaMelo Ball** (`19.2 PPG` L5).
   - **POR (`Ja Morant & Shaedon Sharpe Out`)**: **Damian Lillard** (`22.3p/5.0a` in `3G` w/o Morant), **Deni Avdija** (`24.3p/6.3a`), and **Donovan Clingan** (`12.7 RPG`).
   - **MEM (`Isaiah Stewart & Pippen Jr. Out`)**: **Cameron Boozer** (`33–35m` frontcourt lock) & **Cam Spencer** (`8.4 APG` L5).
   - **NOP (`Yves Missi Out`)** & **DAL (`Dereck Lively II Out`)**: **Derik Queen** (`24.1m`, `7/8` at `7+ REB`) and **Daniel Gafford / P.J. Washington** (`25.2m` / `35.8m` L5).
6. **Players Most Vulnerable to Fatigue, Foul Trouble, or Restrictions**:
   - **Foul Trouble**: **LaMelo Ball** (`MIN` — `4+ PF` in `8/9` games, fouled out in `20m` @ SAS!), **Kyshawn George** (`WAS` — `4+ PF` in `4/8`), **Cedric Coward** (`MEM` — `4+ PF` in `5/7`), **Donovan Clingan** (`POR` — `4+ PF` in `4/7`), and **Zion Williamson** (`NOP` — `4+ PF` in `4/8`, charging into Gobert).
   - **Schedule / Travel Fatigue**: **Toronto Raptors** (`4th` straight road game, `4-in-6`, coming off Denver altitude), **Boston Celtics** (`4-in-6`), **LA Lakers** (`4-in-6`), **Utah Jazz** (`3rd` straight road game after OT loss), and **Portland Trail Blazers** (`4th` straight road game + B2B tomorrow).
7. **Strongest Evidence-Supported Statistical Projections Tonight**:
   - **Tyrese Maxey**: `28.5 PTS` (`25+` floor) & `5.8 AST` (`4+` floor) @ CLE.
   - **Luka Doncic**: `37.5 PTS / 8.4 AST / 8.2 REB` (`25+p / 5+a / 5+r` floor) vs POR.
   - **Domantas Sabonis**: `14.2 REB` (`12+` floor, blowout-resistant) vs SAS.
   - **Deni Avdija**: `24.0 PTS / 6.8 AST` (`20+ PTS` floor) @ LAL.
   - **Shai Gilgeous-Alexander**: `31.5 PTS` (`20+` floor) @ MEM.
   - **Trae Young**: `9.8 AST` (`8+` floor) & `20.5 PTS` (`15+` floor) @ ATL.
   - **Walker Kessler** & **Donovan Clingan**: `10.6 REB` & `11.4 REB` (`8+ REB` floors) in `POR @ LAL`.
8. **Biggest Pre-Tip Uncertainties Requiring Final Shootaround / `30-Min` Lineup Re-Checks**:
   1. **Anthony Davis (`WAS`, Questionable — R Ankle)** & **Jalen Johnson (`ATL`, Questionable — L Ankle)**: Single largest usage/rebound swing on the slate (governs NAW's `30.0` vs `19.3` PPG split, Okongwu's `13.0` vs `7.1` RPG split, and Sarr/Trae/Kyshawn George projections).
   2. **Scottie Barnes (`TOR`, Questionable — L Adductor/Groin)**: Determines whether TOR is a true `-6.5` road favorite or whether RJ Barrett & Quickley absorb `+8–10` extra FGA in a tighter game at MIL.
   3. **Jarrett Allen (`CLE`, Questionable — R Knee Contusion)**: Exited after `7` MIN Wednesday with a B2B tomorrow; if ruled Out, upgrade **Evan Mobley REB** and **Joel Embiid PTS/REB**.
   4. **Moussa Diabate & Dennis Schroder (`CHA`, Questionable)** + **Payton Pritchard (`BOS`, Questionable)**: If Diabate sits, upgrade **Naz Reid** (`35m` lone-5 workload).

---

### Verified Sources & Research Citations (Retrieved Nov 6, 2026)
- **Official NBA Injury Reports (`11/06/2026 04:45 AM ET` & `04:30 AM ET`)**: [official.nba.com/nba-injury-report-2026-27-season](https://official.nba.com/nba-injury-report-2026-27-season/) — Local verified PDFs: [Injury-Report_2026-11-06_04_45AM.pdf](../data/injury_reports/Injury-Report_2026-11-06_04_45AM.pdf) & `Injury-Report_2026-11-06_04_30AM.pdf`.
- **Official 2026–27 NBA Schedule, Box Scores (123 Completed Games Oct 20 – Nov 5, 2026), BPI Predictor & DraftKings Odds**: [espn.com/nba/schedule/_/date/20261106](https://www.espn.com/nba/schedule/_/date/20261106) & ESPN Site v2 Summary/Scoreboard APIs (archived in `data/nba_data_cache_2026-11-06.json`).
- **2026–27 & Separate 2025–26 Team Ratings, Four Factors, Opponent Shooting Distance & Player Advanced Metrics**: [basketball-reference.com/leagues/NBA_2027.html](https://www.basketball-reference.com/leagues/NBA_2027.html), [NBA_2027_advanced.html](https://www.basketball-reference.com/leagues/NBA_2027_advanced.html), and [NBA_2026_per_game.html](https://www.basketball-reference.com/leagues/NBA_2026_per_game.html) (processed in `data/master_analytics_2026-11-06.json`).
