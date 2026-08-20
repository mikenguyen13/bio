# Review Queue

**One draft exists but is not in this repo yet.**

| | |
|---|---|
| Title | Uplift Modeling in R: Your Best Customers Are the Wrong Target |
| Target query | uplift modeling in R |
| Slot | Friday evergreen |
| Packages | `grf` and `policytree`, both already installed |
| Status | written by the cloud routine, push blocked by a 403 |

The routine could not push because the cloud session's GitHub token is read-only. It packaged
the work as a git-am-able patch instead. Recover it from the run session:

<https://claude.ai/code/session_01UsRVfrgjSQ1aVYJhNVdPFQ>

Download the `.patch` file, then from the repo root:

```
git checkout master
git am <path-to-patch>
```

Then open a local session and say "render and publish the new draft".

## Known blocker

Cloud routine runs cannot write to `mikenguyen13/bio`. Fix is to grant the Claude GitHub App
`contents: write` on the repo at <https://github.com/settings/installations>, or to grant the
GitHub connection write access at <https://claude.ai/settings/connectors>. Until that is done,
every run will fall back to delivering a patch instead of a branch. The routine now handles
that fallback deliberately rather than by improvising.

## Unverified in that draft

- No code was executed, so every number is an inline expression waiting on a real render.
- The run reported one specific uncertainty: the post claims a response-model ranking scores
  near zero on the Qini RATE. If the render disagrees, the numbers win and that section gets
  rewritten around the real output.
- Some documentation domains were blocked by the sandbox proxy, so parts of the `grf` and
  `policytree` API were verified from GitHub source rather than from the reference manual.

## Also still open

The Python block in the shipped `staggered-rollouts-break-twfe` post has never been executed.
Python is not installed on this machine and WSL is broken. Run it once wherever you have
Python, or say the word and it gets removed.
