# Changelog — Widget

Tags: `widget/vX.Y.Z`. Versioned independently of the other components; see `versions.json` for the current set.
Each release lists what changed for users and integrators.

## [1.7.1] - 2026-09-11

- The holder map's usage hints moved behind a small ? in the map's corner,
  shown on hover, freeing room on the narrow card that a permanent line of
  instructions used to take.
- The loading figure keeps climbing through a long cluster scan instead of
  stalling near 90, and says the scan is still working after about fourteen
  seconds.

## [1.7.0] - 2026-09-11

- The cluster map opens as soon as a scan starts: its window is there from
  the first frame with the DigitalDon mark filling in while holders load,
  replacing the two-step text loader.
- A token nameplate (logo, name and ticker) heads the group list. If the
  logo cannot be loaded, a monogram is shown instead.
- The map has a new visual encoding: share of supply on the bubble, a
  wallet's role shown on its rim, one number format throughout, cluster
  outlines weighted by how strong the evidence is, and a boxed legend.

## [1.6.1] - 2026-09-11

_Internal changes only; no public notes for this release._

## [1.6.0] - 2026-09-10

- Group cards in the holder map carry a TEAM SUPPLY stamp when a group is
  the project's own wallets, or a partial form such as 7/10 TEAM SUPPLY when
  only some of its wallets are.
- Project wallets are excluded from the bubble-risk grade wallet by wallet,
  so a group that is only partly team-owned is graded on the rest.

## [1.5.0] - 2026-09-09

- Project treasury wallets are marked with a ring in the holder map, with a
  matching "project treasury" legend row and a "team supply" line on the
  group card.
- A chip next to the bubble-risk grade shows how much supply was left out
  of it, so a large treasury group is not read as a concentration risk.

## [1.4.0] - 2026-09-08

- DigitalDon's own token, $DON, is analysed under a stated house policy:
  the score is lifted and floored, and the short-term plan is replaced by the
  long-term zones. The card says so with an "our token · house view" chip
  under the score and "our token" in the header.
- The numbers are the same as on the analyzer, since both run the same
  engine.
- The project treasury is named in the holder map and left out of the
  bubble-risk grade, with a chip showing how much supply was excluded.

## [1.3.2] - 2026-09-08

- The holder panel uses a stacked layout suited to the card's width on
  every device, instead of a desktop layout squeezed into a narrow frame.
- The in-page expand, used when native fullscreen is not available, now
  actually stretches the widget over the host page. It had been silently
  doing nothing.
- While a group's detail drawer is open, the corner controls and filter row
  are hidden instead of being drawn over it.

## [1.3.1] - 2026-09-08

- The holder panel now has the same 16px side margin as the rest of the
  card. Its title, hints, legend, group line and export links had run flush
  to the card edge.

## [1.3.0] - 2026-09-07

- The holder map is now the same interactive map as the analyzer's,
  replacing the static picture: group cards with their share of supply, a
  drawer per group with its wallets, the evidence linking them (shared
  funder, funding timing, each link rated strong or weak) and the estimated
  price impact if the whole group sells.
- Also from the analyzer: filter chips, hiding and restoring wallets or
  groups, the funding replay, changes since your last scan, and keyboard
  shortcuts.
- Fullscreen for the map. Frames created by embed.js carry
  allow="fullscreen", which enables native fullscreen. Without that grant,
  the loader stretches the frame over the page and Esc closes it. A
  hand-written iframe with neither shows no fullscreen button at all.
- Unique visitors per embedding site were undercounted and are now counted
  correctly.

## [1.2.0] - 2026-09-06

- The demo page at widget.digitaldon.net is readable in dark mode and meets
  contrast guidelines for body text in both themes.
- The demo shows four integration shapes (pinned token, scanner,
  cluster-scan-only, opens-on-holders), each captioned with the exact
  attributes that produce it, such as data-tools="holders" or
  data-view="holders", plus copyable snippets and a link to the guide.
- A day/night toggle on the demo page is shared with the website and the
  analyzer; the example cards follow it, which demonstrates setTheme().

## [1.1.0] - 2026-09-06

- Holder intelligence in the widget: a second tool beside the analysis that
  runs a two-stage cluster scan and shows holders, top-10 share, largest
  wallet, concentration, a wallet cluster map, connected supply with the
  bubble risk, the cluster list and launch signals.
- data-tools chooses which tools the card offers ("analysis,holders" by
  default, "analysis", or "holders" for a cluster-scan-only embed), and
  data-view chooses which opens first. Pin an address and open on holders
  for a token page, or omit it for a scanner.
- The JavaScript API adds .show(view) to switch tools and an onHolders
  callback that fires when a cluster scan completes.
- Per-site usage counts now include completed holder scans; a scan is
  counted once per token per frame.

## [1.0.0] - 2026-09-06

- One script tag from https://widget.digitaldon.net/embed.js mounts a
  compact DigitalDon card in a sandboxed iframe: price and 24h change, the
  signal score and band, four category reads, short- and long-term
  entry/exit zones, market cap, liquidity, volume, buy share, risk flags and
  a link to the full analysis on analyzer.digitaldon.net.
- Same engine as the analyzer, so a token scores identically on every
  surface; the engine version is shown in the card's footer.
- Pinned or search mode, a multi-chain picker, light / dark / auto theme,
  fluid width with automatic height. JavaScript API: DigitalDon.mount(),
  .update(), .setTheme(), .destroy(), an onResult callback, and declarative
  data-digitaldon-widget containers.
- Runs on our origin under a strict content security policy and sets no
  cookies. Views, scans, link clicks and errors are counted per embedding
  site per day, with unique visitors via an anonymous id.
