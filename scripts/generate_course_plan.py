"""Generate the homepage calendar with links only for released exercises."""

from __future__ import annotations

import re
from pathlib import Path

try:
    from .schedule_support import read_schedule
except ImportError:  # Executed as a repository script by Quarto.
    from schedule_support import read_schedule


ROOT = Path(__file__).resolve().parent.parent
COURSE_ROOT = ROOT / "course_notes"
TEMPLATE = COURSE_ROOT / "config" / "course-plan.template"
OUTPUT = COURSE_ROOT / "_generated" / "course-plan.md"
EXERCISE_LINK = re.compile(r"\[([^]]+)]\((exercises/[^)]+\.qmd)\)")


def main() -> None:
    schedule = read_schedule(COURSE_ROOT / "_schedule.yml")
    released = {item.href for item in schedule.documents if schedule.is_released(item)}

    def select_link(match: re.Match[str]) -> str:
        label, href = match.groups()
        return match.group(0) if href in released else label

    rendered = EXERCISE_LINK.sub(select_link, TEMPLATE.read_text(encoding="utf-8"))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    main()
