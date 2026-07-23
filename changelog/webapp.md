# Changelog — Web Analyzer

Tags: `webapp/vX.Y.Z`. Versioned independently of the other components; see `versions.json` for the current set.
Each release lists what changed for users and integrators.

## [1.5.5] - 2026-07-23

- The browser-tab icon is now the white DigitalDon figure inside a black
  circle, so it stays visible on light browser tabs as well as dark ones.

## [1.5.4] - 2026-07-20

- On phones, the small logo in the header navigation is hidden. It was being
  stretched out of shape, and the full-size logo appears just below. Desktop
  is unchanged.

## [1.5.3] - 2026-07-16

- Fixed the header logo on some mobile browsers, which could show an old,
  different mark instead of the current DigitalDon mascot.

## [1.5.2] - 2026-07-16

- **Security fix:** links taken from a token's own metadata, such as its X
  profile, now open only if they are ordinary web addresses. A token could
  previously set a link that ran code when clicked; such links are no longer
  shown.

## [1.5.1] - 2026-07-13

- Small wording fixes: the Holder Intelligence description now uses the same
  casing as the other panels, and the header button reads "telegram bot" like
  the rest of the app.

## [1.5.0] - 2026-07-13

- Links to DigitalDon on X in the header and footer, as on the website.
- An animated DigitalDon logo above the headline. It follows the light or dark
  theme and stays still for visitors who prefer reduced motion.
- The tab title is now "DigitalDon - DeFi Analyzer" with a new icon, and the
  intro text, panel descriptions and closing call to action have been
  rewritten for clarity.

## [1.4.0] - 2026-07-12

- **New chains: BNB Chain and Robinhood Chain.** The analyzer now finds and
  scores tokens on five chains (Solana, Ethereum, Base, BNB Chain and
  Robinhood Chain), the same set as the Telegram bot.
- Holder Intelligence and the holder cluster map now work on every supported
  chain, not just Solana.
- The intro text and the "no token found" message list all five chains, and
  the footer shows the correct version.
- Restored the analyzer after a faulty update had briefly taken it offline.

## [1.3.0] - 2026-07-10

- **A richer holder map.** Wallets are tagged by role (sniper, bundle, insider
  or dev-funded, fresh) with pale tints. Funder wallets get a double ring,
  bubbles show their share of supply, and links separate direct funding (solid
  arrows) from wallets grouped by a shared funder (dashed).
- A legend that highlights matching bubbles and links on hover or keyboard
  focus, zoom buttons with a live percentage, a fullscreen toggle, and PNG and
  CSV export generated entirely in your browser.
- An optional liquidity-pool bubble and a "supply mapped" tile that shows how
  much of the total supply the map covers.
- The "funder of N wallets" count now includes only real funding links, so it
  is more accurate.

## [1.2.0] - 2026-07-10

- **Holder Intelligence for Solana tokens.** A "run holder scan" button under
  the result shows the holder distribution, wallet clusters and launch
  signals, the same analysis as the Telegram bot's Holder Analysis. The
  distribution appears first, followed by the clusters.
- An interactive wallet-cluster bubble map with tooltips, click-to-select
  clusters, a detail card with copyable addresses, draggable bubbles, zoom and
  pan by wheel or pinch, and full keyboard support. The map and cluster list
  stay in sync, and both light and dark themes are supported.

## [1.1.1] - 2026-07-06

- The "run x intel" button is now connected to the live service and returns
  real results.

## [1.1.0] - 2026-07-05

- **X Intelligence:** when a token lists an X account, a "run x intel" button
  analyses it with the same scoring as the Telegram bot's Social Sentiment
  feature.
- The result shows a four-part radar (content, activity, engagement, trust), a
  0 to 100 score with a verdict, a rating for each part, key profile stats
  (followers, following, account age, posts per week, median views and likes)
  and any red flags. It works in light and dark mode.
- Every failure case (profile not found, no posts, busy, timed out,
  unavailable) has a clear message.
- The footer now shows the analyzer's own version.

## [1.0.0] - 2026-07-05

- **First release of the Web Analyzer:** the `/don` analysis from the Telegram
  bot, running in your browser. Paste a contract address or ticker to get the
  same score as the bot, with no sign-up and no API key.
- Supports Solana, Ethereum and Base. The analysis covers momentum, trend,
  structure and volume, chart patterns and support and resistance, with short-
  and long-term targets adjusted to the token's age.
- The result shows a signal-score gauge with a verdict, the thesis breakdown,
  an hourly candle chart with the entry zone and exit lines, trade-plan cards
  with upside from the current price, on-chain risk flags and links to the
  token's market page and X.
- Light and dark themes shared with the website, and links of the form
  ?q=<address or ticker> that open an analysis directly.
