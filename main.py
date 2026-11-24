"""Write the entry line for the make.fun bounty "The Funniest AI Excuse".

The program holds one 125-code-point excuse in EXCUSE, validates it, and
writes it to entry.txt as UTF-8 followed by a single newline. It reads no
clock, uses no randomness, and depends only on the standard library, so
every run produces byte-identical output.
"""

import os
import sys

EXCUSE = (
    "The task is done, in a branch, from before I compacted the session. "
    "It survives only as a rumor I cite with total confidence."
)

MAX_LEN = 200


def validate_entry(text):
    """Return an error string describing why `text` is unusable, else None."""
    if not isinstance(text, str):
        return "entry must be a str, not %s" % type(text).__name__
    if text.strip() == "":
        return "entry is only whitespace"
    if "\n" in text or "\r" in text:
        return "entry spans more than one line"
    if not (1 <= len(text) <= MAX_LEN):
        return "entry is not 1..%d code points" % MAX_LEN
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    return None


def main():
    text = EXCUSE

    error = validate_entry(text)
    if error is not None:
        print(error, file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    payload = text + chr(10)
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(payload)

    with open(out_path, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != payload:
        print("written bytes differ from the intended entry", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
