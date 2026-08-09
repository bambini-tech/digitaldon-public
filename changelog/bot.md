# Changelog — Telegram bot and API

Tags: `bot/vX.Y.Z`. Versioned independently of the other components; see `versions.json` for the current set.
Each release lists what changed for users and integrators.

## [2.52.0] - 2026-08-09

_Internal changes only; no public notes for this release._

## [2.51.0] - 2026-08-09

- **Auto-scan can skip fresh launches.** A new "Fresh launches" switch under
  auto-scan (off by default) limits unprompted cards to tokens with enough chart
  history for a full analysis. `/don` still answers everything.
- `/autoscan` takes `on|all|ta|off`.

## [2.50.2] - 2026-08-09

- **`/help` now lists only commands you can use.** Owner-only commands are no
  longer shown to group members or other users.

## [2.50.1] - 2026-08-09

- **Calls posted by a linked channel are credited to that channel** on `/lb`
  and `/pnl`, instead of all landing on one "@Telegram" caller.
- "@" is no longer added in front of display names that are not usernames.

## [2.50.0] - 2026-08-09

- **New: `/lb`, a per-group leaderboard** of who called what and how it did,
  scored on the peak multiple since the call, with 1D / 1W / 2W / 1M / all-time
  filters.
- Groups can switch it off in `/setup`. `/pnl` and `/lb` share the same peak
  figures.

## [2.49.0] - 2026-08-09

- **Holder analysis on BNB Chain is more resilient.** When the primary holder
  data is unavailable, the distribution, wallet quality and security block
  still load, without wallet clusters.

## [2.48.0] - 2026-08-08

_Internal changes only; no public notes for this release._

## [2.47.0] - 2026-08-08

_Internal changes only; no public notes for this release._

## [2.46.1] - 2026-08-08

_Internal changes only; no public notes for this release._

## [2.46.0] - 2026-08-08

- **The first holder scan of a token is faster**, with no change to the wallets,
  funders or clusters it reports.

## [2.45.0] - 2026-08-08

- **The Holder Analysis button is faster**, and several people tapping it on
  the same token in a group now share one result instead of each waiting for
  their own.

## [2.44.1] - 2026-08-08

- **Fixed cards that mixed two tokens.** On some pools the chart and zones
  described the other asset in the pair, producing absurd entry zones and
  upside figures. Candles now always match the scanned token.
- A chart series that cannot match the token's price is rejected rather than
  analysed.

## [2.44.0] - 2026-08-04

_Internal changes only; no public notes for this release._

## [2.43.0] - 2026-07-31

- **Holder Analysis now includes a wallet cluster map image**: bubbles sized by
  share of supply, clusters outlined, funder arrows, in black and white.
- It uses the same layout as the Web Analyzer's map for the same token.

## [2.42.2] - 2026-07-31

- The Web Analyzer's holder analysis now shows a proper error on a server
  failure instead of reporting that the service could not be reached.

## [2.42.1] - 2026-07-31

- Scan output no longer names third-party data providers: the holder security
  block is headed "Security" and the footer link reads "View Chart".

## [2.42.0] - 2026-07-29

_Internal changes only; no public notes for this release._

## [2.41.1] - 2026-07-29

_Internal changes only; no public notes for this release._

## [2.41.0] - 2026-07-29

_Internal changes only; no public notes for this release._

## [2.40.1] - 2026-07-28

- The `/pnl` card caption is one line again, without the promo line.

## [2.40.0] - 2026-07-27

- **The `/don` chart labels its window high honestly** (e.g. "3W HIGH") and
  says ATH only when it can prove it; a lifetime rail shows the full ATL to ATH
  range beside the chart.
- The chart now matches the Web Analyzer's design, with legible candles and
  non-overlapping price labels, and renders several times faster.

## [2.39.0] - 2026-07-27

- **Token age is now shown to the minute**: `33m old`, `1h 35m old`,
  `4d 7h old`. Ages round down, so a 33-minute-old pair no longer reads
  `1h old` and a very fresh one no longer reads `0h old`.
- The bot and the Web Analyzer use the same age label.

## [2.38.0] - 2026-07-27

- **The bot introduces itself when added to a group** with a setup card:
  what it does, whether it has the admin rights it needs, and a button to
  re-check them.
- Admins can switch **auto-scan** (on by default) and **PNL cards** per group
  with a tap. `/setup` reopens the menu; `/autoscan on|off` still works.

## [2.37.1] - 2026-07-27

- Charts for fresh launches now appear from about five minutes after the
  pool opens, instead of only after ten minutes.

## [2.37.0] - 2026-07-27

- **The fresh-launch card now includes a 1-minute price chart.** It shows
  candles and the current price only: no score, no entry/exit zones and no
  support/resistance lines, since a few minutes of data cannot support them.
- Chart headers and axis labels now match the actual timeframe and span.

## [2.36.0] - 2026-07-27

- **Freshly launched tokens now get a card** in `/don` and group auto-scan
  instead of "No OHLCV data". It shows an on-chain read (liquidity ratio,
  unlock overhang, buy/sell pressure) and no TA score.
- The liquidity verdict now falls back to FDV when no market cap is
  reported, so thin launches still get a liquidity warning.

## [2.35.0] - 2026-07-26

- **Short-term entry/exit zones can no longer invert.** When the 72h range
  is too narrow to trade, the card now says so, e.g. `No tradable range —
  72h band is only 0.2% wide.`, instead of printing crossed zones.

## [2.34.2] - 2026-07-26

- The group short card uses new emojis for the market line and the
  short-term and long-term sections, so the two horizons are easier to tell
  apart.

## [2.34.1] - 2026-07-26

- **The group short card now shows price, market cap and liquidity**, e.g.
  `$0.000400 · MCap $4.2M · Liq $310K`. Missing values are left out, and
  market cap falls back to FDV.

## [2.34.0] - 2026-07-26

- **Group auto-scan:** paste a contract address in a group and the bot
  answers with a short card (score, entry/exit zones for both horizons,
  estimated upside) and a `📊 Full Analysis` button, with no `/don` needed.
- `📊 Full Analysis` replaces the short card with the full card and chart.
  Private chats and `/don <token>` still return the full analysis.
- `/autoscan on|off` lets group admins turn it off. The bot needs admin
  rights in the group to see pasted addresses.

## [2.33.0] - 2026-07-26

- Groups now have an hourly scan limit in addition to the per-minute one.
  Short bursts still work. When a group hits the limit, the reply suggests
  scanning in a direct message, and long waits are shown in minutes.

## [2.32.1] - 2026-07-26

_Internal changes only; no public notes for this release._

## [2.32.0] - 2026-07-26

- **`/don` now has per-user and per-group rate limits**: by default 3 scans
  a minute and 20 an hour per user, and 8 a minute per group. Private chats
  count only against the per-user limits.
- Many people scanning the same token at the same time now get their results
  faster.

## [2.31.0] - 2026-07-26

_Internal changes only; no public notes for this release._

## [2.30.0] - 2026-07-25

- **Holder analysis on Solana is faster** and handles more users at once.
- Sniper and bundler figures now show what those wallets hold **now**.

## [2.29.0] - 2026-07-25

_Internal changes only; no public notes for this release._

## [2.28.0] - 2026-07-24

_Internal changes only; no public notes for this release._

## [2.27.0] - 2026-07-24

_Internal changes only; no public notes for this release._

## [2.26.0] - 2026-07-24

- **In a private chat with the bot, just paste a contract address or
  ticker** to scan it, no `/don` needed. In groups, `/don` is still
  required.

## [2.25.0] - 2026-07-24

_Internal changes only; no public notes for this release._

## [2.24.0] - 2026-07-23

_Internal changes only; no public notes for this release._

## [2.23.0] - 2026-07-23

_Internal changes only; no public notes for this release._

## [2.22.0] - 2026-07-23

_Internal changes only; no public notes for this release._

## [2.21.0] - 2026-07-23

- A slow scan no longer holds up other users' commands, and many people
  scanning the same trending token at once get their results faster.
- `/don` now limits how many scans one user can run per minute.

## [2.20.2] - 2026-07-23

- The `/pnl` caption now ends with a tappable mention of the bot, so people
  who see a shared card can open it and try `/don` right away.

## [2.20.1] - 2026-07-23

- **`/pnl` no longer replies in groups when there is nothing to show**
  (no argument, or a token the group never scanned).
- The PNL card drops the duplicate percent badge beside the multiplier.

## [2.20.0] - 2026-07-23

- **New `/pnl` command (groups only).** The bot remembers the first `/don`
  scan of each token in a group. `/pnl <token>` then posts a shareable card
  with the multiplier since that scan, First Scan / ATH / Profit, and who
  scanned it first.

## [2.19.0] - 2026-07-21

_Internal changes only; no public notes for this release._

## [2.18.7] - 2026-07-21

_Internal changes only; no public notes for this release._

## [2.18.6] - 2026-07-16

- The Web Analyzer's social and holder panels work again after a service
  failure in the previous release.

## [2.18.5] - 2026-07-16

_Internal changes only; no public notes for this release._

## [2.18.4] - 2026-07-16

_Internal changes only; no public notes for this release._

## [2.18.3] - 2026-07-13

- **Holder analysis on EVM chains now shows the real total holder count**
  (e.g. 23,958 instead of `97+`). The `+` suffix appears only when the
  total is not known.

## [2.18.2] - 2026-07-12

_Internal changes only; no public notes for this release._

## [2.18.1] - 2026-07-12

- Fewer `/don` scans fail with "No OHLCV data" when market data is busy.
  The bot now waits and retries more carefully.

## [2.18.0] - 2026-07-12

- **Holder analysis on Ethereum, Base and Robinhood Chain** no longer
  fails with "Could not fetch holder data" when the main holder data is
  unavailable. Wallet clusters still form.

## [2.17.0] - 2026-07-12

- **Robinhood Chain is now supported** in `/don`: search, charts and TA,
  plus holder and cluster analysis.

## [2.16.0] - 2026-07-11

- **BSC tokens can now be found and scanned with `/don`.**
- Charts and analysis now work for more tokens whose price history was
  missing from the main market data.

## [2.15.0] - 2026-07-11

- **The Web Analyzer's holder analysis now covers Ethereum, Base, BSC and
  Robinhood Chain**, with the same holder distribution, wallet clusters and
  security block as the Telegram bot.

## [2.14.0] - 2026-07-11

- **Holder Analysis now includes a security block**: honeypot status,
  buy/sell tax, a rug-risk score, mint/freeze renounced, and sniper, insider,
  bundle and smart-money figures.
- A token reported as a honeypot gets a warning at the top: `⛔ HONEYPOT —
  sells are blocked. Do not buy.`
- The Social Sentiment button now shows for more EVM tokens.

## [2.13.0] - 2026-07-11

- **The `👥 Holder Analysis` button now works for Ethereum, Base and BSC
  tokens**, not just Solana: holder distribution, wallet clusters and
  sniper, bundler and insider signals.

## [2.12.0] - 2026-07-11

_Internal changes only; no public notes for this release._

## [2.11.0] - 2026-07-11

- **Price charts** no longer report "no data" when market data is briefly
  unavailable; short-lived failures are now retried before giving up.

## [2.10.0] - 2026-07-11

- **Holder analysis** marks each wallet cluster as strong or weak evidence,
  and the summary shows how much of the supply sits in strong clusters.
- **Bubble risk** is now graded on strong-evidence clusters only; weak links
  can raise Low to Mid but never to High on their own.
- Snipers and Bundle signals are no longer dropped on popular, long-lived
  pools, and exchange wallets are recognised more reliably.

## [2.9.0] - 2026-07-11

- **Launch signals** are more precise: on tokens with a long trading history,
  later buyers are no longer mislabelled as snipers or bundles.
- Sells into the pool are no longer counted as launch buys, and the dev
  wallet is only named when it can be identified with certainty.
- Clusters built only on weak links need more wallets before they are shown.

## [2.8.0] - 2026-07-10

- **Web Analyzer bubble map** now tags wallets by role (sniper, bundle,
  insider, fresh, dev) and shows which wallet funded each cluster.
- The share of supply held in the liquidity pool is reported as well.

## [2.7.0] - 2026-07-10

- **The Web Analyzer** now shows holder analysis: holder distribution,
  wallet clusters, bubble risk and launch signals, with an interactive
  cluster map. Same analysis as the Telegram Holder Analysis button.

## [2.6.1] - 2026-07-06

- **Snipers and Bundle** supply shares were reported far too low on many
  tokens; the amount bought at launch is now measured correctly.

## [2.6.0] - 2026-07-06

- **Snipers and Bundle** now show the share of supply bought at launch and
  what is still held today (e.g. "sniped 32% → 0% now").

## [2.5.0] - 2026-07-06

_Internal changes only; no public notes for this release._

## [2.4.4] - 2026-07-06

- The holder line now reads `Largest wallet` instead of `Largest owner`.

## [2.4.3] - 2026-07-06

_Internal changes only; no public notes for this release._

## [2.4.2] - 2026-07-06

- **Fixed:** wallet clusters no longer shrink when the same token is scanned
  repeatedly.

## [2.4.1] - 2026-07-06

- **Fixed:** the fresh-wallet signal no longer reads 0% on tokens that had
  been scanned before.

## [2.4.0] - 2026-07-06

- **Holder analysis** adds a Launch Signals line on Solana: fresh wallets,
  insiders, snipers and bundles among the largest holders.

## [2.3.0] - 2026-07-06

- **Holder analysis** now covers the full holder set, which fixes the holder
  count and finds bundles among mid-ranked wallets.
- Concentration figures exclude the liquidity pool by design.

## [2.2.0] - 2026-07-06

- **`/don` Holder Analysis** now works per owner rather than per token
  account and detects wallet clusters ("bubbles") with a Bubble risk grade
  (Solana).

## [2.1.0] - 2026-07-05

- The Web Analyzer can now show X (Twitter) account intelligence for a
  token, served by the bot.

## [1.24.1] - 2026-07-03

_Internal changes only; no public notes for this release._

## [1.24.0] - 2026-07-03

_Internal changes only; no public notes for this release._

## [1.23.0] - 2026-07-02

- **`/don` THESIS** is now a data-driven checklist grouped by category.

## [1.22.0] - 2026-07-01

- **Long-term take-profit** in `/don` is now derived from resistance levels
  on the 4h chart.

## [1.21.4] - 2026-07-01

- **Fixed:** long-term upside could read lower than short-term upside when a
  token traded near its all-time high.

## [1.21.0 – 1.21.3] - 2026-07-01

- **X Intelligence** message redesigned with cleaner formatting and a
  mobile-friendly breakdown.

## [1.20.0] - 2026-06-30

- **X Intelligence** scores account age on a tiered scale calibrated for
  crypto projects.

## [1.19.0 – 1.19.6] - 2026-06-30

- **X Intelligence** lookups run server-side and are more reliable; several
  fixes.

## [1.18.0] - 2026-06-29

- **X Intelligence** reads the 25 most recent posts and tells original posts
  apart from retweets and replies.

## [1.15.0 – 1.17.0] - 2026-06-29

_Internal changes only; no public notes for this release._

## [1.14.0 – 1.14.1] - 2026-06-25/28

- `/don` reads more price history, and the long-term entry zone now always
  sits at or below the short-term entry zone.

## [1.13.0] - 2026-06-25

- **`/don`** recognises five new chart patterns and looks back over 60
  candles instead of 30.

## [1.12.0] - 2026-06-24

_Internal changes only; no public notes for this release._

## [1.10.0 – 1.11.1] - 2026-06-23/24

_Internal changes only; no public notes for this release._

## [1.9.0 – 1.9.1] - 2026-06-21

_Internal changes only; no public notes for this release._

## [1.8.0] - 2026-06-21

_Internal changes only; no public notes for this release._

## [1.7.0] - 2026-06-20

_Internal changes only; no public notes for this release._

## [1.5.0 – 1.6.1] - 2026-06-17/20

_Internal changes only; no public notes for this release._

## [1.4.0] - 2026-06-15

_Internal changes only; no public notes for this release._

## [1.3.0] - 2026-06-14

- **Fixed:** the bot stays responsive while longer requests are running.

## [1.2.0] - 2026-06-08

_Internal changes only; no public notes for this release._

## [1.1.0] - 2026-06

- **X Intelligence** added: a read on a token's X (Twitter) account.

## [1.0.0] - 2026-05

- First release of the DigitalDon Telegram bot with `/don` token analysis.
