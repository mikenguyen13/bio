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
