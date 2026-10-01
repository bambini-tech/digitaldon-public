# Command reference

Everything you can type at the bot. Eight commands, and you'll use one of them
95% of the time.

| Command | Where | What it does |
|---|---|---|
| `/start` | anywhere | Welcome message, a quick example, and an **➕ Add me to a group** button |
| `/help` | anywhere | This reference, inside Telegram |
| `/don <token>` | anywhere | **The main event.** Analyse a token by ticker, name or contract address |
| `/stocks` | anywhere | The tokenized-stock catalogue: xStocks and Robinhood listings, tap one to analyse it |
| `/pnl <contract>` | groups | Call card: the group's first scan of a token vs. its peak since |
| `/lb` | groups | Leaderboard: the group's best callers over 1D / 1W / 2W / 1M / all time |
| `/setup` | groups | Reopen the group settings card. **Admins only** |
| `/autoscan on\|off` | groups | Set auto-scan without opening the menu. **Admins only** |

`/leaderboard` works as a full-length alias for `/lb`.

---

## `/don <token>`

```
/don BONK
/don dogwifhat
/don EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v
/don 0x4200000000000000000000000000000000000006
```

Accepts a ticker, a project name, or a contract address on any
[supported chain](../start/chains.md). If a ticker matches tokens on more than
one chain you get a picker rather than a guess.

A stock ticker resolves to its official tokenized listings first — see
[Tokenized stocks](../start/stocks.md).

Returns a chart image plus the full analysis card — score, both trade plans, the
category reads, on-chain sentiment. Full walkthrough:
[Reading the analysis card](analysis-card.md).

Under the card, two optional buttons: **📣 Social Sentiment** and
**👥 Holder Analysis**.

{% hint style="info" %}
**In a private chat, `/don` is optional.** Paste a contract or ticker on its own
and you get the same card. In groups the command is required — otherwise the bot
would have to answer every message in the chat.
{% endhint %}

## `/pnl <contract>`

Groups only. Renders a shareable card showing the group's **first** scan of that
token versus its peak since — receipts for who called it and what it did.

Full detail: [PNL cards](pnl-cards.md).

Requires the 🃏 **PNL cards** switch to be on. If an admin has turned it off, the
command stays silent.

## `/lb`

Groups only. Ranks the group's callers by how their calls actually performed.

```
/lb          → last 24 hours (default)
/lb 1w       → last 7 days
/lb 2w       → last 14 days
/lb 1m       → last 30 days
/lb all      → all time
```

The same five timeframes are available as buttons under the board, which is the
easier path — tapping one re-renders the board in place instead of posting a new
message.

Full detail: [Leaderboard](leaderboard.md).

Requires the 🏆 **Leaderboard** switch to be on.

## `/setup`

Admins only, groups only. Reopens the settings card — the same one the bot posts
when it joins. Three switches, one tap each. See [Setting it up](setup.md).

Run in a private chat, it tells you it's a group command.

## `/autoscan on|off`

Admins only, groups only. The typed equivalent of the auto-scan switch:

| Argument | Effect |
|---|---|
| `on` | Answer pasted contracts with a short card — the default for a new group |
| `off` | Never answer a pasted contract |

Either way, tokens too young to have a chart are
[passed over](groups.md#fresh-launches-are-not-auto-scanned); that is not a
group setting.

## `/help`

Prints the command list inside Telegram. It only advertises what's actually
reachable — if an optional feature is switched off on this instance, its command
and button aren't listed.

---

## Commands you won't see

A handful of additional commands exist for whoever operates the bot instance.
They're restricted to the operator, they aren't listed in `/help` for anyone
else, and they aren't documented here. Running one as a normal user gets you
nothing useful.
