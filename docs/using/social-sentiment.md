# Social sentiment

The **📣 Social Sentiment** button in Telegram, the **x intelligence** panel in
the Web Analyzer. It looks at the project's X (Twitter) account and scores it
0–100.

The question it answers isn't "is this bullish". It's "does this project's social
presence look like a real project, or like something that was set up last
Tuesday".

## The four dimensions

Each worth 0–25, summing to 100.

### Content (0–25)

Reads the recent posts and classifies each one — technical, announcement,
community, hype, or shill — then scores the mix.

Substance scores up: build updates, releases, actual information. Noise scores
down, and the tells that come with it are picked up too — posts that are all
volume and no content, filler, phrasing that reads as machine-generated.

A feed that's 80% rocket emojis and "LFG" is not the same as a feed with build
updates, and this dimension is where that shows up.

### Activity (0–25)

Is anyone home? Posting cadence, how recently the last post went out, and whether
the pattern is consistent or a burst followed by silence.

Silent for weeks scores badly. So does *only* posting in bursts — that's a
campaign, not a project.

### Engagement (0–25)

Replies, likes and reposts relative to follower count. The key ratio is
views-to-followers: an account with 50,000 followers and 200 views a post has
bought them, and the number is unambiguous about it.

Engagement that's all reposts and no original conversation is penalised too.

### Trust (0–25)

The account itself. Account age is the big input — a two-week-old account with
100K followers is telling you something. Also: verification, the
follower/following relationship, how much of the feed is original, and whether
the profile has the general shape of a throwaway.

## Reading the result

The card gives you the total, the four sub-scores with a coloured dot and a plain
word each, the account age tier, follower stats, and any warnings that tripped.

{% hint style="info" %}
Treat this as a **filter, not a signal**. A high score doesn't mean buy — plenty
of well-run projects go to zero. A low score means the social footprint doesn't
support the market cap, which is worth knowing before you size a position.
{% endhint %}

## Practical notes

* Results are **cached per handle** for a while. Hammering the button won't get
  you fresher numbers.
* It reads a window of **recent** posts. This is a snapshot, not an archive.
* It reads only the public profile the token links to. If a token has no X
  account attached, there's nothing to score.
* If the feature isn't available on this instance, the button and the panel
  simply don't exist, rather than appearing and failing.

Both surfaces produce the same result from the same analysis — the browser panel
isn't a separate implementation.
