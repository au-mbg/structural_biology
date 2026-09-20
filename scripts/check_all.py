from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Sequence

from rich.console import Console
from rich.table import Table


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class Check:
    name: str
    arguments: tuple[str, ...]
    pixi_task: str


CHECKS = (
    Check("Figures", ("scripts/check_figures.py",), "check-figures"),
    Check("Downloads", ("scripts/check_downloads.py",), "check-downloads"),
    Check("Schedule", ("scripts/check_schedule.py",), "check-schedule"),
    Check("Quarto configuration", ("scripts/check_quarto.py",), "check-quarto"),
    Check(
        "PyMOL exercise scripts",
        (
            "scripts/check_scripts.py",
            "--directory",
            "course_notes/exercises/pymol_scripts",
            "--skip-pse",
        ),
        "check-pymol-scripts",
    ),
    Check(
        "PyMOL downloadable scripts",
        (
            "scripts/check_scripts.py",
            "--directory",
            "course_notes/files",
            "--skip-pse",
        ),
        "check-pymol-scripts",
    ),
)


def run_checks(
    checks: Sequence[Check] = CHECKS,
    console: Console | None = None,
    runner: Callable[..., subprocess.CompletedProcess] = subprocess.run,
) -> int:
    console = console or Console()
    results: list[tuple[Check, bool]] = []

    for check in checks:
        try:
            with console.status(f"Running {check.name}...", spinner="dots"):
                completed = runner(
                    [sys.executable, *check.arguments],
                    cwd=REPOSITORY_ROOT,
                    check=False,
                    capture_output=True,
                    text=True,
                )
            passed = completed.returncode == 0
        except OSError:
            passed = False
        results.append((check, passed))

    console.rule("Local check summary")
    table = Table(show_header=True, header_style="bold")
    table.add_column("Check")
    table.add_column("Status")
    for check, passed in results:
        table.add_row(
            check.name,
            "[bold green]PASS[/bold green]" if passed else "[bold red]FAIL[/bold red]",
        )
    console.print(table)

    failed_checks = [check for check, passed in results if not passed]
    failed_count = len(failed_checks)
    if failed_count:
        console.print(
            f"{failed_count} of {len(results)} checks failed.", style="bold red"
        )
        tasks = dict.fromkeys(check.pixi_task for check in failed_checks)
        console.print("Rerun failed checks for details:")
        for task in tasks:
            console.print(f"  pixi run {task}")
        return 1

    console.print(f"All {len(results)} checks passed.", style="bold green")
    return 0


def main() -> None:
    raise SystemExit(run_checks())


if __name__ == "__main__":
    main()
