# Review Queue

## Awaiting review: Friday 2026-08-28 industry post

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
