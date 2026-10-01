# The Widget

The analyzer, on your page. One script tag puts a DigitalDon card on any
website — a token page, a trading terminal, a launchpad, a community site —
running the **same analysis engine** as the [Telegram bot](telegram.md) and
the [Web Analyzer](web-analyzer.md). Same token, same numbers, everywhere.

**Live demo:** [widget.digitaldon.net/demo](https://widget.digitaldon.net/demo)

```html
<script async src="https://widget.digitaldon.net/embed.js"
        data-chain="solana"
        data-address="<token contract address>"
        data-theme="dark"></script>
```

That is the whole integration. No build step, no API key, no account, no CSS
to include. It is free, and there is no rate limit on embedding it.

## What your visitors get

Two tools in one card.

**analysis** — name, price and 24h change, the **signal score** out of 100
with the band it falls in, four category reads (momentum, trend, structure,
volume), the short-term and long-term **entry and exit zones** with upside,
market cap / liquidity / 24h volume / buy share, and the profile and risk
flags. A token too new for a technical read gets the on-chain read instead,
exactly as the bot and the analyzer answer for it.

**holders** — the [wallet cluster scan](holder-analysis.md), and it is the
analyzer's, not a summary of it: holder count, top-10 and largest-wallet
share and concentration, then the **interactive wallet cluster map** —
drag the bubbles, scroll to zoom, click a group. Each group gets an index
card with its share of supply; opening one slides out a dossier with its
**wallets**, the **evidence** for why those wallets are grouped (the exact
transfer, the funding, the shared funder, each marked strong or weak by the
engine) and the estimated **price impact if the group sells**. Filter chips
for sniper / bundle / insider / fresh wallets, an eye to hide a wallet or a
whole group from the map, and a **funding replay** that scrubs from launch
to now so a bundle forms in front of you. It runs the same code as the
analyzer's map, because it is built from the same source file.

**Fullscreen.** The cluster scan expands to fill the screen — see
[Fullscreen](#fullscreen) for the one attribute a hand-written `<iframe>`
needs.

Plus a button through to the full analysis on
[analyzer.digitaldon.net](https://analyzer.digitaldon.net), where the
interactive chart and [x intelligence](social-sentiment.md) live.

## Choose your integration

### 1. The scanner

For a site that is **not about one token** — a tools menu, a community page,
a launchpad dashboard. The card opens with a search box: your visitor pastes
a contract address or a ticker, gets the analysis, and the holders tab is one
click away.

```html
<script async src="https://widget.digitaldon.net/embed.js"
        data-theme="dark"></script>
```

The card mounts where the script tag sits. To place it somewhere else, use a
container (see [Mounting](#mounting) below).

### 2. The token tool

For a **token page**: a chart, a terminal, a listing, an explorer. Pin the
address and the card runs on load — no interaction needed.

```html
<script async src="https://widget.digitaldon.net/embed.js"
        data-chain="solana"
        data-address="EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"></script>
```

Two variants worth knowing:

**Open on the cluster scan.** `data-view="holders"` shows the holders tool
first, with the analysis still one tab away.

```html
<script async src="https://widget.digitaldon.net/embed.js"
        data-chain="solana" data-address="<address>"
        data-view="holders"></script>
```

**Cluster scan only.** `data-tools="holders"` makes the whole card a holder
scan — no tabs, no candles fetched. This is the "holder map" button pattern
that sits next to a chart on the big aggregators: put it behind your own
button, in a modal or a side panel, and it scans the token the page is
already showing.

```html
<div id="holder-panel"></div>
<script async src="https://widget.digitaldon.net/embed.js"></script>
<script>
  document.querySelector('#cluster-scan-btn').addEventListener('click', () => {
    DigitalDon.mount('#holder-panel', {
      chain: 'solana',
      address: currentToken.address,
      tools: 'holders',
      theme: 'dark',
    });
  });
</script>
```

## Mounting

Three ways, pick whichever fits your page.

**In place.** Put the `data-*` attributes on the script tag itself and the
widget replaces it where it stands. Good for a static page or a CMS block.

**In a container.** Mark any element with `data-digitaldon-widget` and the
loader fills it. Good when the script lives in your `<head>` or a bundle.

```html
<div data-digitaldon-widget
     data-chain="base"
     data-address="0x…"
     data-theme="light"></div>

<script async src="https://widget.digitaldon.net/embed.js"></script>
```

**From JavaScript.** `DigitalDon.mount()` returns a handle you can drive.
Required for single-page apps, and the only way to receive callbacks.

```js
const widget = DigitalDon.mount('#slot', {
  chain: 'solana',
  address: 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v',
  theme: 'auto',
});
```

## Options

Every option works as a `data-*` attribute (on the script tag or on a
container) and as a key in the `mount()` options object. The callbacks are
`mount()` only.

| Option | Values | Default | What it does |
|---|---|---|---|
| `chain` | `solana` `ethereum` `base` `bsc` `robinhood` `arbitrum` `mantle` `arc` | — | Chain of the pinned token. `sol`, `eth`, `bnb`, `rh`, `arb`, `mnt` also work. A chain that has no pool for the address falls back to the deepest pool anywhere, so a wrong slug degrades to a right answer. |
| `address` | contract address | — | Pins a token. The card analyses it on load. |
| `q` | ticker, name or address | — | Runs a search on load instead of pinning. A multi-chain hit shows a picker. |
| `tools` | `analysis,holders` `analysis` `holders` | both | Which tools the card offers. `holders` alone fetches no candles at all. |
| `view` | `analysis` `holders` | `analysis` | Which tool opens first when both are offered. |
| `theme` | `light` `dark` `auto` | `auto` | `auto` follows the visitor's `prefers-color-scheme`. Pass the one your page uses. |
| `search` | `1` `0` | on when nothing is pinned | Force the search box on or off. |
| `height` | pixels | `260` | Starting height, before the card reports its real one. Set it near your expected height to avoid a visible jump. |

## The JavaScript API

```js
// mount returns a handle
const w = DigitalDon.mount('#slot', {
  chain: 'solana',
  address: '…',
  theme: 'dark',
  tools: 'analysis,holders',
  view: 'analysis',
  onReady:   info => console.log('widget', info.version, 'engine', info.engine),
  onResult:  res  => console.log(res.symbol, res.score, res.thesis),
  onHolders: h    => console.log(h.symbol, h.bubble_risk, h.clustered_pct),
});

w.update({ chain: 'base', address: '0x…' });  // switch token, no reload
w.show('holders');                            // switch tool
w.setTheme('light');                          // switch theme
w.destroy();                                  // remove it
```

Also on the global:

| | |
|---|---|
| `DigitalDon.mount(target, options)` | `target` is a CSS selector or an element. Returns the handle. |
| `DigitalDon.scan()` | Mounts any `data-digitaldon-widget` container added since the last scan. Call it after rendering new DOM. |
| `DigitalDon.widgets` | Every live handle. |
| `DigitalDon.version` | The loader's version. |
| `DigitalDon.origin` | Where the widget is served from. |

### Callbacks

`onResult` fires when an analysis renders:

```js
{ chain: 'solana', address: '…', symbol: 'BONK', score: 68,
  thesis: 'Bullish, accumulation zone', profile: 'ESTABLISHED', engine: '1.26.0' }
```

`onHolders` fires when a cluster scan completes:

```js
{ chain: 'solana', address: '…', symbol: 'BONK', bubble_risk: 'Low',
  clustered_pct: 6.4, top10_pct: 22.1, clusters: 2 }
```

Use them to badge your own UI — a score chip next to your ticker, a warning
dot when `bubble_risk` is `High`. They are a summary of what the card is
already showing, not investment advice, and they must not be presented as
DigitalDon telling anyone what to buy.

## In a framework

**React / Next.js.** Load the script once, mount into a ref, and destroy on
unmount. `update()` on an address change avoids re-creating the frame.

```jsx
import { useEffect, useRef } from 'react';

function DigitalDonWidget({ chain, address, tools = 'analysis,holders' }) {
  const slot = useRef(null);
  const widget = useRef(null);

  useEffect(() => {
    let cancelled = false;

    const load = () => new Promise((resolve) => {
      if (window.DigitalDon) return resolve();
      const existing = document.querySelector('script[data-digitaldon-loader]');
      if (existing) return existing.addEventListener('load', resolve, { once: true });
      const s = document.createElement('script');
      s.src = 'https://widget.digitaldon.net/embed.js';
      s.async = true;
      s.dataset.digitaldonLoader = '';
      s.addEventListener('load', resolve, { once: true });
      document.head.appendChild(s);
    });

    load().then(() => {
      if (cancelled || !slot.current) return;
      widget.current = window.DigitalDon.mount(slot.current, { chain, address, tools });
    });

    return () => {
      cancelled = true;
      widget.current?.destroy();
      widget.current = null;
    };
  }, []);                       // mount once

  useEffect(() => {             // follow the route's token
    widget.current?.update({ chain, address });
  }, [chain, address]);

  return <div ref={slot} />;
}
```

**Vue, Svelte, Angular.** Same shape: mount in the "mounted" hook, `update()`
in a watcher, `destroy()` in the teardown hook.

**Server-side rendering.** The loader touches `document`, so mount it in a
client-only effect. Nothing needs to run on the server.

## Sizing and layout

The card is fluid. It fills the width of its container and **reports its own
height**, which the loader applies to the frame — so there is never an inner
scrollbar or a clipped footer, and the height follows a tab switch or a
finished scan automatically.

- Minimum sensible width is **260px**; it looks best between **320px and
  520px**.
- Give the container the width you want. Do not set a fixed height.
- In a sidebar or a modal, `width: 100%` on the container is all it needs.
- The frame starts at `height` (default 260px) and resizes as soon as the
  card is ready. On a slow connection that first paint is what your visitor
  sees, so set `height` close to what you expect if the jump bothers you.

## Fullscreen

The cluster scan carries a **fullscreen** button. The widget runs in an
iframe on our domain, and a browser refuses the Fullscreen API to a
cross-origin frame unless the page embedding it says otherwise — so the
button works one of two ways, and is hidden when neither is available.
It is never a control that does nothing.

| How you embedded it | What the button does |
|---|---|
| `embed.js` script tag, or `DigitalDon.mount()` | **Native fullscreen.** The loader sets `allow="fullscreen"` on the frame. Nothing to do. |
| `embed.js` from a stale cache | **Expands** to fill the viewport instead — the loader stretches the frame. `Esc` closes it. Same result, no permission needed. |
| Your own hand-written `<iframe>` | **Nothing, unless you opt in.** No loader to ask and no grant. Add `allow="fullscreen"` (below) and you get the native path. |

If you write the iframe yourself:

```html
<iframe src="https://widget.digitaldon.net/?chain=solana&address=<token>&tools=holders"
        allow="fullscreen" allowfullscreen
        style="width:100%;height:520px;border:0"></iframe>
```

One caveat worth knowing: a `Permissions-Policy` response header on your own
page can switch fullscreen off for everything it contains, and that beats the
iframe attribute. If you send one, keep `fullscreen` enabled — or leave it
out and the default allows it.

## Supported chains

Solana, Ethereum, Base, BNB Chain, Robinhood Chain, Arbitrum, Mantle and Arc —
the same list the bot and the analyzer cover, from
[Supported chains](../start/chains.md). A token on any other chain answers
"no token found on a supported chain" rather than guessing.

The holders tool covers the chains our
[cluster analysis](holder-analysis.md) supports; where it is unavailable the
tab is simply not shown.

## What runs on your page

Effectively nothing of ours.

- The widget renders **inside an iframe on DigitalDon's own domain**. The
  loader's only job is to create that frame and resize it.
- No script of ours runs in your page's context, and nothing of your page is
  visible to the widget.
- The frame is **sandboxed**: `allow-scripts allow-same-origin allow-popups
  allow-popups-to-escape-sandbox allow-forms`. No top-level navigation, no
  pointer lock, no downloads.
- The loader is about 6KB, has no dependencies, sets no cookies on your
  domain, and reads nothing from your page except `location.hostname`, which
  attributes the usage to your site.
- Inside the frame the page runs under a strict Content Security Policy and
  may only talk to the market-data APIs the analyzer already uses and to
  DigitalDon's own API.

**If your site sends a Content Security Policy**, allow the frame and the
script:

```
script-src  https://widget.digitaldon.net;
frame-src   https://widget.digitaldon.net;
```

## What we count

Per embedding website: how often the card loaded, how many distinct visitors
saw it, how many analyses and cluster scans ran, how many people clicked
through to the analyzer, and which chains and tokens were analysed.

No cookies, no IP addresses, no profile, no tracking across sites. The
visitor id is a random string the widget stores in that browser, and modern
browsers partition that storage per embedding site, so it cannot follow
anyone anywhere.

## Troubleshooting

**Nothing appears.** Check that the loader itself was fetched (network tab,
`embed.js`, 200) and that your CSP allows `widget.digitaldon.net` in both
`script-src` and `frame-src`. If you mounted into a container, make sure the
container exists when the loader runs — with `async` it may run before your
markup does; use `DigitalDon.scan()` or `mount()` after render.

**The card says no token was found.** The address is not on a supported
chain, or the token has no pool DexScreener indexes. Check it resolves on
[the analyzer](https://analyzer.digitaldon.net) first — the widget and the
analyzer resolve tokens identically.

**No score, just an on-chain read.** The token is too new, or too thinly
traded, for an honest technical read. That is the answer, not an error, and
the bot answers the same way.

**The holders tab is missing.** The chain is not covered by cluster
analysis, or holder intelligence is temporarily off on our side. The card
falls back to the analysis rather than showing an empty tab.

**The frame is the wrong height.** Something in your CSS is overriding the
height the loader sets. Do not set `height` on the iframe or its container in
your stylesheet.

**There is no fullscreen button.** You are using your own `<iframe>` without
`allow="fullscreen"`, or a `Permissions-Policy` header on your page disables
fullscreen. See [Fullscreen](#fullscreen). We hide the button rather than
show one that cannot work.

**Fullscreen covers the page instead of going truly fullscreen.** That is the
fallback doing its job: the frame was not granted the Fullscreen API, so the
loader stretched it over the viewport. `Esc` closes it. Add
`allow="fullscreen"` to get the native behaviour.

## Get in touch

Building something with it, need an allow-listed deployment, or want a
feature the card does not have yet? Reach us on
[Telegram](https://t.me/digitaldon_official) — we would rather hear from you
early than find out from the usage stats.
