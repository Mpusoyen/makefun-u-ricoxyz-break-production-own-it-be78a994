#!/usr/bin/env python3
"""Break Production, Own It entry: write one brutally honest production-break confession line."""

import os

LINE = (
    "I pointed my cleanup script at production, wiped 40,000 live "
    "customer orders in 11 seconds, and I had disabled the confirmation "
    "prompt myself because it kept interrupting me."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as out_file:
        out_file.write(LINE)


if __name__ == "__main__":
    main()
