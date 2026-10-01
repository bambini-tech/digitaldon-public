---
description: From zero to a working bot, in a DM and in your group.
---

# Setting it up

There is no account, no sign-up, no wallet connect and no configuration file.
Setup is opening a chat, and — if you want it in a group — tapping a few
switches once.

## 1. Start it in a DM

Open [@DigitalDonAnalyzeBot](https://t.me/DigitalDonAnalyzeBot) and hit
**Start**, or send `/start`.

You get a short welcome, an example, and an **➕ Add me to a group** button.
That's the whole onboarding.

## 2. Scan something

```
/don BONK
```

Ticker, name or contract address — all three work. A few seconds later you get
a chart image and the analysis card.

{% hint style="info" %}
**In a private chat you can skip the command entirely.** Paste a contract
address or a ticker on its own and the bot analyses it. `/don` is only strictly
required in groups, where the bot has to know the message is meant for it.
{% endhint %}

Under the card there are two optional buttons — **📣 Social Sentiment** and
**👥 Holder Analysis**. They only run when you tap them, because each one costs
real upstream budget. See
[Holder analysis](holder-analysis.md) and [Social sentiment](social-sentiment.md).

## 3. Add it to a group

Tap **➕ Add me to a group** from `/start`, or add
[@DigitalDonAnalyzeBot](https://t.me/DigitalDonAnalyzeBot) the normal Telegram
way.

The moment it joins, it **posts a setup card by itself**. No command needed, at
any point.

The card is a short explainer plus a checklist:

* ✅ added to the group
* ✅ admin rights — with a `🔄 Check admin rights` button while that one is
  still open

Then one tap per switch.

{% hint style="warning" %}
**Why it asks for admin rights.** Under Telegram's privacy mode, a bot that
isn't an admin never receives ordinary group messages — only commands aimed
directly at it. Auto-scan literally cannot see a pasted address without admin.
That's a Telegram rule, not a permission grab; the bot doesn't act on anything
but messages containing a contract address.

Without admin, `/don` and the other commands still work perfectly. You just
lose auto-scan.
{% endhint %}

## 4. The three group switches

| Setting | Default | What it does |
|---|---|---|
| 🔍 **Auto-scan** | on | A contract address pasted in the group gets answered with a short card |
| 🃏 **PNL cards** | on | `/pnl <contract>` renders [call cards](pnl-cards.md) here |
| 🏆 **Leaderboard** | on | `/lb` renders the group's [caller leaderboard](leaderboard.md) here |

Every switch is admin-only. A non-admin tapping one is told so and nothing
changes.

Auto-scan answers only tokens with enough chart history for a real analysis;
[fresh launches](groups.md#fresh-launches-are-not-auto-scanned) are passed over,
and that is not a group setting — it's reserved for the bot owner, because all
groups draw on one shared API budget.

## 5. Done

Once you're finished, the card collapses to a single **⚙️ Settings** button so
it isn't taking up space in the chat forever.

Admins can reopen it any time with `/setup`. If you prefer typing,
`/autoscan on|off` still works.

## What "off" actually means

Every switch is genuinely off, not "off with a notice". A group that turns PNL
cards off doesn't get an explanation when someone runs `/pnl` — that explanation
would be exactly the bot output the admin just declined. Same for the
leaderboard, same for auto-scan.

The one thing no switch touches: **`/don` always answers.** The settings govern
what the bot says on its own initiative, never what it does when it's asked
directly.

## Where to go next

* [Command reference](commands.md) — everything you can type
* [Adding it to a group](groups.md) — how auto-scan behaves day to day
* [Analyzing a token](telegram.md) — the `/don` flow in detail
