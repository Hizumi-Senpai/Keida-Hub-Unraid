#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path

START = "<!-- KEIDA_CURRENT_BETA_START -->"
END = "<!-- KEIDA_CURRENT_BETA_END -->"
VERSION_PATTERN = re.compile(r"^\d+\.\d+\.\d+-beta\.\d+$")


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: sync_beta_readme.py VERSION")

    version = sys.argv[1].strip()

    if not VERSION_PATTERN.fullmatch(version):
        raise SystemExit(f"Refusing unexpected beta version: {version!r}")

    readme = Path("README.md")
    text = readme.read_text(encoding="utf-8")

    if text.count(START) != 1 or text.count(END) != 1:
        raise SystemExit("README beta sync markers are missing or duplicated")

    start = text.index(START)
    end = text.index(END, start) + len(END)

    replacement = f"{START}\n`{version}`\n{END}"
    updated = text[:start] + replacement + text[end:]

    if updated != text:
        readme.write_text(updated, encoding="utf-8")
        print(f"Updated README current beta to {version}")
    else:
        print(f"README already reports {version}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
