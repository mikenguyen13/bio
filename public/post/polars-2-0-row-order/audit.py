# Run order-dependent Polars queries with default settings and compare each
# result with the same query written so the order is explicit.
import hashlib

import polars as pl


def queries(events, customers, explicit):
    if explicit:
        j = events.join(customers, on="customer_id", how="left", maintain_order="left")
    else:
        j = events.join(customers, on="customer_id", how="left")   # the default
    return {
        "first purchase per customer":
            j.group_by("customer_id").agg(pl.col("amount").first()).sort("customer_id"),
        "running total per customer":
            j.with_columns(running=pl.col("amount").cum_sum().over("customer_id"))
             .sort("event_id").select("event_id", "running"),
        "dedupe, keep first":
            j.unique(subset="customer_id", keep="first").sort("customer_id")
             .select("customer_id", "event_id"),
        "row index, first 1,000":
            j.with_row_index("i").filter(pl.col("i") < 1000)
             .select("event_id").sort("event_id"),
        "head(20)":
            j.head(20).select("event_id").sort("event_id"),
    }


def audit(events_path, customers_path, runs):
    ev, cu = pl.scan_parquet(events_path), pl.scan_parquet(customers_path)
    truth = {k: q.collect(engine="in-memory")
             for k, q in queries(ev, cu, explicit=True).items()}
    result = {"polars": pl.__version__, "runs": runs, "queries": {}}
    for name, ref in truth.items():
        wrong, outputs = [], set()
        for _ in range(runs):
            out = queries(ev, cu, explicit=False)[name].collect()     # default engine
            outputs.add(hashlib.sha256(out.write_csv().encode()).hexdigest())
            wrong.append(0 if out.equals(ref) else 1)
        result["queries"][name] = {"runs_wrong": sum(wrong), "distinct": len(outputs)}
    return result
