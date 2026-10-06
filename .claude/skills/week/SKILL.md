---
name: week
description: Weekly planning & review for the switch year — logs last week's hours per course, compares against SWITCH-PLAN budgets and the phase of the year, computes velocity, runs tools/forecast.py, flags slippage honestly, proposes fixes without cutting the full courses, and writes this week's day-by-day schedule.
argument-hint: [review-only|plan-only]
---

# Weekly review & plan

Run on Sunday evening or Monday morning (~20–30 min).

## A. Review last week
1. `date +%F`; compute last week's Monday. Run `tools/status_all.sh`.
2. Ask the learner for last week's hours per course (DSA, SD, LLD, CS, Behavioral/Career), or derive them
   from each repo's STATUS session log if they don't know (and say it's an estimate). Append/update the row in
   `progress/hours.md` (numbers only) and refresh its *Totals to date*.
3. Collect metrics for `progress/metrics.md` from the repos: problems solved (DSA Practice tables / tracker
   summary), average hint rung, DSA mock scores (`Mock-Interviews/`), HLD mock scores (SD `journal/`),
   LLD mock scores, behavioral mock scores (`behavioral/mocks/`), stories ✅/🟨, applications and
   interviews (`career/applications.md`). Leave blank what doesn't exist; never invent.
4. Run `python3 tools/forecast.py`. Report in ≤ 10 lines:
   - hours vs the plan (last week and 4-week average) and vs 25–28 h/week;
   - per-course progress vs `plan/SWITCH-PLAN.md` for this phase of the year;
   - projected ready date vs 2027-05-15, and required h/week;
   - **slippage stated plainly** ("SD is 9 h behind plan; at this split SD finishes 3 weeks late").
5. Fixes, in this order of preference: (a) re-allocate hours between courses; (b) protect weekend blocks /
   add one weekday hour for a limited period; (c) reorder switch-track sessions (within a repo: only via
   that repo's own process); (d) shift the application window / batch dates and notice-period plan;
   (e) as a last resort, move specific switch-track rows to a repo's "Deferred to the depth pass" table,
   with the learner's agreement and via that repo's `DECISIONS.md` process. **Never cut a full course,
   never compress a course's sessions.** Burnout signs (several low weeks, health, work crunch) → a
   lighter week is a valid fix; say so.

## B. Plan this week
6. Day-by-day schedule respecting `progress/profile.md` availability: for each day, repo + session ID(s) +
   command + hours. Include due reviews/re-solves/story rehearsals, one behavioral slot (~1–1.5 h/week in
   months 1–5, ~2–3 h/week in months 6–9 incl. pipeline/debriefs), and interview prep for any real loop.
7. Write the plan into `README.md` §This week (replace the previous week) and update the dashboard tables
   (courses, hours summary, funnel, mock scores).
8. Log one line in `progress/STATUS.md` session log (date, `WEEK`, "Weekly review", key takeaway).
