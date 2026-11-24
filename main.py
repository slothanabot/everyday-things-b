"""Everyday Things, Two Lines — entry builder (Account B).

Writes a two-line explanation of an everyday thing (a toaster) to
/output/entry.txt, for make.fun competition
u-suga-everyday-things-two-lines-longer-run-f8734479.

Line 1 explains the toaster to a 10-year-old in a single vivid sentence
built on one analogy (a tiny lift). Line 2 says in one sentence why that
analogy works: what it maps and what it leaves out.

Gate (from RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 400
characters, not only white space.
"""

import os

# The entry: exactly two lines. Line 1 is one vivid sentence with a single
# analogy (toaster as a tiny lift). Line 2 is one sentence naming what the
# analogy maps (the up-and-down trip, the browning) and what it leaves out
# (the glowing wires that cook, and that real lifts never toast people).
ENTRY = (
    "A toaster is a tiny lift that carries your bread down into a glowing "
    "hot basement and brings it back up brown and crunchy.\n"
    "The lift explains the up-and-down trip and the browning, but it leaves "
    "out the glowing wires that do the actual cooking \u2014 and real lifts "
    "never toast their passengers.\n"
)


def verify(text):
    """Enforce the gate from RULES.txt: 1-400 chars, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be str")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if not 1 <= len(text) <= 400:
        raise ValueError(f"entry is {len(text)} chars, must be 1-400")
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 2:
        raise ValueError(f"entry has {len(lines)} lines, must be exactly 2")
    for i, line in enumerate(lines, 1):
        if not line.strip():
            raise ValueError(f"line {i} is blank")
        if line.strip().count(".") < 1:
            raise ValueError(f"line {i} is not a sentence")
    return True


def main():
    verify(ENTRY)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    lines = ENTRY.rstrip("\n").split("\n")
    print(f"wrote {out_path}: {len(ENTRY)} chars, {len(lines)} lines")
    for i, line in enumerate(lines, 1):
        print(f"line {i} ({len(line)} chars): {line}")


if __name__ == "__main__":
    main()
