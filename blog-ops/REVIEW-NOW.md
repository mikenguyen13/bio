# Review Queue

## Shipped: Tuesday 2026-08-25 trend-jack

| | |
|---|---|
| Title | Difference-in-Differences With a Continuous Treatment in R: The Dose Coefficient Is Not Marginal ROI |
| Target query | difference in differences with a continuous treatment in R |
| Slot | Tuesday trend-jack |
| Package | `contdid` 0.1.1, on CRAN 2026-07-21, so five weeks old and clear of the freshness rule |
| Status | published 2026-08-25, see POSTS-LOG.md |
| Review page | <https://claude.ai/code/artifact/8b6d4364-86f4-4e5a-b4bb-77400f140c50> |

Headline: with a randomly assigned dose and no confounding anywhere, the two-way fixed effects
spend coefficient still overstates the true average marginal return by 31%. The bias is in the
weights rather than in selection. `contdid` recovers 4.61 against a truth of 4.51.

Nothing in this post is unverified. There is no Python block.

## Blocker cleared on the way through

Packages installed on this machine go to the per-user library, and that directory was not on
R's default search path. blogdown renders each post in a fresh R session, so any post using a
newly installed package failed to knit with "there is no package called ...". Fixed by adding
the per-user library to `.libPaths()` in the repo `.Rprofile`. That change is uncommitted and
part of the current diff.

## Correction to the previous entry

`policytree` is **not installed**, contrary to what this file said. `grf` 2.5.0 is. Friday's
uplift draft depends on both, so install `policytree` before that render.

## Still open

| Item | Status |
|---|---|
| Uplift draft (Friday evergreen) | Written by the cloud routine, push blocked by a 403, recover the patch from <https://claude.ai/code/session_01UsRVfrgjSQ1aVYJhNVdPFQ> then `git am` it |
| Cloud routine cannot push | Grant the Claude GitHub App `contents: write` at <https://github.com/settings/installations>, or grant write at <https://claude.ai/settings/connectors> |
| Python block in `staggered-rollouts-break-twfe` | Never executed. No working Python here. Run it elsewhere or say the word and it goes |
