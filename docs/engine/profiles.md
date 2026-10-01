# Token profiles

A five-day-old token and a two-year-old token are not the same kind of object,
and analysing them the same way produces confident nonsense on at least one of
them.

So the analysis picks a profile, and the profile decides what matters.

| Profile | Selected by | What it leans on |
|---|---|---|
| 🆕 **Fresh** | under 14 days old | Volume and buy/sell pressure |
| 🌱 **Early** | 14–60 days old | Trend plus momentum |
| 🏛 **Established** | 60 days and up | The full indicator suite |
| 📈 **Tokenized equity** | being a [tokenized stock](../start/stocks.md) | Trend and the moving-average stack |

Unknown age is treated as Established — the conservative default, since it avoids
applying memecoin assumptions to something that might be a blue chip.

The first three are age bands. The fourth is not: it is chosen by **what the
token is**, and it wins over age. That distinction is the whole point of it —
see below.

## Why the emphasis differs

On a **Fresh** token, a mean-reversion indicator is measuring the mean of about
four days of trading, most of which was a launch. That mean has no authority.
What *does* have authority is whether volume is still growing and whether buys
outnumber sells — is anyone actually still here.

On an **Established** token, the reverse. There's real history, so the
oscillators mean something, the moving-average stack means something, and the
trend has been tested. Volume trend becomes noise on a mature chart and is
weighted accordingly.

**Early** sits between them, because a three-week-old token is neither.

A **tokenized equity** is a different question again. Robinhood minted its stock
tokens months ago, but the companies behind them have traded for decades, so
scoring them by pool age put Apple in *Early* — where the engine throws away the
first day of candles as a launch and treats DEX swap counts as sentiment. No age
threshold fixes that, because age was never the variable that mattered.

The equity profile keeps every price-derived indicator at its Established weight
and nearly mutes the two that come from the DEX. A few hundred swaps a day is a
rounding error against the billions the same share turns over on its home
exchange, and on a thin listing it would otherwise let a handful of trades speak
for Apple. Trend and the moving-average stack take that weight instead: they are
what equity traders read, and unlike a swap count they are computed from the
price arbitrage keeps honest.

The weighting is also **asymmetric**: on a young token, growing volume is genuine
information while a quiet hour is mostly noise, so the same signal is allowed to
help the score more than it's allowed to hurt it. That asymmetry runs through the
whole table, in both directions depending on the signal.

## Stripping launch candles

The other thing the profile controls is how much of the launch gets thrown away
before anything is measured — a longer window for the youngest tokens, a shorter
one for Early, nothing at all for Established or a tokenized equity.

Why: launch price action is a vertical line into a peak nobody will see again,
followed by a cliff. Left in, it becomes the "resistance" every level is measured
against, it drags every moving average, and it makes "−96% from ATH" look like a
discount when it's just the shape of a launch.

A tokenized equity is exempt for a different reason than Established: it has no
launch to strip. Its first on-chain candles are an ordinary trading day for a
company an exchange was already pricing, so trimming them would delete real
history and manufacture a spike that never happened. For the same reason the
launch-spike flag below never fires on one.

**Safety valve:** if trimming would leave too little chart to analyse, the
untrimmed frame is used instead. Better a noisy chart than no chart.

## The launch-spike flag

Trimming fixes the *analysis*, but the all-time high is still an interesting
fact — and a misleading one when it was set in the first hour.

So the trimmed chart's high is compared against the untrimmed one. If the real
peak lives entirely inside the launch window, the ATH was an artifact, and the
card flags it.

Practical read: when that flag is up, ignore every "% below ATH" number on the
card. It's measuring against a candle that existed for ten minutes and never
recurred.

{% hint style="info" %}
The chart image has its own version of this discipline. It labels the highest bar
on screen with the window it came from (`3W HIGH`) and only calls something an
ATH when a real lifetime high was established separately. If that isn't
available, it says nothing about the ATH at all.
{% endhint %}
