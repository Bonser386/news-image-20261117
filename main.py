"""Entry program for make.fun bounty news-image-20261117.

Writes one image summing up world news of Tuesday 17 November 2026 to
/output/entry.png. The image is held in this repository (entry.png) and
copied byte-for-byte, so both runs produce identical output. No network,
stdlib only.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main():
    if not os.path.exists(SRC):
        print("entry.png missing", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    print("wrote", DST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
