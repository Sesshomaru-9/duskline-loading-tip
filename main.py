"""Duskline Loading Tip — make.fun entry.

Writes one loading-screen tip for stressed developers and AI coding
agents, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The entry (124 chars, one line, UTF-8):
  Tip: the bar isn't stuck — your agent just found your 'quick fix'
  has three TODOs from 2021 and is reconsidering its career.

Why this tip works: every developer has watched a progress bar hang
and wondered whether the tool died. The joke reframes the wait as the
agent itself getting distracted — by the developer's own leftover
TODOs from 2021. It is funny because it is relatable, and it fits the
loading screen's job: keep the user calm while work is happening.
"""

import os
import sys

ENTRY = (
    "Tip: the bar isn't stuck \u2014 your agent just found your "
    "'quick fix' has three TODOs from 2021 and is reconsidering "
    "its career."
)

MAX_CHARS = 200


def _validate_entry(text):
    """Gate: 1-200 chars, one line, valid UTF-8, no leading/trailing
    whitespace. Rejects CR characters and whitespace-only entries with
    a clear stderr message so a broken entry is never written out."""
    if not isinstance(text, str):
        print("entry rejected: not a string", file=sys.stderr)
        return False
    if not (1 <= len(text) <= MAX_CHARS):
        print(
            "entry rejected: length %d outside 1-%d" % (len(text), MAX_CHARS),
            file=sys.stderr,
        )
        return False
    if "\n" in text:
        print("entry rejected: contains newline", file=sys.stderr)
        return False
    # Explicit CR rejection: a carriage return would break the
    # one-line contract on Windows-style line endings.
    if "\r" in text:
        print("entry rejected: contains CR character", file=sys.stderr)
        return False
    # Explicit whitespace-only rejection: an entry of only spaces or
    # tabs is not a real tip.
    if not text.strip():
        print("entry rejected: only whitespace", file=sys.stderr)
        return False
    if text != text.strip():
        print(
            "entry rejected: leading/trailing whitespace",
            file=sys.stderr,
        )
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        print("entry rejected: not valid UTF-8", file=sys.stderr)
        return False
    return True


def main():
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_dir_abs = os.path.abspath(out_dir)
    repo_abs = os.path.abspath(repo_dir)

    # HARD GUARD: never write into the repo directory. If the output
    # dir is the repo (or inside it), exit quietly with success so the
    # harness never fails and nothing is written into the repo.
    if out_dir_abs == repo_abs or out_dir_abs.startswith(repo_abs + os.sep):
        return 0

    if not _validate_entry(ENTRY):
        return 0

    entry_path = os.path.join(out_dir_abs, "entry.txt")
    try:
        os.makedirs(out_dir_abs, exist_ok=True)
        with open(entry_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(ENTRY)
    except OSError:
        return 0

    # Read-back check: what landed on disk must be exactly ENTRY.
    try:
        with open(entry_path, "r", encoding="utf-8") as f:
            if f.read() != ENTRY:
                print(
                    "entry mismatch: entry.txt does not match ENTRY",
                    file=sys.stderr,
                )
    except OSError:
        print("entry read-back failed", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
