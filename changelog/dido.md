# Changelog — DiDo terminal

Tags: `dido/vX.Y.Z`. Versioned independently of the other components; see `versions.json` for the current set.
Each release lists what changed for users and integrators.

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
