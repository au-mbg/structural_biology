from __future__ import annotations

import glob
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml
from rich.console import Console

try:
    from .helpers import ROOT
except ImportError:
    from helpers import ROOT


@dataclass
class NavigationReferences:
    files: set[Path] = field(default_factory=set)
    explicit_files: set[Path] = field(default_factory=set)
    unmatched_targets: set[str] = field(default_factory=set)


def qmd_files(directory: Path) -> set[Path]:
    return {path.resolve() for path in directory.rglob("*.qmd") if path.is_file()}


def expand_generated_target(
    target: str,
    root: Path,
    references: NavigationReferences,
) -> None:
    if target == "auto":
        matches = qmd_files(root)
        matches.discard((root / "index.qmd").resolve())
    else:
        pattern = target.lstrip("/")
        candidate = root / pattern
        if not glob.has_magic(pattern) and candidate.is_dir():
            matches = qmd_files(candidate)
        else:
            matches = {
                path.resolve()
                for path in root.glob(pattern)
                if path.is_file() and path.suffix.lower() == ".qmd"
            }

    if matches:
        references.files.update(matches)
    else:
        references.unmatched_targets.add(target)


def add_navigation_target(
    target: str,
    root: Path,
    references: NavigationReferences,
) -> None:
    normalized_target = target.lstrip("/")
    if not glob.has_magic(normalized_target) and normalized_target.endswith(".qmd"):
        path = (root / normalized_target).resolve()
        references.files.add(path)
        references.explicit_files.add(path)
        return

    expand_generated_target(target, root, references)


def find_all_qmd(config: Any, root: Path = ROOT) -> NavigationReferences:
    references = NavigationReferences()

    def visit(node: Any) -> None:
        if isinstance(node, dict):
            href = node.get("href")
            if isinstance(href, str) and href.lstrip("/").endswith(".qmd"):
                add_navigation_target(href, root, references)

            auto = node.get("auto")
            if isinstance(auto, str):
                expand_generated_target(auto, root, references)

            if "contents" in node:
                visit_contents(node["contents"])

            for key, value in node.items():
                if key not in {"href", "auto", "contents"}:
                    visit(value)
        elif isinstance(node, list):
            for item in node:
                visit(item)

    def visit_contents(contents: Any) -> None:
        if isinstance(contents, str):
            add_navigation_target(contents, root, references)
        elif isinstance(contents, list):
            for item in contents:
                if isinstance(item, str):
                    add_navigation_target(item, root, references)
                else:
                    visit(item)
        elif isinstance(contents, dict):
            visit(contents)

    visit(config)
    return references


def check_quarto(root: Path = ROOT, console: Console | None = None) -> int:
    console = console or Console()
    console.print(f"Root directory is: {root}")

    with open(root / "config" / "quarto" / "website.yml") as config_file:
        website_config = yaml.safe_load(config_file)
    references = find_all_qmd(website_config, root)

    all_qmd_files = qmd_files(root)
    missing_files = sorted(references.explicit_files - all_qmd_files)

    for path in missing_files:
        console.print(f"Missing referenced .qmd file: {path}", style="bold red")
    for target in sorted(references.unmatched_targets):
        console.print(
            f"Navigation target matched no .qmd files: {target}", style="bold red"
        )

    if not missing_files and not references.unmatched_targets:
        console.print("All configured navigation targets are valid.")

    unreferenced_files = sorted(all_qmd_files - references.files)
    for path in unreferenced_files:
        console.print(f"Unreferenced .qmd file: {path}")
    if not unreferenced_files:
        console.print("All .qmd files in the project are referenced.")

    return 1 if missing_files or references.unmatched_targets else 0


def main() -> None:
    raise SystemExit(check_quarto())


if __name__ == "__main__":
    main()
