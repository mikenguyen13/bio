# Review Queue

**Empty.** Nothing is waiting on you.

Last shipped: `staggered-rollouts-break-twfe` on 2026-08-20. See `POSTS-LOG.md`.

## Next up

The continuous-treatment DiD post, which is the real trend-jack that post #1 was not.
Research is done and the estimator is verified working on this machine
(`contdid` 0.1.1, installed to the per-user library on 2026-08-20).

Headline finding from the test runs: a binary DiD on a geo test with varying spend returns
one number (2.99 against a true 2.94), which is correct and useless. It cannot tell you
whether to spend more. The dose-response curve recovers the whole shape, and the data-driven
`cck` method is roughly five times more accurate than the parametric spline
(ATT RMSE 0.046 against 0.155 at n=2000).

## Open item on the shipped post

The Python block was published without ever being executed. Python is not installed on this
machine, the Microsoft Store stubs are not real interpreters, and WSL is broken (Docker's
distro is missing its disk image). If you have Python anywhere, run that block once. If it
fails, say so and I will patch or remove it in a follow-up commit.
