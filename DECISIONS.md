# Hub Decisions Log

**State as of 2026-09-25:** hub built, programme **not started**. Next session: `H.0.1 Intake`.
`plan/SWITCH-PLAN.md` is a stub awaiting the mentor.

## 1. How the system works

```text
  plan/SWITCH-PLAN.md (mentor: budgets, phases of the year)
        │
        ▼
  /week ─► hours.md + metrics.md ─► tools/forecast.py (each repo's TRACK-switch.md from its Next session)
        │                            → remaining h, projected ready date vs 2027-05-15, required h/week
        ▼
  README "This week" (day-by-day) ─► /today ─► "cd <repo> && claude → /today"  (course repos run their own sessions)
                                         └─► or a hub session: /story /bmock /resume /pipeline /offer
  real interview ─► /debrief ─► interview-log + company-notes + weak-areas row in the right repo
  /wrap ─► stories index/matrix · review-queue · weak-areas · metrics · hours · STATUS · README
```

## 2. What exists

| Path | Purpose |
|---|---|
| `CLAUDE.md` | Roles (coach/PM, behavioral interviewer, resume/negotiation advisor), rules, layout, commands, wrap-up |
| `README.md` | Dashboard + how to use |
| `plan/SWITCH-PLAN.md` | Stub; the mentor writes it |
| `plan/roadmap/README.md` | IDs, TRACK convention, session types, mastery bars, probe/coaching ladder, pedagogy |
| `plan/roadmap/TRACK-switch.md` | 49 rows, 60 h (behavioral 40 + career ops 20), year-ordered; 7 deferred rows |
| `plan/behavioral/README.md` + `phase-01…07.md` | Method, rubric /100, 34 sessions B.1.1–B.7.6 |
| `plan/career-ops/README.md` | H.0.1 + 14 sessions CO.1.1–CO.5.2 |
| `behavioral/stories/`, `behavioral/mocks/` | Story bank (index, theme + framework matrices, template); mocks (index, template) |
| `career/…` | resume guide + inventory + versions, LinkedIn, platforms, referrals, applications (tiers, pipeline, funnel), interview log, offers, negotiation, 16 company-notes files (all marked verify) |
| `progress/…` | STATUS, profile, hours (parsed), metrics, story rehearsal queue, weak areas |
| `tools/status_all.sh` | Every repo's Next session / Active track / tracker summary; `--brief` for the hook |
| `tools/forecast.py` | Remaining hours per course → projected ready date; python3.9 stdlib |
| `.claude/skills/` | today, week, intake, story, bmock, resume, pipeline, offer, debrief, wrap |
| `.claude/settings.json`, `.claude/hooks/session-start.sh` | Permissions (edits to progress/behavioral/career/README, read-only across FAANG-* repos, the two tools, date); SessionStart status |

## 3. Key decisions

| # | Decision | Why | Rejected |
|---|---|---|---|
| D1 | Precedence: each course repo governs its sessions; the hub governs hours, cross-course planning, behavioral, career ops | Course repos have their own mastery rules ("progress over timeline" inside a course) | Hub overriding course content |
| D2 | Slippage fixed by re-allocation/pace/order/application window; never by cutting a course | The learner wants depth; switch tracks already separate "now" from "depth pass" | Dropping topics to hit a date |
| D3 | Claude never writes story content or resume facts | Invented achievements fail under probing and BGV; generation effect | Claude-drafted stories |
| D4 | Story mining in month 1, drafting months 2–3, company framing months 3–5, deep dive month 5, hard questions month 6, mocks months 6–8 | Stories need time to recover numbers and spaced rehearsal; mocks just-in-time for loops | Cramming behavioral in the last month |
| D5 | Resume by month 5, applications from month 6 in 3 tiered batches, offers aimed at one 2–3 week window | Negotiation leverage; resign by ~end June with 60–90 day notice | Applying as soon as one course feels ready |
| D6 | Behavioral rubric /100 with the brief's weights; bands like the DSA rubric | Consistent scoring language across repos | Unscored practice |
| D7 | `forecast.py` falls back to the mentor's budget when a repo has no TRACK-switch.md | LLD/CS repos don't exist yet; the forecast should still cover all ~980 h | Ignoring missing repos |
| D8 | `status_all.sh` calls `gen_tracker.py --summary` only if the script supports `--summary` | SD's gen_tracker has no `--summary` and regenerates its tracker when run | Blind calls |
| D9 | `/debrief` may append rows to other repos' `progress/weak-areas.md` only, with a normal permission prompt (no auto-allow) | Real-interview gaps must reach the course that fixes them; other repos stay the learner's | Auto-allowed cross-repo edits |
| D10 | All company loop/value/comp facts marked **verify** until confirmed | They change, and memory/reports can be wrong | Presenting reports as fact |

## 4. Build notes

- 2026-09-25: while inspecting the models, `python3 tools/gen_tracker.py --summary` was run in
  `FAANG-System-Design-Master`; that script ignores `--summary` and **regenerated `progress/tracker.md`**
  from its roadmap (progress preserved; there was none). Content should be unchanged; flagging for honesty.
  Suggest adding `--summary` support to SD's gen_tracker (SD repo's own change).
- First forecast (2026-09-25, default 25 h/week): ~1013 h remaining (DSA track 553.7 h > its 520 h budget;
  SD 189; LLD 150 and CS 60 by budget; hub 60) → ready ~2027-07-06, **~52 days after the 2027-05-15
  target**; ~30.6 h/week needed from now.

## 5. Open items (for the learner / mentor)

| Item | Status |
|---|---|
| YOE, current title, level target (SDE-2?) | H.0.1 intake |
| Notice period (30/60/90), buyout/early release → resign-by date | H.0.1 intake (from HR policy, not memory) |
| Which companies first: tiers Dream / Target / Practice | H.0.1 intake; batches in CO.3.3 |
| Definition of "30–35 LPA" (fixed vs year-1 total vs 4-yr avg) | H.0.1 intake |
| `plan/SWITCH-PLAN.md` content | Mentor, after this build |
| Hours gap: forecast needs ~30.6 h/week vs the 25–28 h assumption (DSA track is 553.7 h vs 520 budget) | Mentor to reconcile in SWITCH-PLAN |
| LLD and CS-core repos: STATUS + TRACK-switch not present yet | Being built; tools pick them up automatically |
| Git | Not initialised (per instruction); recommend a private remote later |
| Human mock partners (B.7.6) | Learner to find by ~Apr 2027 |
