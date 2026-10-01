# The X bot

[**@DigitalDon_Scan**](https://x.com/DigitalDon_Scan) is DigitalDon on X. Tag it
under any post with a contract address and it replies with a scan card.

```
@DigitalDon_Scan 7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU
```

It works anywhere on X — most usefully as a **reply under someone else's call**,
so the people reading that thread get an independent read on the token without
leaving it. The bot answers your reply; the original post is untouched.

## Write it like a person

You do not have to post a bare command. Anything you write around the tag is
fine — the bot looks for its handle and a contract address anywhere in the post
and ignores the rest:

```
looks dope, let's check for a good entry.. @DigitalDon_Scan 7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU
@DigitalDon_Scan is this one actually tradable? 0x4200000000000000000000000000000000000006
@DigitalDon_Scan wen entry https://dexscreener.com/solana/7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU
ser scan pls @DigitalDon_Scan
```

The first three get a card — a DexScreener or Birdeye **token** page counts as
the contract, because the address is right there in the URL. The fourth gets
nothing: no address, no card.

Say something. A reply that is nothing but a handle and a 44-character string
reads like you are shilling a random address; a line of context tells the thread
what the card underneath it is.

## What comes back

A monochrome card, sized for X, carrying the same numbers the Telegram card
shows:

* token, chain, DEX and age
* price, market cap, liquidity, 24h volume
* the TA score out of 100, drawn as a gauge, and the one-line read
* where the price sits right now relative to the entry zone
* both trade horizons as plain labelled rows — entry zone, target zone and the
  estimated upside
* the token's own recent price action as a chart — real hourly candles from the
  same fetch the analysis runs on, so it costs no extra request. Swappable for
  another graphic with `X_CARD_STYLE`
* the analyzer link, so anyone can rerun the scan themselves

The card is rendered at three times X's display size. X re-encodes uploads to
JPEG, so a card built at display size arrives softened — and X keeps a full-size
variant up to 4096px for readers who tap the image, which is exactly when
somebody is trying to read the zones. 3x is sharp in the timeline and still
native when opened.

A token too young to have a chart gets a different card rather than an empty
one: the on-chain read (liquidity ratio, unlock overhang, buy/sell pressure)
takes the place of the score and the zones, because "is this a rug" is the
question a token with no chart actually raises.

The reply text is a short summary of the same thing. **The link lives on the
card, not in the post** — X charges roughly thirteen times as much for a post
containing a URL, so putting it in the image is what makes answering a few
thousand mentions a month affordable instead of a few hundred.

## What it will and won't answer

It answers a post that **tags it and contains a contract address** — Solana or
any supported EVM chain, either as a bare address or inside a DexScreener or
Birdeye link you pasted.

It stays quiet otherwise:

* **No contract, no card.** Tagging it to say hello gets nothing back.
* **One card per token per thread.** Asking about the same token again in the
  same conversation within the hour doesn't produce a second reply — the first
  one is a few posts up.
* **One answer per account at a time.** There's a short cooldown per person, so
  one enthusiastic user can't monopolise the bot.
* **Accounts created in the last day are skipped.** That is the pattern an
  account spun up for a single blast produces. There is no follower requirement
  — a scanner's audience is very often the small, new account, and turning those
  away is the opposite of the point.
* **It never replies to the original post.** Only to the post that tagged it.
  X's rules allow an automated reply only where it was summoned, and that is
  the behaviour we want anyway — nobody asked us to interrupt the thread.

If the token can't be found, or has no usable market data, you get silence
rather than an error. An unsolicited "❌ not found" under someone else's post is
exactly the behaviour that makes reply bots unwelcome.

## Tone

The card never grades the token in a word. It reports a **TA score**, a
technical reading of the current candles, and says whether the price is
**below, at or above** the entry zone — both facts about a chart at a moment,
neither a judgement of a project.

That is deliberate, and it is not squeamishness. The bot answers underneath
somebody else's post. A large "WEAK" there is read as a verdict on the person
who called it, and it adds nothing the score beside it has not already said —
maximum prominence, no extra information, and it turns the accounts whose
threads carry the bot into people who would rather it went away.

Nothing is softened: the score, the read and both zones are unchanged, and a
token with no tradable setup still says so. `X_CARD_VERDICT=grade` restores the
old STRONG / MIXED / WEAK wording for anyone who wants it.

## Where the numbers come from

The same analysis engine as everything else — `/don` in Telegram, the group
short card and the [Web Analyzer](web-analyzer.md) all run the identical
scoring, the identical zones and the identical on-chain read. A token scanned on
X and in Telegram in the same minute gives the same answer, because it is
literally the same computed result.

See [How the score works](../engine/score.md) and
[Entry & exit zones](../engine/zones.md) for what the numbers mean, and
[Reading the analysis card](analysis-card.md) for how to read them.

## For operators

The feature is off by default and needs both a switch and credentials:

| Variable | What it does |
| --- | --- |
| `FEATURE_X_MENTIONS` | The switch. Off by default. |
| `X_API_KEY`, `X_API_SECRET` | The X app's consumer credentials. |
| `X_ACCESS_TOKEN`, `X_ACCESS_TOKEN_SECRET` | The bot account's access token. Needs **Read and write**. |
| `X_MONTHLY_BUDGET_USD` | Hard monthly ceiling. Default `20`. |
| `X_DAILY_BUDGET_USD` | Runaway brake on top of it. Defaults to a fifteenth of the month. |
| `X_POLL_INTERVAL_SEC` | How often to check for mentions. Default `60`. |
| `X_MIN_AUTHOR_AGE_DAYS` | Minimum age of the tagging account. Default `1`; `0` disables. |
| `X_MIN_AUTHOR_FOLLOWERS` | Minimum followers. Default `0`, i.e. off. |
| `X_CARD_STYLE` | The graphic beside the zones: `chart` (default), `meter`, `pressure`, `dials` or `blueprint`. |
| `X_CARD_VERDICT` | The word under the score: `state` (default), `grade` or `off`. |

Nothing is spent without passing the budget ledger first, and the ledger fails
closed — if it can't prove there is budget left, nothing is sent. Spend shows up
in `/apistatus` in dollars, with a projection of where the month ends at the
current rate, and X-sourced scans are counted separately in `/stats`.

The account itself should carry X's **Automated** label and name a managing
account, which is a setting on the profile rather than anything in the bot.
