# Provenance: are-llm-benchmark-differences-statistically-significant

Draft for Tuesday 2026-10-20, written 2026-10-17. This file lists every factual claim in the
post, where it came from, and how it was checked. If anyone questions a number, start here.

Post source: `content/post/2026-10-20-are-llm-benchmark-differences-statistically-significant/index.en.Rmd`

## The data

| Item | Value |
|---|---|
| Dataset | "Model Outputs AIME 2026", `MathArena/aime_2026_outputs` on Hugging Face |
| Creator | MathArena (SRI Lab at ETH Zurich, and INSAIT). Paper: Dekoninck et al. 2026, arXiv 2605.00674 |
| Revision | `f916cfc3eebc6ffbbf57d70918e79804d740806f` (dataset last modified 2026-09-11) |
| File | `data/train-00000-of-00001.parquet`, 76,666,536 bytes |
| sha256 | `22e1aaed0a83b3bb55bbed099838a2595efc8132f0fa67199e010bdf91e9d1c6` (matches the Hugging Face LFS oid) |
| md5 | `fece34532657c69e005a0aa9d2c129ab` |
| License | CC BY-NC-SA 4.0 <https://creativecommons.org/licenses/by-nc-sa/4.0/> |
| Where it lives | Nowhere in this repo or on the site. The post downloads it at render time into the R user cache (`tools::R_user_dir("matharena", "cache")`) and stops if the sha256 differs |
| Columns used | `model_name`, `problem_idx`, `idx_answer`, `correct`. Nothing else is read |

Leaderboard values quoted from matharena.ai are in `matharena_leaderboards_2026-10-17.json` in this
folder. Screenshots of the same pages are in `local/`, which is gitignored and exists only on
Mike's machine, because the repo is public and the screenshots are copies of a third-party site.
The JSON was cross-checked against the values hardcoded in the post's hidden `site` chunk on
2026-10-17: all 31 margins, the release-flag count, the Qwen3.5-4B rank and score, and the two
ArXivMath scores matched exactly.

## Archived copies (Wayback Machine)

Saved on Mike's go-ahead on 2026-10-17 Pacific (2026-10-18 UTC). MathArena's pages are a shell
that loads each leaderboard from a separate data file, so the data files were archived too. **The
data-file captures are the authoritative record.** Each one was downloaded back from the archive
and its sha256 matched a direct download from matharena.ai at 2026-10-18 06:09 UTC.

| What | Archived URL | Captured (UTC) | Verified |
|---|---|---|---|
| AIME 2026 leaderboard data | <https://web.archive.org/web/20261018061022/https://matharena.ai/competition_tables/aime--aime_2026> | 2026-10-18 06:10:22 | sha256 `f7d0b3c4...00b9e`, identical to live. Contains 89.66% for Qwen3.5-4B, the 31 intervals, and Gemini 3.6 Flash and Kimi K3 (Think) |
| September ArXivMath leaderboard data | <https://web.archive.org/web/20261018060754/https://matharena.ai/competition_tables/arxiv--september> | 2026-10-18 06:07:54 | sha256 `8973b7bb...2b3be`, identical to live. Contains 91.51% and 87.74% |
| AIME 2026 page | <https://web.archive.org/web/20261018060628/https://matharena.ai/?comp=aime--aime_2026&view=detailed> | 2026-10-18 06:06:28 | Page shell only, see the caveat below |
| Front page | <https://web.archive.org/web/20261018060751/https://matharena.ai/> | 2026-10-18 06:07:51 | Page shell only, see the caveat below |

Caveat on the page captures. As of 06:15 UTC, replaying the AIME page snapshot pulled its table
from an older capture of the data file dated 2026-07-21, so the replay shows 30 models and
Qwen3.5-4B at 89.70%, rank 27. That is MathArena's July table, not the October one. It may
correct itself once the archive indexes the newer data capture. It does not affect the post:
the October data file is archived above, and its contents match what the post quotes. It does
show that the item response estimate moves as models are added, which is why the post dates its
quoted values.

Local copies of both live data files, downloaded directly from matharena.ai at 06:09 UTC, are in
`local/`, with their full sha256 below. They stay out of git with the screenshots.

- `local/matharena_competition_tables_aime--aime_2026_2026-10-18T0609Z.json`, sha256
  `f7d0b3c430c35476c1ef3ac5535b933a987c524e57fc9d6ed1a64949bf500b9e`
- `local/matharena_competition_tables_arxiv--september_2026-10-18T0609Z.json`, sha256
  `8973b7bb8ea675057eb4c03cedc79d40de49d0a1b15da24d387eaaad2d82b3be`

## Claims and their sources

| # | Claim in the post | Source | How it was checked |
|---|---|---|---|
| 1 | 32 models, 30 problems, 3,516 graded attempts, two or four per model | Dataset | Computed in the post. A `stopifnot` halts the render if the counts change |
| 2 | 25 of 31 full-coverage models have a 95% bootstrap rank interval reaching first | Computed, seed 20261020, 4,000 resamples of problems | `stopifnot` guard. The Python chunk reproduces 25 on seeds 1, 2, and 3 |
| 3 | 16 of 30 problems solved by every model on every attempt, five problems carry 80% of the spread | Computed | Inline expressions, re-derived on every render |
| 4 | MathArena prints a 95% interval next to every AIME 2026 score | matharena.ai, detailed view, column header "Accuracy (± 95% CI)" | JSON plus screenshot `local/matharena_aime2026_detailed_view_ci_2026-10-17.jpg` |
| 5 | All 31 intervals match `1.96 * sqrt(p * (1 - p) / attempts)` to the second decimal | Site values plus the dataset | The post recomputes the formula from the data and counts the matches inline |
| 6 | Over problems the intervals run a median 1.7 times wider, DeepSeek-v3.2 (Think) 4.19 becomes 7.31 | Computed | Inline expressions |
| 7 | Over attempts 14 of 29 are significantly behind (7 after Holm), over problems 2 (1 after Holm) | Computed, Fisher exact and exact sign-flip | Printed table in the post |
| 8 | Qwen3.5-4B has no attempts on problems 10, 15, 17, 28, 29, 30, and a plain mean ranks it 4th of 32 | Dataset | Computed inline |
| 9 | MathArena ranks Qwen3.5-4B 29th at 89.66% using an item response estimate | matharena.ai AIME 2026 table | JSON (rank, score, tooltip text) plus screenshot `local/matharena_aime2026_qwen35_4b_rank29_2026-10-17.jpg` |
| 10 | AIME 2026 is on MathArena's deprecated list | matharena.ai competition menu, "Final-Answer Comps (Deprecated): AIME 2026" | Page text read 2026-10-17. The post states the listing only, not a reason for it |
| 11 | 22 of 32 models are marked as released after the competition | matharena.ai flag, title "Model was released after competition release." | JSON |
| 12 | Gemini 4 Argon 87.74% and GPT-6.1 Sol 91.51% on the 53 problem September ArXivMath set, added Friday 16 October | matharena.ai front page and its news line for October 16 | JSON plus screenshot `local/matharena_arxivmath_2026-09_argon_2026-10-17.jpg`. The post says "at the time of writing" |
| 13 | Moritz Hardt argues absolute scores mislead while rankings still carry real information | Quanta Magazine, John Pavlus, 2026-10-16 | Paraphrase checked against the article on 2026-10-17. No direct quotation in the post |
| 14 | Leaderboard Lottery: on data calibrated to the Open LLM Leaderboard, the reported winner was the true best 0 to 58 percent of the time under prompt resampling | Shourya V Jain, ICML 2026 Hypothesis Testing Workshop poster, <https://icml.cc/virtual/2026/80012>, OpenReview `ZhVvlyFZP9` | Abstract wording checked 2026-10-17. Paraphrase only |
| 15 | GPQA Diamond has 198 items | Rein et al. 2023, arXiv 2311.12022, Section 2.3 | Read 2026-10-17 |
| 16 | SWE-bench Verified has 500 items | Hugging Face `princeton-nlp/SWE-bench_Verified`, `num_examples` | API read 2026-10-17 |
| 17 | Humanity's Last Exam has 2,500 items | Phan et al. 2025, arXiv 2501.14249 (v11, July 2026) | Read 2026-10-17 |
| 18 | Detectable gap is about `2.8 * sqrt(discordance / n)` | Standard paired-test power approximation, derived in the post | Assumptions stated in the post: normal approximation, one attempt per item |
| 19 | Book link | <https://mike-data-analysis.share.connect.posit.cloud/sec-clustered-inference.html> | HTTP 200 on 2026-10-17 |

## Licensing and risk notes

This is a record of what was done to keep risk low. It is not legal advice.

- **The dataset is not redistributed.** An earlier draft placed two derived CSV files next to the
  post. They were deleted on 2026-10-17 before any commit, so they never entered git history
  (checked with `git log --all`). The post now downloads the file from Hugging Face and publishes
  only statistics computed from it, with attribution: title, creator, source link, license link,
  and a note on what was kept.
- **Leaderboard values** quoted from matharena.ai are short factual numbers, cited with the
  retrieval date. Screenshots stay local.
- **Model and company names** appear only to identify what MathArena evaluated. The post makes no
  claim about any model beyond what the data shows, and says the Argon gap "is a statement about
  53 problems, not about either model".
- **Tone toward MathArena.** The post credits them for publishing raw attempts and printing
  intervals, calls their missing-data handling correct, and describes their interval as answering
  a narrower question rather than as an error. It thanks the team in the data note.
- **No direct quotations** from Quanta or the ICML abstract appear in the post.

Decisions left to Mike:

- Whether the blog, which links to his books, counts as NonCommercial under CC BY-NC-SA. Much
  less exposed now that nothing is redistributed, but still his call.
- Whether to send the MathArena team a short courtesy note before publishing.
- Wayback Machine snapshots: done on Mike's go-ahead, see "Archived copies" above.

## Reproduce

From the repo root, with the environment in `blog-ops/README.md`:

```r
Sys.setenv(RSTUDIO_PANDOC = "C:/Program Files/RStudio/resources/app/bin/quarto/bin/tools")
blogdown::build_site(build_rmd = "content/post/2026-10-20-are-llm-benchmark-differences-statistically-significant/index.en.Rmd", run_hugo = FALSE)
```

The first render downloads the 73 MB file and takes about 40 seconds. Later renders read the cache
and take about 12. Every number in the prose is an inline expression, so a successful render
re-derives all of them.

## Publish-day recheck, 2026-10-25

Read directly from the two data files on matharena.ai before publishing:

- September ArXivMath: Gemini 4 Argon 87.74% and GPT-6.1 Sol 91.51%, unchanged. The post now
  says so in its data note.
- AIME 2026: Qwen3.5-4B shows 89.67%, still 29th, against the 89.66% archived on 17 October. The
  item response estimate was refitted. The post now dates that quote inline ("on 17 October it
  ranked the model 29th at 89.66%"), and the archived data file above backs it.
- DeepSeek-v3.2 (Think) still shows plus or minus 4.19.

The hook said "Last Friday", written for a 20 October publish date. It now says "On 16 October".
The front matter date moved to 2026-10-25, the day it went live.
