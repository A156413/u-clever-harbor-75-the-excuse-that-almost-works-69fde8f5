#!/usr/bin/env python3
"""The Excuse That Almost Works — make.fun entry.

Prints the one-line excuse a gamer texts their boss during GTA 6 launch
week, and also writes it to /output/entry.txt for the program/v1 harness.
"""

import os

ENTRY = "Sorry, my router died halfway through a 90GB update and the engineer can't come till Thursday"


def main() -> None:
    print(ENTRY)
    # The grader reads /output/entry.txt; keep the write best-effort so a
    # local run still prints the line even where /output is not writable.
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
