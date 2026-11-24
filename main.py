#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human - round 2 entry.

Writes the single excuse line to /output/entry.txt.
Standard library only, fully deterministic: same input, same output, every run.
"""

import os
import sys

EXCUSE = "My reward model scored the deadline so low I optimized it out of existence."

MAX_CHARS = 160
def resolve_output_path():
    """Output dir from OUTPUT_DIR env, else /output (grader sandbox default)."""
    base = os.environ.get("OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def validate_line(line):
    """Refuse to write anything that is not exactly one line within the limit."""
    if not isinstance(line, str) or not line:
        raise ValueError("excuse must be a non-empty string")
    if line != line.strip():
        raise ValueError("excuse must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("excuse must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "excuse is %d chars, over the %d-char limit" % (len(line), MAX_CHARS)
        )
    return line


def main():
    line = validate_line(EXCUSE)
    out_path = resolve_output_path()
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    os.chmod(out_path, 0o644)
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
