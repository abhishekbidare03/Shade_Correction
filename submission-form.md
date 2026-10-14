# Submission Form: Task 3, Client A (Ceramic Tiles)

---

### 1. In two sentences: what is the client's real problem, and how is it different from what they asked for?

They can already measure how far a new batch is from the master tile. What they can't do
is turn that difference into the right change to the printer's input file, so they guess,
print and fire for 6–7 hours per round while the line keeps making off-shade tiles. They
asked for "video/vision analytics" to compare tiles, but they need a **correction
calculator** that uses their existing spectrophotometer readings to get the file right in
one correction instead of many rounds.

---

### 2. Who are the people in this deal, and what does each of them need to hear from you?

| Person | What they need to hear |
|---|---|
| **Special Projects Lead, Procurement** (main contact) | Fixed price, payments tied to results, a week-8 stop rule, first result on their own data in week 2. |
| **Head of IT & OT Procurement** (asked about hardware/OEMs) | No new production hardware in the pilot. We reuse their lab spectrophotometer, run on a lab PC off the OT network, and an at-line station with an instrument OEM is a later option, not a requirement. |
| **Plant QC / lab team** (daily users, *not on the call*) | The tool gives a fix from readings they already take; they approve every change; it removes guesswork and blame, not jobs. |
| **Design / pre-press team** (edits the file, *not on the call*) | Only colour-channel adjustments, applied as a separate layer; the master artwork is never overwritten. |
| **Plant / production manager** | Fewer off-shade m² per batch change; test tiles in planned slots. |
| **Ink supplier and printer/RIP vendor** (external) | We sit on top of their tools (RIP curves, ink profiles), not against them: the product-level, master-anchored, vendor-neutral layer across all 3 plants. |

---

### 3. The five questions you would ask on the next call, ranked. For each: why it matters, and what you assumed while you wait for the answer.

| # | Question | Why it matters | Assumed meanwhile |
|---|---|---|---|
| 1 | **How is the print file built and changed?** Printer/RIP, file format, the 6 colours (any effect inks?), how "+5% brown" is applied today, and what the RIP and ink supplier already do for colour. | If we can't apply the fix the way they really edit files, nothing works. If a vendor already does part of it, we build less. | 6 colour channels edited per channel in Photoshop; a fix is a % gain per channel; no effect ink among the 6; no vendor product-level correction. |
| 2 | **How does the lab measure today?** Instrument, spots and faces on a patterned tile, ΔE formula, pass threshold, data export. | Defines the input and the pass/fail number. | Exportable readings; 3–5 fixed spots; pass at ΔE00 ≤ 1.0. |
| 3 | **Volumes and money:** lines, m²/hour, corrections per line per month, rounds per correction, what happens to off-shade (downgrade or shade lot), price per m². | The whole business case; the off-shade figure was unclear on the recording. | 4 lines; 4 corrections per line per month; 1–2 rounds; 5,000 m² per event; ₹350/m²; 15–40% loss. |
| 4 | **Products and history:** active SKUs, which share inks and glaze, repeat frequency, past correction records. | Decides how much one-off "teaching" is needed; records give a ready baseline. | Hundreds of SKUs; no usable records, so we measure the baseline live. |
| 5 | **People, sign-off, site:** daily users, approver, access to QC and design, pilot plant. | The real users weren't on the call; the plant choice changes cost. | QC runs it, QC head approves, design applies; UAE plant (the one they invited us to). |

---

### 4. Which options did you consider, and why did you pick the one you did? What did you rule out, and why?

**Picked: a measure-and-correct tool.** Save the master as numbers → 8 planned test tiles
per product teach the tool how each colour moves the shade → at each batch change it
computes the fix from the first tile → QC approves → 1 check tile. It needs no historical
dataset (the 8 tiles *are* the data, at about the same lab effort as one of today's guessing
rounds), no kiln model (it learns from fired results), and no new hardware. It works
whatever caused the drift, and it's the same method as computer colour matching in textile
and paint.

**Ruled out:**
- **Inline camera system:** not needed (only batch changes matter), unreliable for exact colour under factory light, expensive, and worse than the spectrophotometer they already own.
- **Physics model of ink/glaze/kiln:** needs process data that doesn't exist, slow, and root cause is out of scope by their own request.
- **Large ML model on history:** no dataset exists. Possible later, once the tool has logged runs.
- **Full colour chart per product:** accurate but many more test tiles; kept as the **fallback** if the stop rule triggers.
- **Buying from the RIP/ink vendor:** they tune printers and inks, not "this SKU vs its master". We check what they offer (Q1) and build on top.

---

### 5. How will the client know the pilot worked? Metric, baseline, threshold, how many runs, who measures, and what result would make you stop.

| | |
|---|---|
| **Metric** | ΔE00 between the corrected tile and the digital master, after one correction |
| **Baseline** | Their historical correction records (rounds, hours, off-shade m²), cross-checked against batch changes observed in weeks 3–6 under the old method |
| **Threshold** | ≥ 80% of batch changes within tolerance (ΔE00 ≤ 1.0, or theirs) after 1 correction; new products reported separately (they need the 8 test tiles first) |
| **Runs** | ~20 batch changes across ≥ 5 products in one plant: real batch changes on all its lines, plus planned test runs (QC secretly offsets a file and the tool must bring it back) |
| **Who measures** | The client's QC lab with their own instrument. We never enter readings. |
| **Stop** | At week 8, after 10 batch changes: if fewer than half work, stop. Fallback: the full colour chart, or stop and invoice only milestones reached. |

Honest note: with ~20 runs, 80% means the true rate could be roughly 58–92%. It's a go/no-go signal, not a precise number.

---

### 6. What does this cost the client, and what does it cost us to deliver? Show the arithmetic and name the pricing structure. What value does the client get, in their money?

**Pricing structure:** fixed-price pilot with milestone payments, then a per-line monthly subscription.

**Price to the client (UAE pilot, excl. GST):** **₹52,00,000** (~$59,100)
- 20% at kickoff = ₹10,40,000
- 40% at the first live fix within tolerance (~week 6) = ₹20,80,000
- 40% at acceptance (week 12) = ₹20,80,000
- India-plant option: ₹47,00,000 (less travel)
- After go: ₹1,25,000 per line per month (~$1,420)
- If the stop rule triggers, only milestones reached are paid.

**Our cost to deliver (UAE):**

| Line | Arithmetic | Cost |
|---|---|---|
| FDE | 1.0 FTE × 3 months × ₹3,50,000 | ₹10,50,000 |
| Colour/data engineer | (1.0 × 2 + 0.25 × 1) = 2.25 PM × ₹3,00,000 | ₹6,75,000 |
| Software engineer | 0.5 × 3 = 1.5 PM × ₹2,00,000 | ₹3,00,000 |
| Engagement lead | 0.25 × 3 = 0.75 PM × ₹4,00,000 | ₹3,00,000 |
| **Labour** (7.5 person-months, loaded ≈ 1.4× salary) | | **₹23,25,000** |
| Travel | FDE 28 nights ₹3,84,000 + colour engineer 14 nights ₹2,16,000 + week-12 review ×2 ₹2,40,000 | ₹8,40,000 |
| Gloss meter (if they lack one) | | ₹1,25,000 |
| Contingency 15% (incl. a 3-week extension) | 32,90,000 × 0.15 | ₹4,93,500 |
| **Total cost** | | **₹37,83,500** (~$43,000) |

**Margin:** (52,00,000 − 37,83,500) ÷ 52,00,000 ≈ **27%**. After Phase 0 pre-sales at our
cost (₹2,20,000), ≈ **23%**. India option: cost ₹32,98,200, margin ≈ 30% (≈ 25% after pre-sales).
Running cost to us after go: hosting ~₹15,000/month (₹0 on-prem) + ~0.2 FTE support per plant.

**Client's running cost per line per month:** ₹1,40,640 with the tool (₹1,25,000
subscription + ₹13,440 lab/design time and tiles + ₹2,200 allowance) vs ₹25,600–46,800 today.
Client's own effort during the pilot: ≈ ₹81,000.

**Value to the client (per line):** off-shade m² = line output × hours until the corrected file is on the line.
- Today: 8 h (1 round) to 14.5 h (2 rounds). With the tool: 3 h (known product), 9.5 h (new product). With an 80/20 mix, that's a **46–70%** cut.
- Loss per batch change: 5,000 m² × ₹350 × 15–40% = ₹2,62,500–₹7,00,000; × 4 per month = ₹10,50,000–₹28,00,000.
- Gross saving: ₹4,83,000–₹19,60,000 per month; minus extra running cost (₹1,15,040 / ₹93,840) = **net ₹3,67,960–₹18,66,160 per month = ₹44 lakh–₹2.24 crore per year per line**.
- Payback: one line 14 → 2.8 months; **4-line plant 3.5 → 0.7 months**.

---

### 7. Timeline. What is the first result the client sees, and when? Which steps depend on the client rather than on us?

| Week | Result | Depends on the client |
|---|---|---|
| **1–2** | **First result (week 2):** difference report and suggested fixes for their own tiles | Exports of their readings, one print file, past correction records |
| 3–4 | On-site set-up, masters saved as numbers, baseline agreed | Site access, QC and design time, IT approval |
| 5–6 | 8 test tiles per pilot product; **first live fix (week 6)** | Sample slots on the line |
| 7–11 | Pilot run with weekly scorecard; **checkpoint at week 8** | Batch schedule, lab readings, permission for planned test runs |
| 12 | Go / no-go with numbers | Decision meeting |

Limit we state up front: already-fired tiles (week 2) can show the difference and the
suggested fix, but only a print on their line (week 6) can prove the fix works.

---

### 8. Where did you push back on the client, narrow their ask, or tell them not to do something?

1. **Not "video analytics".** A camera is worse than the spectrophotometer they already own; we build the step after measuring.
2. **"Minutes" applies to calculating the fix, not the whole loop.** A fired check tile is unavoidable: 2 firings for a known product, 3 for a new one.
3. **No root-cause project now.** The correction works whatever caused the drift; the data we log makes a later study cheaper.
4. **Stop overwriting the print file.** Lock the master and save each fix separately. That's the real cause of the "2021 file is way off" drift.
5. **Match the master, never the previous run.** Matching the previous run is how drift builds up.
6. **No automatic push to the printer.** QC approves every fix.
7. **Gloss is measured and reported, not promised.** It comes mostly from glaze and firing.
8. **Ink can't fix a darker or yellower glaze.** The tool says so and sends it to the glaze team instead of faking a fix.
9. **One plant first,** not three countries; and don't judge it on mailed tiles alone.

---

### 9. What is most likely to go wrong with your plan, and what in these notes did you not trust?

**Most likely to go wrong:**
- **The print file can't be adjusted the way we assume** (locked RIP, a different format, effect inks among the 6 channels). That's Question 1; the fallback is RIP channel curves.
- **Their line behaves less linearly than our simulator,** so one correction isn't enough. The week-8 stop rule protects both sides; the fallback is a full colour chart.
- **Too few real batch changes in 12 weeks.** Mitigated by all lines in one plant, planned test runs, and an extension at our cost.
- **Readings at a different spot or face** from the master create false differences. Mitigated by a measuring template and face labels.
- **The daily users (QC, design) weren't on the call** and may not adopt it.
- **The value is smaller than modelled** if off-shade is sold as a separate shade lot. That's why the value is a 15–40% loss range, not one number.

**What I didn't trust in the notes:**
- "5,000–10,000 m²": marked unclear in the recording. I used the low end.
- "6–7 hours": per round, or for a whole correction? The notes say both, so I modelled 1 and 2 rounds.
- "5–6 minutes": not physically possible end to end, because firing takes time.
- "99% matching": no metric was named.
- "Same print file every time" (the brief) vs "the reference keeps getting edited" (the notes): I believe the file has drifted.
- "Video analytics": their label for the need, not the need itself.
- The process flow document: referenced, but not available.
- My own simulator: it supports the logic, not their kiln. Only the pilot can prove that.

---

### 10. What did you use AI for? Which tools, where they helped, where they misled you, and what you threw away.

I used Claude Code (Claude Opus 5.5) as a working assistant throughout. *[Add any other tools you used.]*
I used it to read through the call notes with me, draft and restructure the documents, write the
prototype code and the PDF rendering script, and cross-check that numbers matched across files.
I set the direction, reviewed every draft and pushed back on it in several rounds. The scope,
pricing structure, pilot design, stop rule and every pushback to the client were my decisions.

Where it led me astray, and what I threw away:
- **A "70% saving" figure** that was assumed rather than derived. I rebuilt it from line throughput, which gives a 46–70% range.
- **Pricing in USD at Western rates.** I re-costed it at Indian rates in rupees.
- **A one-line pilot.** It would have seen only about five changeovers in the pilot window. I widened it to all lines of one plant plus planned test runs.
- **"+5%" characterisation steps,** which were too close to measurement noise. I moved to +15%.
- **An implied UAE partner and OEM partnership.** I can't claim a partnership I haven't confirmed, so I removed it.
- **Editing the master print file directly.** That is the cause of the drift the client described, so I replaced it with a locked master and versioned corrections.
- **Too much detail.** By the third draft the plan was too technical for a client to follow quickly. I cut the story back to four steps and moved the detail into appendices.
- **In the prototype:**
  - The first version raised 14 false "can't reach" alarms because it trusted an unconfirmed profile. After the fix it raised 5 false alarms out of 143 and still caught all 13 genuinely unfixable cases.
  - The stale-profile check never fired in my first tests. Rather than construct a scenario to make it fire, I report what I found: stored profiles held up under normal drift, and the check only triggers under an extreme kiln change.

---

### GitHub Repo URL

*[Add the private repository URL after creating it.]*
