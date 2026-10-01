# DigitalDon

Crypto token analysis: a signal score, entry and exit zones, an on-chain read
and a wallet-cluster scan. The same analysis runs everywhere we ship it: in
the Telegram bot, the [Web Analyzer](https://analyzer.digitaldon.net), the
embeddable widget, the JSON API and the MCP server for AI agents. The same
token at the same moment scores the same on all of them.

This repository is the **public side** of DigitalDon: how to integrate with
us, and a record of what we ship. It is updated automatically on every
release. The product itself is built in a private repository; nothing here
needs it.

| You want to | Use | Start here |
|---|---|---|
| Show the analysis or the holder map on your website | **Widget**: one script tag, free, no key | [`docs/using/widget.md`](docs/using/widget.md) · [examples](examples/widget/) |
| Pull the analysis as JSON from your backend | **REST API**: pay per call in USDC over x402, no account | [`docs/using/api.md`](docs/using/api.md) · [`api/openapi.json`](api/openapi.json) · [examples](examples/api/) |
| Let an AI agent call it on its own | **MCP server** at `https://api.digitaldon.net/mcp` | [`docs/using/mcp.md`](docs/using/mcp.md) · [examples](examples/mcp/) |

**Building with a coding assistant?** Point it at this repository and tell it
to read [`AGENTS.md`](AGENTS.md) first. That file holds the endpoints, rules
and pitfalls in one place.

## What's in here

```
AGENTS.md          integration guide for developers and coding models
docs/              the full user documentation (also at digitaldon.gitbook.io)
examples/          copy-paste integrations: widget, API, MCP
api/openapi.json   the live API contract, refreshed from production
changelog/         one changelog per component, same versions as our releases
versions.json      the current version of every component
server.json        our MCP registry entry
```

## Versions and releases

DigitalDon ships as independently versioned components. Each has its own
changelog here and its own tag prefix, and every release is published as a
GitHub Release in this repository:

| Component | Changelog | Tags |
|---|---|---|
| Telegram bot and API | [`changelog/bot.md`](changelog/bot.md) | `bot/vX.Y.Z` |
| Web Analyzer | [`changelog/webapp.md`](changelog/webapp.md) | `webapp/vX.Y.Z` |
| Website | [`changelog/website.md`](changelog/website.md) | `site/vX.Y.Z` |
| Widget | [`changelog/widget.md`](changelog/widget.md) | `widget/vX.Y.Z` |
| DiDo terminal | [`changelog/dido.md`](changelog/dido.md) | `dido/vX.Y.Z` |

Two further numbers in [`versions.json`](versions.json) matter to
integrators:

- **`engine_version`**: the analysis contract. When it moves, scores for the
  same input may change. Every API response and widget result carries it.
- **`api_schema_version`**: the shape of the API response. Parse against it.

## Contributing and support

This repository is published from our release pipeline, so pull requests
cannot be merged here. Open an issue for integration questions and bugs, or
reach us through [digitaldon.net](https://digitaldon.net).

Nothing DigitalDon produces is financial advice.
