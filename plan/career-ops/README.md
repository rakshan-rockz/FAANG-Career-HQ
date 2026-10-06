# Career-Ops Track — Resume, Presence, Referrals, Pipeline, Offers

**Budget:** ~20 h (incl. the hub intake). **Sessions:** `H.0.1` and `CO.<phase>.<n>`; year order in
`../roadmap/TRACK-switch.md`. Outputs live in `career/`.

**The one rule:** every fact on a resume, profile, form or in a negotiation is **true and supplied by the
learner**. Claude structures, sharpens and challenges; it never invents a metric, title, date, tool,
offer or number. Unknown metric → `[metric?]` + a plan to measure or estimate it defensibly.

## Timeline logic (why the sessions sit where they do)

| Month | Dates | Career-ops focus | Why then |
|---|---|---|---|
| 1 | Oct 2026 | Intake: YOE, level, notice period, targets ranked | Everything else depends on it |
| 2–4 | Nov 2026–Jan 2027 | Achievement inventory (CO.1.1), grows from behavioral mining | Same facts as the story bank; numbers take weeks to recover |
| 4–5 | Jan–Feb 2027 | Company research & target ranking (CO.3.1); resume rewrite (CO.1.2–1.4); LinkedIn & platforms (CO.2) | Resume ready by ~month 5; recruiters find you before you apply |
| 5–6 | Feb–Mar 2027 | Referral mapping & outreach (CO.3.2), batching plan (CO.3.3) | Referrals take 2–6 weeks to convert into calls |
| 6–9 | Mar–Jun 2027 | Applications in batches, pipeline ops, debriefs (CO.5) | DSA/SD/LLD at interview-ready level by ~2027-05-15; practice companies first, targets later |
| 7–9 | Apr–Jun 2027 | Offers, negotiation (CO.4) | Offers should land within a 2–3 week window to negotiate against each other |
| ~9 | end Jun 2027 | Resignation after signed offer; notice period (60–90 days, confirm) | Join ~Sep 2027 |

Row fields: **Goal** · **Prompt/exercise** · **Covers** · **Output** · **Done-when**.

## Phase 0 — Hub intake

| ID | Type | Session | Est h |
|---|---|---|---:|
| H.0.1 | Intake | **Switch intake** — Goal: the facts every plan depends on. · Prompt: `/intake`: YOE and exact current title; current level estimate vs target (SDE-2?); current CTC structure (fixed/variable/other; only what the learner wishes to share, kept in `progress/profile.md`); **notice period** (from the appointment letter/HR policy: 30/60/90 days, buyout clause?, leave encashment?); target companies **ranked** into tiers (dream / target / practice); location & relocation (Bangalore/Hyderabad/Pune/NCR/remote); weekly availability per day; constraints (work crunch periods, family, exams, travel, health); interview history; resume/LinkedIn status; one-line "why switch". · Covers: calibration of the year plan (resign-by date from notice period, application window), level target, company batching tiers. · Output: `progress/profile.md`; `DECISIONS.md` open items resolved or dated. · Done-when: profile complete; resign-by date and application window computed from the notice period and written into STATUS; the mentor has what's needed to finalise `plan/SWITCH-PLAN.md` | 1.5 |

## Phase 1 — Resume

| ID | Type | Session | Est h |
|---|---|---|---:|
| CO.1.1 | CO | **Achievement inventory & resume audit** — Goal: a factual, quantified raw list before any rewriting. · Prompt: `/resume review` on the current resume (learner saves it as `career/resume/versions/v0-<date>.md` or .pdf); then the learner fills `career/resume/achievement-inventory.md`: per project: problem, your action, tech, result, number (+ how measured / where to find it). Reuses `behavioral/stories/timeline.md`. · Covers: audit checklist (resume-guide §9); what counts as impact for a security/crypto engineer; finding numbers (dashboards, benchmarks, JIRA, release notes, customer counts, incident counts). · Output: audit notes + inventory. · Done-when: ≥ 12 inventory items, ≥ 8 with a real number | 1.5 |
| CO.1.2 | CO | **Rewrite bullets in XYZ form** — Goal: every bullet = accomplished X, measured by Y, by doing Z. · Prompt: `/resume rewrite`: the learner rewrites 3 bullets at a time; Claude critiques (verb, scope, number, tech, "so what"); iterate. · Covers: XYZ and CAR bullets; strong verbs; one idea per bullet; front-loading impact; honest estimates ("~40%"); security/quantum-safe framing for generalist readers. · Output: `career/resume/versions/v1-<date>.md`. · Done-when: every bullet has an action verb + outcome; ≥ 70% quantified; no bullet the learner can't defend for 5 minutes | 2 |
| CO.1.3 | CO | **ATS, one page, skills, projects, format** — Goal: a resume that parses, scans in 7 seconds, and fits one page. · Prompt: the learner produces the formatted version (LaTeX/Google Docs/Word; single column); Claude checks against resume-guide §3–§8; the learner runs it through a plain-text extraction (copy-paste into a text file) to check ATS parse. · Covers: ATS rules; section order; skills section (only what you can be interviewed on); projects (open-source, side projects, C++ work); education; links (GitHub, LinkedIn); file naming. · Output: `versions/v2-<date>.pdf` (+ .md text copy). · Done-when: one page; parses cleanly as text; passes the §9 checklist | 1.5 |
| CO.1.4 | CO | **Tailored variants + outside review** — Goal: 2 variants and a human sanity check. · Prompt: `/resume tailor <company>` for two families: (a) product/backend (Flipkart/Swiggy/Uber/Amazon…), (b) infra/security/platform (Microsoft/Google security teams, Salesforce, Oracle, Adobe, Intuit…). Keywords from 3 real JDs each. The learner asks 1–2 people (a senior engineer, a friend at a target company) for review and logs feedback. · Covers: tailoring without lying (re-ordering, emphasis, keywords you genuinely have); JD keyword mapping. · Output: `versions/v3-product-<date>`, `v3-security-<date>`; feedback notes in `career/resume/README.md`. · Done-when: both variants final by end of month 5; reviewer feedback addressed | 1 |

## Phase 2 — Online presence & platforms

| ID | Type | Session | Est h |
|---|---|---|---:|
| CO.2.1 | CO | **LinkedIn overhaul** — Goal: recruiters find and message you. · Prompt: follow `career/linkedin.md`: headline, About (in the learner's words), experience bullets (from resume v2), skills, featured, open-to-work (recruiters only), location, custom URL; Claude reviews. · Covers: search keywords (C++, distributed systems, security, cryptography, backend, SDE-2), what recruiters filter on, activity (one post/month is plenty). · Output: `career/linkedin.md` checklist ticked + copy of headline/About. · Done-when: checklist complete | 1.25 |
| CO.2.2 | CO | **Platforms & recruiter channel setup** — Goal: inbound pipeline switched on. · Prompt: set up per `career/platforms.md`: Naukri (profile updated, resume uploaded, notice period set correctly), Instahyre, Cutshort, Wellfound, company career-page accounts and job alerts for the ranked list; a recruiter-reply template. · Covers: notice-period field strategy (always truthful); handling recruiter calls (screen questions from B.6.3); spam filtering. · Output: `career/platforms.md` table filled. · Done-when: all platforms live, alerts set for tier-1/tier-2 companies | 0.75 |

## Phase 3 — Targets, referrals & the application plan

| ID | Type | Session | Est h |
|---|---|---|---:|
| CO.3.1 | CO | **Target ranking & company research** — Goal: know each target's loop, level mapping and pay band before applying. · Prompt: for each company in the profile: loop format, level for your YOE (e.g. Amazon SDE-2 / L5, Google L4, Microsoft 61–62, verify), comp band (levels.fyi, AmbitionBox, Glassdoor, LeetCode compensation threads; **verify**), teams in India, notice-period flexibility, re-apply cooldowns. The learner researches; Claude structures and flags stale/uncertain data. Tiers: practice (apply first) → target → dream (apply last, when sharpest). · Output: `career/company-notes/*.md` filled; tiers in `career/applications.md`. · Done-when: every ranked company has loop format, level mapping and a band range with source + date | 1.5 |
| CO.3.2 | CO | **Referral mapping & outreach** — Goal: a referral for most tier-1/2 applications. · Prompt: list contacts per company (college alumni, ex-colleagues, LinkedIn 2nd-degree, communities); draft outreach from `career/referrals.md` templates in the learner's voice; set the follow-up cadence. · Covers: who to ask (engineers on the team > random employees > recruiters); what to send (JD link/ID, resume, 3-line pitch); follow-up etiquette; thanking and closing the loop. · Output: `career/referrals.md` contact table. · Done-when: ≥ 1 contact for each tier-1/2 company, messages drafted | 1 |
| CO.3.3 | CO | **Application batching plan** — Goal: offers that land together. · Prompt: `/pipeline plan`: schedule batches by tier and by each company's typical time-to-offer (Amazon/Google often 4–8 weeks, many Indian cos 2–4 weeks; verify from recruiters/debriefs); target a 2–3 week offer window around May–June 2027; set the pipeline table and weekly cadence. · Covers: practice-first ordering; cooldown periods (verify per company, often 6–12 months after a reject); not over-committing interview slots (max ~3 loops/week); leave planning at work. · Output: batch plan in `career/applications.md`. · Done-when: batches with dates exist for every tier | 1 |

## Phase 4 — Offers & negotiation

| ID | Type | Session | Est h |
|---|---|---|---:|
| CO.4.1 | CO | **India CTC anatomy & total-comp model** — Goal: read any offer letter correctly. · Prompt: walk `career/negotiation.md` §1–§3; the learner models their current CTC and 2 hypothetical offers in `career/offers.md` (fixed, variable at realistic payout, joining bonus, RSUs by year with the vesting schedule, retention, relocation, benefits) → year-1 cash, year-1 total, 4-year average. · Covers: fixed vs CTC inflation (gratuity, employer PF, insurance "in CTC"); variable payout reality; RSU vesting schedules & cliffs; clawbacks; tax at vest (confirm with a CA). · Output: `career/offers.md` model rows. · Done-when: the learner can compute year-1 and 4-yr-avg comp for any offer unaided | 1.25 |
| CO.4.2 | CO | **Negotiation role-play** — Goal: ask confidently, truthfully, specifically. · Prompt: `/offer practice`: Claude plays a recruiter (Amazon-style fixed bands + sign-on; Indian startup with ESOPs; a low-ball); the learner negotiates using competing-offer facts and the scripts in `career/negotiation.md` §6. · Covers: when to negotiate (after the offer, before signing); which levers move (joining bonus, RSUs, level, base within band); the level lever (SDE-2 vs SDE-1 matters more than 10% base); exploding offers; getting it in writing. · Output: phrasing notes in `career/negotiation.md` §Scripts. · Done-when: three role-plays completed; the learner states their walk-away number and reasons | 1.25 |
| CO.4.3 | CO | **Resignation, notice period, buyout, counter-offers** — Goal: leave cleanly. · Prompt: plan the exit: when to resign (after the signed offer letter; BGV timing), the resignation email (template in `career/negotiation.md` §8), handover plan, buyout/early-release request, counter-offer stance, relieving/experience letters, final settlement, PF transfer. · Output: exit checklist in `career/offers.md` §Exit. · Done-when: checklist complete and the notice-period facts confirmed from HR policy | 0.5 |

## Phase 5 — Pipeline operations (recurring)

| ID | Type | Session | Est h |
|---|---|---|---:|
| CO.5.1 | OPS | **Launch batch 1 (practice tier)** — Goal: first applications out, first real data. · Prompt: `/pipeline`: send batch 1 (3–5 practice-tier companies, with referrals where possible); log every application; set follow-ups. · Output: `career/applications.md` rows. · Done-when: batch 1 sent and logged | 1 |
| CO.5.2 | OPS | **Pipeline & debrief operations (recurring, months 6–9)** — Goal: nothing falls through; every real interview makes the prep sharper. · Prompt: weekly `/pipeline` (≤ 15 min) + `/debrief` within 24 h of every real interview (≤ 20 min each), routing gaps to the right repo's weak-areas. · Covers: funnel metrics (applied → OA → screen → loop → offer); conversion problems diagnosed (low screen rate → resume/referrals; low loop pass → prep gaps). · Output: `career/applications.md`, `career/interview-log.md`, weak-area rows in course repos. · Done-when: continuous; the track counts ~3 h budget (actuals logged in `progress/hours.md`) | 3 |

## Deferred to the depth pass
See `../roadmap/TRACK-switch.md` §Deferred.
