# Posts Log

| Date | Slug | Type | Angle | Distributed | Notes |
|---|---|---|---|---|---|
| 2026-08-19 | `staggered-rollouts-break-twfe` | Evergreen | Geo rollout, TWFE bias, Callaway-Sant'Anna | pending | First post of the new cadence. Originally drafted as a trend-jack, reclassified as evergreen because the underlying result dates to 2018 to 2021. Python block shipped unverified and was **fixed on 2026-08-26**, see Amendments. Log previously dated this 2026-08-20, but the front matter says 2026-08-19. |
| 2026-08-25 | `continuous-treatment-did-in-r` | Trend-jack | Continuous-dose DiD, `contdid`, spend coefficient is not marginal ROI | pending | First post to clear the freshness rule properly: `contdid` 0.1.1 reached CRAN 2026-07-21, five weeks before publication. Dose randomized in the simulation, so the 31% overstatement is pure weighting bias rather than selection. Every block executed, no Python. Target query: difference in differences with a continuous treatment in R. |
| 2026-08-28 | `calibrate-mmm-with-incrementality-test` | Trend-jack (industry/SEO) | Feeding a geo test into an MMM as a prior does not fix a misspecified MMM | drafted | Freshness anchors: Meridian generally available Jan 2025 (19 months), IAB State of Data 2026 published Feb 2026. Fills the Friday slot with an industry post rather than an evergreen, per the one-for-one mix rule. Contrarian against the 2026 triangulation consensus, so the framing is the thing to check. Every block executed: six `stan_glm` fits in R plus one executed Meridian 1.8.0 chunk in Python. Target query: calibrate MMM with incrementality test. |

## Amendments

| Date | Post | What changed |
|---|---|---|
| 2026-08-26 | `staggered-rollouts-break-twfe` (live) | Python block converted from a static fence to an executed `{python}` chunk. Output now on the page: True ATT 1.634, TWFE 0.919. Closes the last unverified block on the site. All R numbers re-rendered byte-identical. |
| 2026-08-26 | `calibrate-mmm-with-incrementality-test` (draft) | Added the Meridian repo link, a "What this post did not do" scope section, and an executed Meridian 1.8.0 chunk showing its lognormal ROI prior differs from the post's normal prior by at most 0.055 across the central 95%. |
| 2026-08-26 | `calibrate-mmm-with-incrementality-test` (live) | Post-publication prose correction. No code changed and no computed output changed, verified byte-identical against an independent re-run. Fixed the front matter summary conflating the experiment's answer with the truth, confronted the `spec_first` video result of 3.02 that the section had hidden behind a mean, corrected the sweep claim that social moves toward 1.50 when it overshoots to 1.74, reconciled the 3.77 the precision weighting predicts against the 3.55 the fit returned, disclosed that the geo experiment is simulated without adstock and that this flatters the experiment, and filled the three-to-five hole in the disagreement test rule. Details in REVIEW-NOW.md. |
