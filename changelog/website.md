# Changelog — Website

Tags: `site/vX.Y.Z`. Versioned independently of the other components; see `versions.json` for the current set.
Each release lists what changed for users and integrators.

## [1.21.0] - 2026-09-02

- **Two sections are withdrawn while their features are not live:** the X
  account-intelligence radar and the X reply bot, together with their
  navigation links and the X bot button in the closing panel.
- The remaining sections are renumbered 01 to 06 with no gap.
- The hero now lists holder distribution as a scored signal in place of social
  credibility, which the shipped score does not include.
- The `docs` link in the navigation is set apart from the in-page links and
  marked with an arrow as opening in a new tab, with a matching hint for
  screen readers.

## [1.20.0] - 2026-09-02

- The agent price table now marks the holders depth as Solana only, since that
  is where the API offers it. The summary for AI assistants says the same.

## [1.19.0] - 2026-09-02

- **The for agents section is live**, with its navigation link: the REST
  endpoint and the MCP tool server, priced per call.
- The MCP panel now includes copy-paste setup: a one-line command for Claude
  Code, the configuration snippet for Cursor, Windsurf and VS Code, and a copy
  button on the endpoint address.
- The page now states that the first call each day is free, so an agent can
  see the output before any payment. A plain-text summary for AI assistants,
  with endpoints, tools, prices and doc links, is published at the site root.
- The price table no longer lists prices for the social and full depths, which
  are not yet available; both now read `soon`.

## [1.18.0] - 2026-09-01

- **Mantle joins the supported-chains strip** as a seventh tile, in the same
  monochrome style as the others and legible in both themes.
- The chain counter reads 7 chains, and the page description, hero line and
  footer name Mantle.

## [1.17.1] - 2026-08-31

- The scrolling ticker in the hero runs continuously again. A markup error
  made part of it drift during each cycle, opening a gap that snapped shut at
  the restart.

## [1.17.0] - 2026-08-29

- **Arbitrum joins the supported-chains strip** as a sixth tile, in the same
  monochrome style as the others. On phones the strip now wraps into two rows
  of three.
- The chain counter reads 6 chains, and the page description, hero line and
  footer name Arbitrum.

## [1.16.0] - 2026-08-29

- **The $DON price ticker and the copy-address chip are back**, now for the
  official token on Robinhood Chain. The ticker links to the official pool
  from the moment the page loads, before the price arrives.
- A Telegram icon in the footer, next to the X mark, links to the official
  community.

## [1.15.0] - 2026-08-26

- The $DON price ticker and the copy-address chip in the footer are removed
  ahead of the token's relaunch, so the site shows no address or price for it
  for now.
- The for agents section is taken off the page until launch.
- Fixed the logo in the navigation collapsing into a thin sliver on screens
  narrower than about 1500px. It now stays square at every width, in both
  themes.

## [1.14.0] - 2026-08-24

- **New section: for agents.** DigitalDon now answers machines as well as
  people: a REST endpoint and an MCP tool server, paid per call in USDC over
  x402. A matching link joins the navigation.
- The section shows the request-then-pay exchange and the MCP tool list in two
  terminal panels, a price table by analysis depth, and notes on billing:
  payment is checked before the analysis runs, settled only after it succeeds,
  and an incomplete answer is never charged. Links lead to the docs.
- The terminal panels scroll inside themselves on phones instead of widening
  the whole page.

## [1.13.1] - 2026-08-24

- The X links in the navigation and the closing panel now read `x bot` instead
  of `on x`, so they no longer look like a link to our X profile. The section
  heading was renamed to match.

## [1.13.0] - 2026-08-24

- **The X section now shows the real scan card the bot posts:** header, token
  name and ticker, market cap, liquidity and volume, the thesis, both time
  horizons with entry and target zones, a price chart and the score gauge. It
  stays white on near-black in both themes, as it appears on X.
- A short three-step row (someone posts a call, you reply to the bot, the card
  arrives) replaces the longer thread mock-up.
- The section animates once on scroll: steps appear one by one, the card
  lands, the gauge sweeps up and the price line draws. Reduced-motion settings
  skip the animation.
- Fixed the card overflowing its panel on phones. It now scales to the space
  available; on narrow screens the score becomes a strip along the bottom and
  the chart is hidden.

## [1.12.0] - 2026-08-24

- **New section: the X bot.** A recreated thread shows someone replying to the
  bot with a contract address and the bot answering with a scan card. It is
  built in the page, so it follows the day/night theme.
- An `on x` link in the navigation and an `on x` button in the closing panel,
  next to the Telegram bot and the web app. The chains section is renumbered
  to 07.

## [1.11.1] - 2026-08-13

- Fixed the `docs` links in the navigation and the closing panel, which led to
  a dead address. Both now open digitaldon.gitbook.io.

## [1.11.0] - 2026-08-11

- A `docs` link in the navigation opens the documentation in a new tab.
- A `docs` button in the closing panel, next to `telegram bot` and `web app`,
  keeps the documentation reachable on phones, where the navigation links are
  hidden. The button row wraps on narrow screens.

## [1.10.0] - 2026-08-11

- **The official $DON token appears on the site.** A price pill in the
  top-left corner shows the symbol and the USD price, refreshed every minute
  while the tab is visible, and opens the token's market page when clicked. It
  quotes the deepest pool and keeps the last good price if an update fails.
- The price pill gives up its price, then hides, as space runs out, so it
  never overlaps the navigation.
- A click-to-copy contract address chip in the footer copies the full address,
  shortens it on small screens, confirms in place and announces the result to
  screen readers.

## [1.9.1] - 2026-08-03

_Internal changes only; no public notes for this release._

## [1.9.0] - 2026-08-03

_Internal changes only; no public notes for this release._

## [1.8.1] - 2026-07-29

_Internal changes only; no public notes for this release._

## [1.8.0] - 2026-07-28

- **The chains section is rebuilt.** Each chain sits on a raised round coin
  like the cards elsewhere on the page, with logos about 25% larger.
- The coins rise in one by one on scroll, then a highlight moves along the
  row, one chain at a time with a ring pulsing off it. The loop runs only
  while the row is on screen.
- A blinking "live on 5 chains" marker and a closing "one command, same
  engine, same score" line frame the row, and the heading and spacing now
  match the other sections.

## [1.7.0] - 2026-07-28

- **New section: holder intelligence.** It shows a bubble map of the top
  wallets, a stat strip (holders, top 10, largest), a legend, and a readout
  with the clustered-supply figure, the connected clusters and the launch
  signals the scan looks for.
- The map assembles itself on scroll: wallets drop in, move into their
  clusters and funding links draw last, then the clusters drift gently. It
  uses the same encoding as the Web Analyzer's holder map.
- A `holders` link joins the navigation, and the later sections are
  renumbered.

## [1.6.4] - 2026-07-23

- The favicon figure is sized to fill the black circle right up to its edge
  without clipping.

## [1.6.3] - 2026-07-23

- The figure inside the black-circle favicon is slightly smaller, for a more
  balanced margin.

## [1.6.2] - 2026-07-23

- The figure inside the black-circle favicon is larger, so it reads more
  clearly in the browser tab.

## [1.6.1] - 2026-07-23

- The favicon is now a white DigitalDon figure on a black circle, so it stays
  visible on both light and dark browser tabs.

## [1.6.0] - 2026-07-16

- The chains section now opens with a short paragraph on DigitalDon's aim of
  delivering in-depth, reliable data across all major blockchains.

## [1.5.0] - 2026-07-16

- The closing "start trading smarter today." panel gains a `web app` button
  next to the Telegram button, which is renamed `telegram bot`.
- The `web app` link in the header now opens the Web Analyzer at
  analyzer.digitaldon.net in a new tab.

## [1.4.1] - 2026-07-16

- Fixed the `chains` link in the navigation scrolling the section underneath
  the navigation bar. It now lands in view like every other section.

## [1.4.0] - 2026-07-16

- A section was removed and the rest renumbered: x-intelligence is now 04 and
  chains is 05.
- A `chains` link in the navigation jumps straight to the supported-chains
  strip.

## [1.3.0] - 2026-07-16

- **The score gauge now matches the Web Analyzer's dial:** a semicircle of
  tick marks that light up to the score, replacing the needle and coloured
  zones. The ticks brighten one by one as the number counts up, and
  reduced-motion settings are respected.
- Fixed the gauge's screen-reader label, which described the demo score of 58
  as neutral instead of in the bullish accumulation zone.

## [1.2.0] - 2026-07-16

- **BNB Chain and Robinhood Chain join the supported-chains strip**, with
  their logos, next to Solana, Ethereum and Base.
- The page description, hero line and footer now list all five chains.

## [1.1.0] - 2026-07-13

- A `web app` button in the header links to the Web Analyzer, next to the
  Telegram button, which is renamed `telegram bot`.
- The browser tab now reads "DigitalDon - DeFi Intel" with a new logo favicon,
  and the footer brand is written "DigitalDon".

## [1.0.0] - 2026-07-05

- **First production version of the landing page:** a monochrome ink-on-paper
  design with a day/night toggle, a floating navigation pill, a dot-grid
  backdrop and animated data graphics in the hero.
