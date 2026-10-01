# Entry & exit zones

The score says *whether*. The zones say *where*.

Every card carries two plans on different horizons, and they're built from
different data on purpose.

## Short-term (roughly a day)

Built from **recent swing structure** — the last few days of trading, nothing
older. Entry sits around the support that structure identifies; the target sits
around the resistance above it.

Both are **zones, not lines**. You're not trying to catch the exact tick, you're
defining a band where the setup is valid — which is also why a plan quoted to the
last decimal would be a false precision.

If there's no clean recent structure to work with, volatility bands stand in for
it, so the plan degrades rather than disappearing.

## Long-term (weeks)

Built from the full higher-timeframe chart.

**Entry** is anchored to the better of the structural support and the recent
short-term support. If the long-run structure sits *above* the recent dip, the
recent low is the better accumulation level — a long-term buyer shouldn't be
quoted a worse entry than someone trading the week.

**Exit is the resistance ladder.** This is the part that changed from the obvious
approach and shouldn't change back. Targets are **actual overhead resistance
levels** — prices where the chart has demonstrably reacted — not a fraction of
the all-time high.

* First resistance above current price → primary target
* Next one up → stretch target

Why: a fraction of a possibly-stale high is an arbitrary number that price has no
particular reason to respect. Structural levels offering comparable upside get
reached materially more often. Same upside on paper, meaningfully different odds
of getting there.

Special cases are handled explicitly rather than falling through:

* **Only one level overhead** → target it, with a bounded stretch above.
* **Nothing overhead at all** (price discovery) → the plan extends past the
  all-time high, because that's genuinely where the next resistance is.
* **Any structure overhead** → targets stay capped below the prior-high region.
  While there are levels to clear, don't aim past them.

## The invariants

Two plans on one card have to be coherent with each other, or the card is
nonsense. So after both are computed:

1. **The long-term entry never sits above the short-term entry.** Enforced in two
   independent places, because the padding on each plan could otherwise push it
   over on its own.
2. **The long-term exit never sits below the short-term exit, or below the
   current price.** If the resistance ladder produces a target under that floor,
   it gets lifted, and the stretch target with it.

Net effect: a long-term holder is never told to pay more and take less than
someone trading the same chart for a day.

## When there is no short-term trade

Sometimes there just isn't one, and the honest answer is to say so.

On a flat few days, support and resistance land almost on top of each other. The
padding that makes a zone a zone then **crosses them** — the card would say "buy
up to $X, sell below $X", which is not a plan, it's a typo with prices in it.
Slightly wider bands are no better: a couple of percent of range doesn't survive
slippage and fees.

Both cases are the same fact — *there is no short-term trade here* — so they get
the same answer:

```
No short-term setup — 1.8% range, not worth the fees.
```

Rather than rendering nothing (which reads as a broken bot) or rendering an
untradeable plan (which is worse).

**This isn't repaired by widening the zones.** Unlike the long-term case, there's
no higher structure to aim at. Any "fix" would be inventing a resistance the data
doesn't contain.

The long-term plan is usually still valid when this happens, and is still shown.

### The bar is lower for a tokenized stock

How much upside is "worth the fees" depends on what you're trading. A memecoin
routinely moves 30% in a day; Apple moving 3% is a news event. Applied to a
[tokenized stock](../start/stocks.md), the token bar answered *no tradable
range* on almost every stock on almost every day — the engine reporting its own
mis-calibration as a finding about the asset.

So an equity is quoted from about **1%** of upside instead, and its zones are
padded a few tenths of a percent around the measured levels rather than a few
percent — a $312 share doesn't need a $6 entry band.

The padding was the bigger problem. The token pads cost roughly two percentage
points of band, which is more than a large-cap's whole 72-hour band, so they
didn't just suppress the plan — they turned it upside down. Apple's 0.81% band
came out at *negative* 1.18% of upside.

What this doesn't do is turn blue chips into day traders. The nearest structure
around the current price on a tokenized large-cap is typically 0.3–1.2% wide,
and it doesn't widen if you look back further. So **no swing setup** is the
normal answer for most of them, most of the time — which is a fact about the
asset, not a failure of the tool. The position zones are always there, and the
line says so.

The two horizons are named for how they're actually held, too: **swing (days)**
and **position (weeks)**, rather than the token card's 1d and weeks.

## Related numbers on the card

* **% above chart low / % below chart high** — where price sits in the plotted
  window.
* **Range position** — the same thing as a 0–1 fraction. `0.1` near the low,
  `0.9` near the high.
* **Stretch flag** — set when the long-term stretch target is close to the
  all-time high. Means the upside quoted requires a genuine re-test of the prior
  high, not just a bounce.
