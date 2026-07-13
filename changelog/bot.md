# Changelog — Telegram bot and API

Tags: `bot/vX.Y.Z`. Versioned independently of the other components; see `versions.json` for the current set.
Each release lists what changed for users and integrators.

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
