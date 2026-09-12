# Review Queue

> **Three drafts are still queued.** Benchmarking, Unicode normalization, and structured output
> are all sitting at `draft: true`. Two posts went live in September. Suggested order:
> benchmarking (most self-contained), Unicode normalization (strongest of the two token cost
> posts), then structured output.

## Shipped 2026-09-12: customer lifetime value post (Friday slot, a day late)

Review page: <https://claude.ai/code/artifact/e674582b-f7b1-426c-ab86-df796895ed97>

| | |
|---|---|
| Title | Customer Lifetime Value in R: A Third of Your Best Customers Have Already Left |
| Target query | customer lifetime value in r |
| Lane | Marketing and measurement, which was down to one post against three for AI |
| Status | **LIVE** at </post/customer-lifetime-value-in-r/> (`draft: false`, published 2026-09-12 on Mike's approval) |
| File | `content/post/2026-09-12-customer-lifetime-value-in-r/index.en.Rmd` |

**This is the first post on the site built on real third-party data rather than a simulation.**
CDNOW, 2,357 customers, 6,696 transactions, split into 39 weeks of history and 39 weeks of
holdout. Every comparison is against what customers actually did, not against a generated truth.

Rank customers by historical spend and take the top decile. Pareto/NBD flags 76 of those 236 as
probably inactive. Their median holdout spend is 0.00 against 130.45 for the rest of the same
decile, and 61% of them buy nothing at all against 21%. The mean gap is 3.08x, with a Python
bootstrap interval of 1.92 to 5.77 across 4,000 resamples.

The mechanism is shown in raw data before the model is invoked. Hold calibration purchase count
fixed and split on recency alone, and the recent half outspends the stale half by 1.48x to 2.63x.
No model is doing any work in that table.

### The three questions

1. **Is the claim right?** The ground truth is real customer behaviour, so the central claim is
   about as solid as this site gets. The judgment calls are scope, see below.
2. **Is the hook right?** It opens on the retention list itself being a third dead. That is the
   most concrete thing in the post.
3. **Ship, fix, or kill?**

### Known soft spots, in the order I would look at them

- **The post corrects its own headline mid-article, and you should decide whether that is
  strength or weakness.** The naive extrapolation overstates the holdout by 145%, but CDNOW is a
  cohort where every customer's acquisition purchase falls inside the calibration window and
  cannot fall inside the holdout. Stripping first purchases drops the overshoot to 35%. The post
  now runs that correction in its own section and tells the reader to use 35% as the honest
  number. I added this because 145% was the strongest fair attack available on the post, but it
  does mean the abstract and the body quote different figures by design.
- **The model undershoots the total by 16%.** The post says so in the same table that indicts the
  naive method, and again in "What this does not fix". A skeptic gets to say the fix is also
  wrong. The defence is that Pareto/NBD is a ranking and attrition tool rather than a forecast,
  which the post states, but confirm you are happy leading with a method that misses the level.
- **The ranking gain is genuinely small.** Targeting by model rather than by historical spend
  moves captured holdout revenue by about 5 points at the top 5% and under 1 point at the top
  20%. The post confronts this and reframes the value as knowing which names on the same list to
  stop spending on. That reframing is the main interpretive move in the post and is worth your
  eyes.
- **CDNOW is 1997 compact disc buyers.** One dataset, one category, one era. Stated plainly at the
  end. It is the standard public benchmark, which is the defence, but it is not your customers.
- **The 0.5 threshold on PAlive is a convention, not a result.** Nothing in the data picks it. The
  figure bins the full probability range precisely so the reader is not stuck with the cut point,
  and the effect is monotone in the median across bins.
- The figure plots mean and median together on purpose. The mean is not monotone across bins,
  because a few flagged customers did come back and the low-probability bins are small. The
  caption says this rather than quietly showing only the median.

Nothing in this post is unverified. Every R block executed, plus one executed `{python}` chunk.
Renders in about 10 seconds, the fastest post on the site, because Pareto/NBD fits in under a
second.

---

## Shipped 2026-09-08: synthetic respondents post (Tuesday slot)

Review page: <https://claude.ai/code/artifact/8acea528-6016-41f5-9145-321e7c2656c8>

| | |
|---|---|
| Title | Synthetic Respondents in Conjoint Analysis: The Average Survives, the Price Does Not |
| Target query | synthetic respondents conjoint analysis |
| Lane | AI and LLM engineering, crossed with marketing research. Lanes 3 and 4 were the underweighted ones |
| Freshness | Maier et al., arXiv 2510.08338, October 2025. 11 months old, clears the 24-month rule |
| Status | **LIVE** at </post/synthetic-respondents-conjoint-analysis/> (`draft: false`, published 2026-09-08 on Mike's approval) |
| File | `content/post/2026-09-08-synthetic-respondents-conjoint-analysis/index.en.Rmd` |

The literature says LLM respondent panels produce distributions that are too narrow. Nobody has
written down what that costs. This post holds mean price sensitivity fixed at exactly 0.050
across every panel while shrinking only the spread, runs both panels through the same mixed
logit and the same market simulator, and prices the difference.

The validation passes convincingly. Mean price sensitivity 0.0487 human against 0.0478
synthetic, feature part-worth 1.375 against 1.368, and the synthetic model predicts the human
holdout product share at 0.2472 against an actual 0.2478, which is *closer than the human
panel's own model* at 0.2545. On that evidence the panel gets signed off.

The decision then breaks. Optimal price 43.5 against a truth of 58.5, which is 26% low and 31%
below what the human panel recommends. Premium segment 14.0% against 34.1%. Market share at a
price of 125 is 28% of the truth, because high-price demand is made entirely of the
price-insensitive tail that compression removes.

Mechanism is shown rather than asserted: a sweep over the compression factor holds the mean
coefficient flat at 0.050 to four decimals across the whole range while optimal price falls to
71% of truth and the premium segment falls to essentially zero. That is the figure.

Python cross-check by 24-node three-dimensional Gauss-Hermite quadrature reproduced the R Monte
Carlo optimum at all five compression levels exactly, so the collapse is a property of the model
and not of the random draws.

### The three questions

1. **Is the claim right?** The arithmetic is solid and independently verified two ways. The
   judgment call is scope, see the first bullet below.
2. **Is the hook right?** It opens on the validation report checking exactly the numbers that
   survive the failure. That is the strongest sentence in the post.
3. **Ship, fix, or kill?**

### Known soft spots, in the order I would look at them

- **No language model was queried.** This is the one that decides the post. It takes the
  narrowness the literature documents, applies it as a compression factor, and prices the
  consequence. It is not new evidence that synthetic panels are narrow. The post says this
  outright in a section headed "What this post did not measure" rather than burying it, and it
  names the method built to fix the problem (semantic similarity rating) so the criticism is not
  a straw man. Confirm you are comfortable publishing a consequence study rather than a
  measurement study. Running real LLM respondents is possible but cannot be reproducible at
  render time, which is why it was not done.
- **The compression factor of 0.4 is my choice, and the headline 26% is one point on a curve.**
  The sweep is in the post precisely so the reader sees the whole range rather than a staged
  number, and the direction is monotone throughout. But the abstract quotes the single number.
  Decide whether the summary should quote a range instead.
- **Two premium-segment numbers appear and they differ.** The fitted table says 14.0% and the
  sweep at the same compression factor says 6.1%. Both are correct: the first uses parameters
  estimated from the synthetic panel, the second uses the true compressed parameters. Estimation
  noise inflated the fitted feature spread. A careful reader could read this as a contradiction,
  so it may be worth one clarifying sentence.
- **The money number is the weakest number in the post.** Contribution at the synthetic price is
  94.8% of the best available, so only about 5% of profit is lost. The post confronts this
  directly and argues the flatness of profit curves near their peak is exactly why a 26% price
  error survives undetected, and that segment sizing is the decision that really breaks. Check
  you find that argument convincing, because a skeptic will quote the 94.8%.
- **The human panel is also wrong**, at 63.5 against a truth of 58.5, purely from sampling noise
  at n = 300. It is visible in the table and the post does not hide it, but it is not discussed.
  The synthetic error is three times larger and systematic rather than noisy.
- **The estimator is given the correct functional form.** Truth is a mixed logit and the model
  fitted is the same mixed logit, so the post loses the price under the most favourable
  specification available. That is stated, and it strengthens rather than weakens the result.
- The variance-ratio diagnostic is honest about being weak. Ratios came back 0.34, 0.56, and
  0.01 against a true 0.40. The post now says explicitly it is a screen and not a rescaling
  factor, after an earlier draft called two of three "reasonable" when one was 40% off.

Nothing in this post is unverified. Every R block executed, plus one executed `{python}` chunk.
Renders in about 80 seconds.

---

## Awaiting review: benchmarking post, 2026-09-01 (Tuesday slot)

Review page: <https://claude.ai/code/artifact/7633ad35-91bf-49d8-b854-6973479d43d5>

| | |
|---|---|
| Title | How to Benchmark R Code Correctly: I Raced a Function Against an Identical Copy of Itself |
| Target query | how to benchmark r code correctly |
| Lane | Coding and tooling, the first one on the site. Lane 4 was empty and the last three log rows were AI, AI, marketing |
| Status | **DRAFT** (`draft: true`), rendered, not live |
| File | `content/post/2026-09-01-how-to-benchmark-r-code-correctly/index.en.Rmd` |

Two byte-identical functions, raced against each other, with the listing order swapped as the
control. Under the block ordering `bench::mark` uses (`a a a a b b b b`, verified by instrumenting
the expressions to log themselves) the first-listed slot is measured as 10.3% off in the knit
session and 98% of races land the same way. Under `microbenchmark`'s default random ordering the
same comparison returns a clean null, every time, in every session tested.

The mechanism is measured rather than asserted: timing one expression alone with no competitor
shows position structure across the run: garbage-collection spikes every 29 calls or so, on a
baseline that drifts on its own. Block ordering charges the first half of both to one expression
and the second half to the other, and the effect survives whether the run is summarised with a
median or a mean. Randomizing breaks the alias.

The practical half is a negative control. Put a second copy of one candidate in the benchmark under
a different name, and the gap it reports against its own twin is your resolution limit for that
machine on that day. In the post's real comparison (`2 * x` against `x + x`) the control was off by
more than the effect, which is the whole argument for including it.

Python chunk reproduces the design flaw with `numpy` and `time.perf_counter_ns`, where the symptom
is variance rather than bias.

### The three questions

1. **Is the claim right?** The measurement is solid and swap-controlled, and the randomized null
   has now reproduced across roughly ten independent runs. The soft spot is the *interpretation*
   of one number, see the first bullet below.
2. **Is the hook right?** It opens on racing a function against a byte-identical copy of itself and
   one of them winning. That is the strongest thing in the post.
3. **Ship, fix, or kill?**

### Known soft spots, in the order I would look at them

- **The headline number changes on every render, by design, and it is large.** Successive renders
  of the same file produced 13.5%, 13.8%, 25.3%, 12.7%, 13.2%, and 10.3% for the block artifact in the knitting
  session. That is not instability in the finding (the randomized null and the direction were
  stable throughout), it is the post's actual thesis: the size is a property of the session. Every
  number in the prose is an inline expression, so the text re-derives itself and cannot go stale,
  and the direction word is computed too. But it does mean **the figure a reader sees is whatever
  the last render produced**, and if you want a fixed headline number the post needs a cached
  result instead. Worth a decision.
- **The knit session and fresh sessions disagree by roughly 8x and I could not explain why.** The
  knitting session measured 10.3%, eight fresh `callr` sessions averaged 1.3%. Heap size is the
  obvious suspect and it did **not** reproduce the gap when I added ballast to a clean session. The
  post says this outright in "What this post did not measure" rather than hiding it. Confirm you
  are comfortable publishing a measured effect with an unexplained magnitude. The direction and the
  fix do not depend on it.
- **The post criticises `bench::mark` by name** for something that is a reasonable design choice on
  its part (block ordering is what lets it do its memory accounting). The post says to keep using
  it for exactly that and to prefer `microbenchmark` only for close races, and it explicitly does
  not test whether the *minimum* `bench::mark` reports inherits the problem the median does. That
  untested caveat is the fairness check worth your eyes.
- **The fresh-session artifact is small.** 1.3% average, though all 8 of 8 leaned the same way. On its own
  that is a minor effect. The post is carried by the loaded-session number, which is the one a
  reader is most likely to be unable to reproduce.
- One machine, one OS, one R build. Stated in the post.

Nothing in this post is unverified. Every R block executed, plus one executed `{python}` chunk.
Renders in about two minutes.

---

## Awaiting review: two AI posts, 2026-08-28

Review page: <https://claude.ai/code/artifact/1a9a3847-d676-4485-bf04-e4e5a3f72082>

Both are the AI lane, written after the interaction power draft was killed for topic mix. They are
a deliberate pair, cross-linked, one on the input side and one on the output side of the same
question: what are you actually paying for when you call a model.

### 1. Unicode Normalization and LLM Token Costs

| | |
|---|---|
| Target query | unicode normalization llm token costs |
| Status | **DRAFT** (`draft: true`), rendered, not live |
| File | `content/post/2026-08-28-unicode-normalization-and-llm-token-costs/index.en.Rmd` |

The same Korean greeting is 2 tokens composed (NFC) and 36 decomposed (NFD). The two strings are
canonically equivalent, so they render identically everywhere and differ only on the bill. Across
UDHR Article 1 in 11 languages, Korean pays 9.82x decomposed and Vietnamese 3.02x, while several
languages pay nothing because their scripts have no composed forms to pull apart.

The calibration that makes it a post rather than a curiosity: once everything is normalized, the
gap *between languages* tops out near 2x. The gap *between normal forms within one language*
reaches ten. Normalization is the bigger lever and it is the one you control.

Not hypothetical: 1 of the 11 translations in the Unicode Consortium's own reference corpus ships
decomposed. Fixing it is one function call and cuts that entry by 55%.

### 2. What Structured Output Costs You in Tokens

| | |
|---|---|
| Target query | llm structured output token cost |
| Status | **DRAFT** (`draft: true`), rendered, not live |
| File | `content/post/2026-08-28-what-structured-output-costs-you-in-tokens/index.en.Rmd` |

Fifty records, five formats, identical information. Pretty printed JSON is 3.59x tab separated
text. Decoding every token and classifying it: 45% content, 34% punctuation, 21% whitespace. The
repeated key names are 69% of a minified payload and that share is flat from about twenty records
upward, so unlike the schema (188 tokens, paid once) it never amortizes.

### The three questions

1. **Is the claim right?** Both are measurement posts with no modeling, so the numbers are as
   solid as `tiktoken` itself. The judgment calls are the framing ones. The normalization post
   says normalization matters more than language choice, which is true in the measured range but
   is a comparison between a thing you fix once and a thing you cannot change at all. The JSON
   post recommends TSV over JSON on cost grounds while explicitly not having tested accuracy.
2. **Is the hook right?** Post 1 opens on 2 tokens against 36 for the same word. Post 2 opens on
   a fifty row extraction priced five ways.
3. **Ship, fix, or kill?** They can ship separately. Post 1 is the stronger of the two.

### Known soft spots

- **Post 1 nearly shipped a wrong headline.** The first draft reported Vietnamese at 3.55x English
  and framed the post as a multilingual cost gap. That number was an artifact of the source file
  being partly decomposed rather than a property of Vietnamese. Normalizing every language
  consistently drops it to 1.54x and moved the post onto its real subject. Worth knowing the
  original framing was wrong, because the corrected one is a stronger claim.
- **Post 1 measures OpenAI tokenizers only** (`o200k_base`). Llama, Gemma, and Claude tokenizers
  are not tested. The byte-fallback mechanism is general, but the exact multipliers are not.
- **Post 2 measures cost and nothing else.** Descriptive key names plausibly help the model fill
  values correctly, and TSV means writing a parser and handling embedded tabs. The post says this
  outright in a "What this post did not measure" section rather than burying it, but confirm you
  are happy recommending a format change on cost evidence alone.
- **The 50 record example is synthetic** with short, regular values. Real extractions with long
  free text values would shift the content share up and the overhead share down.

## Shipped 2026-08-26: Friday 2026-08-28 industry post

| | |
|---|---|
| Title | Calibrating a Marketing Mix Model With an Incrementality Test in R: Why the Experiment Loses |
| Target query | calibrate MMM with incrementality test |
| Slot | Friday, filled with an industry/SEO post rather than an evergreen |
| Freshness | Meridian generally available Jan 2025 (19 months). IAB State of Data 2026 published Feb 2026. Clears the rule. |
| Status | **LIVE** at </post/calibrate-mmm-with-incrementality-test/> (`draft: false`, published 2026-08-26). Note the folder is named `2026-08-28-...` for the Friday slot but the front matter date is 2026-08-26, and the front matter is what Hugo uses. Do not forward-date it to the 28th, that would unpublish it. |
| Amended | 2026-08-26, prose only. See "Post-publication correction" below. |
| File | `content/post/2026-08-28-calibrate-mmm-with-incrementality-test/index.en.Rmd` |
| Review page | <https://claude.ai/code/artifact/62aa2fe0-7faa-4877-98c2-c7357defa62f> |

Headline: the 2026 consensus says to calibrate your MMM with a geo test by setting the prior
mean and scale from the experiment. On simulated data with a known answer, that recipe left
video ROI at 3.55 against a truth of 2.00, still 77% high. The experiment itself was right at
2.30. The prior lost because the misspecified MMM likelihood is sharper than the experiment, so
the posterior is a precision-weighted average that hands 41% of the vote to a model already
shown to be wrong by 7.8 standard errors.

The constructive half: run the disagreement test first, use a failed test to find the missing
variable, then calibrate. Mean absolute error across three channels goes 2.07 (MMM alone), 0.78
(calibrated), 0.47 (specification fixed first).

Nothing in this post is unverified. Six `stan_glm` fits in R, plus one executed Python chunk
running Meridian 1.8.0.

### The three questions, with what I would look at

1. **Is the claim right?** The numbers are real, but this post argues against the current
   industry consensus and names Google's Meridian while doing it. The post is careful to say the
   recipe helps (MAE more than halves), links the public repo, and now carries a section headed
   "What this post did not do" separating the recipe (tested) from Meridian's own model (not
   fitted). Check that the criticism reads as fair rather than as a straw man, because that is
   the one thing that would embarrass you.
2. **Is the hook right?** It leads on "I ran that recipe on data where I picked the true ROI
   myself. The experiment was right. The calibrated model was not."
3. **Ship, fix, or kill?**

### Known soft spots

- Point 3 and point 5 in the Monday checklist pull in opposite directions (tighten the prior
  because the model is untrustworthy, widen it because one experiment does not generalize). The
  post says so explicitly rather than hiding it. Confirm you are happy admitting that.
- The bias magnitude is a choice. Video loads on unlogged demand hard enough to produce a 194%
  overstatement. Realistic for MMM, but a skeptic could call it staged.
- I did not fit Meridian's own model, and an early draft never said so. That is now stated
  outright in "What this post did not do". Meridian 1.8.0 **is** installed and running here, and
  the post uses it to kill the strongest objection: its lognormal ROI prior and the normal prior
  used in the post differ by at most 0.055 across the central 95%, against a 1.55 gap between the
  calibrated estimate and the truth. So the result is not an artifact of the prior family. What
  remains untested is whether a hierarchical geo-level model shrinks the 77%. That paragraph is
  the one that decides whether the criticism reads as fair, so it is worth your eyes.

## Post-publication correction, 2026-08-26

A read-through of the live page found four claims that the post's own printed tables contradict.
No code changed and no computed output changed. Every number re-rendered byte-identical, verified
against an independent re-run. What changed is prose that was reading the tables wrong.

1. **The front matter summary said the recipe moved the estimate "only two thirds of the way to
   the truth."** It moved 65% of the way to *the experiment's answer* of 2.30, which is 60% of the
   way to the truth of 2.00. The summary conflated the experiment with the truth, which is exactly
   the conflation the post exists to attack. Rewritten.
2. **The "fix the specification first" section declared victory on a mean and never showed the
   video row.** With the proxy added, video is 3.02 against a truth of 2.00, still 51% high and
   still worse than the experiment's own 2.30. The section quoted MAE 0.47 and search recovering
   to 2.97 and stopped there, which is the single best cell in the table. It now states the video
   result outright, decomposes where the MAE gain came from (search error 0.47 to 0.03, video
   1.55 to 1.02, social slightly worse at 1.17 to 1.14), explains why video survives the repair
   (the proxy correlates 0.80 with demand, so about a third of the confounder's variance is still
   unmodeled and loads onto the channel whose spend chases demand), and ranks all four video
   estimates honestly. The experiment wins.
3. **The prior-sweep paragraph said search and social "both move toward" their true values.**
   Search does, 2.53 to 2.84. Social crosses 1.50 by the second row and finishes at 1.74, so it
   overshoots by about as much as it began short. Rewritten to say reallocation rather than
   correction, with a matching change to Monday checklist point 6.
4. **The precision-weighting section presented the 59/41 split as the explanation without
   checking it.** The formula predicts 3.77 and the fit returned 3.55. The gap is collinearity
   plus priors on the other two slopes, so video's marginal posterior is not the one-parameter
   case. Now stated rather than left for a reader to catch.

Two additions in the same pass:

- **An undisclosed simplification that favored the post's own argument.** The geo experiment is
  generated with no adstock, so the blackout has no carryover and the Wald estimator recovers the
  truth cleanly. Putting the same 0.6 carryover into the geo world drops the identical estimator
  to about 1.8 against a truth of 2.0, biased low by roughly a tenth, because treated markets keep
  earning on pre-blackout spend. Verified by simulation, 400 replications. This one makes the
  experiment look better than a real one would, which is the side the post argues for, so leaving
  it out was the strongest fair attack available on the post. It is now named in "What this post
  did not do" along with what it does and does not cost the conclusion.
- **The disagreement test had a hole in its own rule.** Checklist point 1 said "under three,
  reconcile. Over five, misspecified" and said nothing about three to five. Filled in. A seventh
  checklist point was added: for the channel you actually tested, report the test.

Net effect on the thesis: unchanged and better defended. The headline result (77% high after
calibration, 7.8 standard errors of disagreement) was always correct. What was wrong was the
constructive half overselling its own fix.

## Correction to the previous entry

`policytree` **is** installed on this machine, contrary to what this file said on 2026-08-25.
So is `grf` 2.5.0. The uplift draft is unblocked on that front.

## Still open

| Item | Status |
|---|---|
| Uplift draft (Friday evergreen) | Written by the cloud routine, push blocked by a 403, recover the patch from <https://claude.ai/code/session_01UsRVfrgjSQ1aVYJhNVdPFQ> then `git am` it. Now displaced to a later slot by the MMM post. |
| Cloud routine cannot push | Grant the Claude GitHub App `contents: write` at <https://github.com/settings/installations>, or grant write at <https://claude.ai/settings/connectors> |
| ~~Python block in `staggered-rollouts-break-twfe`~~ | **CLOSED 2026-08-26.** See below. |
| Buffer | Still empty. The standing rule wants two finished evergreens in reserve and there are zero. |

## Python is fixed, and one live post changed

The "no working Python here" note in README.md was wrong. `uv` was already installed and already
managing real CPython builds. The PATH stub and the broken WSL were real, but they were never the
whole story, and nobody checked past them.

What changed:

- Blog venv at `C:\Users\miken\.venvs\bio-blog` (CPython 3.12.12), with `RETICULATE_PYTHON`
  pointed at it from `.Rprofile`. `{python}` chunks now execute at render time.
- **`staggered-rollouts-break-twfe` is live and its Python block was edited.** The fenced
  ```` ```python ```` became an executed ```` ```{python} ```` chunk. Output is now on the page:
  True ATT 1.634, TWFE 0.919, against the R side's 1.652 and 0.981. Different generators, same
  conclusion, exactly as the prose already claimed. Every R number in that post re-rendered
  byte-identical and the event-study figure is intact. Only the code fence and the new output
  changed.
- The MMM post gained an executed Meridian chunk. Meridian 1.8.0 installed and running locally,
  used to confirm that its lognormal ROI prior and the normal prior used in the post differ by at
  most 0.055 across the central 95%, against a 1.55 gap between the calibrated estimate and the
  truth. That closes the "your criticism is just the wrong prior family" objection with a number
  rather than an assurance.

Worth a glance because it touches a published URL, but the change is additive.
