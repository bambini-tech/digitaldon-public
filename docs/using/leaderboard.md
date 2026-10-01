# Leaderboard

```
/lb
```

Groups only. Ranks the group's callers by what their calls actually did.

## What counts as a call

Every `/don` scan in a group registers a **call** — the first scan of that token
in that chat, credited to whoever got there first. Later scans of the same token
never overwrite it, so the credit belongs to whoever actually called it, not
whoever scanned it most recently.

That's the same record the [PNL card](pnl-cards.md) is built from. The
leaderboard is that record, ranked.

You don't opt in and there's nothing to register. Scan a token first, and it's
your call.

## What's on the board

Three blocks, in this order.

### The group's numbers

```
🌐 Total Calls: 34  Callers: 9
🚀 Moons: 2x: 11 • 5x: 4 • 10x: 1
💀 Flops: 6
📈 Avg Gain: +212%  Median: 1.4x
🎯 Hit Rate: 44% ≥2x
```

The part that gets screenshotted. It's a claim about the *group*, it's the same
five lines every day, and it compares against yesterday without anyone having to
read a ranking.

Moon counts are **cumulative, not buckets** — a 6x is counted in both the 2x and
the 5x line. "How many calls did at least Nx" is the question people actually ask
of a board.

### MVPs

The top three callers, with their call count, their single best call, and their
points.

Three names, deliberately. A board where everyone appears has no MVPs.

### Calls

The best individual calls in the timeframe — the multiple, the ticker, who
called it, and the market cap move (`$180K → $2.1M`). Everything beyond the top
few is summarised as a count, so the message stays readable in a chat.

## Timeframes

Five, as buttons under the board and as arguments:

| Button | Command | Window |
|---|---|---|
| **1D** | `/lb` or `/lb 1d` | Last 24 hours (default) |
| **1W** | `/lb 1w` | Last 7 days |
| **2W** | `/lb 2w` | Last 14 days |
| **1M** | `/lb 1m` | Last 30 days |
| **All** | `/lb all` | All time |

Tapping a button **re-renders the same message** rather than posting a new one,
so a group's chat doesn't fill with boards no matter how much the filters get
tapped. It also means an old board sitting in the scrollback stays usable
forever — the buttons carry only a timeframe, so there's no session to expire.

## How calls are scored

**On the peak multiple since the call** — the same number the PNL card shows,
and for the same reason. A caller is judged on what the token did *after* they
called it, not on where it happens to trade at the moment somebody opens the
board. A call that ran 8x and round-tripped was still a good call, and a
scoreboard that forgets it by the next morning is measuring the timing of the
viewer rather than the skill of the caller.

Ranking is by **points**, not by raw multiple and not by call count:

* Ranking by average multiple hands first place to whoever called one lucky
  token once.
* Ranking by call count rewards spam.
* Points do neither. Each call earns a fixed amount for the tier its peak
  multiple reached, so a second good call always beats a single good call, while
  ten flat calls still add up to nothing.

The tiers are coarse on purpose — the difference between 11x and 14x is noise,
the difference between 1.5x and 5x is not. Nothing scores negative: the board is
a record of hits, and whoever calls a rug is already having a bad enough day.

Two definitions used in the headline stats:

| Term | Means |
|---|---|
| **Hit** | The call reached at least 2x |
| **Flop** | The call never got above where it was called |

The gap between them is deliberate. A call that went nowhere in particular is
neither, and labelling it either would overstate what the number knows.

Ties are broken by best single call, then by call count, then by name — so two
views of the same data always come out in the same order.

## "Still pricing"

The first board in a group takes a moment. Peak prices are refreshed in bounded
batches rather than all at once, so a board can honestly be incomplete on its
first view — and when it is, it says so:

```
⏳ 4 calls still pricing — tap a filter again in a moment.
```

Tap any filter again a few seconds later and it's filled in. A partial board
never pretends to be a complete one.

## Turning it off

The 🏆 **Leaderboard** switch in the group setup card. Admins only, on by
default. See [Setting it up](setup.md).

With it off, `/lb` stays silent in that group — an explanation would be exactly
the bot output the admin declined.

Run outside a group, `/lb` tells you it's a group feature. In a private chat
there's nobody to rank.
