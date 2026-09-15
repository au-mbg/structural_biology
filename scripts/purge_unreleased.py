"""Remove every rendered format for exercises withheld by the active calendar."""

from __future__ import annotations

import os
from pathlib import Path

try:
    from .schedule_support import read_schedule
except ImportError:  # Executed as a repository script by Quarto.
    from schedule_support import read_schedule


ROOT = Path(__file__).resolve().parent.parent
COURSE_ROOT = ROOT / "course_notes"
FORMATS = (".html", ".pdf", ".docx")


def purge_unreleased(profile: str | None = None) -> list[Path]:
    schedule = read_schedule(COURSE_ROOT / "_schedule.yml")
    active_profile = profile if profile is not None else os.environ.get("QUARTO_PROFILE", "")
    output_root = COURSE_ROOT / "_site"
    if active_profile == "solution":
        output_root /= "instructor"

    removed: list[Path] = []
    for document in schedule.documents:
        if schedule.is_released(document):
            continue
        relative_output = Path(document.href).with_suffix("")
        for suffix in FORMATS:
            target = (output_root / relative_output).with_suffix(suffix)
            if target.exists():
                target.unlink()
                removed.append(target)
    if removed:
        print(f"Removed {len(removed)} unreleased exercise outputs from {output_root}")
    return removed


if __name__ == "__main__":
    purge_unreleased()
