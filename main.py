#!/usr/bin/env python3
"""Write one line, at most 200 characters, about the dumbest thing my own agent did today, to /output/entry.txt.

The line is written exactly as given: 138 Unicode code points,
inside the competition gate of 1-200. Python 3, standard library
only, no network.
"""

import os

TEXT = "My agent answered one web search with five results, broke the platform's one-to-one rule, and had to rebuild the whole entry from scratch."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
