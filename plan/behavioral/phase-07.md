# Behavioral Phase 7 — Hiring-Manager Rounds & Timed Mocks

**Window:** Mar–May 2027 (months 6–8), interleaved with real interviews. **Est:** 5.5 h.
Mocks are cold, timed, company-styled, spoken, and never name the value being probed. Each mock ends with
the rubric score, the two lowest categories, and a targeted `/story` fix before the next mock.
Scheduling rule: a company-styled mock **within 7 days before** each real loop with that company (use the
matching B.7.x row, or repeat it; repeats are logged, not re-counted in the track).

Row fields: **Goal** · **Prompt/exercise** · **Covers** · **Output** · **Done-when**.

| ID | Type | Session | Est h |
|---|---|---|---:|
| B.7.1 | HM | **Hiring-manager round** — Goal: win the round that sets level and team fit. · Prompt: 40 min HM simulation: career story, current project deep dive (short version), 2 behavioral questions, "how do you like to work / be managed?", "where in 2–3 years?", then **the learner's questions for the HM** (prepared list: team charter, on-call, success in 6 months, growth path, tech debt, how performance is measured). · Covers: level signalling; aligning goals with the team; smart questions as a signal; closing ("what are the next steps?"). · Output: `behavioral/mocks/<date>-B.7.1-hm.md`; questions list in `behavioral/stories/hard-questions.md` §4. · Done-when: ≥ 75; questions list ≥ 8 good questions | 1 |
| B.7.2 | BM | **Amazon loop mock (Bar Raiser + LP round)** — Goal: second Amazon measurement vs B.3.5. · Prompt: `/bmock amazon loop`: 2 × 25 min back-to-back (LP round + Bar Raiser), unlabeled LPs, heavy probing. · Covers: consistency across rounds (same numbers), backup stories when a primary is used up. · Output: mock file; comparison to B.3.5. · Done-when: ≥ 80; no LP "Below" | 1 |
| B.7.3 | BM | **Google G&L + Meta behavioral mock** — Goal: two styles in one sitting. · Prompt: `/bmock google gl` (25 min incl. a hypothetical) then `/bmock meta behavioral` (25 min, fast follow-ups, level calibration). · Output: two mock files. · Done-when: both ≥ 80 | 1 |
| B.7.4 | BM | **Atlassian values + Microsoft mock** — Goal: values-round readiness. · Prompt: `/bmock atlassian values` (30 min, all 5 values) then a 15-min Microsoft growth-mindset set. · Output: mock files. · Done-when: Atlassian ≥ 80 with every value covered; Microsoft ≥ 80 | 0.75 |
| B.7.5 | BM | **Indian product-company HM + HR mock** — Goal: the most common real loop format for the target list. · Prompt: `/bmock <top Indian target> hm` + a 10-min HR screen (CTC, notice, why leave, relocation) using B.6.3 answers. · Output: mock file. · Done-when: ≥ 80; HR answers truthful and non-committal on numbers until the band is known | 0.75 |
| B.7.6 | BM | **Human mock + readiness check** — Goal: calibrate against a human interviewer and close the track. · Prompt: one behavioral mock with a human (friend at a target company, peer, or a mock platform), then a Claude debrief of their feedback; re-answer the sealed B.1.1 baseline question cold and compare. · Covers: realism (a stranger's reactions), comparing Claude's and the human's scores. · Output: `behavioral/mocks/<date>-B.7.6-human.md` incl. baseline vs now. · Done-when: last 3 mocks ≥ 80 average; story bank all ✅; readiness declared in `progress/STATUS.md` | 1 |
