#!/usr/bin/env bash
# One-screen status of every switch-year repo. Tolerates missing repos/files.
# Usage: tools/status_all.sh [--brief]
# Only calls a repo's gen_tracker.py if it supports --summary (without it, the script would REGENERATE
# that repo's tracker, which the hub must never do).
hub="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
projects="${FAANG_PROJECTS_DIR:-$(dirname "$hub")}"
brief=0; [ "$1" = "--brief" ] && brief=1

for name in FAANG-DSA-Master FAANG-System-Design-Master FAANG-LLD-Master FAANG-CS-Core-Master FAANG-Career-HQ; do
  repo="$projects/$name"
  if [ ! -d "$repo" ]; then
    echo "■ $name: (not created yet)"; [ $brief = 0 ] && echo; continue
  fi
  status="$repo/progress/STATUS.md"
  next=$(grep -m1 '^\*\*Next session:\*\*' "$status" 2>/dev/null | sed 's/^\*\*Next session:\*\* *//')
  track=$(grep -m1 '^\*\*Active track:\*\*' "$status" 2>/dev/null | sed 's/^\*\*Active track:\*\* *//')
  summary=""
  gt="$repo/tools/gen_tracker.py"
  if [ -f "$gt" ] && grep -q -- '--summary' "$gt"; then
    summary=$(cd "$repo" && timeout 20 python3 tools/gen_tracker.py --summary 2>/dev/null | head -1)
  fi
  if [ "$name" = "FAANG-Career-HQ" ]; then
    stories=$(ls "$repo"/behavioral/stories/[0-9]*.md 2>/dev/null | wc -l)
    mocks=$(ls "$repo"/behavioral/mocks/20*.md 2>/dev/null | wc -l)
    apps=$(awk '/^## Pipeline/{f=1;next} /^## /{f=0} f && /^\| [0-9]+ \|/' "$repo/career/applications.md" 2>/dev/null | wc -l)
    summary="Stories $stories · Behavioral mocks $mocks · Applications $apps"
  fi
  if [ $brief = 1 ]; then
    echo "■ $name · next: ${next:-?} · track: ${track:-—}${summary:+ · $summary}"
  else
    echo "■ $name"
    echo "  Next session: ${next:-(no STATUS.md / line)}"
    echo "  Active track: ${track:-(not set)}"
    [ -n "$summary" ] && echo "  Summary:      $summary"
    [ -f "$repo/plan/roadmap/TRACK-switch.md" ] || echo "  (no plan/roadmap/TRACK-switch.md yet)"
    echo
  fi
done
