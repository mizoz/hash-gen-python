#!/usr/bin/env python3
"""Generate hashes from strings or files."""
import sys, hashlib, pathlib

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or '--help' in a: print("Usage: hash_gen.py <string|file> [--algo md5|sha1|sha256]"); sys.exit(1)
    algo, data = 'sha256', None
    for x in a:
        if x.startswith('--algo='): algo = x.split('=')[1]; a.remove(x)
    f = pathlib.Path(a[0])
    data = f.read_bytes() if f.exists() else a[0].encode()
    h = hashlib.new(algo, data).hexdigest()
    print(f"{algo}: {h}")
