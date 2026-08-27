# Review Queue

## Awaiting review: Friday 2026-08-28 industry post

| | |
|---|---|
| Title | Calibrating a Marketing Mix Model With an Incrementality Test in R: Why the Experiment Loses |
| Target query | calibrate MMM with incrementality test |
| Slot | Friday, filled with an industry/SEO post rather than an evergreen |
| Freshness | Meridian generally available Jan 2025 (19 months). IAB State of Data 2026 published Feb 2026. Clears the rule. |
| Status | rendered, `draft: true`, not committed |
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

Nothing in this post is unverified. There is no Python block.

### The three questions, with what I would look at

1. **Is the claim right?** The numbers are real, but this post argues against the current
   industry consensus and names Google's Meridian documentation while doing it. The post is
   careful to say the recipe helps (MAE more than halves) and that the demo is a linear national
   MMM rather than Meridian's hierarchical geo model. Check that the criticism reads as fair
   rather than as a straw man, because that is the one thing that would embarrass you.
2. **Is the hook right?** It leads on "I ran that recipe on data where I picked the true ROI
   myself. The experiment was right. The calibrated model was not."
3. **Ship, fix, or kill?**

### Known soft spots

- Point 3 and point 5 in the Monday checklist pull in opposite directions (tighten the prior
  because the model is untrustworthy, widen it because one experiment does not generalize). The
  post says so explicitly rather than hiding it. Confirm you are happy admitting that.
- The bias magnitude is a choice. Video loads on unlogged demand hard enough to produce a 194%
  overstatement. Realistic for MMM, but a skeptic could call it staged.
- I did not run Meridian, and an early draft of this post never said so. Meridian is
  Apache-licensed Python (v1.8.0, no R interface) at <https://github.com/google/meridian>, and
  there is no working Python on this machine. The post now carries a section headed "What this
  post did not do" that states the scope limit outright, links the repo, and explains that the
  mechanism is a property of Bayesian updating rather than of Meridian's code. Worth a look,
  because it is the paragraph that decides whether the criticism reads as fair.

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
