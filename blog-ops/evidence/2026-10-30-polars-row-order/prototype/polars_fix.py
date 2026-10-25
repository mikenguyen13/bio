import time
import numpy as np
import polars as pl
from polars.testing import assert_frame_equal

rng = np.random.default_rng(20261030)
n_cust, n_ev = 100_000, 2_000_000
C = pl.DataFrame({"customer_id": np.arange(n_cust),
                  "segment": rng.choice(["a", "b", "c", "d"], n_cust)}).lazy()
E = pl.DataFrame({"event_id": np.arange(n_ev),
                  "customer_id": np.sort(rng.integers(0, n_cust, n_ev)),
                  "amount": rng.gamma(2.0, 20.0, n_ev).round(2)}).lazy()

def first_q(join_order=None, expr=None):
    j = E.join(C, on="customer_id", how="left") if join_order is None \
        else E.join(C, on="customer_id", how="left", maintain_order=join_order)
    e = expr if expr is not None else pl.col("amount").first()
    return j.group_by("customer_id").agg(e).sort("customer_id")

truth = first_q("left").collect(engine="in-memory")
variants = {
    "default": lambda: first_q().collect(),
    "join maintain_order='left'": lambda: first_q("left").collect(),
    "sort_by inside agg": lambda: first_q(expr=pl.col("amount").sort_by("event_id").first()).collect(),
    "engine='in-memory'": lambda: first_q().collect(engine="in-memory"),
}
R = 20
order = [k for k in variants for _ in range(R)]
rng2 = np.random.default_rng(7)
rng2.shuffle(order)                      # interleave variants so timing is fair
times = {k: [] for k in variants}
wrong = {k: [] for k in variants}
for k in order:
    t0 = time.perf_counter()
    out = variants[k]()
    times[k].append(time.perf_counter() - t0)
    wrong[k].append(int((out["amount"] != truth["amount"]).sum()))
for k in variants:
    print(f"{k:30s} runs_wrong {sum(w > 0 for w in wrong[k]):2d}/{R}  median_s {np.median(times[k]):.3f}")

# Does Polars' own test helper catch it?
bad = variants["default"]()
for kw in [{}, {"check_row_order": False}]:
    try:
        assert_frame_equal(bad, truth, **kw)
        print("assert_frame_equal", kw, "PASSED (missed it)")
    except AssertionError as e:
        print("assert_frame_equal", kw, "FAILED (caught it):", str(e).splitlines()[0][:100])
# config-level fix
pl.Config.set_engine_affinity("in-memory")
print("set_engine_affinity in-memory wrong:", int((first_q().collect()["amount"] != truth["amount"]).sum()))
