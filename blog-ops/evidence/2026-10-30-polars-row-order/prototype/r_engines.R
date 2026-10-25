source("C:/Users/miken/github/bio/.Rprofile")
suppressPackageStartupMessages({
  library(data.table)
  library(dplyr)
  library(arrow)
})
dir <- commandArgs(trailingOnly = TRUE)[1]
ep <- file.path(dir, "events.parquet")
cp <- file.path(dir, "customers.parquet")
ev <- read_parquet(ep)
cu <- read_parquet(cp)

# Truth: the first purchase per customer, by event order
truth <- as.data.table(ev)[order(event_id), .(amount = amount[1L]), by = customer_id][order(customer_id)]

check <- function(label, f, runs = 20) {
  outs <- lapply(seq_len(runs), function(i) f())
  wrong <- sum(vapply(outs, function(o) !isTRUE(all.equal(o$amount, truth$amount, tolerance = 0)), TRUE))
  distinct <- length(unique(vapply(outs, function(o) digest::digest(o$amount), "")))
  cat(sprintf("%-28s runs wrong %2d/%d  distinct %2d\n", label, wrong, runs, distinct))
}

DT_ev <- as.data.table(ev)
DT_cu <- as.data.table(cu)
check("data.table", function() {
  j <- DT_cu[DT_ev, on = "customer_id"]
  j[, .(amount = amount[1L]), by = customer_id][order(customer_id)]
})
check("dplyr", function() {
  left_join(ev, cu, by = "customer_id") |>
    summarise(amount = first(amount), .by = customer_id) |> arrange(customer_id)
})
check("arrow (Acero), join then collect", function() {
  j <- open_dataset(ep) |> left_join(open_dataset(cp), by = "customer_id") |> collect()
  as.data.table(j)[, .(amount = amount[1L]), by = customer_id][order(customer_id)]
})
# Does arrow's join keep event order?
o <- open_dataset(ep) |> left_join(open_dataset(cp), by = "customer_id") |> collect()
cat("arrow join output sorted by event_id:", !is.unsorted(o$event_id), "\n")
