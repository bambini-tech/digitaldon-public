# On-chain sentiment

The chart can look perfect on a token you can't get out of. This section is
computed entirely from pair data — no candles involved — and it's the part that
answers "is this thing even tradable".

## Liquidity vs market cap

How much is actually in the pool, relative to what the token claims to be worth.

| Liq / MCap | Verdict | |
|---|---|---|
| ≥ 10% | very healthy | ✅ |
| 5–10% | healthy | ✅ |
| 2–5% | low | ⚠️ *price impact on large trades will be high* |
| < 2% | **critical** | 🛑 *high rug / manipulation risk* |

This is the single most useful number on the card for anything small. A $2M
market cap with $18K of liquidity means the market cap is a story, not a price
you could realise.

## FDV vs market cap

Fully diluted valuation against circulating market cap — i.e. how much supply
hasn't hit the market yet.

| FDV / MCap | Verdict | |
|---|---|---|
| < 1.2× | fully circulating | ✅ |
| 1.2–2× | moderate unlock risk | ⚠️ |
| 2–5× | significant unlock overhang | ⚠️ *potential future sell pressure* |
| ≥ 5× | **extreme unlock risk** | ⚠️ *most supply still locked, heavy dilution* |

A 5× FDV ratio means that for every token trading, four are waiting. You're not
just betting on demand, you're betting on demand that outruns scheduled supply.

## Volume vs market cap

Also reported, with its own read:

| Vol / MCap | Label |
|---|---|
| > 1.0× | Very high — possible manipulation |
| 0.3–1.0× | High — strong interest |
| 0.05–0.3× | Normal |
| < 0.05× | Low — little activity |

Note the top band is a *warning*, not a compliment. Daily volume exceeding the
entire market cap usually means wash trading or a very small number of very busy
bots.

## Buy/sell pressure

The raw 24h split:

```
📊 1,284 buys / 743 sells — 63% buy pressure
```

Crude, but it's real transactions rather than sentiment, and it's one of the
signals feeding the [score](score.md).

## Fresh-launch cards

A token only a few days old usually has no usable chart history — the pool has
barely existed. Rather than returning "no data", the card flips to a pure
on-chain read: liquidity ratio, unlock overhang, buy/sell pressure. No score, no
zones.

Which is the right call, because at that age the question isn't "where's the
entry", it's "is this a rug".

Two details that make this trustworthy rather than convenient:

**Unknown age counts as not-fresh.** If the age can't be determined, the token
does *not* get a fresh-launch card. So a data outage degrades to the ordinary "no
data" message instead of labelling established tokens as new launches.

**No market cap is not the same as no verdict.** Very new tokens often have no
reported market cap, in which case the liquidity thresholds are re-run against
FDV and relabelled. Without that, the one card that most needs a liquidity
verdict would be the one silently missing it — and what's left reads misleadingly
bullish. If neither cap is known, the card states the absolute liquidity figure
rather than staying silent about liquidity altogether.
