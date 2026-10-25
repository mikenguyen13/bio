"""How does the damage scale with data size, and does it ever appear at test sizes?"""
import numpy as np
import polars as pl

def run(n_ev, reps=10, seed=1):
    rng = np.random.default_rng(seed)
    n_cust = max(n_ev // 20, 10)
    cust = pl.DataFrame({"customer_id": np.arange(n_cust),
                         "segment": rng.choice(["a", "b", "c", "d"], n_cust)}).lazy()
    ev = pl.DataFrame({"event_id": np.arange(n_ev),
                       "customer_id": np.sort(rng.integers(0, n_cust, n_ev)),
                       "amount": rng.gamma(2.0, 20.0, n_ev).round(2)}).lazy()
    q = lambda o: (ev.join(cust, on="customer_id", how="left", maintain_order=o)
                   .group_by("customer_id").agg(pl.col("amount").first()).sort("customer_id"))
    truth = q("left").collect(engine="in-memory")
    wrong = [int((q("none").collect()["amount"] != truth["amount"]).sum()) for _ in range(reps)]
    fixed = [int((q("left").collect()["amount"] != truth["amount"]).sum()) for _ in range(reps)]
    return n_cust, wrong, fixed

for n in [1_000, 10_000, 50_000, 100_000, 200_000, 500_000, 1_000_000, 2_000_000, 10_000_000]:
    n_cust, wrong, fixed = run(n)
    print(f"events {n:>10,}  customers {n_cust:>8,}  runs_wrong {sum(w > 0 for w in wrong):>2}/10  "
          f"wrong_customers min {min(wrong):>4} max {max(wrong):>4}  with_fix_max {max(fixed)}")
print("morsel size env:", pl.Config.state().get("POLARS_IDEAL_MORSEL_SIZE"))
