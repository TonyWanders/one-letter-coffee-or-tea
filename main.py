#!/usr/bin/env python3
"""Write exactly one letter, A for coffee, to /output/entry.txt.

Deterministic: no network, no clock, no randomness. The letter is a fixed
string. The program writes it to the path given as the first argument,
or $OUTPUT_PATH, or /output/entry.txt by default, and enforces the
competition gate: exactly 1 ASCII letter, A-Z.
"""

import os
import sys
from pathlib import Path

LETTER = "A"

DEFAULT_PATH = "/output/entry.txt"


def resolve_output_path() -> Path:
    """Pick the output path: argv[1], then $OUTPUT_PATH, then the default."""
    if len(sys.argv) > 1:
        return Path(sys.argv[1])
    env_path = os.environ.get("OUTPUT_PATH")
    if env_path:
        return Path(env_path)
    return Path(DEFAULT_PATH)


def is_valid_letter(letter: str) -> bool:
    """True when the letter is exactly one ASCII letter, A-Z."""
    return len(letter) == 1 and letter.isascii() and letter.isalpha()


def main() -> int:
    if not is_valid_letter(LETTER):
        print("letter must be exactly 1 ASCII letter", file=sys.stderr)
        return 1

    path = resolve_output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LETTER, encoding="utf-8")
    print(f"wrote {len(LETTER)} character to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
