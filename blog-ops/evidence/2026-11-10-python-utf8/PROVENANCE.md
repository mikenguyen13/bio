# Provenance: python-3-15-utf-8-windows

Draft for Tuesday 2026-11-10, written 2026-11-09. Every factual claim in the post, where it came
from, and how it was checked.

Post source: `content/post/2026-11-10-python-3-15-utf-8-windows/index.en.Rmd`, with
`encoding_audit.py` beside it.

## Data

No third-party data. The six names and the three cp1252 names are written in the post. The
character universe is every assigned code point in the Unicode database that ships with Python
3.15.2 (Unicode 17.0.0), generated at render time. Every file the post writes goes to a scratch
folder under `tempdir()`, never into the post folder. House rule 7 is satisfied trivially.

## Determinism

Nothing in the post is random, so every number is identical on every render on this machine.
Two full renders on 2026-11-09 gave the same output. The prose is inline over computed objects,
and `stopifnot` halts the render if any of these stop holding:

- the interpreters are exactly 3.14.10 and 3.15.2, with default encodings cp1252 and utf-8
- the six names are NFC, and 3.14 gets 3 silently wrong and raises on 3, while 3.15 gets 6 right
- 159,706 characters, 0 right under 3.14, 82% silent after rounding, 123 writable by 3.14, all
  123 raise under 3.15 (these back the title and summary)
- all 11 cells of the handoff table under each version, exactly as the prose describes them
- R reads the 3.14-written cp1252 file correctly with `read.csv(fileEncoding = "cp1252")`

## Versions

| Software | Version used | Current release when checked (2026-11-09) |
|---|---|---|
| Python 3.15 | 3.15.2 (`C:/Users/miken/.venvs/py315`, via `PY315_PYTHON` in `.Rprofile`) | 3.15.2, released 2026-10-25 (python.org/downloads) |
| Python 3.14 | 3.14.10 (`C:/Users/miken/.venvs/py314`, via `PY314_PYTHON`) | 3.14.10, released 2026-10-25 |
| pandas | 3.1.1 in both venvs | 3.1.1, the latest on PyPI at install |
| R | 4.4.3 (ucrt) | R 4.6.2 is current (29 October 2026 per Wikipedia, not checked on CRAN). The behavior tested, UTF-8 as the native encoding, dates from 4.2.0 and is unchanged since |
| uv | 0.13.7 | Upgraded from 0.9.14 to get 3.15 final builds. 0.9.14 only listed 3.15.0a2 |

## Claims and their sources

| Claim | Source | How checked |
|---|---|---|
| Python 3.15 released 9 October 2026 | What's New in Python 3.15, docs.python.org/3.15/whatsnew/3.15.html | Fetched 2026-11-09. The page says "Python 3.15 was released on 9 October 2026" |
| 3.15 uses UTF-8 when no encoding is given, opt out with `PYTHONUTF8=0` or `-X utf8=0` | Same page, "Other language changes", and PEP 686 | Fetched 2026-11-09. Also measured: `utf8_mode` 0 against 1, open default cp1252 against utf-8 |
| 3.14.10 and 3.15.2 are the current releases | python.org/downloads | Fetched 2026-11-09. Both dated 25 October 2026 |
| R 4.2.0 (April 2022) made UTF-8 the native encoding on Windows | Tomas Kalibera, "Issues While Switching R to UTF-8 and UCRT on Windows", R blog, 2022-11-07 | Fetched 2026-11-09 |
| cp1252 leaves 0x81, 0x8D, 0x8F, 0x90, 0x9D undefined | Executed in the post (`mechanism` chunk) | Python's own cp1252 codec |
| 82% silent, 18% raise, 0 right, by block | Executed in the post (`exhaustive` chunk) | Every code point, both interpreters |
| `subprocess.run()` returns `stdout = None` when the reader thread fails to decode | Executed in the post (handoff table), and CPython source | `Lib/subprocess.py` line 1682 at tag v3.14.10 reads `stdout = stdout[0] if stdout else None`. The same line is at 1848 in v3.15.2. Both fetched raw from GitHub 2026-11-09 |
| pandas assumes UTF-8 regardless of locale | Executed in the post | pandas row right under both versions, cp1252 row raises under both |
| `-X warn_default_encoding` exists since 3.10 | PEP 597 (Python 3.10) | Known from the PEP, and executed under 3.14 in the post |
| `PYTHONUTF8` and `-X utf8` exist since 3.7 | PEP 540 (Python 3.7) | Known from the PEP, and `-X utf8` executed under 3.14 in the post |
| Nguyễn is the most common Vietnamese surname | General knowledge | Not separately cited. "and mine" is an inference from Mike's name, flagged in REVIEW-NOW |

## Known issue search (house rule 6)

Searched for a CPython issue matching the `subprocess` reader-thread behavior on 2026-11-09.
Nothing matched exactly. Closest: bpo-27179 (2016, subprocess decoding with the ANSI code page on
Windows), bpo-43431 (decoding on timeout), and gh-82388 (Windows reader threads hanging). The post
describes the behavior and links the source line rather than calling it a bug.
