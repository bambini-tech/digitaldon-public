# Quickstart

Three surfaces, same brain. Pick whichever is closer to hand.

## In Telegram

1. Open [@DigitalDonAnalyzeBot](https://t.me/DigitalDonAnalyzeBot) and hit
   **Start**.
2. Send `/don` plus whatever you've got:

```
/don BONK
/don wif
/don EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v
/don 0x4200000000000000000000000000000000000006
```

Ticker, name, or contract address — all work. If the ticker matches tokens on
more than one chain, you get a small picker instead of a guess.

A few seconds later you get a chart image plus the analysis card. Under it, two
optional buttons: **📣 Social Sentiment** and **👥 Holder Analysis**. They cost
real budget to run, so they only go when you tap them.

That's the whole onboarding. There is no account, no wallet connect, no sign-up.

{% hint style="info" %}
In a private chat you can skip `/don` entirely — paste a contract or a ticker on
its own and it analyses it.
{% endhint %}

## In the browser

Go to the [Web Analyzer](https://analyzer.digitaldon.net), paste the same thing,
hit **analyze**.

The web version renders the chart interactively and adds a **bubble map** for
holder analysis — clusters of connected wallets drawn as bubbles you can zoom
into and export.

You can also deep-link straight into a result:

```
https://analyzer.digitaldon.net/?q=BONK
https://analyzer.digitaldon.net/?q=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v
```

Handy for pasting a pre-loaded analysis into a chat.

## On X

Tag [**@DigitalDon_Scan**](https://x.com/DigitalDon_Scan) in a post with a
contract address and it replies with a scan card. It is most useful as a reply
under someone else's call — the thread gets an independent read on the token
without leaving it:

```
looks dope, let's check for a good entry.. @DigitalDon_Scan 7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU
```

Write whatever you like around the tag; the bot finds its handle and the
contract and ignores the rest. No contract in the post, no card.

Details: [The X bot](../using/x-bot.md).

## In a group

Add the bot to a Telegram group and it introduces itself with a setup card — a
checklist and one tap per switch. No commands needed.

Once it's set up, anyone pasting a contract address into the chat gets a compact
card back automatically, with a **📊 TA Analysis** button for the whole thing and
a **👥 Holder Scan** button for the wallet-cluster check.
Your group also gets [PNL cards](../using/pnl-cards.md) and a
[leaderboard](../using/leaderboard.md) of who called what.

Walkthrough: [Setting it up](../using/setup.md).

## What now

* [digitaldon.net](https://digitaldon.net) — the project's home page
* [The X bot](../using/x-bot.md) — tagging it under a call, and what it will
  and won't answer
* [Command reference](../using/commands.md) — everything you can type
* [Reading the analysis card](../using/analysis-card.md) — the card is dense on
  purpose; this walks through every line of it
