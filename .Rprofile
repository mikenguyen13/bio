# REMEMBER to restart R after you modify and save this file!

# First, execute the global .Rprofile if it exists. You may configure blogdown
# options there, too, so they apply to any blogdown projects. Feel free to
# ignore this part if it sounds too complicated to you.
if (file.exists("~/.Rprofile")) {
  base::sys.source("~/.Rprofile", envir = environment())
}

# The system library at C:/Program Files/R/R-4.4.3/library is not writable without
# admin, so packages installed here land in the per-user library instead. That
# directory is not on the default search path on this machine, and blogdown renders
# each post in a fresh R session, so without this a post using any user-installed
# package fails to knit with "there is no package called ...".
local({
  user_lib <- file.path(Sys.getenv("LOCALAPPDATA"), "R", "win-library", "4.4")
  if (nzchar(Sys.getenv("LOCALAPPDATA")) && dir.exists(user_lib)) {
    .libPaths(c(user_lib, .libPaths()))
  }
})

# Python for reticulate, so `{python}` chunks actually execute at render time.
# The `python` on PATH is a Microsoft Store stub that does nothing. The real
# interpreter is a uv-managed CPython 3.12 in a venv outside the repo, created with
#   uv venv --python 3.12 C:/Users/miken/.venvs/bio-blog
# Keep this out of individual posts so no published .Rmd carries a machine path.
local({
  py <- "C:/Users/miken/.venvs/bio-blog/Scripts/python.exe"
  if (file.exists(py)) Sys.setenv(RETICULATE_PYTHON = py)
})

# Now set options to customize the behavior of blogdown for this project. Below
# are a few sample options; for more options, see
# https://bookdown.org/yihui/blogdown/global-options.html
options(
  # to automatically serve the site on RStudio startup, set this option to TRUE
  blogdown.serve_site.startup = TRUE,
  # to disable knitting Rmd files on save, set this option to FALSE
  blogdown.knit.on_save = TRUE,
  # build .Rmd to .html (via Pandoc); to build to Markdown, set this option to 'markdown'
  blogdown.method = 'html',
  blogdown.ext = ".Rmd", 
  blogdown.author = "Mike Nguyen"
)

# fix Hugo version
# options(blogdown.hugo.version = "0.91.0")
options(blogdown.hugo.version = "0.113.0")
