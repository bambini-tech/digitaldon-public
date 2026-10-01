# FAQ

### Do I need to connect a wallet?

No. There's nothing to connect. The bot and the analyzer read public data and
give you a verdict — no wallet, no account, no signature.

### Do I have to type `/don` every time?

Not in a private chat. Paste a contract address or a ticker on its own and it
analyses it. In groups the command is required, otherwise the bot would have to
answer every message in the chat.

### Is the Telegram score the same as the browser score?

Yes, and not approximately. The two surfaces are checked against each other
automatically before any change to the analysis is allowed to ship — the score
has to match exactly. If they ever drift, the change doesn't merge.

### Does the X bot give the same score?

Yes — it is the same code. [@DigitalDon_Scan](https://x.com/DigitalDon_Scan)
runs the bot's own analysis engine, so a token scanned on X and in Telegram in
the same minute returns the identical computed result. Only the card layout
differs, because it has to be readable in a timeline.

### Why does this token score 50 with no signals?

Because 50 is *no opinion*, not *bad*. The score normalises "everything neutral"
to the midpoint. A token with too little history for most signals lands near the
middle by construction, and that's the honest answer.

### Why does the score not match my TradingView?

Most likely the launch candles. For young tokens the analysis drops the opening
stretch of trading before measuring anything, because launch price action poisons
every level downstream. Your chart still has it.

Also: this is a composite of many signals weighted by token age. Any single
indicator will disagree with it regularly — that's the point of a composite.

### It says "no short-term setup". Is it broken?

No, that's a deliberate message. When recent support and resistance sit within a
couple of percent of each other, any tradable zone around them crosses and you'd
get "buy up to $X, sell below $X" — a plan that can't be executed. Rather than
render nonsense or render nothing, the card says there's no short-term trade
here. The long-term plan is usually still valid.
[Details](engine/zones.md#when-there-is-no-short-term-trade).

### Why is my token showing "−94% from ATH" when it launched yesterday?

Check whether the card flagged a launch spike. If the all-time high was set in the
first hours and never revisited, every "% below ATH" number is measuring against a
candle that existed for ten minutes. The card marks this; the chart refuses to
call a window high an ATH at all.

### Why can't it find my token?

Three possible reasons: there's no discoverable trading pair for it (the most
common), the pool has no chart history yet, or it's on a chain that isn't active.
[Supported chains](start/chains.md).

### Why are holder analysis and social sentiment behind buttons?

Because they cost real money per run — a full holder scan is orders of magnitude
more work than reading a chart. Running them on every `/don` would exhaust the
budget everyone's scans depend on. On demand, cached, rate limited.

### The holder panel doesn't appear in the browser

Either it's switched off, or the page couldn't confirm it's available. The panel
fails closed by design: no confirmation means no panel, because a button that
produces an error is worse than a missing one.

### I got rate limited

Defaults are 3 scans a minute and 20 an hour per person, plus per-group ceilings.
The limits exist so one person holding down `/don` can't degrade the service for
everyone. Group chats have their own windows; DMs are exempt from those, so you
can keep scanning privately.

### Does the bot need to be an admin in my group?

Only for auto-scan. Under Telegram's privacy mode a bot that isn't an admin never
receives ordinary group messages, so it cannot see a pasted contract address —
that's a Telegram rule, not a permission grab. Every command, including `/don`,
works fine without admin.

### Someone pasted a contract and nothing happened

Most likely the token is too new to analyse: auto-scan
[skips fresh launches](using/groups.md#fresh-launches-are-not-auto-scanned), and
that isn't a group setting. Use `/don`, which always answers. Failing that: the
bot isn't an admin, auto-scan is off, or the group is rate limited.
[More](using/groups.md#when-auto-scan-stays-quiet).

### `/pnl` or `/lb` did nothing

An admin has switched that feature off for the group. It stays silent rather than
explaining itself, because the explanation would be exactly the bot output the
admin declined. Reopen `/setup` to turn it back on.

### Who gets credit for a call?

Whoever ran the first `/don` on that token in that group. Later scans never
overwrite it, so credit belongs to whoever actually called it — not whoever
scanned it most recently. [PNL cards](using/pnl-cards.md) ·
[Leaderboard](using/leaderboard.md).

### Can I get the raw data out?

The Web Analyzer's bubble map has **export png** and **export csv**, which covers
taking a holder set somewhere else. There's no public data API.

### Where do I report a security issue?

Privately, not in public. Contact the team directly rather than posting details
anywhere they can be read by whoever else finds them useful.

### Is it financial advice?

No. [At length](disclaimer.md).
