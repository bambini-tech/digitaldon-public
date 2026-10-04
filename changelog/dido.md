# Changelog — DiDo terminal

Tags: `dido/vX.Y.Z`. Versioned independently of the other components; see `versions.json` for the current set.
Each release lists what changed for users and integrators.

## [0.10.0] - 2026-10-04

- The search bar now sits in the middle of the top bar, always ready: it
  widens when you point at it or press `/`.
- DiDo is dark only now.
- A copy button next to the token's name copies its contract address, to
  pass it on.

## [0.9.0] - 2026-10-04

- The background water now flows smoothly instead of stepping.
- The top bar is frosted glass, with the background running on under it.
- The token's logo now sits in the top bar next to its ticker.
- A wallet's menu on the map no longer closes by itself when the clusters finish loading.

## [0.8.0] - 2026-10-03

- The terminal's background is now soft water behind frosted glass, tinted
  in the colours of the token you are looking at (taken from its logo).
- Moving the mouse sets the water rippling, gently.

## [0.7.0] - 2026-10-03

- While a token's clusters are being mapped, the terminal shows what it is
  doing and how far it has got, with a progress bar.
- Click any bubble on the map for a small menu: the wallet's details, its
  cluster, and an option to scan the wallet.

## [0.6.0] - 2026-10-03

- **Holder maps appear in seconds.** The terminal shows a token's top
  holders right away and gathers them into clusters as soon as those are
  mapped, with a counter while it works.
- A token opened recently shows its cluster map instantly, labelled with how
  old it is, while a fresh one loads behind it.
- Holder maps on tokens with many holders no longer stop at "timed out"
  while the scan is still finishing.

## [0.5.1] - 2026-10-02

- The holder map's cluster menu is labelled "Cluster" next to the token's
  name, and when folded it keeps that top card, with the number of groups,
  instead of shrinking to a small chip.

## [0.5.0] - 2026-10-02

- **Price, 24h change, market cap, liquidity and volume now sit next to
  the token's name** at the top, always in view, whether the chart is open,
  folded or moved.
- The holder map's group menu can be folded to a small chip, like the chart.

## [0.4.2] - 2026-10-02

- On the field, a cluster's detail panel is now only as tall as its content.

## [0.4.1] - 2026-10-02

- The holder map on the field has a new glass look, with each cluster's
  wallets melted into one liquid shape.

## [0.4.0] - 2026-10-02

- Fixed the holder map sometimes reading "not live" right after the terminal
  was updated, even though it was available.
- The chart and the rest of the terminal are usable while the holder map is
  still loading, instead of waiting behind it.
- The holder map makes room for the chart, the watchlist and an open wallet:
  bubbles arrange themselves around the panels instead of hiding behind them.
- Smoother all round: dragging panels, hovering and panning the chart, and
  the holder map settling now run at a steady frame rate, and panels ease in
  when they open.
- **Arrange the terminal your way:** drag the chart, the watchlist or a
  wallet by its title bar to anywhere on screen. Your layout is remembered;
  double-click a title bar (or press 0) to put things back.

## [0.3.0] - 2026-10-02

- **New look:** the terminal now has the same glass design as the analyzer.
- **Watchlist in the terminal:** star any token and see, at a glance, which
  ones are in their buy zone, waiting for a dip, under the zone or showing no
  buy signal. Lists shared from the analyzer open here too.
- **Open any holder's wallet:** on the holder map, an EVM wallet opens beside
  the map with its whole portfolio across chains, and any token it holds
  opens as its own terminal. The browser's back button retraces the path.

## [0.2.3] - 2026-10-01

- Holder map: on clusters that hold project treasury, the "team supply"
  label no longer overlaps the cluster's percentage.

## [0.2.2] - 2026-09-28

- Cleaner error text when a token cannot be found.

## [0.2.1] - 2026-09-28

- A pasted or linked contract address now always opens that token, not the
  token it is paired against in its deepest pool.

## [0.2.0] - 2026-09-18

- The funding replay strip is hidden in the terminal, to leave the bottom
  of the field free for the upcoming trade bar. Wallet funding times remain
  visible as the rug along the bottom of the chart, against price and time.

## [0.1.0] - 2026-09-18

- DiDo, the DigitalDon terminal, is a new product: the wallet cluster map
  fills the whole page and everything else sits on top of it, with the same
  dossier, replay and keyboard shortcuts as the analyzer.
- A chart docked over the map shows all four plan bands (short-term entry
  and exit, long-term entry and target) switchable from the legend, plus
  volume, optional 20/50 EMAs and funding times of mapped wallets. It zooms,
  pans, measures moves between two points, resizes or folds away, and
  becomes a sheet on phones.
- A security strip shows honeypot, mint, freeze, owner and tax checks;
  missing data reads as missing, never as safe. Live price refreshes every
  30 s with a status dot, and a $DON house-policy badge appears when it
  applies.
- Every view is a link: the token, a search, the timeframe and chart size
  all live in the URL. Arc is supported from launch.
