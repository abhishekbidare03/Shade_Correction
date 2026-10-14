# Print Shade Correction: Case Study and Prototype

Case study, pilot proposal and a working prototype for correcting printed shade drift on
ceramic tiles at batch changeover.

## Repository contents

| Path | Description |
|---|---|
| `case-study.pdf` | Case study and pilot proposal (6-page main body + appendices) |
| `case-study.md` | Source of the case study |
| `procurement-note.pdf` / `.md` | One-page summary note for a non-technical reader |
| `submission-form.md` | Submission form answers |
| `prototype/shade_correction.ipynb` | Prototype notebook, executed, with all outputs |
| `prototype/shade_correction.py` | The same prototype as a plain Python script |
| `prototype/rounds_to_match.png` | Main result chart |
| `prototype/build_notebook.py` | Rebuilds and executes the notebook from the script |
| `assets/solution-flowchart.png` | Solution flowchart used in the case study |
| `tools/make_flowchart.py` | Regenerates the solution flowchart |
| `tools/render_pdf.py` | Renders the markdown documents to PDF |

## How to view

- **Documents:** open `case-study.pdf` and `procurement-note.pdf`, or read the `.md` files directly on GitHub.
- **Prototype:** open `prototype/shade_correction.ipynb` on GitHub. It renders with all outputs and the chart, so nothing needs to be installed to read it.

## How to run the prototype locally

Requirements: Python 3.12 with `numpy`, `scipy` and `matplotlib` (plus `nbformat`, `nbconvert`
and `ipykernel` to rebuild the notebook).

```bash
pip install numpy scipy matplotlib nbformat nbconvert ipykernel
cd prototype
python shade_correction.py      # prints results and saves rounds_to_match.png (about 1 minute)
python build_notebook.py        # rebuilds and executes shade_correction.ipynb
```

To regenerate the PDFs (Windows, Microsoft Edge installed):

```bash
pip install markdown
python tools/render_pdf.py case-study.md
python tools/render_pdf.py procurement-note.md
```
