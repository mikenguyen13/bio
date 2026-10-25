# Provenance: polars-2-0-row-order

Draft for Friday 2026-10-30, written 2026-10-24. Every factual claim in the post, where it came
from, and how it was checked.

Post source: `content/post/2026-10-30-polars-2-0-row-order/index.en.Rmd`, with `audit.py` and
`run_audit.py` beside it.

## Data

No third-party data. Both tables are simulated inside the post (seed 20261030) and written to a
temporary Parquet file at render time. Nothing is stored in the repo. House rule 7 is satisfied
trivially.

## The results change on every render, by design

The post measures nondeterminism, so its counts move from render to render. Successive renders on
2026-10-24 gave, for the first purchase on 2,000,000 events, 6 to 12, 9 to 13, and 6 to 13 wrong
customers out of 100,000, and for the in-memory fallback 18, 17, 19, and 16 wrong runs of 20.
Every number in the prose is an inline expression over the computed objects, so the text always
matches its own output. The qualitative claims that the front matter makes are guarded with
`stopifnot` and halt the render if they stop holding:

- every query matches under 1.44.2, exactly 4 of 5 are wrong under 2.0.0, and those 4 are wrong
  on all 20 runs
- both real fixes are right on all 20 runs, and the in-memory fallback is wrong at least once
- data.table and DuckDB with `ORDER BY` are right on all 20 runs, and DuckDB without it is wrong
  at least once

## Versions

| Package | Version used | Current release when checked (2026-10-24) |
|---|---|---|
| Polars | 2.0.0 (blog venv) | 2.0.0, released 2026-10-06 on PyPI |
| Polars 1.x | 1.44.2 (`C:/Users/miken/.venvs/polars1`, via `POLARS1_PYTHON` in `.Rprofile`) | 1.44.2, released 2026-09-09, the last 1.x on PyPI |
| DuckDB (R) | 2.0.0, built from source | 2.0.0 on CRAN. The Windows binary for R 4.4 was 1.5.2, so it was compiled |
| data.table | 1.18.6.1 | 1.18.6.1 on CRAN |
| arrow (R) | 25.0.1, used only to write the Parquet files | 25.0.1 on CRAN |

## Claims and their sources

| # | Claim in the post | Source | How it was checked |
|---|---|---|---|
| 1 | Polars 2.0 shipped on 6 October | PyPI release history for `polars` | Upload date of 2.0.0 is 2026-10-06. rc1 was 2026-09-02 and rc2 2026-09-20 |
| 2 | 1.44.2 is the last 1.x release | PyPI release history | Latest non-prerelease 1.x is 1.44.2 (2026-09-09). An earlier check that stopped at 1.39.3 was wrong because its filter only matched `1.3*`, and the comparison was rerun on 1.44.2 |
| 3 | `collect()` on a lazy query now runs on the streaming engine | Upgrade guide <https://docs.pola.rs/releases/upgrade/2/> | Guide: `"auto"` now resolves to the streaming engine for lazy queries |
| 4 | The streaming engine does not guarantee row order for joins, group-bys, and similar operations | Upgrade guide | Guide names `unpivot`, `group_by`, and joins |
| 5 | The announcement gives row order as one reason the change needed a major version | <https://pola.rs/posts/announcing-polars-2/>, 2026-09-02, the rc1 announcement | Read 2026-10-24. The post gives two reasons for 2.0, and the wording was changed from "the one change" to "one reason" after this check |
| 6 | The guide offers `collect(engine="in-memory")` to restore the previous default | Upgrade guide | Also offers `pl.Config.set_engine_affinity("in-memory")`. The guide does not say the in-memory engine guarantees order |
| 7 | The in-memory fallback did not restore the order on a Parquet source | Measured | In the post, and confirmed beforehand over 50 runs: 43 of 50 wrong, at most 1 customer each, for both `engine="in-memory"` and `set_engine_affinity`. Polars 1.44.2 was 0 of 50 on the same file. An eager `DataFrame` join in 2.0.0 was 0 of 50. See `prototype/inmem.py` |
| 8 | A Polars issue opened in November 2024 set out that left-join order should not be guaranteed | <https://github.com/pola-rs/polars/issues/19576>, "Don't guarantee left join ordering", opened 2024-11-01, closed 2026-06-24 | Read via the GitHub API 2026-10-24 |
| 9 | An optimizer bug dropped `maintain_order=True` with a `head()` between a group-by and a sort, fixed 21 October after 2.0.0 | <https://github.com/pola-rs/polars/issues/30079>, opened 2026-10-20, closed 2026-10-21 | PyPI had no release after 2.0.0 on 2026-10-24, so the fix is unreleased |
| 10 | DuckDB documents that `first()` can be non-deterministic without an `ORDER BY` | <https://duckdb.org/docs/2.0/sql/functions/aggregates.html> | Page names `first`, `last`, `list`, and `string_agg` |
| 11 | data.table's `amount[1L]` by group is the first purchase | Measured | 0 of 20 runs wrong in the post |
| 12 | `assert_frame_equal(..., check_row_order=False)` still fails on the bad output | Measured | The post prints the assertion message |
| 13 | Book link | <https://mike-data-analysis.share.connect.posit.cloud/replication-and-synthetic-data.html> | HTTP 200 on 2026-10-24 |

Every outbound link in the post returned HTTP 200 on 2026-10-24.

## Pre-render checks that shaped the post

Scripts in `prototype/`. They ran on in-memory data before the post existed and are kept so the
reasoning can be retraced.

- `polars_v2.py` under 1.39.3, 1.44.2, and 2.0.0: identical default code, 20 runs. 1.x versions
  matched on every order-dependent query, 2.0.0 matched on none except `head(20)`. Float
  `group_by` sums differed in the last bits (about 1e-15 relative) run to run on every version,
  which is older, unrelated behavior and is left out of the post.
- `polars_scale.py`: the first check of how errors scale with size. It disproved my first guess,
  that small data would hide the problem. A 1,000 row table was wrong on 10 of 10 runs.
- `polars_fix.py`: the fixes and `assert_frame_equal`. On in-memory data the in-memory engine
  looked like a full fix. On a Parquet source it was not, which a `stopifnot` in the first full
  render caught. That is how claim 7 was found.
- `gen_data.R`, `r_engines.R`, and `duck_test.R`: the R side. Arrow's join also kept event order
  on all 20 runs, which the post leaves out, because Arrow is used here only to write files.

## Licensing and risk notes

This is not legal advice. The post uses no third-party data, quotes no third-party text beyond
function names, and paraphrases the Polars and DuckDB docs with links. It says plainly that the
behavior is documented and not a bug, and it frames 1.x as relying on an order Polars never
promised. Polars and DuckDB are named only to identify the software tested.

## Publish-day recheck, 2026-10-25

Polars 2.1.0 reached PyPI at 17:58 UTC on 2026-10-25, a few hours before the post went live. Its
release notes include order-related changes, including "Emit unmatched build rows of single-key
joins in row order (#30037)" and "Preserve order of sliced maintain-order group_by (#30096)",
which is the fix for #30079 (PR body: "Fixes #30079", merged 2026-10-21). Under house rule 6
the post was re-tested on 2.1.0 in a scratch venv before anything changed:

- `run_audit.py`, 20 runs: four of five queries wrong on all 20 runs, 20 distinct answers each,
  `head(20)` right on all 20. Identical in pattern to 2.0.0.
- `prototype/inmem.py`, 20 runs: default wrong 20 of 20 (at most 12 customers),
  `engine="in-memory"` and `set_engine_affinity` both wrong 20 of 20 (at most 1 customer), eager
  `DataFrame` join right on all 20.

The blog venv was then upgraded to 2.1.0, the post now compares 1.44.2 with 2.1.0, its guard
checks for `2.1.0`, and the #30079 sentence says the fix is in 2.1.0. The statement that 2.0.0
gave the same results rests on every render and prototype run made 2026-10-24, recorded above.
The front matter date moved from 2026-10-30 to 2026-10-25 so Hugo would publish it.
