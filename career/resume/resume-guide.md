# Resume Guide

Used by `/resume` and sessions CO.1.1–CO.1.4. **Every fact comes from the learner.** Unknown number →
`[metric?]`, never a guess dressed as fact.

## 1. What a resume must do
A recruiter scans it for 7–10 seconds; an ATS parses it first; a hiring manager reads it before the HM
round and **asks about every line**. So it has to: parse cleanly → show level and impact at a glance →
survive 5 minutes of questions per bullet.

## 2. Impact bullets: the XYZ formula
> **Accomplished [X] as measured by [Y], by doing [Z].** (Google's recruiting advice; also CAR:
> Challenge → Action → Result.)

| Weak | Why | Strong (shape only; learner supplies facts) |
|---|---|---|
| Worked on key management module | duty, not achievement | Cut key-rotation downtime from [X min] to [Y s] for [N] devices by redesigning rotation as a two-phase hot swap in C++ |
| Responsible for performance improvements | vague, passive | Improved [PQC handshake] throughput [N×] (p99 [a] → [b] ms) by batching [operation] and removing heap allocations on the hot path |
| Helped with testing | no ownership | Built a fuzzing + sanitizer CI stage that caught [N] memory-safety bugs pre-release; adopted by [M] teams |

Rules: start with a strong past-tense verb (Designed, Built, Reduced, Led, Migrated, Automated, Hardened);
one idea per bullet; ≤ 2 lines; impact first when the number is strong; name the tech only if it helps
(C++17, gRPC, Linux, OpenSSL/liboqs, Kafka, Docker…); 3–6 bullets for the current role, fewer for older ones.

**Honest estimates:** "~40%", "est. 10 h/week saved" are fine if the learner can explain how they
estimated. Never inflate scope ("led" only if you led; "architected" only if you owned the design).

## 3. ATS basics
- Single column; standard section headings (Experience, Skills, Projects, Education).
- No tables, text boxes, icons, images, headers/footers for content; standard fonts.
- PDF from Word/Google Docs/LaTeX is fine if the text layer extracts cleanly: **test by copy-pasting
  the PDF into a plain text file**; order and words must survive.
- Include the keywords you genuinely have, in the words JDs use ("distributed systems", "C++",
  "multithreading", "Linux", "system design", "security").
- Filename: `Firstname-Lastname-SDE-Resume.pdf`.

## 4. One page
Under ~10 YOE: one page. Cut: objective statements, "references available", soft-skill lists, school
marks (unless asked), old/irrelevant bullets, duplicate tech. Keep white space; 10–11 pt.

## 5. Section order
Header (name, phone, email, LinkedIn, GitHub, city) → **Experience** → **Skills** (Languages · Systems ·
Tools · Domain) → **Projects** (if they add signal) → **Education** → Achievements (competitive
programming ranks, patents, papers, certifications, only if real and relevant).

## 6. Security / quantum-safe domain framing
Generalist interviewers at Amazon/Flipkart may not know QKD or PQC. Frame for them:
- Lead with the **engineering** (C++ performance, concurrency, protocol implementation, reliability,
  scale: devices, sessions/sec, uptime), then the domain ("post-quantum TLS", "key management").
- One short phrase of context: "quantum-safe key distribution product used by [banks/telecoms/defence]".
- For security-heavy targets (Microsoft/Google security orgs, Salesforce, Oracle, Adobe, Intuit), move
  the domain forward: standards, threat modelling, crypto agility, compliance.
- NDA: no customer names, no unreleased features, no internal metrics you're not allowed to share
  (use relative numbers: "3× faster", "−60% latency").

## 7. Projects
Include if they show something experience doesn't: a C++ systems project (allocator, KV store, thread
pool, networking library), open-source contributions, a serious side project. Each: one line on what +
one on the hard part + link. Course repos' LLD/machine-coding projects qualify only if substantial and
the learner's own work.

## 8. Tailoring (CO.1.4)
Two base variants: **product/backend** and **infra/security/platform**. Per application: reorder bullets,
adjust the skills line, mirror 3–5 real JD keywords you have. Never add a skill you can't be interviewed on.

## 9. Audit checklist (used by `/resume review`)
- [ ] One page, single column, parses as plain text in order
- [ ] Header complete; LinkedIn URL matches the profile content
- [ ] Every bullet: verb + what + impact; ≥ 70% have a number or a clear measure
- [ ] No "responsible for", "worked on", "helped", "various"
- [ ] Scope matches the target level (SDE-2: owned components/features end to end)
- [ ] Dates, titles consistent with LinkedIn and what BGV will show
- [ ] Skills: only interview-able items; C++ standard named
- [ ] No typos; consistent tense and punctuation
- [ ] Each bullet defensible for 5 minutes (the learner can tell its story; ideally it's in the story bank)
- [ ] Domain explained for a generalist; nothing confidential

## 10. Versions
Stored in `versions/`: `v0-<date>` (original) · `v1` (XYZ rewrite) · `v2` (formatted, ATS-checked) ·
`v3-product`, `v3-security` (tailored). Log what changed in `README.md` here.
