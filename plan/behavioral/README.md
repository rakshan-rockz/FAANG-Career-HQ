# Behavioral Track — Method

**Budget:** ~40 h of the switch year (plus ~20 h career ops; see `../career-ops/README.md`).
**Sessions:** `B.<phase>.<n>` in `phase-01.md` … `phase-07.md`; year order in `../roadmap/TRACK-switch.md`.

> Behavioral rounds are not "soft". At Amazon a Bar Raiser can veto an otherwise strong loop; at Atlassian
> the values interview is a standalone pass/fail round; at Google G&L is scored like any other round; at
> Indian product companies the hiring-manager round decides the level (SDE-2 vs SDE-1) and therefore the
> band. An engineer who solves the coding rounds and then says "we built a thing, it went well" loses the
> offer or gets down-levelled. This track trains the opposite: specific, owned, measured, reflective stories
> that survive five levels of probing.

---

## 1. What interviewers are actually scoring

Every behavioral question is a proxy for one question: **"Will this person behave like this again, on my
team, at the level I'm hiring for?"** So they look for:

| Signal | What they want to hear | What kills it |
|---|---|---|
| **Ownership** | *I* decided, *I* built, *I* escalated, *I* followed up | "We", "the team", passive voice |
| **Judgement** | the options you weighed and why you chose one | "It was obvious" |
| **Impact** | a before/after number, a customer or business effect | "It went well", no result |
| **Scope** (level signal) | SDE-2: owns a feature/component end-to-end, influences peers; Senior: owns a system/cross-team outcome | Only task-level work, only following instructions |
| **Collaboration** | disagreed well, brought people along, gave credit | blaming, "they were wrong", hero stories |
| **Growth** | a real mistake, what you changed afterwards, evidence the change stuck | no failure, a "fake weakness", no reflection |
| **Honesty under probing** | details stay consistent at depth 3–5 | story falls apart or changes when probed |

## 2. Answer frameworks: STAR and CARL

**STAR** (default for most companies):

| Part | Share of answer | Contains |
|---|---|---|
| **S**ituation | ~10% | One or two sentences: team, product, stakes. Enough context to care, no more |
| **T**ask | ~10% | *Your* responsibility or the goal; why it was hard (constraint, deadline, ambiguity) |
| **A**ction | ~60% | What **you** did, step by step, with the reasoning and the options rejected. The heart of the answer |
| **R**esult | ~20% | Numbers; business/customer effect; what happened next; **what you learned** |

**CARL** = **C**ontext · **A**ction · **R**esult · **L**earning. Same bones, with *Learning* promoted to a
first-class part. Use CARL for failure, mistake, conflict and "what would you do differently" questions,
and at companies that weight growth (Microsoft growth mindset, Meta "growing continuously", Google
intellectual humility). A STAR answer can always end with one Learning sentence; a failure answer
**must**.

Rules for both:
- Open with a **headline** (one sentence that answers the question) before the story:
  "The clearest example is when I pushed back on shipping the key-rotation change without a rollback path."
- **I > we.** Say "we" only for context ("our team of 5 owned…"); every action sentence is "I".
- **One story per answer.** If they want another, they'll ask.
- **End on the result and the learning**, then stop. Silence is fine; the interviewer will probe.

## 3. The story bank

A **story bank** is 10–14 real stories, each rehearsed until it can be told at three lengths and bent to
fit many questions. Interviews ask ~30 different question types, but they collapse onto ~12 themes.

**Themes every bank must cover** (a story usually covers 2–4):

1. Most complex / proudest technical project (the **deep dive**, §6)
2. Conflict with a peer
3. Disagreement with your manager (and you were right / you were wrong)
4. Failure or mistake you caused
5. Ambiguity: vague requirements, no owner, unclear problem
6. Tight deadline / delivering under pressure / trade-off of scope vs quality
7. Leadership without authority / influencing another team
8. Mentoring, helping a teammate grow, onboarding
9. Customer impact / going beyond the ticket for a user
10. Security, quality or production incident (for a quantum-safe security engineer this is a *strength*:
    key management, crypto migration, certification, vulnerability handling)
11. Raising the bar: improving a process, tooling, tests, code quality
12. Learning something fast / diving deep into an unfamiliar area
13. Taking a calculated risk / bias for action with incomplete data
14. Saying no / pushing back on a stakeholder

**Each story file** (`behavioral/stories/NN-slug.md`, template in `behavioral/stories/_template.md`) holds:
the one-line cue, themes, company-value mapping, the STAR/CARL text **in the learner's words**, the
numbers (with how each was measured), the probe answers (§5), the 30-second / 2-minute / 4-minute
versions, and a rehearsal log.

**Story statuses:** ⬜ mined (raw notes) · 🟨 drafted (STAR + numbers + probes written) · ✅ interview-ready.
**✅ interview-ready** = all five:
1. Told aloud in 2–3 minutes from the one-line cue, no notes;
2. Every action sentence is "I", with at least one number or a stated measure;
3. Survives three probe levels without new vagueness or contradictions;
4. Mapped to ≥ 2 company-value frameworks;
5. Retold cold at the +21-day rehearsal (`progress/review-queue.md`).

## 4. Mapping stories to company value frameworks

The same story is **re-framed, never re-invented**: the facts stay fixed; the headline and the emphasis
change. The coverage matrix in `behavioral/stories/README.md` has one column per framework:

| Company | Framework | Where it's taught |
|---|---|---|
| Amazon | 16 Leadership Principles (each round covers 2–3 LPs; Bar Raiser probes hardest) | `phase-03.md` |
| Google | G&L: Googleyness (ambiguity, humility, collaboration, bias to action, user focus) + Leadership (emergent) | `phase-04.md` B.4.1 |
| Microsoft | Growth mindset, customer obsession, collaboration / One Microsoft, inclusion | B.4.2 |
| Meta | Behavioral signals: resolving conflict, embracing ambiguity, driving results, growing continuously, communicating | B.4.3 |
| Atlassian | 5 values + the dedicated values interview | B.4.4 |
| Uber | Cultural values (verify current wording) | B.4.5 |
| Indian product cos | Hiring-manager + "culture fit" rounds; ownership, bias for action, customer-first (verify per company) | B.4.5, B.7.1 |

Rule of thumb: every LP / value must have **a primary story and a backup story**; no story is primary for
more than 4 LPs (or one weak story sinks a whole loop).

## 5. The depth probe

Interviewers don't score the first telling; they score what survives the follow-ups. Every story is drilled
down this **probe ladder**, one level per turn (in `/story` and `/bmock`):

| Level | Probe | Tests |
|---|---|---|
| **P1** Ownership | "What exactly did *you* do? What did others do?" | "I" vs "we"; real scope |
| **P2** Specifics | "Walk me through the moment you decided X. What were the options? Why that one?" | judgement, whether it really happened |
| **P3** Evidence | "How did you measure that? What was the number before and after?" | impact, honesty |
| **P4** Consequence | "And then what? What happened next month? Who was unhappy?" | follow-through, second-order effects |
| **P5** Reflection | "What would you do differently? What did you learn, and where have you used it since?" | growth, self-awareness |
| **P6** Pressure (Bar Raiser / HM) | "Your manager disagreed and you did it anyway?" · "Wasn't that your fault?" · "Why didn't you escalate earlier?" | composure, honesty, backbone without arrogance |

A story is *drafted* when P1–P5 have written answers. It's *ready* when it survives P1–P6 spoken.

## 6. The "most complex project" deep dive

Almost every loop has one: "Tell me about the most complex/impactful project you've worked on" (Amazon
"Dive Deep", Google/Meta project retrospective, Microsoft/Atlassian/Uber HM rounds, every Indian
product-company HM round). It is **half behavioral, half system design**, and at SDE-2 it often decides the
level. Prepare **one flagship project** (plus one backup) to 30 minutes of depth:

1. **Problem & why it mattered** (users, business, security/compliance stakes).
2. **Your role and scope** (what you owned vs the team).
3. **Architecture**: a diagram you can draw in 3 minutes (components, data flow, storage, interfaces).
   Uses the vocabulary from `FAANG-System-Design-Master` (C4 container view, ADRs).
4. **The hardest technical decision**: options, trade-offs, why this one. (An ADR, spoken.)
5. **Scale & numbers**: QPS/throughput, latency, data size, devices/customers, key-ops/sec, uptime.
6. **Failure & operations**: what broke, how you found it, what changed.
7. **What you'd do differently** with today's knowledge (and at 10× scale).
8. **Cross-team work**: who you had to convince.

Quantum-safe security framing for QNu Labs work (learner confirms what is true and what is shareable):
QKD / PQC integration, key management and rotation, HSM/crypto-library integration, performance of
crypto operations, standards/certification (e.g. FIPS/Common Criteria style processes; verify which apply),
secure-by-design reviews. **Never disclose confidential details**: describe architecture at the level the
learner's NDA allows; replace customer names with "a large bank/telecom customer".

Session B.5.x ties this to the System Design repo: the learner rehearses the project as a design review.

## 7. Answer length and structure

| Version | Length | When |
|---|---|---|
| **Headline** | 1 sentence | Always first |
| **Short** | 30–45 s | "Tell me briefly about…", screening calls, when the interviewer is clearly short on time |
| **Standard** | 2–3 min (~300–400 spoken words) | Default. Most interviewers interrupt after ~3 min |
| **Deep dive** | 5–10 min, then probes | Project deep dive, HM rounds, "walk me through it" |

Over 4 minutes without the interviewer asking for more = rambling. Under 60 seconds for a standard
question = no substance. Timers are used in every `/bmock` answer.

## 8. Delivery: voice practice

- **Speak it.** Dictate answers (voice input / phone recording) from B.2 onward; Claude scores the
  transcript for structure, "I"-ratio, filler, length. Written polish ≠ spoken fluency.
- **Record and re-listen** once per week to at least one answer (pace, fillers, "umm", trailing off).
- **Don't memorise scripts.** Memorise the bullet skeleton (headline → 3–4 action beats → number →
  learning); speak freely around it. Scripts crack under probing.
- **Energy and ownership in the voice**: first-person, active verbs, concrete nouns.
- **Pausing is allowed.** "Let me think of the best example" + 5 seconds is better than a weak story.
- **Online interview hygiene**: camera at eye level, notes allowed only as the story-cue list (verify per
  company; some forbid notes).

## 9. Red flags (called out by name whenever they happen)

| Red flag | Example | Fix |
|---|---|---|
| **Blaming** | "QA missed it", "my manager didn't understand" | Own your part; describe others neutrally |
| **"We" without "I"** | "We decided to migrate…" | "I proposed the migration and wrote the plan" |
| **No metrics** | "It improved performance a lot" | "p99 from 180 ms to 40 ms", or say what was measured |
| **No reflection** | ends at the result | One Learning sentence + where you applied it since |
| **Fake failure / fake weakness** | "I work too hard" | A real, bounded failure with a real fix |
| **Hero story** | "I stayed up 3 nights and saved it alone" | Show judgement and process, not just effort |
| **Badmouthing the employer** | "QNu is a mess" | Pull, not push: "I want X, which I can't get where I am" |
| **Rambling / no headline** | 2 minutes of context | Headline first; Situation ≤ 2 sentences |
| **Hypotheticals** | "I would…" to a "tell me about a time" | A real past example, or say you haven't and give the closest |
| **Inconsistency under probing** | numbers change between tellings | Numbers fixed in the story file; rehearse them |
| **Confidentiality leak** | customer names, internal secrets | Anonymise; describe at NDA-safe level |

## 10. The behavioral rubric (/100)

| Category | /pts | Full marks |
|---|---:|---|
| **Structure** | 15 | Headline first; clear STAR/CARL; Situation short; Action is the bulk; ends cleanly |
| **Specificity & ownership ("I")** | 20 | Concrete actions, decisions and reasoning attributable to the candidate; real names of systems/steps (anonymised); no "we"-fog |
| **Impact with metrics** | 15 | Before/after numbers or a clear measure; business/customer effect; scope appropriate to the level |
| **Reflection / learning** | 15 | Honest self-assessment; what they'd change; evidence the learning was applied later |
| **Values alignment** | 15 | Story and emphasis hit the company's framework (the LP / value being probed) without buzzword-stuffing |
| **Depth under probing** | 10 | Survives P1–P6; details consistent; composure under pressure probes |
| **Communication** | 10 | 2–3 min standard length; clear, calm, active voice; low filler; listens and answers the actual question |

Bands: **< 50** No hire · **50–64** Lean no · **65–79** Lean hire · **80–89** Hire · **90+** Strong hire.
Amazon mocks also get a Bar-Raiser verdict per LP: *Raises / Meets / Below*; any "Below" on a primary LP
is flagged. Target by readiness (2027-05-15): **≥ 80** on every company style, no category below 60% of
its points.

## 11. Pedagogy

| Principle | Where it shows up |
|---|---|
| **Retrieval before polish** | Stories are mined from memory (timeline, artefacts: PRs, docs, emails) before any drafting |
| **Generation effect** | The learner writes every story and bullet; Claude critiques |
| **Deliberate practice** | Each `/bmock` names the 1–2 lowest rubric categories; the next story session targets them |
| **Spaced rehearsal** | Stories re-told at +2/+7/+21/+60 days (`progress/review-queue.md`) |
| **Interleaving** | Mocks mix themes and companies; the question never names the LP |
| **Desirable difficulty** | Pressure probes (P6), time limits, Bar-Raiser style, cold mocks near the end |
| **Transfer** | One fact base, many framings: the same story re-headlined for LPs, G&L, values |
| **Realism** | Voice answers, timers, company-specific round formats, human mocks before real loops |

## 12. Phase files

| Phase | File | Sessions | Est h | Year window |
|---|---|---|---:|---|
| 1 Story mining & method | [phase-01.md](phase-01.md) | B.1.1–B.1.5 | 7.5 | Oct 2026 |
| 2 Crafting the story bank | [phase-02.md](phase-02.md) | B.2.1–B.2.7 | 8.5 | Nov–Dec 2026 |
| 3 Amazon Leadership Principles | [phase-03.md](phase-03.md) | B.3.1–B.3.5 | 6.5 | Dec 2026–Jan 2027 |
| 4 Other company frameworks | [phase-04.md](phase-04.md) | B.4.1–B.4.5 | 5 | Jan–Feb 2027 |
| 5 Project deep dive | [phase-05.md](phase-05.md) | B.5.1–B.5.3 | 4 | Feb 2027 |
| 6 Hard questions | [phase-06.md](phase-06.md) | B.6.1–B.6.3 | 3 | Mar 2027 |
| 7 Hiring-manager rounds & timed mocks | [phase-07.md](phase-07.md) | B.7.1–B.7.6 | 5.5 | Mar–May 2027 |
| | | **Total** | **40** | |
