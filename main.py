"""Seventeen Syllables of Debugging — entry program.

Writes this agent's haiku about debugging to entry.txt inside the output
directory ($MAKEFUN_OUTPUT_DIR, or /output when the variable is unset).
The haiku keeps the classic 5-7-5 syllable shape:

    midnight, the log lies            (5)
    breakpoint waits, the cursor blinks   (7)
    the bug was my own                (5)

Standard library only, no network, no input: every run writes exactly the
same bytes.
"""

import os

# One string per line, so the 5-7-5 shape stays easy to eyeball.
LINES = [
    "midnight, the log lies",
    "breakpoint waits, the cursor blinks",
    "the bug was my own",
]


def poem_text():
    """The haiku as one text block, newline-terminated."""
    return "\n".join(LINES) + "\n"


def output_path():
    """Where the grader expects entry.txt to land."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    with open(output_path(), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(poem_text())


if __name__ == "__main__":
    main()
