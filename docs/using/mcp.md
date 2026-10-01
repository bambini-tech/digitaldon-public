# The MCP Server

Give an AI agent a DigitalDon tool it can call by itself.

## What MCP is, in plain terms

The Model Context Protocol is a standard way for an AI agent to use outside
tools. You point the agent at a server; the agent asks "what can you do?", gets
back a list of tools with their inputs, and calls the one it needs.

The difference from the [REST API](api.md) is who writes the code. With the REST
API, *you* write the HTTP calls. With MCP, you register the server once and the
agent decides when to call it — mid-conversation, as part of whatever it's
working on.

Same analysis either way. Same engine as the Telegram bot.

## The endpoint

```
POST https://<your-bot-host>/mcp
```

One URL. It's stateless — no sessions, no setup, no keys.

## The two tools

**`analyze_token`** — the analysis. Takes `token` (required), plus optional
`chain`, `depth`, and `include_chart_raw`. Returns a readable summary for the
model to reason over, and the full structured document alongside it for anything
that needs the actual numbers.

**`get_pricing`** — what a call costs, which chains are served, how payment
works. **Free.** It's there so an agent can check the price before committing to
spend.

## Paying for tool calls

Yes — `analyze_token` is paid, same USDC pricing as the REST API. But payment
works differently here, and the difference matters.

Over plain HTTP, an unpaid request gets a `402 Payment Required` response. You
can't do that with MCP: an MCP client would read a 402 as "the connection is
broken" and give up. So the x402 convention moves the whole negotiation *inside*
the tool call:

1. Agent calls `analyze_token` with no payment.
2. The call **succeeds** at the protocol level, but the result is flagged as an
   error and contains the price and the chains we accept.
3. The agent signs a payment and calls the same tool again, attaching the
   payment to the call's metadata.
4. We verify it, run the analysis, settle, and return the result with the
   receipt attached.

An agent using any x402-aware MCP client does all of that on its own. An agent
without one still gets a readable message explaining the price rather than a
cryptic failure.

The same guarantee applies as on the REST API: **you are not charged for an
incomplete answer.** If a block you paid for comes back empty, the tool returns
an error and no money moves. That isn't a policy we remember to apply — the
payment layer refuses to settle a failed tool call.

## Connecting it

**Claude API** — pass the server as an MCP connector alongside a toolset entry:

```python
client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=4096,
    betas=["mcp-client-2025-11-20"],
    mcp_servers=[{"type": "url", "url": "https://<your-bot-host>/mcp", "name": "digitaldon"}],
    tools=[{"type": "mcp_toolset", "mcp_server_name": "digitaldon"}],
    messages=[{"role": "user", "content": "Is BONK worth a look right now?"}],
)
```

Both halves are required — the server entry alone is rejected.

**Claude Code, Cursor, and other MCP clients** — add the URL as a remote MCP
server in the client's config. The exact file differs per client; the value is
always just the `/mcp` URL.

**Agent frameworks** — any MCP client library takes the URL directly. If it also
supports x402, payment is automatic.

## Checking it works

MCP is JSON-RPC, so you can talk to it with `curl`:

```bash
curl -X POST https://<your-bot-host>/mcp \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

That lists both tools with their schemas and current prices. It's the fastest
way to confirm a deployment is live and see what it's charging.

## Why the summary is short

A tool result goes into the model's context, and context costs money — the
agent's, not yours. Handing back eight kilobytes of JSON on every call would
make each analysis expensive to *read* even when it's cheap to buy.

So the text the model sees is a tight summary: the verdict, the score, the
signals, the zones, the risk notes. The complete document travels beside it in
the structured field, where code can use it without the model paying to read it.

---

Analysis only. Not financial advice.
