# The Twice-Weekly Routine

Two posts a week. Your total commitment is **30 minutes**, split as two 15-minute reviews.

---

## Your 15 minutes (per post)

Open the rendered draft and answer three questions. That's the whole job.

1. **Is the claim right?** The code ran and the numbers are real, but you're the one who
   knows if the framing would embarrass you in front of a co-author.
2. **Is the hook the right one?** If the first two sentences don't make an analytics lead
   or a reviewer keep reading, say so and I'll re-angle it.
3. **Ship, fix, or kill?** Kill is a legitimate answer. A killed draft costs you nothing and
   goes back in the backlog.

Then flip `draft: true` to `false`, or tell me to.

If a review is taking longer than 15 minutes, the draft was not ready. Say "too rough" and
I'll take it back. Don't spend your Saturday rescuing it.

---

## What is actually fixed, and what is not

Only the **publish days** are fixed, because readers and search engines reward a steady
cadence. Everything else is flexible.

The prep days below are a default rhythm, not a requirement. A trend scan done Wednesday
instead of Monday costs almost nothing, because these topics run for months rather than days.
MMM calibration and synthetic respondents will still be live subjects in October.

### The buffer is what makes missing a day survivable

**Keep two finished evergreen posts in reserve at all times.** They are written, rendered,
reviewed, and sitting at `draft: true`, ready to publish in under a minute.

That single rule absorbs almost every failure:

- Missed the trend scan? Publish a buffered evergreen on Tuesday instead. Readers never
  notice, because they don't know what was scheduled.
- Travelling, teaching, or deadline week? Ship from the buffer both days.
- Buffer runs dry? Drop to one post a week until it refills. One post a week forever beats
  two posts a week for a month followed by another 15-month silence.

Refilling the buffer is my job, not yours. When we have spare cycles I write ahead rather
than write more.

### Recovery rules

- **Missed a prep day.** Do nothing. Move the work to the next session.
- **Missed a publish day.** Do not double up to catch up, and do not apologize on the blog.
  Publish the next scheduled slot as if nothing happened.
- **Missed a full week.** Also fine. Restart at the next Tuesday. There is no debt to repay,
  and no streak to protect.

The only genuine failure mode is a month of silence, because that is the state we just spent
15 months in.

### How drafts actually arrive (set up 2026-08-20)

A scheduled cloud agent runs **Tuesday and Friday at 6am Pacific**. It researches, picks a
topic, writes the post, and commits it to a branch as `draft: true`. It cannot run R, so the
code it writes is unverified and it marks it as such.

Your two-step, twice a week:

1. Open a local session and say **"render and publish the new draft"**. Claude pulls the
   branch, runs every code block, fixes anything that breaks, renders, and rebuilds the site.
   About two minutes of waiting.
2. Review for 15 minutes using the three questions above. Then it ships.

The split exists because the cloud has no R, no pandoc, and no Hugo, and the standing rule is
that nothing publishes with code that was never executed. The cloud does the part that needs
research and writing. This machine does the part that needs a working R installation.

**If the rendered numbers contradict the draft's prose, the numbers win.** The cloud agent is
guessing at what the code will produce. Rewrite the prose around the real output rather than
tuning the code until it matches the story.

### One way to stop relying on memory

None of this runs unless you open a session. If you would rather not be the trigger, Claude
Code can run a scheduled cloud agent on a cron. It could do the Monday trend scan and have a
draft waiting for you Tuesday morning without you remembering anything. Say the word and I
will set it up.

---

## Claude's tasks

### Monday, trend scan (for Tuesday's post)
- Search what's moving this month in causal inference, marketing analytics, measurement,
  and applied ML. Check arXiv, industry blogs, R and Python release notes, conference programs.
- Update the TREND-JACK section of `IDEAS.md`, newest and hottest at the top.
- Pick one, draft it, run every code block, render, self-check against the house rules.
- Hand it over with a one-paragraph "why this, why now."

### Tuesday, publish the trend post
- Ship after your review. Push, verify live.
- Draft the LinkedIn framing (2 sentences plus link) for you to paste.

### Thursday, evergreen build (for Friday's post)
- Pull an EVERGREEN or SALVAGE item from `IDEAS.md`.
- Same drill: write, run, render, self-check.

### Friday, publish the evergreen post
- Ship, push, verify, log in `POSTS-LOG.md`.
- Append anything I hit during the week to the friction log.

### Monthly
- **Check the buffer first.** If it holds fewer than two finished posts, refilling it
  outranks everything else on this list.
- Analytics pass. Which posts pull traffic, which types to write more of.
- Refresh one old post (dead links, stale code, new package versions).
- Re-check the trend list from scratch, because trends decay fast.
- Report what shipped, what worked, and what to change.

---

## Distribution checklist (per post)

- [ ] Live URL verified
- [ ] LinkedIn post drafted
- [ ] R-heavy? Submit to R-bloggers / R Weekly. **One-time feed setup, then automatic, and
      likely the single biggest traffic multiplier available.**
- [ ] Method post? Consider r/rstats and Bluesky
- [ ] One link to the relevant book, in the post

---

## Standing quality bar

A post ships only if:
- Every code block was executed, not imagined
- Every empirical claim traces to output or a citation
- It reads in under 6 minutes
- Someone could reproduce the headline number from what's on the page
- It contains no em dash, no en dash, and no semicolon
