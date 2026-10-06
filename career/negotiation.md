# Negotiation (India market)

Used by `/offer` and CO.4.1–CO.4.3. **Honesty rule:** never misstate current CTC, notice period or
competing offers. Indian BGV commonly verifies payslips, relieving letters and employment dates, and
recruiters at big companies talk to each other. Every number marked *verify* must be checked against
the actual offer letter, the recruiter, or current data (levels.fyi, AmbitionBox, Glassdoor, peers).
Tax: **confirm with a CA**; this file is not tax advice.

## 1. Anatomy of an Indian offer ("CTC")

| Component | What it is | Watch for |
|---|---|---|
| **Fixed / base** | Monthly salary × 12 (basic + HRA + special allowance + others) | The only fully guaranteed cash; many hikes are negotiated on this |
| **Employer PF** | 12% of basic, often shown *inside* CTC | Not in-hand; yours but locked |
| **Gratuity** | ~4.81% of basic, payable only after ~5 years of service (verify current law) | Often inflates CTC; worth ~0 if you leave before 5 years |
| **Insurance / benefits in CTC** | Health/term/accident premiums | Inflates CTC; compare benefits separately |
| **Variable / performance bonus** | Target % of base, paid on rating × company factor | Treat as ~70–100% of target unless the payout history is known (verify with employees) |
| **Joining / sign-on bonus** | One-time (sometimes split year 1/2) | **Clawback** if you leave within 12 (sometimes 24) months; taxed as salary |
| **RSUs** | Stock granted in USD/INR value, vesting over years | Schedule, cliff, refreshers, currency and share-price risk |
| **ESOPs** (startups, Flipkart/PhonePe/Razorpay/Swiggy/Zomato-type) | Options with a strike price | Liquidity (buybacks/IPO), strike, exercise window after leaving, dilution; value skeptically |
| **Retention bonus** | Paid if you stay N months | Conditional; clawback |
| **Relocation** | Lump sum / reimbursements / temporary housing | One-time; sometimes clawback |
| **Other** | Meal cards, internet, NPS, learning budgets, WFH allowance | Small; in-hand effect varies with the tax regime |

## 2. RSU vesting schedules (all **verify**: companies change them and offers differ by level)

| Company (commonly reported) | Schedule | Cliff | Notes |
|---|---|---|---|
| Amazon | 5% / 15% / 40% / 40% over 4 years | 1 year | Back-loaded; sign-on bonus in years 1–2 compensates. Model years separately |
| Google | Front-loaded over 4 years (reported ~33/33/22/12 or similar), monthly after start | Reported no cliff for new grants | verify current schedule |
| Microsoft | 25% per year (often quarterly/semi-annual vesting) | ~1 year typical | Annual stock refreshers by rating |
| Meta | 25% per year, quarterly | Reported no cliff (verify) | |
| Uber, Atlassian, Salesforce, Adobe, Intuit, Walmart, Oracle | Typically 4 years, 25%/yr, various frequencies | often 1 year | Check each offer letter |

**Refreshers** (annual top-up grants) matter for years 2–4; ask what's typical for "meets"/"exceeds".

## 3. Evaluating total comp

Compute for every offer (in `offers.md`):
- **Year-1 cash** = base + expected variable + joining bonus (yr-1 part) + relocation.
- **Year-1 total** = year-1 cash + RSUs vesting in year 1 (at grant-value price; note FX).
- **4-year average** = (Σ base + Σ variable + Σ bonuses + total RSU grant) / 4 (+ expected refreshers,
  labelled as an assumption).
- **In-hand monthly** (approx; tax regime choice changes it; CA to confirm).
- **Non-cash**: level (SDE-2 vs SDE-1 changes the next 2–3 years' bands), team/product, learning, WLB,
  on-call, location/commute, stability, brand for the *next* switch.

The target "30–35 LPA" must be defined at intake: **fixed**, **year-1 total**, or **4-yr average**? They
differ by lakhs at RSU-heavy companies.

## 4. Before the offer: the recruiter screen

- **Current CTC**: state accurately (fixed + variable + other), because it will be verified.
- **Expected CTC**: prefer to defer until the level is known: "I'd like to understand the level and
  role first; I'm confident we can find a number that works if it's a fit." If pressed: a researched range
  for the *role and level* (not a % over current), top of range = your real target plus margin.
- **Notice period**: the true contractual figure + what's possible ("90 days contractual; I'll request early
  release and can discuss buyout").
- **Other processes**: truthfully, without names/numbers unless it helps: "I'm in final rounds elsewhere."

## 5. After the offer: levers (roughly most → least negotiable at big tech; verify per company)

1. **Level** (the biggest long-term lever; ask for re-levelling with evidence if you were down-levelled).
2. **Joining bonus** (most flexible, one-time cost to them).
3. **RSUs** (grant size within band).
4. **Base** (bands are tight at big tech; more room at Indian product cos).
5. **Start date / notice buyout reimbursement**, relocation.

A competing offer in writing is the strongest lever. Negotiate **once, clearly, with all asks together**,
after the full written offer and before signing. Get every change in the revised letter.

## 6. Scripts (the learner adapts; phrasing bank grows in CO.4.2 and B.6.3)

- **Opening**: "Thank you, I'm genuinely excited about the team. Before I sign I'd like to discuss the
  compensation so I can say yes with full commitment."
- **Using a competing offer**: "I have an offer from <company> at <year-1 total / structure>. <Your company> is
  my first choice because <specific>. If you can get to <number/structure>, I'm ready to accept this week."
- **No competing offer**: "Based on my research for SDE-2 at this level (levels.fyi / peers) and the scope
  we discussed, I was expecting closer to <range>. Is there flexibility on the joining bonus or RSUs?"
- **Exploding offer / deadline**: "I'm finishing another process by <date>. Could we extend the deadline to
  <date>? I want to decide with complete information."
- **Low-ball**: "I appreciate it, but this is well below what the role pays in the market and below
  <competing offer>. What's the best you can do on <lever>?"
- **Closing**: "If we can agree on X, I'll accept today."
- Never: invent an offer, inflate current CTC, or accept verbally and keep shopping for weeks.

## 7. Notice period, buyout, early release

- Typical India notice: **30 / 60 / 90 days** (confirm yours in the appointment letter / HR policy).
- **Early release**: request in the resignation; offer a solid handover plan; managers can often release
  after 30–60 days if handover is done. Get it in writing.
- **Buyout**: pay the employer basic (or gross, per policy) for the unserved days; many new employers
  reimburse this (ask during negotiation; it's often via the joining bonus).
- **Leave encashment offset**: some policies let earned leave shorten notice (verify).
- **Garden leave / non-compete**: rare/weakly enforceable in India, but read the clause; confidentiality
  and IP clauses are enforced.
- Offer letters commonly specify a joining date; tell the new employer your realistic date up front.

## 8. Resignation etiquette

1. Resign **only after** a signed offer letter (and ideally after BGV has started without issues).
2. Tell your manager first, in person/call, then email the formal letter the same day.
3. Email (short): *"Dear <manager>, I'm writing to formally resign from my position as <title>, effective today;
   per my notice period my last working day will be <date>. I'm grateful for <1 genuine thing>. I'll make
   sure the handover of <areas> is complete and documented. I'd also like to request early release on
   <date> if the handover allows. Regards, <name>"*
4. No criticism in the exit interview; be constructive and brief.
5. Handover doc: systems owned, runbooks, open work, contacts; knowledge-transfer sessions scheduled.
6. Collect: relieving letter, experience letter, final payslips, Form 16; full & final settlement; **PF
   transfer** (UAN) to the new employer; return assets.

## 9. Counter-offers

Decide the stance **before** resigning. Common view: if money were the only reason, you should have
negotiated internally before interviewing; accepting a counter can mark you as a flight risk. If you'd
genuinely stay for a specific change, say so *before* you accept an outside offer, not after. Never use a
counter-offer just to squeeze the new employer.
