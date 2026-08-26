# Blog Ops

A two-post-per-week publishing system for <https://mikenguyen.netlify.app/>.

## The contract

| Who | Does what | Time |
|---|---|---|
| Claude | Picks topic, researches trend, writes, runs all code, renders, self-checks | all of it |
| Mike | Reads the draft, answers 3 questions, says ship / fix / kill | **15 min per post, max** |

Drafts land in `content/post/<date>-<slug>/` with `draft: true` in the front matter.
Nothing goes live until you flip that flag.

## Files

- `IDEAS.md` is the backlog. Trend-jack candidates at the top, evergreens below, salvage list at the bottom.
- `WEEKLY.md` is the twice-weekly routine, split into Claude's tasks and your 15 minutes.
- `POSTS-LOG.md` records what shipped, when, and how it performed.
- `templates/post-template.Rmd` holds the standard front matter and section skeleton.
- `new_post.R` scaffolds a dated post folder from the template.

## Cadence

- **Tuesday** is the trend-jack post. Timely, opinionated, tied to something moving in the field this month.
- **Friday** is the evergreen post. A method, a fix, a workflow. Built to rank in search for years.

## House rules for every post

1. One idea. 600 to 1,200 words.
2. Code that runs. R first (this machine can execute it), Python second where it adds reach.
3. A number or a plot in the first screen. Show the result before explaining it.
4. Ends with one link to the relevant book. One, not five.
5. No claim in a post that wasn't executed or cited.

## Style rules

**Never use em dashes, en dashes, or semicolons.** Not in posts, not in these ops docs, not
anywhere written in Mike's voice. Rewrite the sentence instead of substituting another
separator. Use a period, a comma, a colon, parentheses, or a restructured clause.

Hyphens in compound words are fine (market-weeks, Goodman-Bacon). Hyphenate paired author
names rather than reaching for an en dash, so "Callaway-Sant'Anna" and never
"Callaway–Sant'Anna". Semicolons inside code are syntax rather than style, but split the
statement across two lines anyway so none appears on the page.

Check for all three characters before handing over any draft.

## Where things live

Everything needed to run this system, so no knowledge depends on a chat session existing.

| Thing | Where |
|---|---|
| Live site | <https://mikenguyen.netlify.app> |
| Repo | <https://github.com/mikenguyen13/bio> (Netlify deploys from `public/` on push to master) |
| Scheduled routine | `trig_01AVRDPRKvtTVMr2K83foFQ5` <https://claude.ai/code/routines/trig_01AVRDPRKvtTVMr2K83foFQ5> |
| Routine schedule | `0 13 * * 2,5` UTC, which is Tue and Fri 6am Pacific |
| Pending uplift draft | <https://claude.ai/code/session_01UsRVfrgjSQ1aVYJhNVdPFQ> (patch attached, see REVIEW-NOW.md) |
| First post review page | <https://claude.ai/code/artifact/a1b9e177-6f4a-4fa1-9484-3b1b2f61e7ec> |

## Local environment notes

Rendering needs this machine. The cloud routine cannot do it.

- R lives at `C:\Program Files\R\R-4.4.3`. Its library is not writable without admin, so extra
  packages go to the per-user library at `%LOCALAPPDATA%\R\win-library\4.4`.
- **That per-user library is not on R's default search path here**, and blogdown renders each
  post in a fresh R session, so a post using a newly installed package used to fail with
  "there is no package called ...". The repo `.Rprofile` now prepends it to `.libPaths()`.
  Leave that block in place. When installing, still pass `lib =` explicitly, because
  `R_LIBS_USER` is empty in this environment and `install.packages` otherwise aims at the
  unwritable system library.
- Pandoc is not on the PATH. Before rendering, run:
  `Sys.setenv(RSTUDIO_PANDOC = "C:/Program Files/RStudio/resources/app/bin/quarto/bin/tools")`
- Render one post with:
  `blogdown::build_site(build_rmd = "content/post/<dir>/index.en.Rmd", run_hugo = FALSE)`
  then `blogdown::hugo_build()` to refresh `public/`.
- Hugo is pinned to 0.113.0 in `.Rprofile`.
- `install.packages` segfaults when run through the Git Bash shell on this machine. Run it
  through PowerShell, or from a script file, instead of an inline `-e` expression.
- There is no working Python here. The `python.exe` on the PATH is a Microsoft Store stub, and
  WSL fails to start because Docker's distro is missing its disk image. Any Python in a post is
  therefore unverified unless it is run elsewhere.

## Commit convention

Commits are authored as `mike <nguyennghia1301@gmail.com>`. Never add a Co-Authored-By trailer
and never mention Claude or AI in a commit message. This applies to the cloud routine too.
