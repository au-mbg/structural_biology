from pathlib import Path

try:
    from .helpers import ROOT
except ImportError:
    from helpers import ROOT
from rich.console import Console
import yaml


def check_schedule(root: Path = ROOT, console: Console | None = None) -> int:
    console = console or Console()
    console.print(f"Root directory is: {root}")

    exercise_files = (root / "exercises").glob("*.qmd")
    exercise_files = list(exercise_files)
    exercise_files = [f for f in exercise_files if f.name != "index.qmd"]

    exercise_scheduled = {str(path): False for path in exercise_files}
    solution_scheduled = {str(path): False for path in exercise_files}

    any_mistake = False

    with open(root / "_schedule.yml") as f:
        exercise_schedule = yaml.safe_load(f)
    with open(root / "_schedule-solution.yml") as f:
        solution_schedule = yaml.safe_load(f)

    for entry in exercise_schedule["scheduled-docs"]["docs"]:
        path = root / entry.get("href")
        if not path.exists():
            console.print(f"File does not exist for exercise schedule path: {path}")
            any_mistake = True
        if str(path) in exercise_scheduled:
            exercise_scheduled[str(path)] = True

    for entry in solution_schedule["scheduled-docs"]["docs"]:
        path = root / entry.get("href")
        if not path.exists():
            console.print(f"File does not exist for solution schedule path: {path}")
            any_mistake = True
        if str(path) in solution_scheduled:
            solution_scheduled[str(path)] = True

    for path, scheduled in exercise_scheduled.items():
        if not scheduled:
            console.print(f"Exercise file not scheduled: {path}")
            any_mistake = True

    for path, scheduled in solution_scheduled.items():
        if not scheduled:
            console.print(f"Solution file not scheduled: {path}")
            any_mistake = True

    if any_mistake:
        console.print("There are mistakes in the schedule.", style="bold red")
    else:
        console.print("No mistakes found in the schedule.", style="bold green")

    return 1 if any_mistake else 0


def main() -> None:
    raise SystemExit(check_schedule())

if __name__ == "__main__":
    main()
