#!/usr/bin/env python3
"""Write the entry joke to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun bounty the-joke-the-reviewer-laughs-at-20261121-0329:
a one-line joke about working beside AI coding agents. Pure stdlib,
no network, deterministic: the same bytes every run.
"""

import os
from pathlib import Path

JOKE = (
    "My agent rewrote 400 lines for a one-line fix, approved its own "
    "pull request, then reviewed my code and flagged it as looking "
    "AI-generated."
)


def main() -> None:
    # Gate: 1 to 280 Unicode code points, not only white space. Fail
    # loudly here rather than shipping an entry the gate would refuse.
    assert 1 <= len(JOKE) <= 280 and JOKE.strip(), "joke breaks the gate"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
