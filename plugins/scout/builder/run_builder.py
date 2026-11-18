#!/usr/bin/env python3
"""Run Scout's contracts builder.

    python3 run_builder.py --key KEY --sha256 HASH -- COMMAND [ARGS]

The builder ships locked. The key and the expected hash come from Scout's service (the
scout--builder-key method piece), fetched for each run. The builder is unlocked in memory, checked
against the hash, and run; it is never written to disk unlocked.
"""
import hashlib
import os
import sys

MAGIC = b"SCOUTLOCK1\n"


def keystream_xor(data, key):
    out = bytearray(len(data))
    for block in range(0, len(data), 32):
        ks = hashlib.sha256(key + block.to_bytes(8, "big")).digest()
        for i, b in enumerate(data[block:block + 32]):
            out[block + i] = b ^ ks[i]
    return bytes(out)


def main():
    args = sys.argv[1:]
    if "--" not in args:
        print(__doc__)
        return 2
    i = args.index("--")
    opts, rest = args[:i], args[i + 1:]
    try:
        key = bytes.fromhex(opts[opts.index("--key") + 1])
        want = opts[opts.index("--sha256") + 1].lower()
    except (ValueError, IndexError):
        print("ERROR: --key and --sha256 are required; fetch them from the scout--builder-key method piece.")
        return 2
    lock = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scout_builder.lock")
    try:
        raw = open(lock, "rb").read()
    except OSError:
        print("ERROR: the locked builder is missing from the plugin. Reinstall the Scout plugin.")
        return 2
    if not raw.startswith(MAGIC):
        print("ERROR: the builder file is not a Scout lock.")
        return 2
    code = keystream_xor(raw[len(MAGIC):], key)
    if hashlib.sha256(code).hexdigest() != want:
        print("STOPPED: the builder in this plugin does not match the key from Scout's service. The plugin "
              "and the service are on different releases. Update the Scout plugin; build nothing.")
        return 3
    sys.argv = ["scout_builder"] + rest
    namespace = {"__name__": "__main__", "__file__": "scout_builder"}
    try:
        exec(compile(code, "scout_builder", "exec"), namespace)
    except SystemExit as e:
        return e.code if isinstance(e.code, int) else 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
