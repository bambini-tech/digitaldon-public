# Analyzing a token

The `/don` flow, end to end.

## What you can paste

```
/don BONK
/don dogwifhat
/don EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v
/don 0x4200000000000000000000000000000000000006
```

Ticker, project name, or contract address. In a **private chat** you can drop
the command and paste the token on its own.

### When a ticker matches several chains

Plenty of tickers exist on more than one chain, and picking one for you would be
a guess presented as an answer. Instead you get a small picker listing each
match with its chain, price and liquidity — tap the one you meant.

Contract addresses skip this. An address resolves directly to its pair.

## What happens next

A status message appears and updates as it works: resolving the token, pulling
the chart, running the analysis. Then it's replaced by the result.

Typical round trip is a few seconds. Almost all of that is waiting on market
data, not on the analysis itself.

You get back:

* a **candlestick chart** with the support and resistance levels the trade plan
  is built on
* the **analysis card** — score, both trade plans, category reads, token stats,
  on-chain sentiment

Every line of it is explained in [Reading the analysis card](analysis-card.md).

## The two optional buttons

Under the card:

* **📣 Social Sentiment** → scores the project's X account. See
  [Social sentiment](social-sentiment.md).
* **👥 Holder Analysis** → who holds it, and which of those wallets are the same
  person. See [Holder analysis](holder-analysis.md).

They sit behind buttons rather than running automatically because each one costs
significantly more to produce than the chart analysis does. Running them on every
scan would burn the capacity that everyone's scans depend on.

Either can be switched off for the whole instance, in which case the button
simply isn't rendered rather than appearing and failing.

## When there isn't enough data

The bot doesn't invent numbers to fill a card.

* **Very new token, no usable chart** → you get a
  [fresh-launch card](../engine/onchain.md#fresh-launch-cards) instead: liquidity,
  unlock overhang, buy/sell pressure. No score, no zones, because there's nothing
  honest to compute them from.
* **Thin chart history** → the card is produced but marked *limited data*. Treat
  the levels on it as a first guess.
* **Older token, no chart at all** → the card says the data source failed rather
  than pretending the token is brand new.

## Rate limits

Scanning isn't free, and one person holding down `/don` can degrade the service
for everyone. So there are sliding windows:

| Window | Default |
|---|---|
| Per user, per minute | 3 |
| Per user, per hour | 20 |
| Per group chat, per minute | 8 |
| Per group chat, per hour | 120 |

A few things worth knowing:

* **DMs are exempt from the per-chat windows.** If a group is throttled, you can
  keep scanning privately.
* **A refused request doesn't cost you a slot.** All windows are checked before
  any of them is consumed.
* **The per-group hour cap bounds the sustained rate, not bursts.** A busy
  minute in an active group is fine; a chat running six hundred scans an hour is
  not.

{% hint style="info" %}
Scanning the same trending token as fifty other people in the same minute
doesn't cost fifty times as much — concurrent requests for the same token are
collapsed and everyone is served the same fresh result. Rate limits exist for
the pathological case, not the popular one.
{% endhint %}

## In groups

The bot needs admin rights to see pasted addresses at all — that's Telegram's
privacy mode, not a choice. `/don` works either way.

See [Adding it to a group](groups.md).
