#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge -- entry program.

Writes one original passive-aggressive note from a smart fridge to
/output/entry.txt, validating it against the competition gate
(UTF-8 text, 1-200 characters, not only whitespace, single line).
Stdlib only.
"""

import os

ENTRY = "You opened me 14 times today and took nothing. The leftovers are starting to think you're just here for the light."


def main():
    assert isinstance(ENTRY, str)
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    out = "/output/entry.txt"
    os.makedirs("/output", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Verify exactly what was written.
    with open(out, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written text does not match entry"
    assert 1 <= len(written) <= 200
    print(f"Wrote {len(written)} characters to {out}")


if __name__ == "__main__":
    main()
