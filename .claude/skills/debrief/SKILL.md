---
name: debrief
description: Debrief a real interview within 24 hours — log the questions and what happened in career/interview-log.md, score it honestly, update company notes, and route each gap to the right course repo's progress/weak-areas.md (DSA, System Design, LLD, CS core) or this repo's.
argument-hint: [company] [round]
---

# Interview debrief: $ARGUMENTS

`date +%F`. Read `career/interview-log.md`, `career/company-notes/<company>.md`, `career/applications.md`.

1. Ask, a few at a time: round type and format; each question as precisely as remembered (constraints,
   follow-ups); what the learner did (approach, stuck points, hints, time); interviewer reactions; what they'd
   redo. For behavioral rounds: which story was used and where the probes went.
2. Honest self-score with the matching repo's rubric (DSA /100 roadmap §8; SD /120; LLD per its README;
   behavioral /100). Say what probably helped or hurt.
3. **Route gaps** (be specific: "couldn't derive monotonic-stack for next-greater with circular array"):
   | Gap type | Append to |
   |---|---|
   | DSA / coding speed / patterns | `/home/qnu/Documents/personal/projects/FAANG-DSA-Master/progress/weak-areas.md` |
   | HLD / system design | `…/FAANG-System-Design-Master/progress/weak-areas.md` |
   | LLD / machine coding / concurrency | `…/FAANG-LLD-Master/progress/weak-areas.md` |
   | OS / networks / DBMS / C++ internals | `…/FAANG-CS-Core-Master/progress/weak-areas.md` |
   | Behavioral / story / HR / negotiation | this repo's `progress/weak-areas.md` |
   Read the target file first and **append a row to its Open table in that file's own column format**
   (`| date | topic | gap | correct understanding | 0 |`, tagged "(real interview: <company>)"). This is the
   only write allowed in other repos. If the repo or file doesn't exist, keep the gap in the hub's weak-areas
   with a "route to <repo> when it exists" note.
4. Update `career/company-notes/<company>.md` §From my interviews (and mark any loop-format facts **verified**).
5. Update `career/applications.md` stage/next action; `progress/metrics.md` interviews count.
6. Append the entry to `career/interview-log.md` (index row + entry in the commented shape).
7. Tell the learner in 3 lines: gaps routed where, what to do before the next round (e.g. "`/mock amazon`
   in DSA within 3 days", "`/story` 05 P3 numbers").
