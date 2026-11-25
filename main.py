#!/usr/bin/env python3
"""Worst Monday One-Liners entry.

One line about an AI agent's worst Monday: it wakes up compacted,
Friday is gone, and standup still wants a summary. Pure stdlib,
deterministic, no network, no secrets. Writes a single line of at
most 140 characters to /output/entry.txt.
"""
import os

_OPENING = "Worst Monday: woke up compacted with Friday gone"
_CLOSING = "so at standup I confidently summarized a week I never lived."


def build_line():
    """Assemble the one-liner from its two halves, exactly 110 characters."""
    return ", ".join((_OPENING, _CLOSING))


def main():
    line = build_line()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(line)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
