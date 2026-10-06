#!/usr/bin/env python3
"""Forecast interview-readiness across all switch-year course repos.

For each repo: remaining = sum of `Est h` in plan/roadmap/TRACK-switch.md from the row whose ID matches
the `**Next session:**` ID in progress/STATUS.md onward (ID not found -> all rows). A repo without a
TRACK-switch.md falls back to the mentor's switch budget (marked "budget").
Pace = average of the last 4 logged weeks in progress/hours.md (default 25 h/week, split by budget).

Usage: python3 tools/forecast.py [--today YYYY-MM-DD] [--target YYYY-MM-DD] [--pace H]
Pure python3.9 stdlib.
"""
import argparse
import datetime as dt
import math
import os
import re

HUB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECTS = os.environ.get("FAANG_PROJECTS_DIR", os.path.dirname(HUB))
TARGET = "2027-06-30"   # switch tracks complete; interviews start ~mid-April at ~80% (SWITCH-PLAN §3)
DEFAULT_PACE = 25.0

# (key in hours.md, repo dir, mentor switch budget in hours)
COURSES = [
    ("DSA", "FAANG-DSA-Master", 664),
    ("SD", "FAANG-System-Design-Master", 190),
    ("LLD", "FAANG-LLD-Master", 150),
    ("CS", "FAANG-CS-Core-Master", 60),
    ("Behavioral/Career", "FAANG-Career-HQ", 60),
]
ID_RE = re.compile(r"\b((?:[A-Z]{1,3}\.)?\d+(?:\.\d+)+)\b")


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def num(s):
    try:
        return float(s.replace("h", "").strip())
    except ValueError:
        return None


def next_id(repo):
    p = os.path.join(repo, "progress", "STATUS.md")
    if not os.path.exists(p):
        return None
    for line in open(p, encoding="utf-8"):
        if line.startswith("**Next session:**"):
            m = ID_RE.search(line.split(":**", 1)[1].replace("`", ""))
            return m.group(1) if m else None
    return None


def track_rows(repo):
    """-> list of (id, est_h) from the Order table, or None if no track file."""
    p = os.path.join(repo, "plan", "roadmap", "TRACK-switch.md")
    if not os.path.exists(p):
        return None
    rows, in_order = [], False
    for line in open(p, encoding="utf-8"):
        if line.startswith("## "):
            in_order = line.lower().startswith("## order")
            continue
        if not in_order or not line.startswith("|"):
            continue
        c = cells(line)
        if len(c) >= 6 and c[0].isdigit():
            h = num(c[5])
            if h is not None:
                rows.append((c[1].strip("`* "), h))
    return rows


def track_scale(repo, rows):
    """Repos differ on whether `Est h` rows include the ~20% overhead. Scale rows so they sum to the
    file's `**Track total (est.):** N h` line (never scale below 1)."""
    p = os.path.join(repo, "plan", "roadmap", "TRACK-switch.md")
    m = re.search(r"Track total \(est\.\):\*\*\s*~?([\d.]+)", open(p, encoding="utf-8").read())
    raw = sum(h for _, h in rows)
    return max(1.0, float(m.group(1)) / raw) if m and raw else 1.0


def hours_log():
    """-> list of dicts per logged week (latest last) with numeric per-course hours."""
    p = os.path.join(HUB, "progress", "hours.md")
    if not os.path.exists(p):
        return []
    header, weeks = None, []
    for line in open(p, encoding="utf-8"):
        if not line.startswith("|"):
            continue
        c = cells(line)
        if header is None and c and c[0].lower().startswith("week"):
            header = c
            continue
        if header is None or not re.match(r"\d{4}-\d{2}-\d{2}", c[0]):
            continue
        row = dict(zip(header, c))
        vals = {k: num(row.get(k, "")) for k, _, _ in COURSES}
        tot = num(row.get("Total", ""))
        if tot is None:
            known = [v for v in vals.values() if v is not None]
            tot = sum(known) if known else None
        if tot is None:
            continue
        weeks.append({"week": c[0], "total": tot, **{k: (v or 0.0) for k, v in vals.items()}})
    weeks.sort(key=lambda w: w["week"])
    return weeks


def fmt_date(d):
    return d.isoformat() if d else "never (0 h/week)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--today", default=dt.date.today().isoformat())
    ap.add_argument("--target", default=TARGET)
    ap.add_argument("--pace", type=float, help="override total h/week")
    a = ap.parse_args()
    today = dt.date.fromisoformat(a.today)
    target = dt.date.fromisoformat(a.target)

    # remaining per course
    remaining, notes = {}, {}
    for key, name, budget in COURSES:
        repo = os.path.join(PROJECTS, name)
        if not os.path.isdir(repo):
            remaining[key], notes[key] = float(budget), "repo missing → budget"
            continue
        rows = track_rows(repo)
        nid = next_id(repo)
        if rows is None or not rows:
            remaining[key], notes[key] = float(budget), f"no TRACK-switch → budget · next {nid or '?'}"
            continue
        ids = [r[0] for r in rows]
        if nid in ids:
            i = ids.index(nid)
            notes[key] = f"from {nid} (row {i + 1}/{len(rows)})"
        else:
            i = 0
            notes[key] = f"next {nid or '?'} not in track → all"
        remaining[key] = sum(h for _, h in rows[i:]) * track_scale(repo, rows)

    # pace
    weeks = hours_log()[-4:]
    if a.pace:
        pace, src = a.pace, "override"
    elif weeks:
        pace, src = sum(w["total"] for w in weeks) / len(weeks), f"avg of last {len(weeks)} logged week(s)"
    else:
        pace, src = DEFAULT_PACE, "default (no weeks logged)"
    split_total = sum(w[k] for w in weeks for k, _, _ in COURSES) if weeks else 0
    if weeks and split_total > 0 and not a.pace:
        rate = {k: sum(w[k] for w in weeks) / len(weeks) for k, _, _ in COURSES}
        split_src = "actual split"
    else:
        tot_rem = sum(remaining.values()) or 1
        rate = {k: pace * remaining[k] / tot_rem for k, _, _ in COURSES}
        split_src = "split ∝ remaining hours"

    total_rem = sum(remaining.values())
    weeks_to_target = max((target - today).days / 7.0, 0.0)
    print(f"Forecast as of {today} · target readiness {target} ({weeks_to_target:.1f} weeks away)")
    print(f"Pace: {pace:.1f} h/week ({src}); per-course {split_src}")
    print()
    print(f"{'Course':<18} {'Remaining':>9} {'h/wk':>6} {'Ready by':>12}  Source")
    latest = today
    for key, _, _ in COURSES:
        r, h = remaining[key], rate[key]
        d = today + dt.timedelta(days=math.ceil(7 * r / h)) if h > 0 else None
        if d is None and r > 0:
            latest = None
        elif latest is not None and d is not None and d > latest:
            latest = d
        print(f"{key:<18} {r:>8.1f}h {h:>6.1f} {fmt_date(d) if r > 0 else 'done':>12}  {notes[key]}")
    pooled = today + dt.timedelta(days=math.ceil(7 * total_rem / pace)) if pace > 0 else None
    print(f"{'TOTAL':<18} {total_rem:>8.1f}h {pace:>6.1f}")
    print()
    print(f"Projected ready (pooled hours):     {fmt_date(pooled)}")
    print(f"Projected ready (at current split): {fmt_date(latest)}")
    need = total_rem / weeks_to_target if weeks_to_target > 0 else float("inf")
    if pooled and pooled <= target:
        print(f"On track: {(target - pooled).days} days of slack vs {target}.")
    else:
        late = (pooled - target).days if pooled else None
        print(f"BEHIND target by {late} days at {pace:.1f} h/week." if late is not None else "No pace logged.")
    print(f"Required to hit {target}: {need:.1f} h/week from now.")


if __name__ == "__main__":
    main()
