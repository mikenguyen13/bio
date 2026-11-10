"""Text encoding audit for the Python 3.15 UTF-8 post.

Run it under any interpreter. Every mode except `print` reports one JSON object
on stdout, and that JSON is pure ASCII (ensure_ascii), so the channel carrying the
results back to R cannot be damaged by the encoding being tested.

Nothing here passes an `encoding` argument to open(), TextIOWrapper, or
subprocess unless the comment says so. Testing the default is the whole point.
"""
import csv
import io
import json
import subprocess
import sys


def emit(obj):
    sys.stdout.write(json.dumps(obj, ensure_ascii=True))


def attempt(fn):
    try:
        return {"ok": True, "value": fn()}
    except Exception as e:  # report the failure instead of crashing the audit
        return {"ok": False, "error": type(e).__name__}


def default_encoding():
    # The encoding open() picks when you do not name one
    return io.TextIOWrapper(io.BytesIO()).encoding


def info():
    return {"python": sys.version.split()[0],
            "utf8_mode": sys.flags.utf8_mode,
            "open_default": default_encoding(),
            "stdout": sys.stdout.encoding}


def read_csv_module(path):
    def go():
        with open(path, newline="") as f:
            rows = list(csv.DictReader(f))
        # Look the column up by name, the way analysis code does
        return [row["name"] for row in rows]
    return attempt(go)


def read_pandas(path):
    import pandas as pd
    return attempt(lambda: pd.read_csv(path)["name"].tolist())


def write_csv_module(path, names):
    def go():
        with open(path, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["id", "name"])
            for i, n in enumerate(names, 1):
                w.writerow([i, n])
        return True
    return attempt(go)


def run_rscript(rscript, script):
    def go():
        out = subprocess.run([rscript, "--vanilla", script],
                             capture_output=True, text=True, check=True)
        # On Windows, run() decodes the pipe in a background thread. If decoding
        # fails there, the thread prints a traceback, run() still returns, and
        # stdout comes back as None rather than raising in this thread.
        if out.stdout is None:
            raise LookupError("stdout is None")
        return out.stdout.splitlines()
    try:
        return {"ok": True, "value": go()}
    except LookupError as e:
        return {"ok": False, "error": str(e)}
    except Exception as e:
        return {"ok": False, "error": type(e).__name__}


def encode_all(cps):
    # Bytes each character becomes when written through the default encoding.
    # TextIOWrapper encodes with errors="strict", and so does this.
    enc = default_encoding()
    out = []
    for cp in cps:
        try:
            out.append(chr(cp).encode(enc).hex())
        except UnicodeEncodeError:
            out.append(None)
    return out


def decode_all(hexes):
    # What the default encoding reads those bytes back as, one character at a time
    enc = default_encoding()
    out = []
    for h in hexes:
        if h is None:
            out.append(None)
            continue
        try:
            out.append([ord(c) for c in bytes.fromhex(h).decode(enc)])
        except UnicodeDecodeError:
            out.append("error")
    return out


def assigned_code_points():
    # Every assigned, printable code point above ASCII in this Python's Unicode
    # database. Controls, surrogates, private use, and unassigned are left out.
    import unicodedata
    skip = {"Cc", "Cs", "Co", "Cn"}
    cps = [cp for cp in range(0x80, 0x110000)
           if unicodedata.category(chr(cp)) not in skip]
    return {"unicode": unicodedata.unidata_version, "cps": cps}


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "info":
        emit(info())
    elif mode == "print":
        # Read the names with an explicit encoding, so only stdout is under test
        with open(sys.argv[2], encoding="utf-8") as f:
            for line in f.read().splitlines():
                print(line)
    elif mode == "read":
        emit({"csv": read_csv_module(sys.argv[2]),
              "pandas": read_pandas(sys.argv[2])})
    elif mode == "write":
        with open(sys.argv[3], encoding="utf-8") as f:  # input list, explicit
            names = f.read().splitlines()
        emit(write_csv_module(sys.argv[2], names))
    elif mode == "rscript":
        emit(run_rscript(sys.argv[2], sys.argv[3]))
    elif mode == "universe":
        emit(assigned_code_points())
    elif mode == "encode":
        with open(sys.argv[2], encoding="ascii") as f:
            cps = json.load(f)
        with open(sys.argv[3], "w", encoding="ascii") as f:
            json.dump(encode_all(cps), f)
    elif mode == "decode":
        with open(sys.argv[2], encoding="ascii") as f:
            hexes = json.load(f)
        with open(sys.argv[3], "w", encoding="ascii") as f:
            json.dump(decode_all(hexes), f)
