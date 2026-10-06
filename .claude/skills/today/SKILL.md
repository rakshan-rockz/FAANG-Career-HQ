---
name: today
description: Daily router for the job-switch year — reads every course repo's STATUS and this week's plan, then says exactly which repo to open, which session ID and which command to run today (or runs this repo's next session if today belongs to Behavioral/Career).
---

# What to do today

1. `date +%F` and weekday. Run `tools/status_all.sh` (every repo's Next session / Active track / summary).
2. Read `progress/STATUS.md`, `progress/profile.md` (availability per day), the latest week's plan in
   `README.md` §This week (written by `/week`), `progress/hours.md` (hours so far this week), and
   `plan/SWITCH-PLAN.md` (budgets / phase of the year, if written).
3. If `progress/profile.md` is blank → today is **H.0.1 Intake** here (`/intake`). If there is no plan for
   the current week (no `/week` run since Monday) → recommend `/week` first (≤ 30 min), then today's slot.
4. Pick today's slot:
   - Follow this week's day-by-day plan. If none, allocate by remaining hours from `python3 tools/forecast.py`
     (largest remaining × behind-schedule first), respecting: weekdays ~3 h (one main repo + optional 20–30 min
     review block), weekends ~6–7 h (two repos, e.g. a DSA mock + an SD design).
   - Never schedule a repo whose STATUS shows its intake/baseline pending out of order: its Next session wins.
   - Due spaced items in any repo (reviews / re-solves / story rehearsals) are part of that repo's session,
     not extra work; mention if one repo has a large due backlog.
   - A real interview within 7 days → that company's prep takes priority (matching `/bmock` here, `/mock`
     in DSA, `/design` in SD, etc.).
5. Output ≤ 8 lines, concrete:
   ```
   Today (Tue 2026-10-06, ~3 h): DSA 2.5 h + story rehearsal 20 min
   1. cd /home/qnu/Documents/personal/projects/FAANG-DSA-Master && claude  → /today   (next: 1.2.3 …)
   2. Back here: /story rehearse 03 (due +7)
   Week so far: 7.5 / 26 h · behind by 2 h on SD → Saturday adds 1 h SD
   ```
   Always give the absolute directory and the exact command. The course repo's own `/today` decides the
   session's content.
6. If today's slot is in **this** repo, run the session now: the `Next session` row from
   `plan/roadmap/TRACK-switch.md` (details in `plan/behavioral/phase-0N.md` / `plan/career-ops/README.md`)
   with the matching skill (`/story`, `/bmock`, `/resume`, `/pipeline`, `/offer`, or directly from the row),
   then the wrap-up protocol in `CLAUDE.md`.
7. Short on time? Floor day: 15 min in the most-behind repo (its `/quiz` or floor-day mode) or one story rehearsal here.
