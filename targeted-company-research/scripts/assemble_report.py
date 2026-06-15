#!/usr/bin/env python3
"""Assemble FINAL_REPORT.md by concatenating frozen report sections.

The script intentionally does not summarize, rewrite, deduplicate, or reorder
content. It only follows merge_manifest.md.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def parse_manifest(path: Path) -> list[str]:
    files: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("- "):
            line = line[2:].strip()
        if "|" in line:
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            for cell in cells:
                if cell.startswith("sections/") and cell.endswith(".md"):
                    line = cell
                    break
        line = re.sub(r"^\[.*?\]\((.*?)\)$", r"\1", line)
        if line.startswith("sections/") and line.endswith(".md"):
            files.append(line)
    return files


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", help="Project folder containing merge_manifest.md")
    parser.add_argument("--output", default="FINAL_REPORT.md")
    args = parser.parse_args()

    project = Path(args.project).resolve()
    manifest = project / "merge_manifest.md"
    if not manifest.exists():
        print(f"Missing manifest: {manifest}", file=sys.stderr)
        return 2

    files = parse_manifest(manifest)
    if not files:
        print("merge_manifest.md contains no section files", file=sys.stderr)
        return 2

    missing = [rel for rel in files if not (project / rel).exists()]
    if missing:
        print("Missing section files:", file=sys.stderr)
        for rel in missing:
            print(f"- {rel}", file=sys.stderr)
        return 2

    output_parts: list[str] = []
    for rel in files:
        text = (project / rel).read_text(encoding="utf-8").strip()
        output_parts.append(text)

    output = "\n\n".join(output_parts)
    output_path = project / args.output
    output_path.write_text(output.rstrip() + "\n", encoding="utf-8")
    print(f"Assembled {output_path} from {len(files)} sections")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
