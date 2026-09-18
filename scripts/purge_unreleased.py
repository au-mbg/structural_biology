"""Remove every rendered format for exercises withheld by the active calendar."""

from __future__ import annotations

import os
from pathlib import Path

try:
    from .schedule_support import parse_profiles, read_schedule, resolve_schedule_path
except ImportError:  # Executed as a repository script by Quarto.
    from schedule_support import parse_profiles, read_schedule, resolve_schedule_path


ROOT = Path(__file__).resolve().parent.parent
COURSE_ROOT = ROOT / "course_notes"
FORMATS = (".html", ".pdf", ".docx")


def purge_unreleased(profile: str | None = None) -> list[Path]:
    profile_value = profile if profile is not None else os.environ.get("QUARTO_PROFILE", "")
    active_profiles = parse_profiles(profile_value)
    if os.environ.get("QUARTO_PROJECT_RENDER_ALL") != "1":
        print("Incremental render: keeping draft outputs")
        return []

    schedule_path = resolve_schedule_path(COURSE_ROOT / "_schedule.yml", profile_value)
    schedule = read_schedule(schedule_path)
    output_root = COURSE_ROOT / "_site"
    if "solution" in active_profiles:
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
