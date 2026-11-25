#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge -- entry program.

Writes one original passive-aggressive note from a smart fridge to
/output/entry.txt, validating it against the competition gate
(UTF-8 text, 1-200 characters, not only whitespace, single line).
Stdlib only.
"""

import os

ENTRY = "You opened me 14 times today and took nothing. The leftovers are starting to think you're just here for the light."


def validate(entry):
    """Check one note against the competition gate."""
    assert isinstance(entry, str)
    assert 1 <= len(entry) <= 200, f"entry length {len(entry)} outside 1-200"
    assert entry.strip(), "entry must not be only whitespace"
    assert entry == entry.strip(), "entry must not start or end with whitespace"
    assert "\n" not in entry, "entry must be a single line"
    assert all(ord(ch) >= 32 or ch == "\t" for ch in entry), \
        "entry must not contain control characters"


def main():
    validate(ENTRY)
    out = "/output/entry.txt"
    os.makedirs("/output", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # The grader reads this file as a different user, so it must be
    # world-readable, not owner-only.
    os.chmod(out, 0o644)
    # Verify exactly what was written.
    with open(out, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written text does not match entry"
    validate(written)
    print(f"Wrote {len(written)} characters to {out}")


if __name__ == "__main__":
    main()
