# Changelog — Web Analyzer

Tags: `webapp/vX.Y.Z`. Versioned independently of the other components; see `versions.json` for the current set.
Each release lists what changed for users and integrators.

## [1.41.0] - 2026-09-24

- **The footer links to our public GitHub repository**, next to X and
  Telegram: integration guides for the widget and the API, examples and the
  changelog of every DigitalDon product.

## [1.40.0] - 2026-09-22

- **The wallet card now shows the NFTs a wallet holds**, behind a Tokens |
  NFTs switch above the holdings list. Every scan opens on tokens, and a
  wallet with no NFTs gets no switch, so its card is unchanged.
- The NFTs tab is a gallery of square tiles with artwork, name, collection and
  chain, plus a ×N badge for an edition held more than once. Collections are
  grouped, the most widely held first; the first 24 tiles show at once and a
  button reveals the rest.
- Each tab shows its count, and the NFTs tab notes how many collections there
  are and that NFTs are not counted in the total. The arrow keys move between
  the tabs.
- Artwork loads lazily as you scroll, with a placeholder showing the
  collection's monogram until it arrives. Pixel art is upscaled crisply, and
  airdropped spam NFTs are hidden and counted in the footnotes.

## [1.39.0] - 2026-09-20

- **Chain names and coin tickers no longer overlap in the wallet orbit.** Each
  chain's name is now placed clear of its largest coin, and the picture is a
  little taller so the outer labels no longer fall off the top.
- The dollar figure under large coins has been removed to make room. Values
  remain in the readout under the orbit and in the total at its centre.

## [1.38.0] - 2026-09-20

- **A chain the wallet scan could not read is now shown as not scanned**,
  instead of looking like an empty chain. The chain row marks it, the total's
  sub-line counts it as unread, and a footnote says the total is missing that
  chain.

## [1.37.0] - 2026-09-20

- **Holdings in the wallet orbit are drawn as coins.** A token with artwork
  shows its logo sharp and edge to edge, finished with a thin rim that keeps
  dark logos legible in dark mode. The ticker sits under the coin; other
  details appear in the readout on hover.
- Holdings without artwork keep the plain bubble with the ticker inside.
- **ETH and the major stablecoins now show their official logos** in the orbit
  and the holdings list, including ETH, MNT, USDC, USDT, DAI, WETH and WMNT.

## [1.36.0] - 2026-09-20

- **Token logos on the wallet scan.** Each holding shows its artwork in the
  orbit and as a round avatar in the holdings list, with the ticker's first
  two letters standing in when no logo exists. Logos keep the token's own
  colours.
- In the orbit the logo fills the bubble behind a readable ticker; small
  bubbles too tiny for a ticker show the logo sharp, so they are no longer
  blank discs.
- **The loading strip now describes a wallet scan** with its own steps (probe
  chains, read balances, price holdings, cost basis) instead of the
  token-analysis steps.

## [1.35.0] - 2026-09-20

- **The wallet orbit.** A scanned wallet is now drawn as a picture: the
  address at the centre and every holding around it, sized by its value and
  grouped by chain, with each chain's name and share of the portfolio. The
  ranked list stays underneath.
- A chain's gas coin carries a dashed rim to set it apart from positions the
  wallet took.
- Hover or focus a holding to preview it, click to pick it: the others dim and
  the matching row below is highlighted and scrolled into view. Every holding
  is reachable by keyboard; Enter picks, Escape clears.
- Details appear in a fixed readout under the orbit rather than a floating
  tooltip, so nothing covers the picture and it works on touch.

## [1.34.0] - 2026-09-19

- **The wallet card now has proper padding**, so its name, address, chain row
  and footnotes no longer sit flush against the border. Checked from 320px
  phones to wide desktops, with no sideways scrolling.
- Footnote qualifiers now sit neatly under their value at every screen width
  instead of wrapping raggedly.

## [1.33.0] - 2026-09-19

- **The wallet card's footnotes are a labelled grid** (cost basis, dust,
  unpriced, empty chains) instead of one dense paragraph. The methodology sits
  behind a "how these numbers are worked out" disclosure; nothing was removed.
- More space between the card's sections and a taller chain strip, so the
  strip reads as its own element. On phones, sub-labels stack under their
  values.
- A single-chain wallet no longer shows a solid full-width chain bar; the
  chain labels still show which chains came back empty.

## [1.32.0] - 2026-09-18

- **Wallets: a third mode beside tokens and stocks.** Paste an EVM address to
  see the wallet across every chain we cover: the cross-chain total, a chain
  strip showing the split, one ranked list of holdings tagged by chain (gas
  coins included), and an approximate cost basis per position and overall.
- The chain strip doubles as a filter: click a chain to narrow the list to it
  instantly. The card uses the same scan as the Telegram bot, so both give the
  same answer for an address.
- Link straight to wallet mode with ?view=wallets. The card works at phone
  widths without clipping or sideways scroll, and gains and losses use the
  monochrome ink scale rather than green and red.
- Positions whose cost cannot be reconstructed (airdrops, bridged deposits,
  token-for-token swaps) read "no basis" instead of showing a gain they never
  earned.

## [1.31.0] - 2026-09-18

- **The price chart is interactive.** Pan by dragging or with the arrow keys,
  zoom with the wheel, pinch, +/- buttons or range presets, and read any
  candle's open, high, low and close from a crosshair. Double-click or reset
  returns to the default view.
- A 1h / 4h switch appears when four-hour history is available, so the
  long-term plan can be checked on the timeframe it was read from.
- All six trade-plan levels are now drawn and can be toggled from the legend;
  levels outside the view are marked on the price rail with an arrow. A
  measure tool shows the percent move, bar count and time between two points.
- Chart labels stay readable on phones, and the wheel only zooms after you
  click the chart, so scrolling past it no longer gets stuck. The fresh-launch
  chart gets the same controls.

## [1.30.1] - 2026-09-16

_Internal changes only; no public notes for this release._

## [1.30.0] - 2026-09-16

- **Arc tokens can now be analysed**, with chart and score like any other
  chain, and Arc is named in the page's chain list and the "no token found"
  message.
- **Fixed: tokens too new for a full analysis crashed the analyzer** with
  "Something went wrong" on every chain. Their fresh-launch card shows again,
  including the $DON house-policy badge where it applies.
- **Fixed: tokens whose main pool had no candle history yet showed no chart or
  score.** The analyzer now tries the token's other pools on the same chain,
  checked against the main pair's price.

## [1.29.0] - 2026-09-12

- **The navigation is now a bar at the top of the page** instead of a pill
  floating over the content, so it no longer covers anything, including the
  cluster map. The $DON ticker and the day/night toggle moved into the same
  bar.
- In-page links no longer land their target underneath the bar, and the small
  brand mark shows in the bar on phones again.

## [1.28.2] - 2026-09-12

- **Fixed: the cluster map's loading window collapsed to a thin line** while
  the scan ran. It now opens at the map's full height, so nothing jumps when
  the bubbles arrive.
- Fixed: the export row appeared during the scan, the token nameplate showed
  an empty slot before the name loaded, and an empty verdict area left a gap.

## [1.28.1] - 2026-09-11

- **The cluster map's usage hints moved behind a ? button** in the map's
  corner, opening a key on hover, focus or tap, instead of a permanent line of
  text above the panel.
- **Fixed: token logos never appeared** on the map's nameplate; the monogram
  always stood in. Logos now load.
- **The loading percentage no longer stalls at 90 on slow scans.** It keeps
  climbing, and after a while the loader explains that a first scan of a token
  can take up to a minute.

## [1.28.0] - 2026-09-11

- **The cluster map opens as soon as you scan**, with a loader showing the
  DigitalDon mark filling up and a percentage that reaches 100 only when the
  data is in, instead of the panel appearing out of nowhere after a long wait.
- **A token nameplate** (logo, name, ticker) heads the group list, so a
  fullscreen screenshot of the map shows which token it is.
- **Bubble shade shows share of supply again**, darkest for the largest
  holders; a wallet's role moved to its rim. Labels use one decimal
  throughout, group outlines are solid for strongly rated groups and dashed
  otherwise, and the zoom and funding replay controls share one bottom bar.
- On phones the group cards form one horizontal shelf so the map keeps its
  shape. Faded bubbles stay visible in light mode, and PNG export keeps the
  new rims.

## [1.27.0] - 2026-09-11

- **Tokenized stocks are analysed as equities**, with the same result as the
  Telegram bot. Zones and targets suit a large-cap share, fixing cases where
  the plan came out inverted, and the plans are labelled swing (days) and
  position (weeks) under a Tokenized equity profile.
- **A stock-specific on-chain section** shows depth, on-chain volume and flow,
  and notes that the supply is custodial, replacing wording about unlocks and
  rug risk that did not apply to a share.
- A stock with too narrow a range for a swing setup says so with the actual
  figure instead of calling it untradable.

## [1.26.0] - 2026-09-10

- **Group cards on the holder map now say TEAM SUPPLY in words** next to the
  group letter, or for example 7/10 TEAM SUPPLY when only part of the group
  belongs to the project.
- The summary under the map names partly project-owned groups too, so the risk
  grade beside it explains itself.

## [1.25.0] - 2026-09-09

- **The project's own wallets are marked on the holder map**: a double ring on
  each treasury wallet, a project treasury legend entry that filters to them,
  and a tooltip that leads with it, including treasury wallets outside any
  group.
- The group is named wherever its numbers appear (map label, group card,
  dossier), and the summary under the map says when the largest group is the
  project treasury.
- The chip showing how much supply was excluded from the risk grade is now
  solid, since it explains the grade beside it.

## [1.24.0] - 2026-09-08

- **The analyzer now applies the $DON house policy**, the same as the Telegram
  bot: the score is lifted by 8 and floored at 50, and the short-term plan is
  withheld in favour of the long-term zones. Everything else is computed as
  for any other token.
- **This is always labelled.** An "our token · house view" chip sits under the
  score, the header notes our token, and the short-term plan card explains why
  it is empty.
- On the holder map the largest $DON group is labelled project treasury, and a
  second chip shows how much team-owned supply was excluded from the
  bubble-risk grade.

## [1.23.1] - 2026-09-08

- **The holder panel is tidy on phones.** Below 640px it becomes a vertical
  stack (map, filters, group cards, funding replay) instead of controls
  overlapping the bubbles, and the open dossier no longer has other controls
  sitting on top of it.
- Fixed expanding the holder map inside the embeddable widget, which undid
  itself immediately.

## [1.23.0] - 2026-09-07

- **The cluster panel now lives inside the holder map**, so fullscreen shows
  everything. Group cards down the side show each group's share; click one to
  fly to it and open a drawer with its wallets, the evidence linking them, and
  an estimate of the price impact if the group sold.
- **Hide and restore wallets**, and filter chips for the roles found on the
  token. A funding replay scrubs from launch to now, showing wallets as they
  were funded, with a play button.
- **Since your last scan:** your browser remembers the previous holder set per
  token and shows new and departed wallets and how groups changed.
- Keyboard shortcuts in the map (arrows cycle groups, h hides, f refits, Esc
  clears); tooltips show when a wallet was funded, and CSV export gains
  funding times and hidden state.

## [1.22.1] - 2026-09-07

- The holder map summary no longer adds all clusters into one connected-supply
  figure, which read as a single holder. It now gives the number of separate
  groups and the size of the largest, matching the Telegram bot.

## [1.22.0] - 2026-09-04

- **The holder map shows direct token transfers between wallets** as heavy
  arrows from sender to recipient, with their own legend entry that filters
  the map on hover. A sender's tooltip says how many wallets it sent tokens
  to, and group reasons can combine, for example "token transfer · shared
  funder".

## [1.21.0] - 2026-09-03

- **Tokenized stocks.** A tokens | stocks switch at the top of the page opens
  a board of official tokenized equities from xStocks (Solana) and Robinhood
  (Robinhood Chain), sorted by liquidity and filterable by kind, issuer or
  typing. One click analyses the deepest listing; stocks listed by both
  issuers get a switch in the card header.
- **Searching a stock ticker finds the official token first**, ahead of
  copycats with faked liquidity; tokens sharing the ticker remain reachable
  below it.
- The card tags the stock and its issuer and shows whether the US market is
  open or closed. Holder analysis is not offered for stocks, and the panel
  explains why.
- Link straight to stocks with ?view=stocks or ?view=stocks&q=TSLA.

## [1.20.1] - 2026-09-01

- **Fixed: holder intelligence and X intelligence were missing from every
  scan.** The page was calling a retired address; it now uses
  api.digitaldon.net and both panels are back.

## [1.20.0] - 2026-09-01

- **Mantle tokens can now be analysed**, tagged MNT on the card as in the
  Telegram bot, and Mantle is named in the page's chain list and the "no token
  found" message.

## [1.19.2] - 2026-08-31

- **A finished analysis is no longer held back while optional panels wait on a
  slow backend.** The result now appears promptly; the holder and X panels are
  skipped for that scan if the backend has not answered in time, and return on
  the next scan.

## [1.19.1] - 2026-08-31

- **The holder intelligence panel no longer disappears when the backend is
  slow to wake.** The page now retries before giving up, so the first visitor
  after a quiet period still gets holder and X intelligence.

## [1.19.0] - 2026-08-29

- **Arbitrum tokens can now be analysed**, with chart, score and holder panel
  like other EVM chains, tagged ARB on the card. Arbitrum appears in the
  multi-chain picker and in the page's chain list, matching the Telegram bot.

## [1.18.0] - 2026-08-29

- **A Telegram link in the footer**, beside the X link, pointing to the
  official community.
- **The $DON price ticker and copy-contract chip are back**, now quoting the
  official Robinhood Chain token (0x0B551573D731090B3F57129c11B0A4A9e4D0A69c)
  and linking to its pool.

## [1.17.0] - 2026-08-26

- **The $DON price ticker and contract-address chip were removed** ahead of
  the token's relaunch on Robinhood Chain. Analysing any other token is
  unchanged.
- **Fixed: the logo in the navigation collapsed into a thin sliver** on
  screens narrower than about 1500px. It now stays square at every width, in
  both themes.

## [1.16.1] - 2026-08-25

- The token-age profile formerly shown as "Established (>90d)" now reads
  "Established (60d+)", which is the range it has always covered. Tokens aged
  60 to 90 days were mislabelled; scores are unchanged.

## [1.16.0] - 2026-08-22

- **Share Intel:** a finished scan can be turned into a branded image for X
  from a new panel at the foot of the result. Choose between three layouts,
  and the choice is remembered: a ticket card with the full read and a score
  stub, a portrait poster built around the score, and a tape card showing the
  real hourly candles with the entry zone and both targets marked.
- Copy the image, download it, or send it straight to X. Phones get the native
  share sheet with the image attached; on desktop the image goes to the
  clipboard and the X composer opens.
- The preview and the exported image are identical, exported at double
  resolution, and follow the light or dark theme (switching theme repaints the
  card).
- The version shown in the page footer was out of date and now matches the
  release.

## [1.15.1] - 2026-08-13

- The docs link in the navigation and the "how the score works" link under a
  result were pointing at an address that no longer works. Both now open the
  live documentation.

## [1.15.0] - 2026-08-11

- A "docs" link now sits in the navigation and opens the DigitalDon
  documentation in a new tab.
- Under every result, a "how the score works" link goes straight to the page
  that explains how the score is derived.

## [1.14.0] - 2026-08-11

- **The official $DON token appears in the analyzer.** A small ticker in the
  top-left corner shows the $DON price in USD, refreshes once a minute while
  the tab is open, and links to its market page. If an update fails, the last
  known price stays on screen; on narrow screens the ticker drops the price
  first, then hides.
- The footer has a click-to-copy contract-address chip for $DON. It shows a
  shortened address, copies the full one, confirms in place and announces the
  copy to screen readers.
- Both are about DigitalDon's own token only and do not affect the token being
  analyzed.
- The version shown in the footer was out of date and has been corrected.

## [1.13.2] - 2026-08-10

- **Old tokens that have barely traded now get a result instead of an error.**
  A months-old contract with only a couple of candles used to show "not enough
  chart history" and the advice to wait a few hours. It now gets the reduced
  view with the on-chain read and the minute chart, whatever its age. If no
  chart data comes back at all, the error is still shown.
- That reduced view is now titled "no chart history" instead of "fresh
  launch", so a token that is months old no longer calls itself a new launch.
  Genuine new launches look as before.

## [1.13.1] - 2026-08-08

- **Fixed an analysis that could describe the wrong token.** For some trading
  pairs the chart and the whole analysis were built from the other token in
  the pair, while the header showed the right price. One case produced entry
  and exit zones in the hundreds of dollars for a coin trading well under a
  cent. The analyzer now always reads the token you asked for, and rejects
  chart data whose prices cannot belong to it.
- The Web Analyzer and the Telegram bot received the same fix, so they agree
  on these tokens again.

## [1.13.0] - 2026-08-04

_Internal changes only; no public notes for this release._

## [1.12.0] - 2026-07-31

- **The holder cluster map frames itself.** The camera fits the map to its
  panel and keeps it framed while the layout settles, then hands control back
  as soon as you zoom, pan or drag. "Reset view" or a double-click refits it,
  and 100% zoom now means the whole map fitted.
- Clicking a cluster, on the map or in the cluster list, flies the camera to
  it. Groups of connected wallets sit inside a soft outline with their letter
  and share of supply. Hovering a wallet lights up everything it funded or was
  funded by, plus the rest of its cluster.
- A refreshed look: shaded bubbles, curved and animated funding links, a
  layout that spreads clusters across the panel, fullscreen that uses the
  whole screen, and a tooltip that no longer gets clipped at the edges.
- Fixed: clicking a bubble now highlights its row in the cluster list,
  dragging while zoomed keeps the bubble under the pointer, and the PNG export
  is no longer cropped in fullscreen.

## [1.11.3] - 2026-07-31

_Internal changes only; no public notes for this release._

## [1.11.2] - 2026-07-31

- **Fixed scans failing on every token and every chain.** A fault introduced
  in 1.11.0 stopped each analysis at the last step. Scans work again. The
  Telegram bot was not affected.
- If the optional holder or X intelligence services cannot be reached, those
  panels are now simply left out and the analysis still completes.
- The error message no longer blames rate limiting when the cause is unknown.

## [1.11.1] - 2026-07-31

- **The analyzer no longer hangs on "loading".** Some scans that worked in the
  Telegram bot could spin forever on the web with no result or error.
  Market-data requests now time out and retry once on temporary failures, and
  any unexpected problem during an analysis now shows a readable error instead
  of an endless spinner.
- The version shown in the page footer was out of date and has been corrected.

## [1.11.0] - 2026-07-29

- **Security fix:** a specially crafted link to the analyzer could make it
  show results supplied by an outside server under DigitalDon's name. That is
  no longer possible on the live site, which only uses DigitalDon's own
  services.
- A stricter browser security policy now limits which servers the page can
  talk to, as an extra layer of protection.

## [1.10.0] - 2026-07-27

- **Token age is now accurate to the minute.** A 33-minute-old pool used to
  read "1h old" and anything under half an hour "0h old". Ages now show two
  units, for example "33m old", "1h 35m old", "4d 7h old" or "6mo 12d old",
  rounded down, and match the Telegram bot exactly.

## [1.9.1] - 2026-07-27

- Charts for brand-new tokens now appear from 5 one-minute candles instead of
  10, so a pool a few minutes old already shows its price action. The Telegram
  bot uses the same rule.
- When there is still too little data to draw a chart, the chart panel stays
  visible and says why: either the pool is not indexed yet, or only a few
  candles exist so far. Both suggest running the scan again shortly.

## [1.9.0] - 2026-07-27

- **One-minute candle chart for fresh launches.** The fresh-launch view now
  includes a chart of the pool's first minutes of trading. Its caption states
  the candle size and the real time span, and notes that there are no entry or
  exit zones yet. It matches the chart on the Telegram bot's fresh-launch
  card.

## [1.8.0] - 2026-07-27

- **Freshly launched tokens now get a result instead of an error.** A pool too
  young for chart analysis gets a dedicated fresh-launch view: no signal score
  and no trade plan, but an on-chain read of liquidity ratio, unlock overhang
  and buy/sell pressure, each with a risk marker. It matches the Telegram
  bot's fresh-launch card, down to the wording.
- Holder intelligence and X intelligence are available on the fresh-launch
  view too, since "who holds this, and was it bundled" is the key question for
  a new token.
- An older token with missing chart data still shows an error rather than
  being presented as a new launch.
- The dashes in the on-chain notes now match the rows above them.

## [1.7.0] - 2026-07-26

- The short-term plan panel no longer disappears when there is no tradable
  setup. It now stays on screen with the reason, for example "No tradable
  range — 72h band is only 0.2% wide.", worded the same way as in the Telegram
  bot.

## [1.6.0] - 2026-07-26

- The optional X intelligence and holder intelligence panels now appear only
  when those features are live. They are switched on and off together with the
  Telegram bot, and stay hidden if their service cannot be reached.
- If a feature is switched off while the page is open, its panel says it is
  not live yet and asks you to reload, instead of showing a generic error.

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
