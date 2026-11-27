# Data plan: making the picks analysis better

Reachability was tested from the cloud session on 28 Nov 2026 (Sydney). "Reachable" means the page or API answered; it does not mean the data is in the shape we need yet.

## Priority 1: build now (no new accounts)

| Data | Source | Reachable? | How we use it |
|---|---|---|---|
| Our own results log | Repo + ESPN box scores (already used) | Yes | `bets/bets_log.csv`: every leg, its line, and hit/miss, filled in automatically after each slate. Shows which leg types fail most (assists, threes, Probable players). |
| With/without teammate splits | Our ESPN game logs (already cached) | Yes | For each player, averages and hit rates in games with and without each key teammate. Catches role swaps (Davion Mitchell, Garland). |
| Longer samples, home/away, rest splits | Our game logs + ESPN athlete splits (`site.web.api.espn.com/.../athletes/{id}/splits`) | Yes | Last 20 games and home vs away added beside the last 10, so a 10/10 run on a tiny sample counts for less. |
| Minutes trend and restriction flags | Our game logs + official injury report | Yes | Flag players whose minutes fell in the last 3 games or who just returned from injury (Kessler). |

## Added: NBA.com game pages (last 6 games)

`src/nbacom_games.py` reads the box score and full play-by-play that NBA.com embeds in each game page (`nba.com/game/<slug>/play-by-play`), walking back through `nba.com/games?date=` until every slate team has 6 finished games. No browser is needed. It adds shot mix (rim / short / mid / three), fourth-quarter share of points, rebounds and assists (blowout exposure), who each player's assists go to, missed games with NBA.com's reason, and with/without-teammate averages. Checked against our ESPN logs on 28 Nov 2026: 420 of 420 player-games matched. Output: `output/<date>_last6_nbacom.md` and `output/dashboard/nbacom_lastn.json`; pages cached in `data/nbacom/`.

## Priority 2: free sources, small scraper per site

| Data | Source | Reachable? | Notes |
|---|---|---|---|
| Confirmed / projected starting lineups | Rotowire NBA lineups (`rotowire.com/basketball/nba-lineups.php`), NBA.com today's lineups (`nba.com/players/todays-lineups`) | Yes (both 200) | Run about 30-60 minutes before tip-off to catch late scratches (Maxey) and lineup changes. |
| Defence vs position | FantasyPros (`fantasypros.com/nba/defense-vs-position.php`) | Yes (200) | Points, rebounds and assists each opponent allows to PG/SG/SF/PF/C. Replaces team-wide defence in the matchup step. |
| Schedule, advanced team stats | Basketball Reference | Yes (already used) | Already in the pipeline. |

## Priority 3: needs a key, a subscription, or a different route

| Data | Source | Reachable? | Notes |
|---|---|---|---|
| Player prop lines and prices | The Odds API (`api.the-odds-api.com`) | Yes, but needs an API key (401 without one) | Free tier exists. Check whether its Australian region covers Sportsbet player props; US books (DraftKings, FanDuel) are well covered and are a good price reference. Lets us pick legs where our chance beats the bookmaker's implied chance. |
| Sportsbet's own lines | Sportsbet site | Blocked from the cloud (403) | Read through Claude in Chrome on the user's own browser. A prompt can ask it to list each player's lowest offered line and price before building the slip. |
| Tracking stats (potential assists, rebound chances, touches) | stats.nba.com | Times out from the cloud (NBA blocks cloud servers) | Would need to run on the user's own computer, or a paid provider (e.g. Sportradar, SportsDataIO). |
| NBA live JSON feed | cdn.nba.com | Blocked from the cloud (403) | Not needed: ESPN's live feed already covers scores and box scores. |
| Minutes projections | Rotowire / FantasyPros premium | Paid | Optional later. |

## Rollout

1. **Now:** results log, with/without splits, longer samples and minutes flags (all from data we already pull).
2. **Next:** lineup and defence-vs-position scrapers, run on the morning of each slate.
3. **When a key is available:** The Odds API for prop prices, plus a Claude in Chrome prompt that reads Sportsbet's real lines.
4. **Optional:** tracking stats from the user's own computer or a paid feed.

## Ground rules

- Respect each site's terms of use and rate limits; cache pages and fetch once per slate.
- Never store API keys in the repo. Keys are saved as environment network secrets.
- Every new input must be checked against at least one past slate before it changes picks.
