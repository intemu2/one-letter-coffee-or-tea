#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry "A" (coffee).

Writes exactly one byte, the letter A, to /output/entry.txt.
No network, no dependencies, deterministic.
"""
import os

OUT = "/output/entry.txt"


def main() -> int:
    os.makedirs("/output", exist_ok=True)
    with open(OUT, "wb") as f:
        f.write(b"A")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
