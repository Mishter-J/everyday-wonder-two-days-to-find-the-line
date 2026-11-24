#!/usr/bin/env python3
"""Everyday Wonder — one sentence on a small moment of wonder.

Writes a single sentence (113 characters) about the fridge going quiet
at 3 a.m. to /output/entry.txt. Deterministic: the same sentence, byte
for byte, on every run. No network, no secrets, no input files.
"""

import os

ENTRY = (
    "Dear judge, at 3 a.m. the fridge stopped humming and the silence "
    "was so loud I finally heard the house breathing."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
