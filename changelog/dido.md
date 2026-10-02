# Changelog — DiDo terminal

Tags: `dido/vX.Y.Z`. Versioned independently of the other components; see `versions.json` for the current set.
Each release lists what changed for users and integrators.

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
