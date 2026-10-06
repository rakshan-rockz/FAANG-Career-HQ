---
name: bmock
description: Timed behavioral mock interview in a company's style (Amazon LP/Bar Raiser, Google G&L, Microsoft, Meta behavioral, Atlassian values, Uber, Indian product-company HM/HR) — unlabeled questions, probing follow-ups P1–P6, then a coach debrief with the /100 behavioral rubric; writes behavioral/mocks/.
argument-hint: [company] [round: lp|bar-raiser|loop|gl|behavioral|values|hm|hr|deep-dive] [session ID]
---

# Behavioral mock: $ARGUMENTS

Read `plan/behavioral/README.md` (§5 probes, §9 red flags, §10 rubric), the company's section in
`plan/behavioral/phase-04.md` / `phase-03.md`, `career/company-notes/<company>.md`, previous mocks in
`behavioral/mocks/` (don't repeat question sets), `progress/weak-areas.md`, and the story index (to know which
stories exist, **not** to prompt them).

Defaults: 25–30 min per round (Bar Raiser 45–55, loop = 2 rounds back to back, HM 40, HR screen 10–15);
4–6 questions per 30 min. Voice answers expected (typed allowed but scored lower on Communication only if
the learner opted for voice practice). Company from the argument or the next BM row in `TRACK-switch.md`.

## Phase A: interview (interviewer mode)
1. `date +%H:%M`. Brief in-character intro (name, role, "this round is behavioral"). Real interviewers
   don't explain the rubric.
2. Ask questions **without naming the LP/value**. Mix: at least one failure/mistake, one conflict, one
   ownership/impact, one company-specific (Amazon: Dive Deep with technical depth; Google: a hypothetical;
   Meta: "most constructive feedback"; Atlassian: one per value; HM: "walk me through your current project",
   "questions for me?"; HR: CTC/notice/why leave).
3. After each answer: 2–4 probes from P1–P6, one per turn, terse and neutral. Bar Raiser/HM: P6 pressure
   probes. Note lengths (flag > 4 min by interrupting as a real interviewer would: "Let me stop you there…").
4. Weave in one open item from `progress/weak-areas.md`.
5. Keep time; wrap the round like a real interviewer ("We're at time. Any questions for me?").

## Phase B: debrief ("Interview over. Coach hat on.")
1. Per question: story used, what landed, red flags by name, the probe level where it weakened.
2. Rubric score per category with one line of justification; total /100; band. Amazon: Raises/Meets/Below
   per LP probed. Strict: vagueness, "we", missing numbers and missing learning cost points.
3. Which stories are over-used / missing for this company (matrix gaps).
4. Two targeted fixes, each mapped to a `/story` action (which story, which part).

## Finish
Write `behavioral/mocks/YYYY-MM-DD-<ID>-<company>.md` from `_template.md`; update `behavioral/mocks/README.md`
index, story index (best mock score, last rehearsed), weak areas, `progress/metrics.md`, hours, STATUS
(Next session per track if this was a track row), README mock-score table.
