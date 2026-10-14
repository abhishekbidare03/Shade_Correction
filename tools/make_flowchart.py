"""Draw the solution flowchart used in section 6.1 of the case study.

Usage:  python tools/make_flowchart.py   ->  assets/solution-flowchart.png
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon

OUT = Path(__file__).resolve().parent.parent / "assets" / "solution-flowchart.png"

STYLE = {
    "setup":    dict(fc="#eef0f8", ec="#4a4f8a"),
    "process":  dict(fc="#e8f1f4", ec="#1f5566"),
    "decision": dict(fc="#fff4e0", ec="#b7791f"),
    "release":  dict(fc="#e6f4ea", ec="#2e7d32"),
    "escalate": dict(fc="#fdecea", ec="#c62828"),
}
LINE = "#37474f"

fig, ax = plt.subplots(figsize=(10, 6.7))
ax.set_xlim(0, 100)
ax.set_ylim(-1.5, 67)
ax.set_aspect("equal")
ax.axis("off")


def box(x, y, text, kind, w=28, h=7, bold=False):
    s = STYLE[kind]
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.25,rounding_size=1.2",
                                fc=s["fc"], ec=s["ec"], lw=1.4))
    ax.text(x, y, text, ha="center", va="center", fontsize=9.2, color="#1d1d1d",
            fontweight="bold" if bold else "normal", linespacing=1.25)


def diamond(x, y, text, w=20, h=10):
    s = STYLE["decision"]
    ax.add_patch(Polygon([(x, y + h / 2), (x + w / 2, y), (x, y - h / 2), (x - w / 2, y)], closed=True,
                         fc=s["fc"], ec=s["ec"], lw=1.4))
    ax.text(x, y, text, ha="center", va="center", fontsize=9.2, linespacing=1.2)


def arrow(p0, p1, label=None, offset=(0, 0), dashed=False):
    ax.annotate("", xy=p1, xytext=p0, arrowprops=dict(arrowstyle="-|>", color=LINE, lw=1.3,
                                                      linestyle="--" if dashed else "-",
                                                      shrinkA=0, shrinkB=0, mutation_scale=13))
    if label:
        ax.text((p0[0] + p1[0]) / 2 + offset[0], (p0[1] + p1[1]) / 2 + offset[1], label,
                fontsize=8.6, color=LINE, ha="center", va="center", fontweight="bold")


# Column headers
ax.text(16, 65, "ONE-TIME SET-UP, PER SKU", ha="center", fontsize=10, fontweight="bold", color="#4a4f8a")
ax.text(50, 65, "AT EVERY BATCH CHANGEOVER", ha="center", fontsize=10, fontweight="bold", color="#1f5566")
ax.plot([33, 33], [6.5, 66], color="#cfd8dc", lw=1, ls=":")

# One-time set-up (left)
box(16, 57.5, "Measure the master tile\n→ stored as digital master", "setup", w=26)
box(16, 46, "Print & fire 8 test tiles\n(one ink channel +15% each)", "setup", w=26)
box(16, 34.5, "Tool builds the SKU's\nsensitivity profile", "setup", w=26)
arrow((16, 54), (16, 49.5))
arrow((16, 42.5), (16, 38))

# Changeover flow (centre)
box(50, 57.5, "Print & fire the first tile;\nQC lab measures it", "process")
diamond(50, 46, "Within\ntolerance?")
box(50, 34.5, "Tool calculates the correction\ne.g. brown +3%, yellow −1%", "process")
diamond(50, 23, "Reachable\nwith ink?")
box(50, 11.5, "QC lead approves; pre-press\napplies it as a versioned layer\n(master file stays locked)", "process", h=8.5)
box(50, 1.8, "Fire a confirmation tile and measure it", "process", w=34, h=4.6)

arrow((50, 54), (50, 51))
arrow((50, 41), (50, 38), "No", offset=(3, 0))
arrow((50, 31), (50, 28))
arrow((50, 18), (50, 15.75), "Yes", offset=(3.5, 0.2))
arrow((50, 7.25), (50, 4.1))

# Profile feeds the calculation
arrow((29, 34.5), (36, 34.5), dashed=True)
ax.text(32.5, 36.2, "profile", fontsize=8.2, color=LINE, ha="center", style="italic")

# Outcomes (right)
box(84, 46, "Release the batch", "release", w=24, bold=True)
box(84, 23, "Flag: ink cannot fix it\n→ escalate to glaze /\nkiln team", "escalate", w=24, h=8.5)
arrow((60, 46), (72, 46), "Yes", offset=(0, 1.4))
arrow((60, 23), (72, 23), "No", offset=(0, 1.4))

# Loop: confirmation tile back to the tolerance check
ax.plot([67, 98.5, 98.5, 52], [1.8, 1.8, 52.6, 52.6], color=LINE, lw=1.3)
arrow((52, 52.6), (50.2, 52.6))
ax.text(98.5, 30, "re-check", rotation=90, fontsize=8.4, color=LINE, ha="right", va="center",
        fontweight="bold")

OUT.parent.mkdir(exist_ok=True)
fig.savefig(OUT, dpi=200, bbox_inches="tight", pad_inches=0.05)
print("wrote", OUT)
