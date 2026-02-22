#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import shutil
import subprocess
import tempfile
from pathlib import Path


def run(cmd: list[str], *, check: bool = True) -> str:
    p = subprocess.run(cmd, text=True, capture_output=True)
    if check and p.returncode != 0:
        raise RuntimeError(
            f"Command failed: {' '.join(cmd)}\nSTDOUT:\n{p.stdout}\nSTDERR:\n{p.stderr}"
        )
    return p.stdout

def detect_repo() -> str:
    out = subprocess.check_output(
        ["git", "config", "--get", "remote.origin.url"],
        text=True,
    ).strip()

    # handle both SSH and HTTPS
    if out.startswith("git@"):
        # git@github.com:OWNER/REPO.git
        repo = out.split(":", 1)[1]
    else:
        # https://github.com/OWNER/REPO.git
        repo = out.split("github.com/", 1)[1]

    return repo.removesuffix(".git")

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default = "Myanmar-Data-Tech/MMDT_T-PY102_Batch01", help="OWNER/REPO")
    ap.add_argument("--workflow", default="Autograde", help='Workflow name, default "Autograde"')
    ap.add_argument("--artifact", default="autograder_result", help="Artifact name")
    ap.add_argument("--limit", type=int, default=50, help="How many runs to scan")
    ap.add_argument("--out", default="autograder/gradebook.csv", help="Gradebook CSV path")
    args = ap.parse_args()
    repo = args.repo.strip() or detect_repo()

    gradebook = Path(args.out)
    gradebook.parent.mkdir(parents=True, exist_ok=True)

    seen_run_ids: set[str] = set()
    if gradebook.exists():
        with gradebook.open("r", encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                rid = (row.get("run_id") or "").strip()
                if rid:
                    seen_run_ids.add(rid)

    runs_json = run(
        [
            "gh",
            "run",
            "list",
            "--repo",
            repo,
            "--workflow",
            args.workflow,
            "--limit",
            str(args.limit),
            "--json",
            "databaseId,conclusion",
        ]
    )
    runs = json.loads(runs_json)

    new_rows: list[list[str]] = []

    with tempfile.TemporaryDirectory(prefix="gradebook_dl_") as td:
        tdir = Path(td)

        for r in runs:
            if r.get("conclusion") != "success":
                continue
            run_id = str(r["databaseId"])
            if run_id in seen_run_ids:
                continue

            dest = tdir / run_id
            dest.mkdir(parents=True, exist_ok=True)

            # download artifact; ignore if not found
            subprocess.run(
                ["gh", "run", "download", run_id, "--repo", repo, "--name", args.artifact, "--dir", str(dest)],
                check=False,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

            # find the json inside downloaded artifact
            matches = list(dest.glob("**/autograder_results.json"))
            if not matches:
                continue

            data = json.loads(matches[0].read_text(encoding="utf-8"))
            student_dir = data.get("student_dir", "")
            student_id = student_dir.strip("/").split("/")[-1] if student_dir else "UNKNOWN"
            final_score = int(data.get("final_score", data.get("earned", 0)))
            maxp = int(data.get("max", 0))
            submitted_at = data.get("submitted_at") or ""

            new_rows.append([student_id, str(final_score), str(maxp), str(submitted_at), run_id])

    if not new_rows:
        print("No new rows to append.")
        return

    write_header = not gradebook.exists()
    with gradebook.open("a", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        if write_header:
            w.writerow(["student_id", "final_score", "max_points", "submitted_at", "run_id"])
        for row in new_rows:
            w.writerow(row)

    print(f"Appended {len(new_rows)} rows to {gradebook}")


if __name__ == "__main__":
    main()