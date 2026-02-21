# autograder/grade.py
from __future__ import annotations

import os
import subprocess
import sys
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Set

from zoneinfo import ZoneInfo

REPO_ROOT = Path(__file__).resolve().parents[1]
SUBMISSIONS_DIR = REPO_ROOT / "submissions"
RESULTS_FILE = None

# Student IDs: PY102001001 .. PY102001020
ID_PREFIX = "PY102001"
MIN_ID = 1
MAX_ID = 44

# Allowed lab filenames
ALLOWED_LABS = {"lab00.py", "lab01.py", "lab02.py", "lab03.py", 
                "lab04.py", "lab05.py", "lab06.py", "lab07.py"}

TZ = ZoneInfo("America/Chicago")
LAB_DEADLINES = {
    "lab00.py": "2026-02-26 23:59",
    "lab01.py": "2026-03-07 23:59",
    "lab02.py": "2026-03-14 23:59",
    "lab03.py": "2026-03-21 23:59",
    "lab04.py": "2026-03-28 23:59",
    "lab05.py": "2026-04-04 23:59",
    "lab06.py": "2026-04-11 23:59",
    "lab07.py": "2026-04-18 23:59",
}

LAB_TO_TEST = {
    "lab00.py": "autograder/tests/test_lab00.py",
    "lab01.py": "autograder/tests/test_lab01.py",
    "lab02.py": "autograder/tests/test_lab02.py",
    "lab03.py": "autograder/tests/test_lab03.py",
    "lab04.py": "autograder/tests/test_lab04.py",
    "lab05.py": "autograder/tests/test_lab05.py",
    "lab06.py": "autograder/tests/test_lab06.py",
    "lab07.py": "autograder/tests/test_lab07.py",
}

# Late policy
GRACE_DAYS = 2
LATE_PENALTY_POINTS = 6      
ZERO_AFTER_DAYS = 7
LAB_MAX_POINTS = 20 

def run(cmd: List[str]) -> str:
    """Run a command and return stdout; exit on error."""
    p = subprocess.run(cmd, cwd=REPO_ROOT, text=True, capture_output=True)
    if p.returncode != 0:
        print("Command failed:", " ".join(cmd))
        print(p.stdout)
        print(p.stderr)
        sys.exit(p.returncode)
    return p.stdout.strip()


def is_valid_student_id(student_id: str) -> bool:
    if not student_id.startswith(ID_PREFIX):
        return False
    if len(student_id) != len(ID_PREFIX) + 3:
        return False
    suffix = student_id[-3:]
    if not suffix.isdigit():
        return False
    n = int(suffix)
    return MIN_ID <= n <= MAX_ID


def get_changed_files(base_ref: str) -> List[str]:
    run(["git", "fetch", "origin", base_ref])
    diff = run(["git", "diff", "--name-only", f"origin/{base_ref}...HEAD"])
    return [line for line in diff.splitlines() if line.strip()]

def parse_deadline(deadline_str: str) -> datetime:
    # "YYYY-MM-DD HH:MM" in America/Chicago
    return datetime.strptime(deadline_str, "%Y-%m-%d %H:%M").replace(tzinfo=TZ)

def get_pr_updated_time() -> datetime | None:
    """
    GitHub Actions provides event payload JSON at GITHUB_EVENT_PATH.
    For pull_request events, it contains pull_request.updated_at in ISO format.
    """
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path or not Path(event_path).exists():
        return None

    data = json.loads(Path(event_path).read_text(encoding="utf-8"))
    pr = data.get("pull_request")
    if not pr:
        return None

    # Example: "2026-01-30T12:34:56Z"
    updated_at = pr.get("updated_at") or pr.get("created_at")
    if not updated_at:
        return None

    # Parse as UTC then convert to America/Chicago
    t_utc = datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
    return t_utc.astimezone(TZ)


def days_late(submitted_at: datetime, deadline: datetime) -> int:
    delta = submitted_at - deadline
    if delta.total_seconds() <= 0:
        return 0
    return (delta.days + 1)

def apply_late_policy(
    *,
    earned: int,
    labs_touched: set[str],
    submitted_at: datetime | None,
) -> tuple[int, list[str]]:
    messages: list[str] = []

    if submitted_at is None:
        return earned, ["⚠️ Could not read PR timestamp; no late penalty applied."]

    deduction = 0

    for lab in sorted(labs_touched):
        deadline = parse_deadline(LAB_DEADLINES[lab])
        dlate = days_late(submitted_at, deadline)

        if dlate == 0:
            messages.append(f"{lab}: on time")

        elif dlate <= 7:
            penalty = dlate  
            deduction += penalty
            messages.append(f"{lab}: {dlate} day(s) late → -{penalty}")

        else:
            deduction += LAB_MAX_POINTS
            messages.append(f"{lab}: >7 days late → 0 for lab")

    final_score = max(0, earned - deduction)

    if deduction:
        messages.append(f"⚠️ Total late deduction: -{deduction}")
    else:
        messages.append("✅ No late deduction applied")

    return final_score, messages


def main() -> None:
    base_ref = os.environ.get("BASE_REF", "main")
    changed = get_changed_files(base_ref)

    if not changed:
        print("No changes detected. Nothing to grade.")
        return

    # 1) Forbid modifications to autograder / workflows
    forbidden_prefixes = ("autograder/", ".github/")
    forbidden = [p for p in changed if p.startswith(forbidden_prefixes)]
    if forbidden:
        print("❌ Forbidden changes detected (do not modify autograder/workflow):")
        for p in forbidden:
            print("  -", p)
        sys.exit(1)

    # 2) Only allow changes inside submissions/
    outside = [p for p in changed if not p.startswith("submissions/")]
    if outside:
        print("❌ Changes outside submissions/ are not allowed:")
        for p in outside:
            print("  -", p)
        sys.exit(1)

    # 3) Identify which student folder(s) were touched + which labs were submitted
    student_ids: Set[str] = set()
    labs_touched: Set[str] = set()

    for p in changed:
        parts = Path(p).parts  # submissions, <ID>, <file...>
        if len(parts) < 3 or parts[0] != "submissions":
            print("❌ Invalid path (expected submissions/<ID>/<file>):", p)
            sys.exit(1)

        sid = parts[1]
        filename = parts[-1]

        student_ids.add(sid)
        if filename in ALLOWED_LABS:
            labs_touched.add(filename)

    if len(student_ids) != 1:
        print("❌ This PR modifies multiple student folders. Only one is allowed.")
        print("Student folders touched:", ", ".join(sorted(student_ids)))
        sys.exit(1)

    student_id = next(iter(student_ids))

    if not is_valid_student_id(student_id):
        print(f"❌ Invalid student ID folder: {student_id}")
        print(f"Expected: {ID_PREFIX}001 .. {ID_PREFIX}{MAX_ID:03d}")
        sys.exit(1)

    student_dir = SUBMISSIONS_DIR / student_id
    results_file = student_dir / "autograder_results.json"
    if not student_dir.exists():
        print(f"❌ Student folder does not exist: {student_dir}")
        sys.exit(1)

    if not labs_touched:
        print("❌ No lab file detected in this PR.")
        print("Expected one of:", ", ".join(sorted(ALLOWED_LABS)))
        sys.exit(1)

    missing_deadlines = [lab for lab in labs_touched if lab not in LAB_DEADLINES]
    if missing_deadlines:
        print("❌ Missing deadline config for:", ", ".join(missing_deadlines))
        print("Edit LAB_DEADLINES in autograder/grade.py")
        sys.exit(1)

    print(f"✅ Student: {student_id}")
    print(f"✅ Lab file(s) changed in PR: {', '.join(sorted(labs_touched))}")

    # 4) Export info for pytest (tests can use these)
    env = os.environ.copy()
    env["STUDENT_ID"] = student_id
    env["STUDENT_DIR"] = str(student_dir)
    env["LABS_TOUCHED"] = ",".join(sorted(labs_touched))

    # 5) Run tests
    tests_to_run = [LAB_TO_TEST[lab] for lab in sorted(labs_touched)]
    cmd = ["pytest", "-q", *tests_to_run, "--timeout=5"]
    p = subprocess.run(cmd, cwd=REPO_ROOT, env=env, text=True)
    if p.returncode != 0:
      sys.exit(p.returncode)

   # 6) Apply late policy

    if not results_file.exists():
        print(f"Could not find results file: {results_file}")
        print("Did conftest.py write it?")
        sys.exit(1)

    results = json.loads(results_file.read_text(encoding="utf-8"))
    earned = int(results.get("earned", 0))
    max_points = int(results.get("max", 0))

    submitted_at = get_pr_updated_time()

    final_score, late_messages = apply_late_policy(
        earned=earned,
        labs_touched=labs_touched,
        submitted_at=submitted_at,
    )

    if submitted_at:
        print(f"Submitted (PR updated): {submitted_at:%Y-%m-%d %H:%M %Z}")

    for msg in late_messages:
        print(" -", msg)

    print(f"FINAL SCORE: {final_score}/{max_points}")
    sys.exit(0)


if __name__ == "__main__":
    main()
