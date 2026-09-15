"""Small, dependency-free helpers for the course release calendars."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path


@dataclass(frozen=True)
class ScheduledDocument:
    href: str
    release_date: date
    draft_override: bool | None = None


@dataclass(frozen=True)
class Schedule:
    draft_after: str
    timezone: str
    documents: tuple[ScheduledDocument, ...]

    @property
    def threshold(self) -> date:
        if self.draft_after == "system-time":
            return datetime.now(timezone.utc).date()
        return date.fromisoformat(self.draft_after)

    def is_released(self, document: ScheduledDocument) -> bool:
        if document.draft_override is not None:
            return not document.draft_override
        return document.release_date <= self.threshold


_VALUE = re.compile(r'^\s*(draft-after|timezone|date):\s*["\']?([^"\'#]+)')
_HREF = re.compile(r'^\s*-\s+href:\s*["\']?([^"\'#]+)')
_DRAFT = re.compile(r"^\s+draft:\s*(true|false)\s*$", re.IGNORECASE)


def read_schedule(path: Path) -> Schedule:
    """Parse the deliberately small scheduled-docs schema used by this repository."""
    draft_after: str | None = None
    timezone_name: str | None = None
    documents: list[ScheduledDocument] = []
    current_href: str | None = None
    current_date: date | None = None
    current_override: bool | None = None

    def finish_document() -> None:
        nonlocal current_href, current_date, current_override
        if current_href is None:
            return
        if current_date is None:
            raise ValueError(f"Missing date for {current_href} in {path}")
        documents.append(ScheduledDocument(current_href, current_date, current_override))
        current_href = None
        current_date = None
        current_override = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        href_match = _HREF.match(raw_line)
        if href_match:
            finish_document()
            current_href = href_match.group(1).strip()
            continue
        value_match = _VALUE.match(raw_line)
        if value_match:
            key, value = value_match.groups()
            value = value.strip()
            if key == "draft-after":
                draft_after = value
            elif key == "timezone":
                timezone_name = value
            elif key == "date" and current_href:
                current_date = date.fromisoformat(value)
            continue
        draft_match = _DRAFT.match(raw_line)
        if draft_match and current_href:
            current_override = draft_match.group(1).lower() == "true"
    finish_document()

    if draft_after is None or timezone_name is None or not documents:
        raise ValueError(f"Incomplete scheduled-docs calendar: {path}")
    if timezone_name != "+00:00":
        raise ValueError(f"Only UTC (+00:00) is supported by the course tooling: {path}")
    return Schedule(draft_after, timezone_name, tuple(documents))
