"""Render a markdown deliverable to PDF via HTML + headless Microsoft Edge.

Usage:  python tools/render_pdf.py case-study.md [--main-only]
--main-only renders only the text before the "# Appendix"/"# Appendices" heading (used to check the 6-page limit).
"""
import re
import subprocess
import sys
from pathlib import Path

import markdown

EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
CSS = """
@page { size: A4; margin: 16mm 16mm 16mm 16mm; }
body { font-family: 'Segoe UI', Arial, sans-serif; font-size: 10pt; line-height: 1.38; color: #1d1d1d; }
h1 { font-size: 19pt; margin: 0 0 4px; color: #123b4a; }
h2 { font-size: 13.5pt; margin: 16px 0 6px; color: #123b4a; border-bottom: 1px solid #c9d6db; padding-bottom: 2px; }
h3 { font-size: 11pt; margin: 12px 0 4px; color: #1f5566; }
table { border-collapse: collapse; width: 100%; margin: 6px 0 10px; font-size: 8.8pt; }
th, td { border: 1px solid #cfd8dc; padding: 3px 6px; vertical-align: top; text-align: left; }
th { background: #eef3f5; }
pre { background: #f6f8f9; border: 1px solid #e0e6e8; padding: 6px 8px; font-size: 7.8pt; line-height: 1.25; overflow: hidden; }
code { font-family: Consolas, monospace; }
img { max-width: 100%; }
img[src*="flowchart"] { display: block; width: 78%; margin: 2px auto 4px; }
hr { border: none; border-top: 1px solid #d5dde0; margin: 12px 0; }
ul, ol { margin: 4px 0 8px; padding-left: 20px; }
p { margin: 4px 0 8px; }
.pb { page-break-before: always; }
h1, h2, h3 { page-break-after: avoid; break-after: avoid; }
tr, img { page-break-inside: avoid; break-inside: avoid; }
"""

def render(md_path: Path, main_only: bool) -> Path:
    text = md_path.read_text(encoding="utf-8")
    if main_only:
        text = re.split(r"\n# Appendi(?:x|ces)\b", text)[0]
    else:
        text = re.sub(r"\n# (Appendi(?:x|ces)\b)", r'\n<div class="pb"></div>\n\n# \1', text, count=1)
    html = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists"])
    suffix = ".main" if main_only else ""
    html_path = md_path.with_name(md_path.stem + suffix + ".html")
    pdf_path = md_path.with_name(md_path.stem + suffix + ".pdf")
    html_path.write_text(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head>"
                         f"<body>{html}</body></html>", encoding="utf-8")
    subprocess.run([EDGE, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf_path.resolve()}", html_path.resolve().as_uri()],
                   check=True, capture_output=True, timeout=120)
    html_path.unlink()
    pages = len(re.findall(rb"/Type\s*/Page[^s]", pdf_path.read_bytes()))
    print(f"{pdf_path.name}: {pages} pages")
    return pdf_path

if __name__ == "__main__":
    render(Path(sys.argv[1]), "--main-only" in sys.argv)
