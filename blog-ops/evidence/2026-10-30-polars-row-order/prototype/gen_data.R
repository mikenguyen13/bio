source("C:/Users/miken/github/bio/.Rprofile")
out <- commandArgs(trailingOnly = TRUE)[1]
set.seed(20261030)
n_cust <- 100000L
n_ev <- 2000000L
customers <- data.frame(customer_id = 0:(n_cust - 1L),
                        segment = sample(c("a", "b", "c", "d"), n_cust, TRUE))
events <- data.frame(event_id = 0:(n_ev - 1L),
                     customer_id = sort(sample.int(n_cust, n_ev, TRUE) - 1L),
                     amount = round(rgamma(n_ev, shape = 2, scale = 20), 2))
arrow::write_parquet(events, file.path(out, "events.parquet"))
arrow::write_parquet(customers, file.path(out, "customers.parquet"))
cat("wrote", nrow(events), nrow(customers), "\n")
