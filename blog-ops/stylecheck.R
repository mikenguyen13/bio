#!/usr/bin/env Rscript
# Check a draft against the house style rules and report its prose length.
#   Rscript blog-ops/stylecheck.R content/post/<dir>/index.en.Rmd
#
# Why this exists rather than a grep one-liner: `grep -P` is not available in the
# Git Bash on this machine ("-P supports only unibyte and UTF-8 locales"), so the
# obvious `grep -P '[\x{2013}\x{2014}]' file || echo CLEAN` prints CLEAN when grep
# ERRORS, not when the file is clean. That is a false pass on the one check that
# matters most. Fixed-string matching in R has no such failure mode.
#
# Note: run this as a script file. `Rscript -e` segfaults through Git Bash here.
#
# This script is the one file that cannot be run against itself. The `banned`
# vector below literally contains all three characters, so it reports three
# failures on that line. Expected, not a bug.
#
# The same is true of the ops docs, which quote the banned characters as
# counter-examples: README.md carries an en dash inside "Callaway-Sant'Anna"
# shown as the thing never to write, and README, IDEAS and POSTS-LOG all quote a
# bare dollar sign while documenting the MathJax trap. Run this on POSTS, where a
# failure is always real.

args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 1) stop("Usage: Rscript blog-ops/stylecheck.R <path to .Rmd>")
f <- args[1]
if (!file.exists(f)) stop("No such file: ", f)

x <- readLines(f, warn = FALSE, encoding = "UTF-8")

banned <- c("em dash" = "—", "en dash" = "–", "semicolon" = ";")
fail <- FALSE
for (nm in names(banned)) {
  hit <- grep(banned[[nm]], x, fixed = TRUE)
  if (length(hit)) {
    fail <- TRUE
    cat(sprintf("FAIL  %-10s on line(s) %s\n", nm, paste(hit, collapse = ", ")))
    cat(paste0("        ", x[hit]), sep = "\n")
  } else {
    cat(sprintf("ok    %-10s none\n", nm))
  }
}

# Bare dollar signs in prose. The Wowchemy theme loads MathJax 3 with the default
# TeX delimiters, so any PAIR of `$` in rendered prose is silently eaten as inline
# math. A pricing post that wrote "$24 ... $25 ... $85" shipped with a whole
# sentence rendered as an italic equation. MathJax ignores <pre> and <code>, so
# `$obs` and `d$price` inside chunks are safe and are not checked here.
# Write "24 dollars" instead, or spell the currency out.
fence_d  <- grepl("^```", x)
in_code  <- cumsum(fence_d) %% 2 == 1
prose_ln <- which(!in_code & !fence_d)
# Strip inline `code` spans first, since a $ inside those renders literally.
stripped <- gsub("`[^`]*`", "", x[prose_ln])
bad_d <- prose_ln[grepl("\\$[0-9]", stripped) | grepl("\\\\\\$", stripped)]
if (length(bad_d)) {
  fail <- TRUE
  cat(sprintf("FAIL  %-10s on line(s) %s\n", "bare $",
              paste(bad_d, collapse = ", ")))
  cat(paste0("        ", x[bad_d]), sep = "\n")
  cat("        MathJax will pair these. Write the word dollars instead.\n")
} else {
  cat(sprintf("ok    %-10s none\n", "bare $"))
}

# Prose length, excluding code and front matter. House rule is 600 to 1200.
# Three things are code rather than prose: fenced chunks, the YAML header, and
# four-space-indented literal blocks, which markdown renders as <pre><code>.
fence  <- grepl("^```", x)
inside <- cumsum(fence) %% 2 == 1
indented <- grepl("^    \\S", x) & !inside
yaml_end <- which(x == "---")
prose <- x[!inside & !fence & !indented]
if (length(yaml_end) >= 2) {
  drop <- sum(!inside[seq_len(yaml_end[2])] & !fence[seq_len(yaml_end[2])] &
              !indented[seq_len(yaml_end[2])])
  prose <- prose[-seq_len(drop)]
}
w <- unlist(strsplit(paste(prose, collapse = " "), "[[:space:]]+"))
n <- sum(nzchar(w))
cat(sprintf("\nprose words: %d  (house rule: 600 to 1200) %s\n", n,
            if (n >= 600 && n <= 1200) "ok" else "OUT OF RANGE"))

quit(status = if (fail) 1 else 0)
