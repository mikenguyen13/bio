# Idea Backlog

Rules: append freely, never delete. Anything that costs >30 min to solve goes here immediately.
Claude pulls from here twice a week. Tuesday takes a TREND, Friday takes an EVERGREEN.

Status key: `[ ]` open · `[~]` drafted · `[x]` shipped (move to POSTS-LOG.md)

---

## THE FRESHNESS RULE (added 2026-08-20)

**A topic only counts as a trend-jack if the underlying method, package, or paper is under
24 months old.** Anything older is evergreen, no matter how it gets framed.

This rule exists because post #1 failed it. The TWFE bias result was dressed up in 2026 geo
experiment language, but Goodman-Bacon circulated in 2018 and the method now has an Annual
Reviews article and an NBER practical-guidelines paper. Consolidated knowledge, not frontier.
Mike caught it, and he was right.

The test: **name the paper or package and its date.** If that date is more than two years
back, file it as evergreen and stop calling it a trend. State the age when proposing a topic.

## TREND-JACK (hot right now, Aug 2026, recheck monthly)

Re-audited against the freshness rule on 2026-08-20. Ages shown.

These sit where industry money and academic method overlap. That intersection is where
your audience actually is: analytics leads who read papers, and academics who want their
methods used.

- [x] **Staggered geo rollouts break TWFE.** SHIPPED 2026-08-20 as an EVERGREEN, not a trend. See POSTS-LOG.md.
- [ ] **Calibrating MMM with geo experiments.** MMM investment is up sharply for 2026 and the
      defensible setups anchor the model to experimental ground truth. Show the calibration
      step concretely: priors from a geo lift test, then the MMM. R + Python.
- [ ] **LLMs as synthetic survey respondents, and where they break.**
      Very hot in academic marketing. Run a small conjoint, compare LLM respondents against
      a human benchmark, report where WTP estimates diverge. High attention, high citation
      potential, directly feeds Marketing Research book.
- [ ] **Geo experiments when you can't randomize individuals.** Signal loss has erased a large
      share of trackable conversions. Geo tests survive it. Design + power analysis + code.
      Pairs naturally with the Experimental Design volume.
- [ ] **Synthetic control vs. matched-market tests.** Same problem, two traditions (Abadie vs.
      industry practice). Head-to-head on the same simulated data.
- [ ] **Honest DiD / sensitivity analysis.** Parallel trends is untestable, so show what to report
      instead of a pre-trend plot that "looks fine."
- [ ] **Agentic AI for research workflows.** What actually works in a real paper pipeline vs. demo
      hype. You have credibility here from the AI in Action book.
- [ ] **Doubly robust estimation, explained without the measure theory.** Trending on every
      "methods every data scientist should master" list, and almost all explanations are bad.

## EVERGREEN (search traffic that compounds)

- [ ] Power analysis for interaction effects (the thing everyone underpowers)
- [ ] Fixed effects vs. random effects, decided by what you're estimating not by a Hausman test
- [ ] Clustered standard errors: which level, and what happens when you get it wrong
- [ ] Multiple testing in marketing experiments without killing your power
- [ ] Regression discontinuity in loyalty tiers / credit score cutoffs (your data fits this)
- [ ] Bootstrapping when your panel is short and wide
- [ ] Reading a meta-analysis forest plot properly
- [ ] `renv` + Docker for a paper that still runs in five years
- [ ] Making a reproducible example (`reprex`) that people will actually answer

## ERROR-OF-THE-WEEK (friction log)

Append the moment something costs you time. One line is enough.

- [ ] (add here)

## SALVAGE (thin existing posts worth rebuilding)

These are already on the site at <300 words and rank for nothing. Rewriting one is cheaper
than a new post and improves an existing URL.

- [ ] `psychological-experiments` (65 w): expand into a real design primer
- [ ] `randomized-study-design` (66 w): merge with the geo experiments trend post
- [ ] `2021-10-14-experimentation-at-scale` (74 w): strong title, no content, so rebuild
- [ ] `scaling-shiny` (80 w) / `caching-for-faster-shiny-app` (61 w): merge into one real guide
- [ ] `use-dplyr-in-python-siuba-library` (77 w): refresh, siuba has moved on
- [ ] `new-pipe-in-r` (111 w): now settled, so rewrite as native pipe vs. magrittr in 2026
- [ ] `arrow` (113 w): Arrow is far more relevant now than in 2021, and worth a real benchmark

## SITE BUGS (found 2026-08-19)

- [ ] **Three live posts have broken plot images.** `config.toml` sets
      `ignoreFiles = [... "_files$" ...]`, so knitr's default `*_files/figure-html/` output is
      never copied to `public/`. The HTML still links to it. Affected:
      `2021-08-16-create-your-own-hexagon-in-r`, `2022-03-03-johnson-neyman-for-meta-analysis`,
      `r-rmarkdown`. Fix is `fig.path = "figs/"` in the setup chunk (now standard in the
      template) plus a re-render. Held back because re-rendering 2021 code under 2026 package
      versions may change more than the figure path, so your call.
- [ ] **Academic theme demo posts still live**: `getting-started`,
      `writing-technical-content`, `jupyter`. Same category of demo content you removed
      elsewhere in recent commits. Deleting published URLs is your call.

## INDUSTRY AND SEO TRACK (added 2026-08-20)

Posts do not have to be academic. The best ones sit where a commercially valuable search
query meets something Mike can actually execute rigorously. That overlap is the moat, because
the people writing for those queries today mostly cannot run the methods, and the people who
can run the methods mostly write for other academics.

### How to pick for SEO

1. **One post targets one primary query.** Write the query down before writing the post.
   If you cannot name it, the post has no search job.
2. **Prefer exact long-tail phrasing over broad terms.** "uplift modeling in R" beats
   "machine learning for marketing". Broad terms are already owned.
3. **New packages are an open window.** The first decent tutorial for a package ranks for
   years. `contdid` (May 2026) has essentially no practitioner content. So do `synthdid`,
   `HonestDiD`, `policytree`, and `fdid`.
4. **Error messages are free traffic.** People paste them verbatim into search. The existing
   expl3.sty and "cannot allocate vector of size" posts already work this way.
5. **Put the query in the H1, the URL slug, and the first paragraph.** Once each, naturally.
6. **Industry vocabulary, academic rigor.** Say incrementality, not ATE, in the title. Then
   be correct in the body. Titling it ATE loses the search, titling it incrementality and
   being sloppy loses the credibility.

### High-value candidates, all runnable with packages already installed

Commercial intent, low competition, and Mike has the tooling:

- [ ] **Uplift modeling and who to actually target.** `grf` plus `policytree`. Industry calls
      it uplift, academics call it CATE and policy learning. Very high commercial intent,
      almost no rigorous R content. Probably the single best SEO opportunity on this list.
- [ ] **Customer lifetime value the right way.** `CLVTools` and `BTYD`. High and steady
      search volume, and most existing content is a naive average-revenue formula.
- [ ] **Multi-touch attribution and why it disagrees with your incrementality test.**
      `ChannelAttribution`. Huge industry search, and the honest answer is genuinely useful.
- [ ] **Synthetic control for a market launch.** `synthdid` and `gsynth`. Industry framing is
      matched-market testing.
- [ ] **Spillovers between test and control markets.** `inferference`. Marketplaces and geo
      tests both break on interference, and nobody writes about it in R.
- [ ] **Honest DiD, or what to report instead of a pre-trend plot.** `HonestDiD`.
- [ ] **RFM segmentation, and when it misleads.** `rfm`. Very high search volume, mostly
      shallow content, easy to do better.
- [ ] **How long should an A/B test run.** Sequential testing and peeking. Perennial query.
- [ ] **Price elasticity from observational data.** `BLPestimatoR` and `micEconAids`.
- [ ] **Google Trends as a real covariate.** `gtrendsR`. Cheap to write, easy to rank.

### Rule for the mix

Roughly one industry or SEO post for every academic or method post. The Tuesday slot leans
trend and industry, the Friday slot leans evergreen and method. Neither slot is required to
be academic.
