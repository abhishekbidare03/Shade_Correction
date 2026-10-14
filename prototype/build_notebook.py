"""Build shade_correction.ipynb from shade_correction.py (percent format) and execute it.

Usage:  python build_notebook.py
"""
import re
from pathlib import Path

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

here = Path(__file__).parent
src = (here / "shade_correction.py").read_text(encoding="utf-8")

cells = []
for block in re.split(r"^# %%", src, flags=re.M)[1:]:
    header, _, body = block.partition("\n")
    if header.strip() == "[markdown]":
        text = "\n".join(line[2:] if line.startswith("# ") else line.lstrip("#") for line in body.strip().splitlines())
        cells.append(nbformat.v4.new_markdown_cell(text))
    else:
        cells.append(nbformat.v4.new_code_cell(body.strip()))

nb = nbformat.v4.new_notebook(cells=cells, metadata={"kernelspec": {"name": "python3", "display_name": "Python 3", "language": "python"}})
ExecutePreprocessor(timeout=1200, kernel_name="python3").preprocess(nb, {"metadata": {"path": str(here)}})
nbformat.write(nb, here / "shade_correction.ipynb")
print("wrote", here / "shade_correction.ipynb")
