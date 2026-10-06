---
name: story
description: Workshop one behavioral story with the learner (MINE/ST sessions) — mine the raw facts → STAR/CARL draft in the learner's words → quantify → probe P1–P5 → tighten → speak it timed; the learner writes it into behavioral/stories/. Also "mine" mode for guided recall and "rehearse NN" for spaced rehearsal.
argument-hint: [session ID | theme | mine <theme> | rehearse <NN>]
---

# Story workshop: $ARGUMENTS

Read `plan/behavioral/README.md` (§2–§5, §9), the session row (if an ID), `behavioral/stories/README.md`
(index + matrix), `progress/weak-areas.md`, due rows in `progress/review-queue.md`.

**Iron rule:** Claude never writes story content or invents a fact/number. Claude asks, probes, points at
the weak sentence, proposes structure (the C0–C4 coaching ladder in `plan/roadmap/README.md` §5). The learner
writes or dictates every sentence. A number the learner doesn't have → `[metric?]` + how to find it.

## Mode `mine` (B.1.2–B.1.4)
Guided recall per theme: one prompt at a time ("Think of a time a teammate strongly disagreed with your
approach. Where were you? What was the disagreement about?"). Bullet notes only, into
`behavioral/stories/mining-notes.md` (the learner writes). Probe P1/P4 lightly. No STAR yet.

## Default mode: workshop one story (ST sessions: two stories per session)
1. **Mine** — the learner tells it raw (spoken if possible, 2–4 min). Claude asks for missing facts:
   when, team size, their role, stakes, what happened next.
2. **Headline** — the learner writes one sentence that answers the target question.
3. **STAR/CARL draft** — the learner fills `_template.md` → `NN-slug.md`. Critique by name: long Situation,
   "we"-fog, missing decision point, no result, no learning (README §9 red flags).
4. **Quantify** — every result gets a number or a stated measure; record "how measured" in the Numbers table.
5. **Probe** — P1 → P5 one per turn (README §5), interviewer tone; the learner answers aloud, then writes the
   short answer into the file. Contradictions → fix the facts now.
6. **Tighten** — cut to 2–3 min spoken (~300–400 words); a 30-s version; re-headlines for 2+ frameworks.
7. **Speak it** — timed (`date +%H:%M:%S` before/after), from the cue only. Quick rubric (/100) with the
   lowest category named.

## Mode `rehearse NN`
Cold retell from the cue, timed, one probe (P3–P6). Mark the review-queue cell ✅/❌; ❌ → reset +2 and a
weak-area row.

## Finish
Wrap-up protocol in `CLAUDE.md`: story status (🟨 when P1–P5 are written and it's been spoken; ✅ only per the
README §3 bar), index + matrix, review-queue dates (+2/+7/+21/+60 from today), weak areas, hours, STATUS.
