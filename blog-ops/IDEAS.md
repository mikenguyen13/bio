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

## THE DIVERSIFY RULE (added 2026-08-28)

**Never ship three consecutive posts from the same methodological family.** Check the last three
rows of POSTS-LOG.md before picking. If all three sit in the same lane, the next post leaves that
lane even if a better idea exists inside it.

This rule exists because the first four posts were all causal inference and applied stats: TWFE,
continuous-dose DiD, MMM calibration, and an interaction power post that got killed on review for
exactly this reason. Each was individually fine. Together they read as a single-subject blog, and
that is not what this site is.

The site covers tech, coding, AI, and data work, not only econometrics. Mike's stats rigor is the
*advantage* he brings to those topics, not the topic itself. An AI post written with real
measurement discipline is more differentiated than another causal inference post, because almost
nobody in the AI-tooling space measures anything properly.

The lanes, so "same family" is unambiguous:

1. **Causal inference and experiments** (DiD, geo tests, power, uplift)
2. **Marketing and measurement** (MMM, attribution, CLV)
3. **AI and LLM engineering** (tokenizers, embeddings, RAG, agents, evals)
4. **Coding and tooling** (R and Python performance, Arrow, reproducibility, workflow)
5. **Career and research process** (writing, reviewing, project management)

Lanes 3 and 4 are badly underweighted. Prefer them until the log balances.

## TREND-JACK (hot right now, Aug 2026, recheck monthly)

Re-audited against the freshness rule on 2026-08-20. Ages shown.

These sit where industry money and academic method overlap. That intersection is where
your audience actually is: analytics leads who read papers, and academics who want their
methods used.

- [x] **Staggered geo rollouts break TWFE.** SHIPPED 2026-08-20 as an EVERGREEN, not a trend. See POSTS-LOG.md.
- [x] **Calibrating MMM with geo experiments.** SHIPPED 2026-08-28, and the angle inverted on
      contact with the data. The recommended recipe (prior mean and scale taken straight from
      the experiment) left video ROI 77% high, because the misspecified MMM likelihood is
      sharper than the experiment. See POSTS-LOG.md. Two follow-ups fell out of it and are
      listed below.
- [ ] **The disagreement statistic as a standing MMM diagnostic.** This post introduced it in
      one line. It deserves its own short evergreen: how far apart can a model and an
      experiment be before the model is disqualified, and what to do at each threshold.
- [ ] **Saturation curves change what an ROI prior even means.** The calibration post used a
      linear response so ROI was a single number. Under a Hill curve, ROI depends on spend
      level, and an experiment run at last year's budget calibrates the wrong point on the
      curve. Nobody writes this down. The calibration post gives this one sentence, so the
      follow-up has room to do it properly with an actual Hill curve.
- [ ] **Meridian in anger, from R.** UNBLOCKED 2026-08-26. Meridian 1.8.0 is installed in the
      blog venv and runs, `reticulate` reaches it, and `{python}` chunks execute at render time.
      The calibration post only touches its prior helper. The real post is fitting an actual
      Meridian model from an R workflow and rerunning this post's experiment against it, which
      would answer the one question the calibration post has to leave open: how much of the
      77% overstatement survives a hierarchical geo-level model. Nobody has written Meridian
      from R at all, so the search window is wide open.
- [~] **LLMs as synthetic survey respondents, and where they break.** DRAFTED 2026-09-08 as
      `synthetic-respondents-conjoint-analysis`. The angle narrowed on contact with the
      literature: rather than running LLM respondents (which cannot be done reproducibly at
      render time), the post takes the documented variance compression as given and prices its
      consequence through a mixed logit and a market simulator. Two follow-ups fell out of it,
      listed below.
- [ ] **Does hierarchical Bayes shrinkage compound the synthetic-panel collapse?** The conjoint
      post estimates with `logitr` maximum simulated likelihood and notes in one sentence that
      HB adds its own shrinkage on top, so a real workflow is probably worse than the post
      shows. `bayesm` is installed. Fitting the same two panels with `rhierMnlRwMixture` and
      comparing the individual-level posterior spread against the truth would settle it.
- [ ] **How small can the human pilot be and still catch the collapse?** The conjoint post
      recommends keeping humans in the study and shows the variance-ratio screen is noisy at
      n = 300. The useful version is a power curve: pilot size against probability of detecting
      a given compression factor. That turns the post's closing advice into a number.
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

- [ ] Power analysis for interaction effects (the thing everyone underpowers). DRAFTED and
      **KILLED on review 2026-08-28**. Nothing wrong with the draft (numbers verified three ways,
      15% power against 80%, 2.6x Type M exaggeration). It was killed on **topic mix**: it would
      have been the fourth causal-inference and stats post in a row. The draft is recoverable from
      git history at commit 67f42d4 if this ever gets pulled again. See the DIVERSIFY rule below.
- [ ] **Type M and Type S error for any experiment, not just interactions.** The interaction post
      shows the significance filter inflating a subgroup effect 2.6x and spends four sentences on
      it. The general version (Gelman and Carlin design analysis, `retrodesign`) applies to every
      underpowered test on the site and to most A/B readouts. It answers the question people
      actually have, which is what to believe about a result that already came back significant.
- [ ] **Interaction power under cluster randomization.** The interaction post assumes independent
      observations. Geo tests randomize markets, so the design effect multiplies the 4x variance
      penalty by another `1 + (m - 1) * ICC`. That compounding is why geo tests essentially never
      resolve a moderator, and it connects directly to the geo experiments item above.
- [ ] **Does `bench::mark`'s minimum survive what its median does not?** The benchmarking post
      shows block ordering biasing a median-based comparison and explicitly does not test whether
      the minimum `bench::mark` also reports is robust to the same GC spikes. It should be, in
      theory, and that is exactly the kind of theory worth checking. Short, self-contained, and it
      closes the one loose end that post names.
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

- [x] 2026-08-26: `geom_segment()` with numeric `y`/`yend` against a discrete y axis throws
      "Example values: search, social, and video" from `scale_y_continuous`. Dodge by hand onto
      a continuous axis with `scale_y_continuous(breaks =, labels =)` instead.
- [ ] 2026-08-26: `bookdown.org/mike/*` now 301 redirects to
      `mike-data-analysis.share.connect.posit.cloud`. Links still resolve, so no action is
      forced, but every book CTA on the site is one hop from broken if that redirect lapses.
- [x] 2026-08-28: **Unicode text is silently recomposed by ordinary tooling, and it corrupted a
      post's central finding twice before it was caught.** Decomposed (NFD) text pasted through an
      editor, a clipboard, or a tool result comes back composed (NFC). The Unicode post measures
      exactly that difference, so every attempt to embed the decomposed sample as a literal in the
      `.Rmd` destroyed the thing being measured, and the post rendered a confident "0 of the 11"
      where the truth is 1 of 11. Escaping to `\uXXXX` by hand failed too, for the same reason.
      The fix that works: have a script write the corpus to a data file straight from the upstream
      source, never routing the bytes through an editor, and have the post read that file. General
      lesson: when the bytes are the subject, do not let any hand-editing step touch them.
- [x] 2026-08-28: `install`ing a package that needs a C++ toolchain fails here. `hnswlib` dies in
      `uv pip install` with an MSVC build error, so anything needing compilation from source is
      out unless a wheel exists. `tiktoken` has wheels and installs in under a second.
- [x] 2026-08-28: printing non-ASCII from Python through Git Bash raises
      `UnicodeEncodeError: 'charmap' codec` because the console defaults to cp1252. Set
      `PYTHONIOENCODING=utf-8` on the command. Does not affect knitr, which handles it correctly.
- [x] 2026-08-28: **the em dash style check can report a false pass.** `grep -P` is unavailable in
      this Git Bash ("-P supports only unibyte and UTF-8 locales"), so the usual
      `grep -P '[\x{2013}\x{2014}]' file || echo CLEAN` prints CLEAN because grep *errored*, not
      because the file was clean. Check with fixed strings instead, from an R script file rather
      than `Rscript -e`, which segfaults here. Working version at
      `blog-ops/stylecheck.R`.

- [x] 2026-08-31: **`bench::mark` runs all iterations of one expression before the next, and has no
      option to interleave.** Verified by instrumenting the expressions to log themselves:
      `a b a a a a a a b b b b b b`. `microbenchmark` shuffles by default
      (`control$order` defaults to `"random"`, with `"inorder"` and `"block"` also available).
      For any close head-to-head, reach for `microbenchmark`. Use `bench::mark` for memory
      accounting, which it does far better.
- [x] 2026-08-31: **a benchmark run inside a knit session is much more biased than one in a fresh
      session.** Same code, same machine, same hour: the knitting session measured a 12.7%
      positional artifact between two identical functions, eight fresh `callr` sessions averaged
      1.0%. Cause not isolated. Heap size is the obvious suspect and did **not** reproduce it when
      tested with ballast, so something else is doing the work. Practical rule: benchmark from
      `callr::r()`, not from the session you have had open all day.
- [x] 2026-09-08: **a dollar sign in prose is eaten by MathJax and can swallow a whole
      sentence.** The Wowchemy theme loads MathJax 3 with default TeX delimiters, so any PAIR of
      `$` in rendered prose becomes inline math. The conjoint post shipped live with "worth $24
      to the average buyer. Prices tested in the survey run from $25" rendered as one italic
      equation reading `24totheaveragebuyer.Pricestestedinthesurveyrunfrom`, with an orphaned
      "$85" left after it. Escaping as `\$` in the Rmd does NOT help, because pandoc turns it
      back into a literal `$` in the HTML and MathJax sees it in the DOM. `$` inside chunks and
      inline backticks is safe, because MathJax skips `pre` and `code`, which is why `d$price`
      never broke. Fix is to write the word dollars. `blog-ops/stylecheck.R` now fails on a bare
      `$` in prose, and the other six 2026 posts were checked clean.
- [x] 2026-09-08: **`logitr` silently returns a garbage fit if you give a lognormal random
      parameter the wrong sign.** `randPars = c(price = "ln")` on a raw price column converged
      without complaint and reported a log-mean of -16, meaning a price coefficient of about
      1e-7. The lognormal is constrained positive, so the variable has to enter negated. Build a
      `negPrice = -price` column and use `randPars = c(negPrice = "ln")`. No warning is issued,
      and the model still prints "Done!", so this fails quietly.
- [x] 2026-09-08: **a naive Monte Carlo market simulator over a price grid is quadratic and will
      blow a render budget.** 4e5 draws over 300 grid points timed out past 120s. Two fixes,
      both needed: draw the population once outside the grid loop rather than per price, and use
      common random numbers (one `set.seed` before the draw, reused across the whole grid) so the
      profit curve is smooth and its argmax is well determined at far fewer draws. 8e4 draws with
      common random numbers located the same optimum as 24-node Gauss-Hermite quadrature.
- [x] 2026-08-31: **prose that hardcodes a direction will eventually contradict its own output.**
      The first draft of the benchmarking post said "the first slot is measured as X% faster" with
      X computed inline and "faster" written by hand. The render came back with the first slot
      *slower* and the sentence shipped backwards. Fix that now stands in that post: compute the
      direction word too (`dirw()`), and write every comparative sentence so the data supplies both
      the number and the word. Cheap insurance for any post whose numbers move between renders.

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

- [ ] **The Text Analysis book returns 403 and is linked from the books page.** Found 2026-08-28
      while looking for a CTA for the tokenization post.
      `https://bookdown.org/mike/text_analysis/` returns HTTP 403, while
      `https://bookdown.org/mike/data_analysis/` returns 200 from the same client, so this is not
      bot blocking. It is linked from `content/books/written_books/_index.md`. Worth checking the
      other books on that page the same way, since only these two were tested. The tokenization
      post routes its CTA to [AI in Action](https://mikenguyen13.github.io/ai_in_action/) instead,
      which returns 200 but currently renders only a preface, so it is a thin landing page for a
      reader arriving from a post.

- [ ] **Broken plot images. Re-audited 2026-08-26 against `public/` and against the live site,
      and the earlier entry undercounted.** `config.toml` sets `ignoreFiles = [... "_files$" ...]`,
      so knitr's default `*_files/figure-html/` output never reaches `public/` while the HTML
      still links to it. Every reference below was confirmed 404 on the live site.

      Real posts, three as originally listed. **URLs corrected 2026-08-28** after re-verifying
      against the live site: the entry previously gave the `content/` folder names, which are not
      the published URLs and simply 404, so anyone checking this would conclude the bug was fixed.
      The live URLs and the exact missing files are:

      | Live URL | 404s on |
      |---|---|
      | `/post/create-your-own-hexagon-in-r/` | `index.en_files/figure-html/unnamed-chunk-1-1.png` |
      | `/post/johnson-neyman-for-meta-analysis/` | `index.en_files/figure-html/unnamed-chunk-4-1.png` |
      | `/post/r-rmarkdown/` | `index_files/figure-html/pie-1.png` |

      Note the first two reference `index.en_files/`, not the `_files/` the entry implied, and the
      third references `index_files/`. Both are caught by the `_files$` ignore rule.

      Fix is `fig.path = "figs/"` in the setup chunk (now standard in the template) plus a
      re-render. Still held back because re-rendering 2021 code under 2026 package versions may
      change more than the figure path, so your call.
- [ ] **Three orphaned duplicate URLs of the same demo post are live with no source.**
      `content/post/r-rmarkdown/` is the stock blogdown demo ("Hello R Markdown", 2020-11-23),
      and it is published four times: `/post/r-rmarkdown/`, `/post/hello-r-markdown/`,
      `/post/2015-07-23-r-rmarkdown/`, and `/post/copyofr-rmarkdown/`. Only the first has a
      source in `content/`. The other three are committed `index.html` files in `public/` that
      Hugo does not manage and therefore never cleans, so they will survive every rebuild
      forever. All four have broken images. Deleting the three orphans is a `git rm` of
      `public/post/{hello-r-markdown,2015-07-23-r-rmarkdown,copyofr-rmarkdown}` and removes
      nothing that any source generates, but it does remove live URLs, so your call.
- [ ] **Two theme demo posts link a dead external image.**
      `getting-started` and `academic-the-website-builder-for-hugo` both embed
      `raw.githubusercontent.com/gcushen/hugo-academic/master/academic.png`, which 404s. Moot if
      the demo posts get deleted, which is the item below.
- [ ] **Academic theme demo posts still live**: `getting-started`,
      `writing-technical-content`, `jupyter`, and now also the whole `r-rmarkdown` family above,
      which is stock blogdown demo content rather than anything you wrote. Same category of demo
      content you removed elsewhere in recent commits. Deleting published URLs is your call.

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

## RESOLVED FRICTION (2026-08-26)

- **"There is no working Python here" was wrong for weeks and blocked real work.** `uv` was
  already installed and already had four CPython builds. The Microsoft Store stub on the PATH
  and the broken WSL were both real, and both were dead ends that nobody looked past. Lesson
  worth keeping: when an environment note says something is impossible, check whether it says
  *impossible* or just *the first two things I tried failed*.
