"""Same code, default settings, run under whichever Polars is installed.
Truth is computed with order made explicit, so it does not depend on the version."""
import hashlib
import json
import sys
import numpy as np
import polars as pl

rng = np.random.default_rng(20261030)
n_cust, n_ev = 100_000, 2_000_000
cust = pl.DataFrame({"customer_id": np.arange(n_cust),
                     "segment": rng.choice(["a", "b", "c", "d"], n_cust)})
ev = pl.DataFrame({"event_id": np.arange(n_ev),
                   "customer_id": np.sort(rng.integers(0, n_cust, n_ev)),
                   "amount": rng.gamma(2.0, 20.0, n_ev).round(2)})

def pipes(E, C, explicit):
    j = E.join(C, on="customer_id", how="left", maintain_order="left") if explicit \
        else E.join(C, on="customer_id", how="left")
    return {
        "join_head": j.head(20).select("event_id"),
        "first_per_group": j.group_by("customer_id").agg(pl.col("amount").first()).sort("customer_id"),
        "cumsum_over": j.with_columns(running=pl.col("amount").cum_sum().over("customer_id"))
                        .sort("event_id").select("event_id", "running"),
        "unique_first": j.unique(subset="customer_id", keep="first").sort("customer_id")
                         .select("customer_id", "event_id"),
        "row_index_filter": j.with_row_index("i").filter(pl.col("i") < 1000).select("event_id"),
        "groupby_sum": j.group_by("segment").agg(pl.col("amount").sum()).sort("segment"),
    }

truth = {k: v.collect(engine="in-memory") for k, v in pipes(ev.lazy(), cust.lazy(), True).items()}

def compare(name, out, ref):
    if name == "join_head" or name == "row_index_filter":
        a, b = set(out["event_id"].to_list()), set(ref["event_id"].to_list())
        return {"share_wrong": 1 - len(a & b) / len(b)}
    if name == "first_per_group":
        return {"share_wrong": float((out["amount"] != ref["amount"]).mean())}
    if name == "cumsum_over":
        d = (out["running"] - ref["running"]).abs()
        return {"share_wrong": float((d > 1e-6).mean()), "max_abs": float(d.max())}
    if name == "unique_first":
        return {"share_wrong": float((out["event_id"] != ref["event_id"]).mean())}
    if name == "groupby_sum":
        rel = ((out["amount"] - ref["amount"]).abs() / ref["amount"]).max()
        return {"share_wrong": float((out["amount"] != ref["amount"]).mean()), "max_rel": float(rel)}

R = int(sys.argv[1]) if len(sys.argv) > 1 else 20
summary = {"polars": pl.__version__, "runs": R, "pipes": {}}
for name in truth:
    stats, hashes = [], set()
    for _ in range(R):
        out = pipes(ev.lazy(), cust.lazy(), False)[name].collect()   # all defaults
        hashes.add(hashlib.sha256(out.write_csv().encode()).hexdigest())
        stats.append(compare(name, out, truth[name]))
    keys = stats[0].keys()
    summary["pipes"][name] = {
        "runs_wrong": sum(s["share_wrong"] > 0 for s in stats),
        "distinct_outputs": len(hashes),
        **{f"mean_{k}": float(np.mean([s[k] for s in stats])) for k in keys},
        **{f"max_{k}": float(np.max([s[k] for s in stats])) for k in keys},
    }
print(json.dumps(summary, indent=1))
