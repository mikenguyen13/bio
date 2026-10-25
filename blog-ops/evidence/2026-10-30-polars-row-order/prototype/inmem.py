import sys
import polars as pl
d, R = sys.argv[1], int(sys.argv[2])
ev, cu = pl.scan_parquet(f"{d}/events.parquet"), pl.scan_parquet(f"{d}/customers.parquet")
q_none = ev.join(cu, on="customer_id", how="left").group_by("customer_id").agg(pl.col("amount").first()).sort("customer_id")
q_left = ev.join(cu, on="customer_id", how="left", maintain_order="left").group_by("customer_id").agg(pl.col("amount").first()).sort("customer_id")
ref = q_left.collect(engine="in-memory")
def count(f):
    w = [int((f()["amount"] != ref["amount"]).sum()) for _ in range(R)]
    return sum(x > 0 for x in w), max(w)
print("polars", pl.__version__)
print("default collect()          runs wrong, max customers:", count(lambda: q_none.collect()))
if pl.__version__.startswith("2"):
    print("collect(engine=in-memory)  runs wrong, max customers:", count(lambda: q_none.collect(engine="in-memory")))
    pl.Config.set_engine_affinity("in-memory")
    print("set_engine_affinity        runs wrong, max customers:", count(lambda: q_none.collect()))
# eager DataFrame path, no lazy engine at all
E, C = ev.collect(), cu.collect()
ref_e = E.join(C, on="customer_id", how="left", maintain_order="left").group_by("customer_id", maintain_order=False).agg(pl.col("amount").first()).sort("customer_id")
w = [int((E.join(C, on="customer_id", how="left").group_by("customer_id").agg(pl.col("amount").first()).sort("customer_id")["amount"] != ref_e["amount"]).sum()) for _ in range(R)]
print("eager DataFrame join        runs wrong, max customers:", (sum(x > 0 for x in w), max(w)))
