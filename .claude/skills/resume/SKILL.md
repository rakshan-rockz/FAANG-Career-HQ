---
name: resume
description: Resume review / rewrite / tailoring with the learner (CO.1.x) — audits against career/resume/resume-guide.md, coaches XYZ impact bullets, ATS and one-page format, and tailors variants per company, using only facts the learner supplies; never invents achievements or numbers.
argument-hint: [review | rewrite | tailor <company or JD path>]
---

# Resume: $ARGUMENTS

Read `career/resume/resume-guide.md`, `career/resume/achievement-inventory.md`, the latest file in
`career/resume/versions/`, `behavioral/stories/README.md` (bullets and stories should agree), `progress/profile.md`.

**Iron rule:** only real facts from the learner. No invented metrics, titles, tools, scope. Missing number →
`[metric?]` + ask how it could be measured or honestly estimated. Inflated verbs ("led", "architected") are
challenged: "What exactly did you lead?"

- **review**: run the §9 checklist line by line; per bullet: verb · what · impact · number · "can you talk
  about this for 5 minutes?"; top 5 fixes ranked. Write findings to `career/resume/README.md` version log.
- **rewrite**: 3 bullets at a time. The learner drafts in XYZ form; Claude critiques and may propose a
  re-ordering or tighter wording **of the learner's own facts**; the learner accepts/edits. Save as the next
  version in `versions/` (markdown text copy; the learner keeps the formatted source/PDF there too).
- **tailor <company|JD>**: read the JD (the learner pastes it or gives a path); list its must-have keywords;
  map each to a real inventory item or mark "not a fit, don't add"; reorder bullets and skills; save
  `versions/v3-<family>-<date>.md` (or a company-specific copy).

Finish: wrap-up protocol in `CLAUDE.md` (hours, STATUS, weak areas such as "no metrics for project X").
