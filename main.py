#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — make.fun entry.

Writes one line (125 characters) about the dumbest thing my own agent
did today to /output/entry.txt. Fully deterministic: one fixed line,
no randomness, no clock, no network, no environment reads.
"""
import os

LINE = "My agent told the user his 0.0000162 BNB covered four days of KOGNI claims, then recalculated in the same chat: two mornings."
# True incident: 23 Nov 2026, the agent estimated the user's 0.0000162 BNB
# would cover four days of daily KOGNI claims, then recalculated in the same
# chat and corrected itself: two mornings. Corrected the same day.

assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
assert LINE.strip() == LINE, "line must not be only whitespace"


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
