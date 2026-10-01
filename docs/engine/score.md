# How the score works

The score is a weighted vote. A set of independent signals each cast a vote for
or against, the votes get weighted by the token's [profile](profiles.md), and the
result is normalised to 0–100.

That's the whole idea.

## What votes

Each signal is computed independently, on its own evidence, and then normalised
onto a common scale so they can be combined. They fall into five families:

| Family | Asks |
|---|---|
| **Momentum** | Is the token stretched — has it run too far, or been sold too hard? |
| **Trend** | Which way is it actually going, on the week and on the day? |
| **Structure** | Does the chart's shape mean anything — a base, a breakout setup, a topping pattern? |
| **Volume** | Is participation growing or draining relative to its own recent history? |
| **Flow** | Are real transactions leaning to the buy side or the sell side? |

Which of these carries the most weight depends on the token's age profile — see
[Token profiles](profiles.md). The specific indicators, their thresholds and the
weight table are the part that makes this analysis different from a stack of
defaults, and they aren't published.

**A signal that doesn't have enough history is left out entirely** — not
defaulted to zero. Dropping it is honest; including a neutral vote it never
earned isn't.

## Reading the result

| Score | Verdict |
|---|---|
| 70–100 | 🟢 Strong buy signal |
| 55–69 | 🟡 Bullish, accumulation zone |
| 45–54 | ⚪ Neutral, wait and see |
| 30–44 | 🟠 Bearish, wait for better entry |
| 0–29 | 🔴 High risk, avoid for now |

## Two things worth internalising

**A token with no signals at all scores around 50, not 0.** The normalisation
maps "everything neutral" to the midpoint. A 50 means *no opinion*, not *bad* —
and a token with too little history for most signals lands near the middle by
construction.

**Thin data can't produce an extreme score.** The scale a token is measured
against is fixed by its profile, not by how many signals happened to fire. So a
token where only a handful could be computed gets pulled toward the middle and
can't reach 100. That's intentional: thin evidence should produce a hedged
verdict, not a confident one.

## What the score is not

It's a *composite*, not a prediction, and it's deliberately hard to move with any
single indicator. Any one indicator you follow will disagree with it regularly —
that's the point of a composite.

{% hint style="warning" %}
The score is a **technical** verdict. It does not know about the token's
liquidity, its unlock schedule, or the fact that 40% of supply sits in six
wallets funded by the same address. That's what
[on-chain sentiment](onchain.md) and
[holder analysis](../using/holder-analysis.md) are for — and it's why an 80 on a
token with critical liquidity is not an 80.
{% endhint %}

## One exception: our own token

`$DON` is analysed by the same engine as everything else, and then two declared
adjustments are applied on top of the finished result:

* the score is lifted by **8 points** and never printed below **50**, so the
  verdict on our own token never reads worse than *Neutral, wait and see*;
* the **short-term (1d) plan is withheld** — only the long-term zones are
  quoted. A tight scalp range on the token whose own holders are reading the
  card is an instruction to sell it, and we would rather not publish one.

Everything else — every indicator, every category, the long-term entry and
target zones — is computed exactly as it is for any other token.

Wherever those adjustments apply, the card says so: the Telegram card, the Web
Analyzer, the embeddable widget and the scan image all carry an **our token ·
house view** badge next to the score, and the API returns the same thing as
data (`analysis.native`). The number is ours to lean on; hiding that we lean on
it is not.
