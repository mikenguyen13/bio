"""Command line entry point, so the same audit can run under another Polars version.

    python run_audit.py <events.parquet> <customers.parquet> <runs>
"""
import json
import sys

from audit import audit

print(json.dumps(audit(sys.argv[1], sys.argv[2], int(sys.argv[3]))))
