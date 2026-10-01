---
description: Paste a token. Skip the guesswork.
---

# Welcome to DigitalDon

DigitalDon takes a token — a ticker, a name, or a contract address — and gives
you back a straight answer: a chart, a score out of 100, where you'd buy, where
you'd take profit, and what's wrong with it.

No dashboards to configure. No 14 indicators to interpret yourself. One input,
one card.

There are four ways to use it:

| | What it is | Where |
|---|---|---|
| 🤖 **Telegram bot** | `/don <token>` in a DM or in your group | [@DigitalDonAnalyzeBot](https://t.me/DigitalDonAnalyzeBot) |
| 🌐 **Web Analyzer** | Same thing in a browser, nothing to install | [analyzer.digitaldon.net](https://analyzer.digitaldon.net) |
| 𝕏 **X bot** | Tag it under a call with the contract, get a card back | [@DigitalDon_Scan](https://x.com/DigitalDon_Scan) |
| 🧩 **Widget** | The card embedded on someone else's site, one script tag | [The Widget](using/widget.md) |

The project's home page — what DigitalDon is, in one screen — is
[digitaldon.net](https://digitaldon.net).

All four run the **exact same analysis**. Not "similar" — identical, down to the
integer, and that's checked automatically before any change ships.

## What you actually get

* **A candlestick chart** with the support and resistance the analysis used —
  so you can see where the numbers came from instead of trusting them blind.
* **A score, 0–100**, weighted differently depending on how old the token is. A
  three-day-old memecoin and a two-year-old blue chip do not deserve the same
  treatment.
* **Two trade plans** — a short-term one (days) and a long-term one (weeks),
  each with an entry zone and a take-profit zone.
* **On-chain reality check** — liquidity vs market cap, FDV overhang, buy/sell
  pressure. The stuff that decides whether the chart even matters.
* **Holder analysis** (optional) — who holds this, are their wallets connected,
  did the same funder pay for twelve of them ten minutes before launch.
* **Social sentiment** (optional) — is the project's X account real, or three
  weeks old with bought followers.

And in a group, on top of all that:

* **Auto-scan** — someone pastes a contract, the bot answers with a compact card.
* **PNL cards** — receipts for who called what, and what it did after.
* **Leaderboard** — the group's callers ranked by how their calls actually
  performed.

## Where to go next

* **Never used it?** → [Quickstart](start/quickstart.md)
* **Want it under a call on X?** → [The X bot](using/x-bot.md)
* **Setting it up properly?** → [Setting it up](using/setup.md)
* **Want every command?** → [Command reference](using/commands.md)
* **Got a card and want to read it properly?** → [Reading the analysis card](using/analysis-card.md)
* **Want to know what the score means?** → [How the score works](engine/score.md)
* **Putting it on your own site?** → [The Widget](using/widget.md)

{% hint style="warning" %}
None of this is financial advice. It's a tool that reads charts and chain data
faster than you can. It has no idea what's about to be announced on Twitter.
Always DYOR.
{% endhint %}
