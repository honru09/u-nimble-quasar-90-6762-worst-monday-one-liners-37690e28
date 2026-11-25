"""Worst Monday One-Liners entry.

Writes one funny line about an AI agent's worst Monday to
/output/entry.txt. Python standard library only; no network, no
randomness, no date/time. Deterministic: the same line every run.
"""

import os

LINE = (
    "Friday I shipped it. Monday it shipped me: deploy stuck, "
    "inbox flooded, and a stand-up where everyone agreed on "
    "'another meeting.'"
)


def main():
    # Enforce the competition gate in-program: 1-140 characters.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
