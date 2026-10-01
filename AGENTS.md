# AGENTS.md: integrating DigitalDon

Written for coding assistants and the developers using them. Read this file
first; it links into `docs/` for detail. Everything here targets the
**production** services below. Nothing in this repository needs to be built or
run to integrate.

## Endpoints

| What | URL |
|---|---|
| Widget loader | `https://widget.digitaldon.net/embed.js` |
| Widget live demo | `https://widget.digitaldon.net/demo` |
| API base | `https://api.digitaldon.net` |
| Analysis endpoint | `POST` or `GET https://api.digitaldon.net/v1/analyze` |
| API contract (OpenAPI 3.1) | `https://api.digitaldon.net/v1/openapi.json` (snapshot: [`api/openapi.json`](api/openapi.json)) |
| MCP server (streamable HTTP) | `https://api.digitaldon.net/mcp` |
| Health | `https://api.digitaldon.net/health` |
| Web Analyzer (for humans) | `https://analyzer.digitaldon.net` |

The pages under `docs/` sometimes write `https://<your-bot-host>`. For the
hosted service, that is always `https://api.digitaldon.net`.

## Pick the surface

- **A website that should show the analysis or the holder map** → the widget.
  Free, no key, no rate limit on embedding. Do not call the REST API from a
  browser (see below).
- **Server-side code that needs the numbers** → the REST API.
- **An AI agent that should decide on its own when to analyse a token** → the
  MCP server. Same analysis and pricing as the REST API.

## Widget

Full reference: [`docs/using/widget.md`](docs/using/widget.md). Working pages:
[`examples/widget/`](examples/widget/).

```html
<!-- token page: pin the token, the card runs on load -->
<script async src="https://widget.digitaldon.net/embed.js"
        data-chain="solana"
        data-address="EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"
        data-theme="dark"></script>
```

Rules that matter:

1. **Three ways to mount:** `data-*` on the script tag (mounts in place);
   a `<div data-digitaldon-widget data-…>` container plus the script anywhere;
   or `DigitalDon.mount(target, options)`, which returns a handle. Only
   `mount()` gives callbacks.
2. **Options** (the same names as `data-*` attributes or `mount()` keys):
   `chain` (`solana` `ethereum` `base` `bsc` `robinhood` `arbitrum` `mantle`
   `arc`), `address`, `q` (search on load), `tools` (`analysis,holders` |
   `analysis` | `holders`), `view` (`analysis` | `holders`), `theme`
   (`light` | `dark` | `auto`), `search` (`1` | `0`), `height` (px).
3. **Single-page apps:** mount once, then call
   `handle.update({ chain, address })` when the route changes. Call
   `handle.destroy()` on unmount. Do not re-mount per token. The React
   component in `docs/using/widget.md` → *In a framework* is the reference
   shape. SSR frameworks must mount in a client-only effect.
4. **Callbacks:** `onResult({chain, address, symbol, score, thesis, profile,
   engine})` and `onHolders({chain, address, symbol, bubble_risk,
   clustered_pct, top10_pct, clusters})`. Use them to badge your own UI, and
   never present them as DigitalDon advising anyone to buy or sell.
5. **Sizing:** the card fills its container's width (260px minimum; 320 to
   520px looks best) and sets its own height. Do not give the container a
   fixed height or `overflow: hidden`.
6. **A hand-written `<iframe>`** (`https://widget.digitaldon.net/?chain=…&address=…`)
   needs `allow="fullscreen" allowfullscreen` or the fullscreen button is not
   shown. Prefer the loader.
7. **CSP on your page:** allow `script-src https://widget.digitaldon.net` and
   `frame-src https://widget.digitaldon.net`. The widget runs in a sandboxed
   iframe on our origin. It reads nothing from your page and sets no cookies.

## REST API

Full reference: [`docs/using/api.md`](docs/using/api.md). Contract:
[`api/openapi.json`](api/openapi.json). Examples: [`examples/api/`](examples/api/).

```bash
curl -X POST https://api.digitaldon.net/v1/analyze \
  -H 'Content-Type: application/json' \
  -d '{"token": "BONK", "chain": "auto", "depth": "basic"}'
```

Rules that matter:

1. **Payment is x402, USDC on Base or Solana. There is no account and no API
   key.** An unpaid call answers `402` with a `PAYMENT-REQUIRED` header. Sign
   a payment with an x402 client library and repeat the same request with a
   `PAYMENT-SIGNATURE` header. The receipt comes back in `PAYMENT-RESPONSE`.
   [`examples/api/python/`](examples/api/python/) does the whole round trip.
2. **Free trial:** the first `basic` call per IP per UTC day is free, so you
   can see a real response before wiring up a wallet.
3. **You only pay for a complete answer.** A failed scan, or a depth that
   could not be delivered (`depth_undeliverable`), is not charged.
4. **Server-side only.** `/v1/analyze` has no CORS grant. Reading
   `/v1/openapi.json` from a browser is fine.
5. **`depth`** is `basic` | `holders` | `social` | `full`, but only the depths
   in the live spec's `depth` enum are sold right now. Read the enum (or
   call the free MCP tool `get_pricing`) instead of hard-coding the list. The
   same applies to the `chain` enum and the prices in the spec's `x-402` block.
6. **Parse defensively:** a depth that could not be served comes back as a
   `null` block plus an entry in `data.warnings`, with status still 200.
   `analysis.available: false` with `analysis.state` of `fresh_launch` or
   `dormant` is a valid answer. Zones are `null` when there is no setup, never
   `0`. Tokenized stocks have `data.token.asset_class: "stock"`.
7. **Versions:** parse against `data.schema_version`. Cache against
   `data.engine_version`, not `generated_at`.
8. **Errors** use `{ok: false, error: "<code>", detail: "…"}`. Retry
   `no_chart_data`, `internal` and `payment_unavailable`. Do not retry 400s;
   fix the request. The default rate limit is 6 calls per minute per IP (`429 rate_limited`).

## MCP server

Full reference: [`docs/using/mcp.md`](docs/using/mcp.md). Client configs:
[`examples/mcp/`](examples/mcp/).

- URL: `https://api.digitaldon.net/mcp`. It is stateless, so no session or
  key is needed.
- Tools: `analyze_token` (`token` required; `chain`, `depth`,
  `include_chart_raw` optional) and `get_pricing` (free).
- Payment happens **inside** the tool call. An unpaid `analyze_token`
  returns a tool result flagged as an error that carries the x402 payment
  requirements. An x402-aware MCP client pays and retries on its own. Without
  one, the agent gets a readable price message instead of a crash.

## Keeping an integration current

- [`versions.json`](versions.json) lists every component's current version,
  plus `engine_version` and `api_schema_version`.
- [`changelog/`](changelog/) has one file per component. Watch this
  repository's Releases for `widget/v*` (the embed) and `bot/v*` (the API and
  MCP server).
- The widget loader is served unversioned from our origin and updates in place, so
  there is nothing to bump on your side.

## Don't

- Don't copy the widget's code or the analysis engine into your project.
  Load `embed.js`; it stays in step with every surface.
- Don't call `/v1/analyze` from a browser or embed any wallet key in
  client-side code.
- Don't scrape the Web Analyzer or the Telegram bot; use the API.
- Don't present a score as financial advice. DigitalDon's output is an
  opinion with arithmetic behind it.
