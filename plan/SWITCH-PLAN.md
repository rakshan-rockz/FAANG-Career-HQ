# 12-Month Job-Switch Plan

**Goal:** offers at **30–35 LPA** (from 22 LPA) at product companies, **within 12 months**. Then keep going to full
mastery of all four courses, at a sustainable pace in the new job.
**Written:** 2026-09-25 · **Start:** 2026-10-01 · **Re-forecast weekly** with `/week` (`tools/forecast.py`).

> Principle: *nothing is deleted.* Each course has a 🎯 **switch track** (what's needed for the switch, in
> prerequisite order) and a **depth track** (everything else, afterwards). You don't need everything to switch.
> You do need everything in the switch tracks to be *actually done*: solved, coded, mocked.

---

## 1. What an SDE-2 loop at the target companies tests, and where each piece lives

| Round (typical) | What's tested | Repo · track | Switch hours |
|---|---|---|---:|
| OA + 2 coding rounds (DSA) | 2 mediums / 45 min, some hards, bug-free code, reasoning | `FAANG-DSA-Master` · 257 lessons (switch scope), anchor practice, 27 mocks | **664** |
| HLD / system design | framework, estimation, core building blocks, ~15 classic designs | `FAANG-System-Design-Master` · 98 sessions, 16 design passes, 5 cold mocks, 3 human mocks | **189** |
| LLD / machine coding (Flipkart, Uber, Atlassian, Amazon, Swiggy, …) | OOP, SOLID, patterns, a working extensible system in 90 min, concurrency | `FAANG-LLD-Master` · 83 sessions | **151** |
| CS fundamentals (Microsoft, Adobe, Oracle, …; follow-ups everywhere) | OS, DBMS + SQL, CN, OOP concepts | `FAANG-CS-Core-Master` · 37 sessions | **62** |
| Behavioral / hiring manager / bar raiser | stories, company values, project deep-dive | `FAANG-Career-HQ` · behavioral + career ops | **60** |
| **Total** | | | **1,126 h** |

Every figure includes ~20% overhead (reviews, overruns, remediation). They come from counting each track's
sessions by type × a realistic duration, the same method as before.

## 2. The honest arithmetic

| Pace (hours/week) | Switch tracks complete | Offers (loops overlap the last ~10 weeks) | Join (60–90 day notice) |
|---:|---|---|---|
| 25 | ~2027-08-07 | Jul–Sep 2027 | Oct–Dec 2027 |
| **29 (the plan)** | **~2027-06-24** | **May–Jul 2027** | **Aug–Oct 2027** |
| 34 | ~2027-05-15 | Apr–Jun 2027 | Jul–Sep 2027 |

"Within 12 months" realistically means **offer in hand by ~month 9–10**, then your notice period. **Check your
notice period now** (appointment letter). If it's 90 days, ask HR whether buyout or early release is possible. It
changes the joining date by up to 3 months.

**29 h/week** = 3 h on weekdays (1 h morning + 2 h evening) + 7 h on each weekend day. It's hard with a full-time
job. The plan survives bad weeks because the forecast is re-run every Sunday. If you average 25, we'll know by
week 6 and adjust (the ⏫ stretch rows are already out of the tracks; the next lever is extra mocks vs lessons).
It never means silently falling behind.

## 3. The calendar (three phases)

### Phase A: Foundations & core patterns · Oct 2026 → Jan 2027 (17 weeks, ~28 h/week)

| Course | Hours | Covers |
|---|---:|---|
| DSA | 330 | Stages 0–13: method, complexity, recursion, arrays, hashing, two pointers, strings, sliding window, sorting & intervals, binary search, linked lists, stack, queues, trees, BST, heaps |
| System Design | 70 | Intake, baseline, framework, estimation, networking/APIs, databases, caching (Phases 0–2 core) |
| LLD | 30 | OOP in C++ (+ Java), SOLID, UML, first katas |
| CS core | 25 | OS processes/threads/scheduling/memory; DBMS + SQL basics |
| Behavioral & career | 15 | Intake (YOE, notice period, companies), story mining from your QNu Labs work, achievement inventory, resume v1 |

**Weekly shape:** Mon–Fri morning 1 h = new DSA lesson (hardest thinking when fresh) · evenings 2 h = DSA practice
(Mon/Wed/Fri) and SD/LLD/CS (Tue/Thu) · Saturday 7 h = SD session + LLD + DSA interleaved set · Sunday 7 h =
LeetCode weekly contest (from ~December), upsolve, cycle review, behavioral 1 h, **`/week`**.

**Checkpoints:** week 4, Stage 0 gate passed and ≥ 25 h/week logged · week 8, easy/medium array/hash/two-pointer
problems in ≤ 25 min at ≤ H1 for ≥ 70% · end of Jan, DSA mock ≥ 65, SD gate 0–2 passed, 8 stories drafted, resume v1.

### Phase B: Advanced patterns + design · Feb → Apr 2027 (13 weeks, ~30 h/week)

| Course | Hours | Covers |
|---|---:|---|
| DSA | 178 | Stages 14–21: bits, backtracking, tries, DP I & II, greedy, graphs, union-find/MST/shortest paths |
| System Design | 80 | Consistency, queues/async, reliability; design learning passes (URL shortener → rate limiter → chat → feed → …) |
| LLD | 80 | Design patterns, machine-coding method, case studies, concurrency (threads, locks, producer–consumer, thread pools) |
| CS core | 25 | Networks (TCP, HTTP, DNS), DB internals at interview level (indexes, transactions, isolation) |
| Behavioral & career | 20 | 12 polished stories mapped to Amazon LPs / Google / Microsoft / Atlassian values; resume final; LinkedIn; referral list |

**Applications:** from **mid-March**, apply to 4–6 *practice* companies you'd still accept (real OAs and loops are
the best mocks). From **April**, target companies, **via referrals**, batched so loops land in the same 3–4 weeks.
**Checkpoints:** end of Mar, DSA mock avg ≥ 75, 8 SD designs, 8 machine codings · end of Apr, DSA through
Stage 21, mock avg ≥ 80, LLD mock ≥ 70, behavioral mock ≥ 70.

### Phase C: Interview mode · May → Jun 2027 (9 weeks, ~30 h/week + interviews)

| Course | Hours | Covers |
|---|---:|---|
| DSA | 156 | Stages 22, 24, 29–30: graph structure, interview data structures, Pattern Atlas synthesis, interview strategy, company-style mock loops, baseline redo |
| System Design | 39 | Cold timed designs, human mocks, trimmed gates |
| LLD | 41 | Timed 90-min machine-coding mocks, LLD discussion rounds |
| CS core | 12 | Rapid-fire viva drills |
| Behavioral & career | 25 | Behavioral mocks, `/debrief` after every real interview, offers, negotiation |

**Offers → negotiation** (competing offers are your leverage; see `career/negotiation.md`) → resign → notice →
join. During the notice period keep ~10–12 h/week going: start the depth tracks and prepare for the new job.

## 4. After the switch: the depth track (forecast)

| Course | Full course | Switch part | Depth remaining |
|---|---:|---:|---:|
| DSA | ~2,000–2,500 h | 664 | ~1,500–1,800 |
| System Design | ~907 | 189 | ~720 |
| LLD + concurrency | ~514 | 151 | ~365 |
| CS core (≈ half is textbook reading) | ~1,505 | 62 | ~1,440 |
| **Total** | **~4,900–5,400** | **1,126** | **~4,000–4,300** |

At 12–15 h/week alongside a new job, that's **5–6 more years**; at 20 h/week, about 4. That's a long game, and it's
fine: after the switch, depth is for mastery, not deadlines. Prioritise by what the new job needs: SD depth and
CS-core OS/networks/databases usually pay off first.

## 5. How to get the maximum out of this

**Learning**
1. **Never read a solution before the time box ends.** Use `/hint` for one rung. The struggle is where the
   learning happens; reading an editorial turns a problem into a reading exercise.
2. **Post-mortem every problem** (2 minutes: heuristic, mistake category, recognition signal). This is the
   difference between 400 problems that stick and 400 you forget.
3. **Do the cold re-solves.** A problem solved with hints isn't learned until you've solved it cold 3 days later.
4. **Talk out loud, always**, even alone. Interviews grade your thinking, and silence reads as being stuck.
5. **Hardest work first.** New lessons in the morning, practice in the evening, reviews when tired.
6. **Interleave from Stage 2 onward.** If you only practise under the chapter heading, you're training recall,
   not recognition.
7. **Weekly contests** (LeetCode weekly contest, Sunday morning IST) from ~December: real time pressure, unseen
   problems, then upsolve.
8. **Write the Pattern Atlas and toolkit entries yourself.** If you can't write the branch, you don't own it yet.
9. **Keep a floor, not a streak.** On a bad day, do 15 minutes (`/quiz 5` or one re-solve). Zero days kill
   momentum; short days don't.
10. **Stretch rows are only for when you're ahead.** Don't go down rabbit holes (suffix automata, flows) before the
    switch.

**Job search**
11. **Referrals over cold applications.** Start the referral list in January; contact people in March.
12. **Batch the loops** so offers overlap. A competing offer is the strongest negotiation lever you have.
13. **Use your domain.** Quantum-safe security at QNu Labs is rare and interesting: make it your project
    deep-dive, and add security-focused product companies to the list.
14. **Mine stories at your current job now.** Take on work with measurable impact over the next 6 months. It
    feeds your resume bullets and behavioral answers, and protects your current review.
15. **Verify pay bands** for your YOE on levels.fyi / AmbitionBox / Glassdoor per company before applying.
    Decide what "30–35 LPA" means to you (fixed, year-1 total or 4-year average), because offers mix fixed,
    bonus and RSUs.
16. **Practise on companies you'd accept but don't prioritise**, before your top targets.

**Sustainability**
17. **Sleep ≥ 7 h and move daily.** Memory consolidation happens during sleep; a sleep-deprived 30 h week learns
    less than a rested 25 h one.
18. **Log hours every Sunday** (`/week`). The forecast only works on real numbers, and it will tell you early
    and honestly if the date is slipping.

## 6. Weekly operating rhythm

- **Sunday:** `/week` in `FAANG-Career-HQ`: log hours, re-forecast, get the day-by-day plan.
- **Each day:** `/today` in `FAANG-Career-HQ` names the repo and session. Then open that repo and run `/today`.
- **After every real interview:** `/debrief`. Gaps go into the right course's weak areas.
