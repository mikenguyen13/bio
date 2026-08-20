#!/usr/bin/env Rscript
# Scaffold a new post folder from the template.
#   Rscript blog-ops/new_post.R "My Post Title" [YYYY-MM-DD]

args  <- commandArgs(trailingOnly = TRUE)
if (length(args) < 1) stop("Usage: Rscript blog-ops/new_post.R \"Post Title\" [date]")

title <- args[1]
date  <- if (length(args) >= 2) args[2] else format(Sys.Date(), "%Y-%m-%d")
stamp <- format(Sys.time(), "%Y-%m-%dT%H:%M:%S-07:00")

slug <- tolower(title)
slug <- gsub("[^a-z0-9]+", "-", slug)
slug <- gsub("(^-|-$)", "", slug)

root <- file.path("content", "post", paste0(date, "-", slug))
if (dir.exists(root)) stop("Already exists: ", root)
dir.create(root, recursive = TRUE)

tpl <- readLines(file.path("blog-ops", "templates", "post-template.Rmd"), warn = FALSE)
tpl <- sub("^title: TITLE$", paste0("title: ", title), tpl)
tpl <- sub("^slug: SLUG$", paste0("slug: ", slug), tpl)
tpl <- sub("^date: 'YYYY-MM-DD'$", paste0("date: '", date, "'"), tpl)
tpl <- sub("^lastmod: 'YYYY-MM-DDTHH:MM:SS-07:00'$", paste0("lastmod: '", stamp, "'"), tpl)

out <- file.path(root, "index.en.Rmd")
writeLines(tpl, out)
cat("Created", out, "\n")
cat("Render with: blogdown::build_site(build_rmd = TRUE)\n")
