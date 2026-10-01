# Reading the analysis card

The card is dense. Here's every part of it, top to bottom.

## The chart

A candlestick chart of the token, drawn to match the Web Analyzer's visual
language — hollow candles up, solid candles down, so direction survives even if
you're colourblind or the image gets compressed to mush.

On it:

* **Support and resistance** lines — the exact levels the trade plan uses.
* **Last price** marker.
* **A lifetime rail** down the right side: the token's entire all-time
  low → high range, with the plotted window highlighted inside it. This is how
  you tell "near the high" from "near the high *of the last three weeks*".

Two things the chart deliberately refuses to do:

* It **never calls the highest bar on screen the all-time high.** The window high
  is labelled with its window (`3W HIGH`). The real ATH is established
  separately; if it isn't available, the chart says nothing about the ATH rather
  than promoting a three-week high into one.
* It **never draws more candles than the frame has room for.** Hundreds of bars
  squeezed into a phone-width image is a smear that reads as noise, so candles
  are bucketed up to the coarsest resolution that stays legible. Highs and lows
  survive the aggregation, so nothing is lost.

Very young tokens are plotted on a finer resolution, because a coarse bar on a
two-day-old token is four data points.

## The score

```
Score: 72/100 — Strong buy signal
```

| Score | Verdict |
|---|---|
| 70–100 | 🟢 Strong buy signal |
| 55–69 | 🟡 Bullish, accumulation zone |
| 45–54 | ⚪ Neutral, wait and see |
| 30–44 | 🟠 Bearish, wait for better entry |
| 0–29 | 🔴 High risk, avoid for now |

The score is a *composite*, not a prediction. It answers "how many of the things
I check are currently pointing the same way", weighted by the token's age
profile. [What it means](../engine/score.md).

## The profile badge

🆕 **Fresh** (under 14 days) · 🌱 **Early** (14–60 days) · 🏛 **Established**
(60 days and up).

This isn't decoration. It changes what the score leans on: on a Fresh token,
flow and participation carry the weight and mean-reversion signals carry little,
because a five-day chart doesn't have a meaningful mean to revert to. On an
Established token it's the reverse. See [Token profiles](../engine/profiles.md).

## The two trade plans

```
Short-term (1 day)     entry $0.0000123 – $0.0000127   →  exit $0.0000151 – $0.0000157
Long-term (weeks)      entry $0.0000116 – $0.0000127   →  exit $0.0000188 – $0.0000242
```

* **Short-term** works off the recent swing structure — the last few days of
  trading, nothing older.
* **Long-term** works off the full higher-timeframe chart, and targets the actual
  resistance ladder overhead (levels price has genuinely reacted to), not a
  made-up fraction of the all-time high.

There are hard invariants: the long-term entry is never quoted *above* the
short-term entry, and the long-term exit is never *below* the short-term one. A
long-term holder should never be told to pay more and take less.

If the short-term structure is too flat to trade, the card says so explicitly
instead of quoting a plan that can't be executed:

```
No short-term setup — 1.8% range, not worth the fees.
```

More: [Entry & exit zones](../engine/zones.md).

## The category read

Four one-line verdicts, each with a colour dot:

| Category | Reads |
|---|---|
| **Momentum** | Whether the token is stretched — oversold / neutral / overbought |
| **Trend** | Short-term and long-term direction, stated separately when they disagree |
| **Structure** | The detected chart pattern (double bottom, ascending triangle, head & shoulders, …) |
| **Volume** | Recent volume against the longer average, as a percentage |

This is the part to read if you only read one part. It's the same evidence the
score is built from, in words.

## On-chain sentiment

Liquidity vs market cap, FDV vs market cap, buy/sell split. Independent of the
chart — a token can score 80 on technicals and still be uninvestable because
liquidity is 0.4% of market cap. See [On-chain sentiment](../engine/onchain.md).

## Data quality

```
187 candles
84 candles — limited data
```

When the chart history is thin, the card says so, and below a certain floor it
doesn't analyse at all. Treat "limited data" as "the levels below are a first
guess".

## The flags worth stopping for

* **⛔ HONEYPOT** — sells are blocked. Nothing else on the card matters.
* **🛑 Critical liquidity** — liquidity is a rounding error next to the market
  cap. Rug and manipulation territory.
* **Launch spike ATH** — the all-time high was set in the first hours and never
  revisited. Any "% below ATH" number is measuring against a candle that existed
  for ten minutes.
