#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — make.fun entry.

Writes the one-line excuse to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Standard library only; fully deterministic: the same text every run.

The dog's defence, in its own voice: the homework looked at it first and
dared it to eat it — a dog that believes it did nothing wrong.
"""

import os
from pathlib import Path

ENTRY = (
    "It looked at me first. The homework started it \u2014 sitting there "
    "all blank and smug, daring me to eat it.\n"
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
