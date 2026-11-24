"""Write one original excuse, in a dog's own voice, to entry.txt.

The dog was caught eating the homework. It explains why — in a single
line, under 200 characters — and it is entirely unrepentant: it believes
it did its owner a favour.

Deterministic: the same line, byte for byte, on every run. No randomness,
no network, no clock, no input files.
"""

import os

EXCUSE = (
    "I ate the homework so the teacher can't mark it wrong. "
    "You're welcome \u2014 where's my treat?"
)


def main():
    # The sealed gate counts the file as-is: 1 to 200 characters, not only
    # whitespace. Validate before writing, and write no trailing newline
    # so the file holds exactly the line, nothing extra.
    assert 1 <= len(EXCUSE) <= 200, f"excuse is {len(EXCUSE)} chars"
    assert EXCUSE.strip(), "excuse must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
