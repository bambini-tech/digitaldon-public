# Changelog — Website

Tags: `site/vX.Y.Z`. Versioned independently of the other components; see `versions.json` for the current set.
Each release lists what changed for users and integrators.

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
