# The Analysis API

The same analysis the bot and the Web Analyzer run, as JSON.

If you're building something — an agent, a dashboard, a bot of your own — this
is the surface to build on. It answers with typed fields instead of a rendered
card, so nothing has to be scraped or parsed out of Markdown.

## The one guarantee

`POST /v1/analyze` runs the *same code path* as `/don` in Telegram and as
[analyzer.digitaldon.net](web-analyzer.md). Not a reimplementation, not a copy
kept in step — literally the same pipeline, in the same process, sharing the
same cache. The same token at the same moment scores the same on all three.

## It's for agents, and it's paid

The Telegram bot and the Web Analyzer are free, and stay free. A human reads one
card at a time.

A machine doesn't. An agent can pull the analysis in a loop, and the market data
underneath it — prices, candles, holder graphs — is metered and billed to us. So
the API is priced per call, in USDC, over
[x402](https://github.com/x402-foundation/x402): the HTTP-native payment
protocol agents already speak.

Roughly a cent for a standard scan. No account, no API key, no invoice — your
agent pays per request and gets an answer.

## Calling it

```bash
curl -X POST https://<your-bot-host>/v1/analyze \
  -H 'Content-Type: application/json' \
  -d '{"token": "BONK"}'
```

First call comes back **402** with the price and the chains we accept:

```
HTTP/1.1 402 Payment Required
PAYMENT-REQUIRED: <base64 payment requirements>
```

Your agent signs a payment and retries with a `PAYMENT-SIGNATURE` header. Any
x402 client library does this for you. The answer comes back 200 with the
receipt in `PAYMENT-RESPONSE`.

We accept **USDC on Base and on Solana** — both are offered in the same 402, so
your agent pays on whichever chain it holds funds on.

A GET form takes the same parameters, for quick checks and browser testing:

```bash
curl 'https://<your-bot-host>/v1/analyze?token=BONK&depth=holders'
```

### Request

| Field | Type | Default | Meaning |
|---|---|---|---|
| `token` | string, **required** | — | Ticker, name, or contract address |
| `chain` | string | `auto` | `sol`, `eth`, `base`, `bsc`, `rh`, `arb`, `mnt`, or `auto` |
| `depth` | string | `basic` | Whichever of `basic`, `holders`, `social`, `full` this deployment sells — see below |
| `options.include_chart_raw` | bool | `false` | Return the candles the analysis ran on |
| `options.include_raw_metrics` | bool | `false` | Return every engine field, unshaped |

**Depth costs money and time.** `basic` is the chart and the on-chain read.
`holders` adds a [wallet-cluster scan](holder-analysis.md), `social` adds an
[X credibility check](social-sentiment.md) on the token's linked account, `full`
adds both. Ask for what you'll actually read.

**The menu is whatever the deployment can actually deliver.** A depth whose
feature is switched off is dropped from the `depth` enum, priced nowhere, and
refused with `depth_unavailable` before any payment is taken — we would rather
not sell you a block that comes back empty. At the time of writing `social` and
`full` are **not live** (the X credibility check is off), so the live menu is
`basic` and `holders`. Don't take that from this page: read the `depth` enum in
[`/v1/openapi.json`](#the-contract), or call the free `get_pricing` MCP tool.
Both are generated from the same table the server charges from.

**`chain: auto`** searches every active chain and analyses the deepest pool. The
others come back in `data.request.alternatives` — there's no interactive picker
over HTTP, so if you wanted a different one, re-request with an explicit `chain`.

### Response

```json
{
  "ok": true,
  "error": null,
  "data": {
    "schema_version": "2.0.0",
    "engine_version": "1.24.0",
    "token":    { "symbol": "BONK", "chain": "solana", "profile": { "key": "ESTABLISHED" },
                  "asset_class": "crypto", "underlying": null },
    "market":   { "price_usd": 0.0000213, "liquidity_usd": 4200000, "txns_24h": { "buy_ratio": 0.58 } },
    "analysis": {
      "available": true,
      "score": 68,
      "score_label": "Bullish, accumulation zone",
      "signals": { "momentum": { "signal": "bullish", "rsi": 41.2, "detail": "oversold (RSI 41)" } },
      "levels":   { "short_term": { "entry": { "low": 0.0000198, "high": 0.0000205 },
                                    "upside_pct": 12.4, "tradable": true } }
    },
    "onchain":  { "liquidity": { "risk": "healthy" }, "notes": [] },
    "holders":  null,
    "social":   null,
    "warnings": []
  }
}
```

Two version fields, and they move independently. **`schema_version`** is the
shape of the document — parse against it. **`engine_version`** is the analysis
contract that produced the numbers — cache against it. A scoring change bumps
the second and leaves the first alone.

## Know what you're looking at

`data.token.asset_class` is `crypto` or `stock`, and it's always there.

`stock` means the token is a tokenized claim on a listed security, matched
against a [verified issuer registry](../start/stocks.md) rather than guessed
from the chain. When it's set, `data.token.underlying` names what's behind it:

```json
"token": {
  "symbol": "NVDA", "chain": "robinhood", "asset_class": "stock",
  "underlying": {
    "ticker": "NVDA", "name": "NVIDIA", "kind": "stock",
    "issuer": "Robinhood", "dual_listed": true,
    "market_status": { "open": true, "label": "market open · closes 16:00 ET" }
  },
  "profile": { "key": "STOCK", "label": "📈 Tokenized equity" }
}
```

**The engine agrees with the field.** A tokenized equity is scored on the
[`STOCK` profile](../engine/profiles.md) — chosen by what the token *is*, not by
its age — so `analysis.profile.key` reads `STOCK` and the short horizon reads
`days` rather than `1d`. The two move together; you can branch on either.

**Branch on it before you apply any priors.** Robinhood Chain is an Arbitrum
Orbit L2 built for tokenized equities — a token there is usually a share, not a
meme. Scoring a tokenized NVIDIA the way you'd score a week-old memecoin
produces a confident, wrong answer, and the chain id alone won't stop you: the
same NVIDIA is also listed on Solana as `NVDAx` by xStocks. That's what
`dual_listed` is telling you, and the other route is in
`data.request.alternatives`.

`market_status` is the **underlying equity market**, not the token's pool. The
token trades around the clock; NVIDIA does not. A read taken at 03:00 ET is
looking at a stale reference price, and you should know that before you act on
it.

**Holder depths aren't sold for tokenized stocks.** Their supply sits with the
issuer and the exchanges custodying it, so clustering would report custody
wallets as insiders. Ask for `holders` on one and you get a warning saying so,
a `null` block — and no charge.

## What it costs

| Depth | Price | What you get | |
|---|---|---|---|
| `basic` | $0.01 | Chart analysis + on-chain read | live |
| `social` | $0.03 | ...plus X credibility | **not live** |
| `holders` | $0.05 | ...plus wallet clustering | live |
| `full` | $0.08 | Everything | **not live** |

Plus $0.01 for `include_chart_raw`, $0.005 for `include_raw_metrics`.

Priced per depth because the cost per depth is genuinely different — a `basic`
scan is two candle fetches, a `holders` scan walks a wallet funding graph. Flat
pricing would just mean shallow calls subsidising deep ones.

The live price list is always in the `x-402` block of
[`/v1/openapi.json`](#the-contract), generated from the same table the server
charges from. Only depths this deployment can actually deliver are listed — and
only those can be bought.

**Free trial:** one call per day per IP at `basic`, no payment needed, so you can
see the shape of a real response before wiring up a wallet.

## You only pay for a complete answer

Two guarantees, and they're enforced in code rather than promised in a FAQ:

**A failed scan is free.** Payment is verified *before* the analysis runs and
settled only *after* it succeeds. If our upstream data source falls over, the
money never moved. There's no refund process because there's nothing to refund.

**A partial answer is free too.** If any block you paid for comes back empty —
the chain has no holder backend, the token has no X account, something upstream
failed — you get `depth_undeliverable` and **you are not charged**. Retry at a
depth that fits the token; `basic` always works.

The one case where you pay and get less than you hoped: the analysis ran fine
and simply says the token looks bad. That's a complete answer.

## Three things that trip people up

**A missing block is not a failure.** If a depth can't be served — the feature
is off, the chain has no holder backend, no X account is linked, an upstream
call failed — you get the blocks that *did* work, `null` for the one that
didn't, and an entry in `data.warnings` explaining which and why. Status stays
200. The chart analysis was already paid for; throwing it away because the
holder scan failed would help nobody.

**No analysis is still an answer.** A token too new to have candles returns 200
with `analysis.available: false`. Check `analysis.state`:

- `fresh_launch` — too young for a chart to exist yet
- `dormant` — old enough, but it has barely traded since launch

Those are different findings and shouldn't be described the same way. A
four-month-old token that stopped trading is not a new launch. Either way,
`data.onchain` is populated — liquidity ratio and unlock overhang need no
candles, and at that age "is this a rug" is the more useful question than
"where's the entry".

**Zones are `null`, never zero.** No short-term setup and a setup at $0 are not
the same thing. If `levels.short_term.entry` is `null`, check `no_setup_reason`
— it'll tell you the band was too narrow to trade.

## Prefer tools over HTTP?

If you're wiring this into an AI agent rather than writing HTTP calls yourself,
use the [MCP server](mcp.md) instead — same analysis, same pricing, but the agent
discovers and calls it on its own.

## Finding your way around

`GET /` returns a small index — what the service is, where the endpoints are,
and whether payment is switched on:

```json
{
  "service": "digitaldon-api",
  "endpoints": { "analyze": "/v1/analyze", "openapi": "/v1/openapi.json",
                 "mcp": "/mcp", "health": "/health" },
  "paid": true
}
```

Handy if you've been handed a hostname and nothing else.

## The contract

```
GET /v1/openapi.json
```

An OpenAPI 3.1 document, built from the running configuration — the chain enum
is that deployment's active chains, the rate limit is the one actually enforced.
Point your client generator (or your agent) at that URL rather than a copy you
keep locally, and it can't drift from the server answering you.

It's free to read, and it carries **three complete worked responses** — a `basic`
call, a `holders` call, and a tokenized stock — so you can see exactly what an
answer looks like before you spend anything. Those are generated by the same code
that builds a real response, so they can't drift either.

## Errors

Failures use the same envelope with `ok: false`, a machine-readable `error`, and
a `detail` string written to be read.

| Code | Status | |
|---|---|---|
| `invalid_request` | 400 | Malformed body, missing or oversized `token` |
| `invalid_depth` | 400 | `depth` wasn't one of the documented values |
| `depth_unavailable` | 400 | That depth isn't sellable here right now — `detail` names what is |
| `payment_required` | 402 | Pay and retry. Price is in the header and in `accepts` |
| `payment_failed` | 402 | Settlement failed, result withheld. No funds moved |
| `depth_undeliverable` | 402 | Couldn't serve this token at that depth — **not charged** |
| `unknown_chain` | 400 | Not a chain this API knows |
| `inactive_chain` | 400 | Known, but switched off on this deployment |
| `token_not_found` | 404 | No pool matched |
| `feature_disabled` | 404 | The endpoint is switched off |
| `no_chart_data` | 422 | Resolved, but the OHLCV source returned nothing — transient |
| `rate_limited` | 429 | Per-IP limit exceeded |
| `internal` | 502 | An upstream call failed — transient |
| `payment_unavailable` | 503 | Payment layer unreachable. Fails closed — transient |

`no_chart_data` and `internal` are worth a retry. The 400s are not — fix the
request.

## Rate limits

Six requests per minute per IP by default, with its own budget: an API caller
can't drain what the Web Analyzer needs. Deep scans are additionally bounded by
a server-side concurrency cap, so a burst queues rather than failing.

Asking for a *price* is cheap and has its own, much higher limit — the
probe-then-pay handshake never eats into your scan budget.

## What's cached, and for how long

Published, because "is this a live read or a cached one" is a fair thing to want
answered before you build on a paid source — and the only other way to find out
is to buy two calls and compare. The live numbers are in the `x-cache` block of
[`/v1/openapi.json`](#the-contract), read from the modules that enforce them:

| | Default | |
|---|---|---|
| Analysis document | 60s | Repeat calls for the same token inside the window are served from one memoised scan — identical numbers |
| Candles behind it | 90s | Maximum age of the OHLCV frame the analysis ran on |
| Holder block | 900s | The wallet-cluster scan is expensive upstream |
| Social block | 1800s | Per X handle |

The cache is shared with Telegram and the Web Analyzer — that's the same-answer-
everywhere guarantee at the top of this page, made of one memoised scan rather
than three.

Two things worth being plain about. **`generated_at` is when the document was
built, not when the data was read** — check `engine_version`, not the timestamp,
when you cache your own copies. And **a cache hit is still charged**: the price
is for the answer, not for our upstream request. The cache is in-memory and
per-process, so treat every number above as a freshness bound rather than a
guarantee.

## Not reachable from a browser

There's no CORS grant on `/v1/analyze`. A web page can't spend the API on a
visitor's behalf. Call it server-side, from your agent — which is where an agent
lives anyway.

The spec at `/v1/openapi.json` *is* browser-readable. Reading a price list isn't
spending it.

---

None of this is financial advice. It's an opinion with arithmetic behind it.
