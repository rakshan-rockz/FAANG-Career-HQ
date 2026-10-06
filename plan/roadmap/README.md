# Hub Roadmap — How the Tracks Work

This repo runs two tracks of its own and coordinates four course repos.

| Track | Plan | Output | Budget |
|---|---|---|---:|
| **Behavioral** (`B.<phase>.<n>`) | [`../behavioral/README.md`](../behavioral/README.md) (method, rubric) + `../behavioral/phase-01…07.md` | `behavioral/stories/`, `behavioral/mocks/` | ~40 h |
| **Career ops** (`H.0.1`, `CO.<phase>.<n>`) | [`../career-ops/README.md`](../career-ops/README.md) | `career/` | ~20 h |
| **Year order of both** | [`TRACK-switch.md`](TRACK-switch.md) (parsed by `tools/forecast.py`; keep its exact table format) | | 60 h |
| **The 12-month plan across all repos** | [`../SWITCH-PLAN.md`](../SWITCH-PLAN.md) (the mentor's) | | ~980 h |

## 1. Session IDs

- `H.0.1`: hub intake. `B.<phase>.<n>`: behavioral. `CO.<phase>.<n>`: career ops.
- `progress/STATUS.md` holds the **Next session** ID; `/today` resumes it (when today's slot belongs to this
  repo; otherwise it sends the learner to the right course repo).
- The order is `TRACK-switch.md`, not the phase-file order: behavioral and career-ops rows interleave
  across the year.

## 2. The TRACK-switch convention (shared by every repo)

Every course repo has (or will have) `plan/roadmap/TRACK-switch.md` with a
`**Track total (est.):** NNN h` line and an ordered table `| # | ID | Type | Topic | Scope | Est h |`.
`tools/forecast.py` sums `Est h` from the repo's **Next session** row onward = remaining hours. Rows under
"Deferred to the depth pass" are not counted (they are not deleted; they wait for after the switch).

## 3. Session types in this repo

| Type | Name | Run by | What happens |
|---|---|---|---|
| `Intake` | Intake | `/intake` | Profile facts for the year plan |
| `L` | Method lesson | Claude from the row | Short explanation → learner attempts → critique |
| `MINE` | Story mining | `/story mine` | Guided recall, bullet notes only; no drafting |
| `ST` | Story workshop | `/story` | Mine → STAR/CARL → quantify → probe P1–P5 → tighten → speak |
| `CF` | Company framework | Claude from the row (+ `/story` for gaps) | Framework + round format → mapping → spoken answers, probed |
| `DD` | Project deep dive | Claude from the row | 8-part outline; defended as a design review |
| `HQ` | Hard questions | Claude from the row | Draft → speak → critique for truth, brevity, framing |
| `HM` | Hiring-manager round | `/bmock hm` | HM simulation incl. the learner's questions |
| `BM` | Behavioral mock | `/bmock` | Timed, company-styled, probed, scored /100 |
| `R` | Review | Claude from the row | Cold retell of the bank, unlabeled questions |
| `CO` | Career-ops workshop | `/resume`, `/offer`, `/pipeline` or from the row | Learner produces, Claude critiques |
| `OPS` | Pipeline ops | `/pipeline`, `/debrief` | Recurring pipeline hygiene and interview debriefs |

## 4. Mastery bars

- **Story ✅ interview-ready**: told in 2–3 min from its cue, "I"-actions + a number, survives 3 probe
  levels, mapped to ≥ 2 frameworks, retold cold at +21 days (`../behavioral/README.md` §3).
- **Company style ready**: ≥ 80/100 in that company's `/bmock`, no rubric category below 60% of its points,
  within 7 days before the real loop.
- **Resume ready**: one page, ATS-clean, every bullet defensible for 5 minutes, ≥ 70% quantified, two
  variants, one human review.
- **Track done** (B.7.6): last three mocks average ≥ 80, all stories ✅.

## 5. The probe ladder (the behavioral analogue of the DSA hint ladder)

In `/story` coaching the learner gets the **smallest nudge** that improves the story, never a rewritten
story: *C0* "What's the headline?" → *C1* "Which sentence says what *you* did?" → *C2* "What number would
prove that?" → *C3* "What was the decision point and the options?" → *C4* a structural outline
(headline / 3 beats / result / learning) for the learner to fill. Interviewer probes P1–P6 are in the
behavioral README §5. Claude never writes the story's content.

## 6. Pedagogy (why it's shaped this way)

| Principle | Evidence base | Where it shows up |
|---|---|---|
| Spacing | Ebbinghaus; Cepeda et al. | Stories mined in month 1, drafted months 2–3, rehearsed +2/+7/+21/+60, mocked months 4–8 |
| Retrieval practice | Roediger & Karpicke | Cold retells (B.2.7), unlabeled mock questions |
| Generation effect | Slamecka & Graf | The learner writes every story and bullet |
| Deliberate practice | Ericsson | Each mock's two lowest rubric categories drive the next story session |
| Interleaving | Rohrer & Taylor | Mocks never name the LP/value; themes and companies mixed |
| Transfer via variation | Marton | One fact base, many framings (LPs, G&L, values, HM) |
| Desirable difficulties | Bjork | Pressure probes, time limits, Bar-Raiser style, human mock |
| Just-in-time | — | Company-style mock within 7 days of each real loop; negotiation practice just before offers |
