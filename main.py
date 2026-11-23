#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch note (at most 160 characters) for a bug in human
biology to /output/entry.txt.
"""

import os

ENTRY = (
    "v4.2.0: fixed a bug where the brain replayed an embarrassing "
    "moment from 2014 at 3:00 a.m. instead of sleeping."
)


def main():
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert all(32 <= ord(c) <= 126 for c in ENTRY), "entry must be plain ASCII"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"entry: {len(ENTRY)} chars")


if __name__ == "__main__":
    main()
