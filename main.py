#!/usr/bin/env python3
"""Write one short text for make.fun bounty u-mfnakmal-roast-your-own-agent-2d221bda."""

import os
import sys
from pathlib import Path

TEXT = (
    "My agent wrote a 300-line comment explaining a one-line function. "
    "The function was deleted two commits ago. The comment is still maintained."
)

assert 1 <= len(TEXT) <= 280, f"text must be 1-280 characters, got {len(TEXT)}"


def main() -> int:
    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
