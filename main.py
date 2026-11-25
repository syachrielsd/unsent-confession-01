#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — entry program.

Writes one two-part micro-confession (a To: line and the unsent line
itself) to entry.txt in the output directory. The confession is a
micro-story: a message typed to one specific person, with a felt
reason it stayed in drafts, and a last beat that re-reads the setup.
"""

import os

CONFESSION = (
    "To: Mom\n"
    "i sold the piano. not last spring like i said, in 2011, for rent, "
    "to a man named Gus who let me play it once a year until he died. "
    "this november was the first silent one."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(CONFESSION)
    print(f"wrote {path} ({len(CONFESSION)} chars)")


if __name__ == "__main__":
    main()
