from helpers import ROOT
from rich.console import Console
import yaml

def main():
    console = Console()
    console.print(f"Root directory is: {ROOT}")

    exercise_files = (ROOT / "exercises").glob('*.qmd')
    exercise_files = list(exercise_files)
    exercise_files = [f for f in exercise_files if f.name != 'index.qmd']

    exercise_scheduled = {str(path): False for path in exercise_files}
    solution_scheduled = {str(path): False for path in exercise_files}

    with open(ROOT / "_schedule.yml") as f:
        exercise_schedule = yaml.safe_load(f)
    with open(ROOT / "_schedule-solution.yml") as f:
        solution_schedule = yaml.safe_load(f)

    for entry in exercise_schedule['scheduled-docs']['docs']:
        path = ROOT / entry.get('href')
        if not path.exists():
            console.print(f"File does not exist for exercise schedule path: {path}")
        if str(path) in exercise_scheduled:
            exercise_scheduled[str(path)] = True

    for entry in solution_schedule['scheduled-docs']['docs']:
        path = ROOT / entry.get('href')
        if not path.exists():
            console.print(f"File does not exist for solution schedule path: {path}")
        if str(path) in solution_scheduled:
            solution_scheduled[str(path)] = True

    for path, scheduled in exercise_scheduled.items():
        if not scheduled:
            console.print(f"Exercise file not scheduled: {path}")

    for path, scheduled in solution_scheduled.items():
        if not scheduled:
            console.print(f"Solution file not scheduled: {path}")



if __name__ == "__main__":
    main()