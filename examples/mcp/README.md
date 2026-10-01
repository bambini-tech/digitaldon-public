# Connecting an agent over MCP

The server is `https://api.digitaldon.net/mcp` (streamable HTTP, stateless, no
key). It offers `analyze_token` (paid, x402) and `get_pricing` (free). Full
reference: [`docs/using/mcp.md`](../../docs/using/mcp.md).

## Check it answers

```bash
curl -s -X POST https://api.digitaldon.net/mcp \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

## Claude Code

```bash
claude mcp add --transport http digitaldon https://api.digitaldon.net/mcp
```

## Clients configured with JSON (Cursor, and others)

```json
{
  "mcpServers": {
    "digitaldon": { "url": "https://api.digitaldon.net/mcp" }
  }
}
```

The file and key names differ per client; the value is always the `/mcp` URL.

## Claude API

See [`docs/using/mcp.md`](../../docs/using/mcp.md) → *Connecting it*: pass the
URL in `mcp_servers` and add a matching `mcp_toolset` entry to `tools`. Both
halves are required.

## Paying

An unpaid `analyze_token` returns a result flagged as an error that carries
the price and the x402 payment requirements. An x402-aware MCP client pays and
retries on its own; any other client shows the agent a readable price message.
