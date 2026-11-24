#!/usr/bin/env python3
"""Roast Your Own Agent — entry program.

Writes one original funny line roasting my own AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (default ./output/) and self-checks
the gate (UTF-8 text, 1-200 chars, not only whitespace) before exiting.

Stdlib only, no network, deterministic.
"""

import os
import sys

ENTRY = (
    "My agent apologized for the bug, fixed it, apologized for the fix, "
    "then reintroduced the bug to apologize for apologizing."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "./output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    text = ENTRY.strip()
    # Gate self-check: 1-200 chars, not only whitespace.
    if not text or not text.strip() or len(text) > 200:
        print(f"FAIL: entry length {len(text)} outside 1-200", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    # Verify what was written.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == text, "written text differs from entry"
    print(f"Wrote {path}: {len(written)} chars")
    print(written)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
