"""Run Quarto with the release calendar belonging to the selected profile."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import socket
import subprocess
import sys
from pathlib import Path


EXERCISE = "exercise"
SOLUTION = "solution"
PROFILES = (EXERCISE, SOLUTION)


class ScheduleSelectionError(RuntimeError):
    """Raised when a release calendar cannot be selected safely."""


def _process_is_alive(pid: int) -> bool:
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


class ScheduleSelection:
    """Serialize renders and temporarily select the solution calendar."""

    def __init__(self, repository_root: Path, profile: str) -> None:
        self.repository_root = repository_root
        self.course_root = repository_root / "course_notes"
        self.profile = profile
        self.state_dir = repository_root / ".schedule-selection.lock"
        self.backup = self.state_dir / "exercise-schedule.yml"
        self.exercise_schedule = self.course_root / "_schedule.yml"
        self.solution_schedule = self.course_root / "_schedule-solution.yml"
        self._locked = False

    def _recover_or_reject_existing_lock(self) -> None:
        if not self.state_dir.exists():
            return
        try:
            owner = json.loads((self.state_dir / "owner.json").read_text(encoding="utf-8"))
        except (OSError, ValueError):
            owner = {}
        same_host = owner.get("hostname") == socket.gethostname()
        try:
            pid = int(owner.get("pid", -1))
        except (TypeError, ValueError):
            pid = -1
        if same_host and _process_is_alive(pid):
            raise ScheduleSelectionError(f"Another profile render is active (PID {pid}).")
        if self.backup.exists():
            os.replace(self.backup, self.exercise_schedule)
        shutil.rmtree(self.state_dir)

    def __enter__(self) -> "ScheduleSelection":
        if self.profile not in PROFILES:
            raise ScheduleSelectionError(f"Unknown profile: {self.profile}")
        if not self.exercise_schedule.is_file():
            raise ScheduleSelectionError(f"Missing exercise schedule: {self.exercise_schedule}")
        if self.profile == SOLUTION and not self.solution_schedule.is_file():
            raise ScheduleSelectionError(f"Missing solution schedule: {self.solution_schedule}")

        self._recover_or_reject_existing_lock()
        try:
            self.state_dir.mkdir()
        except FileExistsError as error:
            raise ScheduleSelectionError("Another profile render started concurrently.") from error
        self._locked = True
        (self.state_dir / "owner.json").write_text(
            json.dumps({"pid": os.getpid(), "hostname": socket.gethostname()}),
            encoding="utf-8",
        )

        if self.profile == SOLUTION:
            shutil.copyfile(self.exercise_schedule, self.backup)
            replacement = self.state_dir / "active-schedule.yml"
            shutil.copyfile(self.solution_schedule, replacement)
            os.replace(replacement, self.exercise_schedule)
        return self

    def __exit__(self, exc_type: object, exc_value: object, traceback: object) -> None:
        try:
            if self.profile == SOLUTION and self.backup.exists():
                os.replace(self.backup, self.exercise_schedule)
        finally:
            if self._locked:
                shutil.rmtree(self.state_dir, ignore_errors=True)
                self._locked = False


def run_quarto(repository_root: Path, command: str, profile: str) -> int:
    with ScheduleSelection(repository_root, profile):
        completed = subprocess.run(
            ["quarto", command, "--profile", profile],
            cwd=repository_root / "course_notes",
            check=False,
        )
    return completed.returncode


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("render", "preview", "render-all"))
    parser.add_argument("profile", nargs="?", choices=PROFILES)
    args = parser.parse_args(argv)
    if args.command != "render-all" and args.profile is None:
        parser.error("render and preview require a profile")
    if args.command == "render-all" and args.profile is not None:
        parser.error("render-all does not accept a profile")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    repository_root = Path(__file__).resolve().parent.parent
    try:
        if args.command == "render-all":
            shutil.rmtree(repository_root / "course_notes" / "_site", ignore_errors=True)
            shutil.rmtree(repository_root / "course_notes" / ".quarto", ignore_errors=True)
            exercise_result = run_quarto(repository_root, "render", EXERCISE)
            if exercise_result != 0:
                return exercise_result
            return run_quarto(repository_root, "render", SOLUTION)
        return run_quarto(repository_root, args.command, args.profile)
    except ScheduleSelectionError as error:
        print(f"Schedule selection failed: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
