# The Web Analyzer

The browser version. Same analysis, no Telegram required.

👉 [analyzer.digitaldon.net](https://analyzer.digitaldon.net)

(The project's home page is [digitaldon.net](https://digitaldon.net) — the
analyzer lives on its own subdomain.)

Nothing to install, no account, no wallet connect. Open the page and paste a
token.

## Using it

Paste a ticker, name or contract address and hit **analyze**. A progress row
shows what it's doing — resolving, fetching the chart, analysing — and then the
result panels render.

Multi-chain matches get a picker, same as the bot.

## Tokenized stocks

The **tokens | stocks** switch under the logo flips the page into the stocks
section: a board of every official tokenized equity from xStocks and Robinhood,
filterable by kind and issuer, that narrows as you type. One click runs the
deepest listing and opens the chart; a stock listed with both issuers gets a
`SOL · RH` switch in the card header. Details, and what is different on a stock
card, in [Tokenized stocks](../start/stocks.md).

**Deep links** run an analysis on page load:

```
https://analyzer.digitaldon.net/?q=BONK
https://analyzer.digitaldon.net/?q=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v
https://analyzer.digitaldon.net/?view=stocks
https://analyzer.digitaldon.net/?view=stocks&q=TSLA
```

Handy for pasting a pre-loaded analysis into a chat.

There's also a day/night toggle, because staring at a dark chart at 2pm is its
own kind of pain.

## What's in the result

The same content as the [Telegram card](analysis-card.md) — score gauge, both
trade plans, the four category reads, token stats, on-chain risk notes — laid out
as panels instead of a single message, with an interactive chart.

Plus two panels the browser does better than Telegram can.

### x intelligence

Runs the [social sentiment](social-sentiment.md) analysis on the project's X
account. Click to run — it isn't automatic.

### holder intelligence — the bubble map

The [holder and cluster analysis](holder-analysis.md), rendered as an interactive
map. Each holder is a bubble sized by its share of supply; wallets that are
demonstrably connected are drawn as a cluster.

You get:

* zoom in / out, fullscreen, reset view
* hover for wallet detail — address, percentage, role tags
* a legend for the role colours (sniper / bundle / insider / fresh / dev)
* **export png** and **export csv**

The CSV export is the fastest way to take the holder set somewhere else for your
own digging.

### share intel — a card, or a link that previews as one

**make card** draws the scan as an image for X. Any link to a scan — **copy
link**, or simply the address in your browser bar — shows up as the scan card
itself wherever you paste it: X, Telegram, Discord, WhatsApp, Slack. Score,
entry and target zones, chain, and the time it was scanned. Whoever taps it
lands straight on the full scan here.

The preview is a snapshot. Platforms keep a link's preview for a while, so the
card says when it was taken; the scan behind the link is always live.

## Watchlist

Every result has a **watch** button in its top bar. Tap it and the token joins
your watchlist, the **★ watchlist** button next to the search box, together with
the score from that moment.

Open the watchlist and your tokens are grouped by what to do:

| Group | Means |
|---|---|
| **In the buy zone** | the price is inside the plan's buy zone and the score supports a buy |
| **Waiting for a dip** | good score, but the price is above the buy zone |
| **Fell under the buy zone** | the price broke below the zone; rescan for a fresh plan |
| **No buy signal** | the score is below 55, there is no setup on this horizon, or the token has not been scanned yet |

Each card shows the score and how it changed since you starred it, the
**potential profit** to the plan's sell level, how far the price is above the
zone's floor, and price and market cap since you starred it. A **moved** tag
marks anything that changed since you last opened the list.

* **Short-term or long-term.** The switch at the top regroups the whole list by
  either plan. Each card has its own short · long switch for a quick look at
  the other plan.
* **Edit view** turns any part of the card on or off, groups by chain instead,
  or makes the cards compact. Everything is on by default.
* **Refresh all** rescans every starred token in turn. Prices update on their
  own while the list is open.
* **Copy list link** gives you a link that rebuilds the list in another
  browser or on another device. Opening it adds the tokens; it never removes
  any.

{% hint style="info" %}
**No account.** The watchlist and your view settings are stored in your
browser only and never sent anywhere. Clearing your browser's site data clears
them; keep the list link if you want a backup.
{% endhint %}

## Same numbers as Telegram

The score you get in the browser is the score you get in Telegram — not "close
to", the same integer. The two surfaces are checked against each other
automatically before any change to the analysis can ship, and a mismatch blocks
the release.

That matters more than it sounds. This is a tool whose entire output is a
verdict; two different verdicts for the same token would be worse than no verdict
at all.

## If a panel is missing

The two optional panels are the only part of the page that needs anything beyond
your browser, and they can be switched off centrally. When they're off, the panel
simply isn't rendered.

It **fails closed** on purpose: if the page can't confirm a feature is live, it
doesn't draw it. Better a missing panel than a button that produces an error.

## What it can't do

The Web Analyzer is analyzer-only, on purpose. Group features — auto-scan, PNL
cards, the leaderboard — are inherently Telegram things, and they stay there. The
page links to the bot for those.
