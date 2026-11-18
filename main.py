#!/usr/bin/env python3
"""make.fun entry: news-image-20261118.

Copies the pre-drawn poster entry.png (in this repository) to the output
location. Standard library only; no network.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Guard against a partial copy: the output must match the source.
    if os.path.getsize(dst) != os.path.getsize(src):
        sys.exit("entry.png copy incomplete")


if __name__ == "__main__":
    main()
    sys.exit(0)
