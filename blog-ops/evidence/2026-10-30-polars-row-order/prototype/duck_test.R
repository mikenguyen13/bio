source("C:/Users/miken/github/bio/.Rprofile")
suppressPackageStartupMessages({
  library(data.table)
  library(DBI)
})
dir <- normalizePath(commandArgs(trailingOnly = TRUE)[1], winslash = "/")
ep <- file.path(dir, "events.parquet")
cp <- file.path(dir, "customers.parquet")
ev <- as.data.table(arrow::read_parquet(ep))
truth <- ev[order(event_id), .(amount = amount[1L]), by = customer_id][order(customer_id)]
con <- dbConnect(duckdb::duckdb())
cat("duckdb", as.character(packageVersion("duckdb")), " threads",
    dbGetQuery(con, "SELECT current_setting('threads') AS t")$t, "\n")
sql <- function(agg) sprintf(
  "SELECT customer_id, %s AS amount
   FROM read_parquet('%s') e LEFT JOIN read_parquet('%s') c USING (customer_id)
   GROUP BY customer_id ORDER BY customer_id", agg, ep, cp)
run <- function(agg, R = 20) {
  w <- vapply(seq_len(R), function(i) sum(dbGetQuery(con, sql(agg))$amount != truth$amount), 1)
  cat(sprintf("%-38s runs wrong %2d/%d  max customers %d\n", agg, sum(w > 0), R, max(w)))
}
run("first(amount)")
run("first(amount ORDER BY event_id)")
run("arg_min(amount, event_id)")
dbDisconnect(con, shutdown = TRUE)
