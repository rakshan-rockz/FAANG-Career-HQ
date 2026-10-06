#!/usr/bin/env bash
# Injects switch-year status into every new Claude session in the hub.
dir="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
today=$(date +%F)
due=$(awk -F'|' -v t="$today" 'NR>2 && /^\| /{for(i=4;i<=NF;i++){g=$i; gsub(/ /,"",g); if(g ~ /^[0-9]{4}-[0-9]{2}-[0-9]{2}$/ && g<=t) n++}} END{print n+0}' "$dir/progress/review-queue.md" 2>/dev/null)
open=$(awk '/^## Open/{f=1;next} /^## /{f=0} f && /^\| [0-9]{4}-/' "$dir/progress/weak-areas.md" 2>/dev/null | wc -l)
echo "Today: $today ($(date +%a)) · Target readiness 2027-05-15 · Story rehearsals due: $due · Open weak areas: $open"
echo
echo "## All repos"
"$dir/tools/status_all.sh" --brief 2>/dev/null | cut -c1-220
echo
cat "$dir/progress/STATUS.md" 2>/dev/null | sed -n '1,12p'
echo
echo "Suggest /today (what to do today, which repo, which command) or /week (weekly review & plan) if the learner hasn't said what they want."
