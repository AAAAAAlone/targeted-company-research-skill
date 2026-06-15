#!/usr/bin/env python3
"""Render FINAL_REPORT.md to HTML/PDF with readable pagination.

Chrome renders the report body. PyMuPDF then adds a running chapter header and
page-number footer, avoiding Chrome's noisy default URL/date header.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import quote

import fitz
import markdown


CSS = r"""
@page { size: A4; margin: 20mm 15mm 18mm 15mm; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, "Noto Sans CJK SC", sans-serif;
  color: #17202a;
  line-height: 1.56;
  font-size: 12.5px;
}
.cover-page {
  break-after: page;
  box-sizing: border-box;
  min-height: 252mm;
  margin: 0;
  padding: 30mm 24mm 22mm 24mm;
  color: #f7fbff;
  background:
    linear-gradient(126deg, rgba(7,20,38,.96) 0%, rgba(14,43,75,.88) 42%, rgba(234,242,248,.78) 43%, rgba(232,240,248,.68) 57%, rgba(11,31,54,.94) 58%, rgba(5,16,32,.98) 100%),
    radial-gradient(circle at 82% 42%, rgba(75,149,223,.38), transparent 28%),
    linear-gradient(180deg, #0b1728, #183d62);
  position: relative;
  overflow: hidden;
}
.cover-page::after {
  content: "";
  position: absolute;
  inset: 0;
  background:
    linear-gradient(90deg, rgba(255,255,255,.08) 1px, transparent 1px),
    linear-gradient(180deg, rgba(255,255,255,.05) 1px, transparent 1px);
  background-size: 28px 28px;
  opacity: .22;
}
.cover-content { position: relative; z-index: 1; max-width: 76%; }
.cover-eyebrow {
  font-size: 10px;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: #9bc7ff;
  margin-bottom: 14mm;
}
.cover-page h1 {
  break-before: auto;
  border: 0;
  color: #fff;
  font-size: 42px;
  line-height: 1.08;
  margin: 0 0 9mm 0;
  padding: 0;
}
.cover-subtitle {
  color: #dcecff;
  font-size: 15px;
  line-height: 1.7;
  max-width: 92%;
}
.cover-meta {
  margin-top: 22mm;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px 18px;
  font-size: 11px;
  color: #d8e8f8;
}
.cover-meta strong { display: block; color: #fff; font-size: 13px; margin-top: 2px; }
.cover-bottom {
  position: absolute;
  left: 24mm;
  right: 24mm;
  bottom: 22mm;
  z-index: 1;
  color: #b9c8d8;
  font-size: 10px;
  border-top: 1px solid rgba(255,255,255,.22);
  padding-top: 7mm;
}
.toc-page {
  min-height: 226mm;
  padding-top: 14mm;
}
.toc-page h1 {
  break-before: auto;
  font-size: 34px;
  margin-bottom: 8mm;
}
.toc-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 11px 18px;
  margin-top: 12mm;
}
.toc-item {
  border-top: 2px solid #1f6feb;
  padding-top: 8px;
  min-height: 34mm;
}
.toc-num {
  font-size: 11px;
  color: #1f6feb;
  font-weight: 700;
  letter-spacing: 1.4px;
}
.toc-title {
  font-size: 17px;
  font-weight: 800;
  color: #0b1f33;
  margin: 5px 0 5px;
}
.toc-desc {
  font-size: 11px;
  color: #536171;
  line-height: 1.5;
}
.divider-page {
  break-before: page;
  break-after: page;
  min-height: 226mm;
  display: flex;
  flex-direction: column;
  justify-content: center;
  color: #0b1f33;
  background:
    linear-gradient(135deg, rgba(31,111,235,.09), transparent 34%),
    linear-gradient(315deg, rgba(14,47,80,.10), transparent 42%);
}
.divider-kicker {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 15px;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: #1f6feb;
  margin-bottom: 8mm;
}
.divider-page h1 {
  break-before: auto;
  border-bottom: 0;
  font-size: 40px;
  line-height: 1.12;
  margin: 0 0 7mm 0;
}
.divider-desc {
  max-width: 70%;
  color: #516173;
  font-size: 14px;
  line-height: 1.7;
}
.summary-box {
  margin: 16px 0 20px;
  padding: 13px 15px;
  background: #f3f7fb;
  border-left: 4px solid #1f6feb;
  color: #203040;
}
.summary-box .summary-title {
  font-weight: 800;
  color: #0b1f33;
  margin-bottom: 6px;
}
.summary-box strong { color: #0b3f7c; }
h1 {
  break-before: page;
  font-size: 27px;
  margin: 0 0 16px;
  color: #0b1f33;
  border-bottom: 3px solid #1f6feb;
  padding-bottom: 8px;
}
h1:first-child {
  break-before: auto;
  font-size: 34px;
  margin-top: 52px;
}
h2 { font-size: 18px; color: #12385f; margin-top: 20px; }
h3 { font-size: 15px; color: #1f3b57; margin-top: 15px; }
p, li { orphans: 2; widows: 2; }
table {
  width: 100%;
  border-collapse: collapse;
  margin: 11px 0 16px;
  font-size: 10.3px;
  page-break-inside: auto;
}
tr { page-break-inside: avoid; }
th { background: #edf3f8; color: #10263d; font-weight: 700; }
th, td {
  border: 1px solid #c9d6e2;
  padding: 5px 6px;
  vertical-align: top;
  word-break: break-word;
}
blockquote {
  border-left: 4px solid #1f6feb;
  padding: 8px 12px;
  background: #f6f8fa;
  color: #334;
}
small { display: block; color: #68717c; margin-top: 12px; }
"""


def chrome_path() -> str:
    candidates = [
        os.environ.get("CHROME_BIN"),
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "google-chrome",
        "chromium",
    ]
    for candidate in candidates:
        if candidate and (Path(candidate).exists() or "/" not in candidate):
            return candidate
    raise FileNotFoundError("Chrome/Chromium not found")


def font_path() -> str | None:
    candidates = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
        "/System/Library/Fonts/Supplemental/Songti.ttc",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return candidate
    return None


def markdown_headings(text: str) -> list[str]:
    headings: list[str] = []
    for line in text.splitlines():
        if line.startswith("# "):
            heading = line[2:].strip()
            if heading:
                headings.append(heading)
    for match in re.finditer(r"<h1[^>]*>(.*?)</h1>", text, flags=re.I | re.S):
        heading = re.sub(r"<[^>]+>", "", match.group(1)).strip()
        if heading:
            headings.append(heading)
    return headings


def report_title(text: str) -> str:
    headings = markdown_headings(text)
    return headings[0] if headings else "Company Research Report"


def next_version(project: Path, basename: str) -> str:
    versions: list[tuple[int, int]] = []
    pattern = re.compile(rf"^{re.escape(basename)}_v(\d+)\.(\d+)\.(?:md|html|pdf)$")
    for path in project.iterdir():
        match = pattern.match(path.name)
        if match:
            versions.append((int(match.group(1)), int(match.group(2))))
    if not versions:
        return "v1.0"
    major, minor = max(versions)
    return f"v{major}.{minor + 1}"


def header_label(heading: str) -> str:
    mappings = [
        ("越疆", "Dobot Research Report"),
        ("目录", "TOC"),
        ("核心结论", "Executive Takeaways"),
        ("公司与财务", "Section 1 - Company & Finance"),
        ("产品", "Section 2 - Products & Technology"),
        ("行业", "Section 3 - Industry & Competitors"),
        ("供应链", "Section 4 - Supply Chain & Channels"),
        ("营销", "Section 5 - Marketing & Events"),
        ("针对供应链", "Section 6 - Strategic Judgment"),
        ("Data Gaps", "Data Gaps"),
        ("数据缺口", "Data Gaps"),
        ("Appendix Task 1", "Appendix 1 - Company & Finance"),
        ("附录一", "Appendix 1 - Company & Finance"),
        ("Appendix Task 2", "Appendix 2 - Products"),
        ("附录二", "Appendix 2 - Products"),
        ("Appendix Task 3", "Appendix 3 - Competitors"),
        ("附录三", "Appendix 3 - Competitors"),
        ("Appendix Task 4", "Appendix 4 - Supply Chain"),
        ("附录四", "Appendix 4 - Supply Chain"),
        ("Appendix Task 5", "Appendix 5 - Marketing"),
        ("附录五", "Appendix 5 - Marketing"),
        ("Sources", "Sources"),
    ]
    for needle, label in mappings:
        if needle in heading:
            return label
    ascii_heading = heading.encode("ascii", "ignore").decode("ascii").strip()
    return ascii_heading[:42] if ascii_heading else "Company Research Report"


def add_header_footer(pdf_path: Path, output_path: Path, headings: list[str], header_title: str) -> None:
    doc = fitz.open(pdf_path)
    current = ""
    font = font_path()
    total = doc.page_count
    for index, page in enumerate(doc):
        page_text = page.get_text("text")
        for heading in headings:
            if heading in page_text:
                current = heading
        rect = page.rect
        if index != 0:
            header = header_label(current or "Company Research Report")
            page.insert_text((42, 20), header[:42], fontsize=7.5, color=(0.35, 0.39, 0.44), fontfile=font)
            page.insert_text((rect.width - 152, 20), header_title[:32], fontsize=7.5, color=(0.35, 0.39, 0.44), fontfile=font)
            page.draw_line((42, 27), (rect.width - 42, 27), color=(0.82, 0.86, 0.90), width=0.4)
        if index != 0:
            footer = f"{index + 1} / {total}"
            page.draw_line((42, rect.height - 32), (rect.width - 42, rect.height - 32), color=(0.82, 0.86, 0.90), width=0.4)
            page.insert_text((rect.width / 2 - 12, rect.height - 18), footer, fontsize=8, color=(0.42, 0.45, 0.50), fontfile=font)
    doc.save(output_path)
    doc.close()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", help="Project folder containing FINAL_REPORT.md")
    parser.add_argument("--header-title", default=None, help="Short ASCII title for the PDF page header")
    parser.add_argument("--basename", default=None, help="Canonical output basename, e.g. 公司名_jiascan_report")
    parser.add_argument("--version", default=None, help="Canonical version, e.g. v1.0. Defaults to next available version.")
    args = parser.parse_args()

    project = Path(args.project).resolve()
    source = project / "FINAL_REPORT.md"
    if not source.exists():
        print(f"Missing report: {source}", file=sys.stderr)
        return 2

    text = source.read_text(encoding="utf-8")
    title = report_title(text)
    header_title = args.header_title or header_label(title)
    body = markdown.markdown(text, extensions=["tables", "toc"])
    html = (
        '<!doctype html><html><head><meta charset="utf-8">'
        f"<title>{title}</title>"
        f"<style>{CSS}</style></head><body>{body}</body></html>"
    )
    html_path = project / "report.html"
    pdf_path = project / "report.pdf"
    html_path.write_text(html, encoding="utf-8")

    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp_pdf = Path(tmp.name)
    url = "file://" + quote(str(html_path))
    subprocess.run(
        [
            chrome_path(),
            "--headless",
            "--disable-gpu",
            "--no-first-run",
            "--no-pdf-header-footer",
            f"--print-to-pdf={tmp_pdf}",
            url,
        ],
        check=True,
    )
    add_header_footer(tmp_pdf, pdf_path, markdown_headings(text), header_title)
    tmp_pdf.unlink(missing_ok=True)
    if args.basename:
        version = args.version or next_version(project, args.basename)
        canonical = f"{args.basename}_{version}"
        shutil.copy2(source, project / f"{canonical}.md")
        shutil.copy2(html_path, project / f"{canonical}.html")
        shutil.copy2(pdf_path, project / f"{canonical}.pdf")
        (project / "latest_report_name.txt").write_text(canonical + "\n", encoding="utf-8")
        print(f"Canonical outputs: {canonical}.md/.html/.pdf")
    print(f"Rendered {html_path}")
    print(f"Rendered {pdf_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
