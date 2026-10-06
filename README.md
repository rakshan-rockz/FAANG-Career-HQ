# FAANG Career HQ — Switch-Year Command Centre

**Goal:** from 22 LPA to **30–35 LPA** at a top product company (Amazon, Microsoft, Google, Uber, Atlassian,
Meta, Flipkart, PhonePe, Razorpay, Swiggy, Zomato, Walmart Global Tech, Adobe, Salesforce, Oracle, Intuit…)
within 12 months. **Interview-ready by 2027-05-15 · applications from ~Mar 2027 · resign by ~end Jun 2027.**
*"Slowly I will get there", with depth and real understanding.*

> Dashboard below is refreshed by `/week` (and `/wrap`). Source of truth: each repo's `progress/STATUS.md`,
> this repo's `progress/*.md`, `career/applications.md`, `behavioral/mocks/`.

## Courses (as of 2026-09-25)

| Course | Repo | Switch budget | Next session | Status |
|---|---|---:|---|---|
| DSA | `FAANG-DSA-Master` | 520 h | 0.0.1 Intake | not started (9 lessons 🟨 carried over) |
| System Design | `FAANG-System-Design-Master` | 190 h | 0.0.1 Intake | not started |
| LLD + machine coding + concurrency | `FAANG-LLD-Master` | 150 h | — | repo being set up |
| CS core | `FAANG-CS-Core-Master` | 60 h | — | repo being set up |
| Behavioral + career ops | `FAANG-Career-HQ` (this) | 60 h | H.0.1 Intake | not started |
| **Total** | | **980 h** | | |

## This week

(Written by `/week`: day-by-day repo · session · command · hours.)

| Day | Repo | Session / command | Hours |
|---|---|---|---:|
| — | — | Run `/intake` here, then `/week` | — |

## Hours & forecast

| Weeks logged | Total hours | 4-week avg | Remaining (switch tracks) | Projected ready | vs 2027-05-15 |
|---:|---:|---:|---:|---|---|
| 0 | 0 | — (default 25) | ~1013 h | 2027-07-06 | 52 days late at 25 h/wk; needs ~30.6 h/wk |

(`python3 tools/forecast.py` as of 2026-09-25; LLD/CS use budgets until their tracks exist.)

## Application funnel

| Applied | OA | Screen | Loop | Offer | Reject | Active |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Mock scores (latest per type)

| Type | Repo | Latest | Best | Target |
|---|---|---|---|---|
| DSA coding /100 | DSA | — | — | ≥ 80 |
| HLD /120 | SD | — | — | ≥ 95 |
| LLD / machine coding | LLD | — | — | verify rubric |
| Behavioral /100 | this | — | — | ≥ 80 every company style |

---

## How to use this repo

1. **Every day:** open this repo (`cd /home/qnu/Documents/personal/projects/FAANG-Career-HQ && claude`) and
   run **`/today`**. It reads every course's STATUS and this week's plan and tells you exactly which directory
   to open and which command to run (usually a course repo's own `/today`).
2. **Every week (Sun/Mon):** **`/week`**: log hours, see velocity and the forecast, get next week's schedule.
3. **Behavioral sessions:** `/story` (build one story), `/bmock <company>` (timed mock).
4. **Career ops:** `/resume`, `/pipeline`, `/offer`; after every real interview: **`/debrief`** (routes gaps
   to the right course repo).
5. End any session with **`/wrap`**.

Tools: `tools/status_all.sh` (every repo on one screen) · `python3 tools/forecast.py` (remaining switch-track
hours → projected ready date; `--pace 28` to try a different pace).

Key files: `CLAUDE.md` (how Claude behaves) · `plan/SWITCH-PLAN.md` (the mentor's 12-month plan) ·
`plan/roadmap/TRACK-switch.md` (this repo's sessions in year order) · `plan/behavioral/README.md` (method +
rubric) · `plan/career-ops/README.md` · `DECISIONS.md`.
