# Behavioral Phase 3 — Amazon Leadership Principles

**Window:** Dec 2026–Jan 2027 (months 3–4). **Est:** 6.5 h.
**Why Amazon gets its own phase:** Amazon's loop is the most behavioral-heavy of the targets (every round,
including coding rounds, typically opens with 1–2 LP questions; one interviewer is a **Bar Raiser** from
another org with veto power; verify current loop format in `career/company-notes/amazon.md`). An LP-ready
bank is also the best general-purpose bank: the 16 LPs cover almost every theme other companies ask about.

## The 16 Leadership Principles — what each tests and the classic questions

Wording of the LPs: check amazon.jobs/principles before the loop (**verify**; two were added in 2021).
"Story slot" = the story-bank number the learner maps (primary / backup), filled in B.3.1–B.3.4.

| # | LP | What they're really testing | Classic questions | Story slot (P / B) |
|---:|---|---|---|---|
| 1 | **Customer Obsession** | Starts from the customer and works backwards; earns and keeps trust | "Tell me about a time you went above and beyond for a customer." · "…when you had to balance customer needs with business needs." · "How do you know what your customers want?" | / |
| 2 | **Ownership** | Acts on behalf of the whole company, long-term; never "that's not my job" | "Tell me about a time you took on something outside your responsibility." · "…when you had to make a decision that sacrificed short-term gain for long-term." · "…when you saw a problem nobody owned." | / |
| 3 | **Invent and Simplify** | Looks for new ideas and simpler ways; not attached to "not invented here" | "Tell me about a time you simplified a complex process/system." · "…your most innovative idea." | / |
| 4 | **Are Right, A Lot** | Good judgement, seeks diverse views, works to disconfirm own beliefs | "Tell me about a time you made a decision with incomplete data." · "…you were wrong." · "…you had to decide between two good options." | / |
| 5 | **Learn and Be Curious** | Never done learning; explores new possibilities | "Tell me about the last thing you learned on your own and applied." · "…you had to learn a new technology quickly." | / |
| 6 | **Hire and Develop the Best** | Raises the performance bar; develops others; mentors | "Tell me about someone you mentored." · "…you helped a struggling teammate." · "…you gave tough feedback." | / |
| 7 | **Insist on the Highest Standards** | Relentlessly high standards; defects don't get sent down the line | "Tell me about a time you refused to compromise on quality." · "…you raised the bar for your team." · "…you weren't satisfied with the status quo." | / |
| 8 | **Think Big** | Bold direction; communicates a vision | "Tell me about your most ambitious proposal." · "…you took a small problem and saw a bigger opportunity." | / |
| 9 | **Bias for Action** | Speed matters; calculated risk; reversible decisions don't need extensive study | "Tell me about a time you acted without full information." · "…you took a calculated risk." · "…you had to decide fast." | / |
| 10 | **Frugality** | More with less; constraints breed resourcefulness | "Tell me about a time you delivered with limited resources/budget/time." · "…you saved cost." | / |
| 11 | **Earn Trust** | Listens, speaks candidly, treats others respectfully, vocally self-critical | "Tell me about a time you had to earn the trust of a skeptical team." · "…you admitted a mistake." · "…you received critical feedback." | / |
| 12 | **Dive Deep** | Operates at all levels; audits; skeptical when metrics and anecdotes differ | "Tell me about a problem you solved by digging into the data/root cause." · "Walk me through the most complex bug you've debugged." | / |
| 13 | **Have Backbone; Disagree and Commit** | Challenges decisions respectfully with data; commits wholly once decided | "Tell me about a time you disagreed with your manager." · "…you went along with a decision you disagreed with." · "…you convinced others to change course." | / |
| 14 | **Deliver Results** | Focuses on key inputs; delivers with quality and on time despite setbacks | "Tell me about a time you delivered under a tight deadline." · "…your biggest setback and how you still delivered." · "…a goal you missed." | / |
| 15 | **Strive to be Earth's Best Employer** | Creates a safer, more productive, more inclusive environment; leads with empathy | "Tell me about a time you improved your team's working environment." · "…you supported a teammate's growth or well-being." | / |
| 16 | **Success and Scale Bring Broad Responsibility** | Considers second-order effects on users, communities, the world | "Tell me about a decision where you considered broader impact beyond your team." · "…you raised an ethical/security/privacy concern." (A quantum-safe security engineer's natural home.) | / |

**Rules for LP answers:** one LP per answer is the target, the interviewer's question names it indirectly;
answers are ~2–3 min then heavy probing ("Dive Deep" style: "what was the exact metric?", "what did you
personally write?"); failure/"missed goal" stories are expected, not avoided. Bar Raiser probes are
P4–P6 level. Amazon also values **data** in every answer.

Row fields: **Goal** · **Prompt/exercise** · **Covers** · **Output** · **Done-when**.

| ID | Type | Session | Est h |
|---|---|---|---:|
| B.3.1 | CF | **LPs 1–4: Customer Obsession, Ownership, Invent and Simplify, Are Right A Lot** — Goal: map and rehearse the first four LPs. · Prompt: for each LP the learner picks primary + backup stories from the bank, rewrites the *headline* for the LP (facts unchanged), and answers one classic question spoken; Claude probes P1–P4 in Amazon style. · Covers: LP meaning + what "Raises the bar" sounds like vs "Meets"; working backwards (PR/FAQ idea in one sentence); ownership beyond the ticket; judgement with incomplete data. · Output: LP table story slots filled for 1–4 (this file) + `behavioral/stories/README.md` matrix Amazon column. · Done-when: each of LP 1–4 has P/B stories and one spoken answer scored ≥ 65 | 1.25 |
| B.3.2 | CF | **LPs 5–8: Learn and Be Curious, Hire and Develop the Best, Insist on the Highest Standards, Think Big** — same format. · Covers: learning with evidence of application; mentoring outcomes; standards (tests, reviews, security bar); vision beyond the task at SDE-2 scale (a proposal, a roadmap item). · Output/Done-when: as B.3.1 for LPs 5–8 | 1.25 |
| B.3.3 | CF | **LPs 9–12: Bias for Action, Frugality, Earn Trust, Dive Deep** — same format; Dive Deep answers must go three technical levels down (metric → component → line/config). · Covers: reversible vs irreversible decisions ("one-way / two-way doors"); constraint-driven creativity; admitting mistakes; root-cause investigation narrative. · Output/Done-when: as B.3.1 for LPs 9–12 | 1.25 |
| B.3.4 | CF | **LPs 13–16: Backbone/Disagree and Commit, Deliver Results, Earth's Best Employer, Success and Scale** — same format. · Covers: disagreeing with data and committing after; delivering despite setbacks + a missed goal told honestly; team environment / inclusion; broader responsibility (security, privacy, compliance consequences). · Output: all 16 LPs mapped; no story primary for > 4 LPs; gaps → a new story in the next `/story` session. · Done-when: 16/16 mapped with backups; weak LPs listed in `progress/weak-areas.md` | 1.25 |
| B.3.5 | BM | **Amazon Bar Raiser mock** — Goal: the first full company-styled mock. · Prompt: `/bmock amazon bar-raiser`: 45–55 min, 4–5 LP questions (unlabeled), heavy P3–P6 probing, one "tell me about a failure/missed goal", one "Dive Deep" technical probe. · Covers: stamina, consistency of numbers across answers, composure under pressure probes, time management. · Output: `behavioral/mocks/<date>-B.3.5-amazon.md` with /100 score + per-LP Raises/Meets/Below. · Done-when: scored and debriefed; lowest two categories feed B.4 story tweaks (a score target is not required here, only honest measurement) | 1.5 |
