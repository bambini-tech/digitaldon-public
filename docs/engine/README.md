---
description: What the analysis actually does, and what it refuses to do.
---

# How the analysis works — overview

This section explains what goes into a card and why, at the level you need to
read one properly and know when to distrust it.

It does **not** publish the recipe — the thresholds, weights and calibration
behind the numbers are the product, and they stay in the product.

## The pipeline

1. **Resolve the token.** A ticker, a name or an address is matched to a real
   trading pair across every active chain. That pair supplies price, liquidity,
   market cap, FDV, the 24h buy/sell split, the pool's age and the project's
   social links. A ticker matching several chains gets you a picker, not a guess.

2. **Pull the chart.** Two timeframes — a short one and a long one — so the
   analysis can separate "what happened this week" from "what's been happening
   for months". Below a floor of usable history, analysis stops here and the card
   says so.

3. **Pick a profile.** Token age decides: **Fresh**, **Early** or
   **Established**. This changes what the rest of the run leans on. See
   [Token profiles](profiles.md).

4. **Clean the launch off the chart.** For young tokens, the opening stretch of
   trading is excluded before anything is measured. Launch price action is a
   vertical line followed by a cliff, and leaving it in poisons every support
   level, every average and every "% below ATH" number downstream. If the token
   also set its all-time high in that window, the card flags it, so you don't
   read "−94% from ATH" as a discount.

5. **Compute the signals.** A set of independent readings spanning momentum,
   trend, chart structure, volume behaviour and transaction flow. Each one is
   normalised onto the same scale so they can be compared and combined.

6. **Weight them into a score.** Profile-specific weights, normalised to 0–100.
   The weighting is asymmetric — some signals are trusted more when they're
   warning than when they're blessing. [What the score means](score.md).

7. **Derive the trade zones.** A short-term plan from recent swing structure and
   a long-term plan from the higher-timeframe structure, then a set of invariants
   that keeps the two coherent with each other.
   [Entry & exit zones](zones.md).

8. **Read the chain data.** Liquidity ratio, FDV overhang, buy/sell pressure —
   computed independently of the chart, because a perfect setup on 0.4% liquidity
   isn't a setup. [On-chain sentiment](onchain.md).

9. **Render.** Telegram gets a chart image plus a formatted message; the Web
   Analyzer renders panels from the same result. The formatting differs. The
   numbers cannot.

## Design principles worth knowing

**One analysis, every surface.** Telegram and the browser don't run "similar"
logic — they produce the same numbers for the same token, and that's verified
automatically before any change to the analysis is allowed to ship. A tool whose
entire output is a verdict cannot afford two verdicts. The X bot doesn't add a
third implementation: it calls the same engine the Telegram bot does, and only
draws the result differently.

**Missing data is stated, never invented.** Every signal has a minimum amount of
history it needs to mean anything. If it isn't there, the signal is dropped from
the score rather than defaulted to neutral-and-counted. The card says "limited
data" instead of quietly producing confident numbers from a handful of candles.

**A number you can't act on is worse than no number.** This shows up in several
places: the short-term plan is suppressed entirely when there isn't a tradable
one, the chart refuses to call a three-week high an all-time high, and "no
short-term trade here" exists as an explicit message rather than an empty panel
that reads as a broken bot.

**Degrade, don't fail.** If an optional data source is unavailable or at its
ceiling, the affected part of the card comes back partial or absent. It doesn't
take the rest of the analysis down with it.
