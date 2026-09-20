from pathlib import Path

try:
    from .helpers import QMDDocument, ROOT
except ImportError:
    from helpers import QMDDocument, ROOT
from rich.console import Console

ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".svg", ".gif"}
EXCLUDE = {"_site", "_preview", ".quarto"}


def relative_to_root(path: Path, root: Path) -> Path:
    return path.relative_to(root.resolve())


def find_figures(directory: Path) -> list[Path]:
    paths = []
    for path in directory.rglob("*"):
        if (
            path.suffix.lower() in ALLOWED_EXTENSIONS
            and not EXCLUDE.intersection(path.parts)
        ):
            paths.append(path.resolve())
    return paths


def check_figures(root: Path = ROOT, console: Console | None = None) -> int:
    console = console or Console()
    figure_files = find_figures(root)
    figure_ref_count = {path: 0 for path in figure_files}
    error_count = 0

    # Loop over all .qmd files and count references to each figure
    console.rule("Figure reference errors")
    console.print(
        "Referenced figures with unsupported formats or missing files will cause "
        "compilation errors in Quarto documents."
    )
    for qmd_file in root.rglob("*.qmd"):
        qmd_document = QMDDocument(qmd_file)
        for figure_path in qmd_document.find_figures():
            figure_path = figure_path.resolve()
            if figure_path.suffix.lower() not in ALLOWED_EXTENSIONS:
                console.print(
                    f"Error: Figure {relative_to_root(figure_path, root)} referenced in "
                    f"{relative_to_root(qmd_file.resolve(), root)} uses unsupported "
                    f"file format '{figure_path.suffix or '<none>'}'.",
                    style="bold red",
                )
                error_count += 1
                continue

            if figure_path in figure_ref_count:
                figure_ref_count[figure_path] += 1
            else:
                console.print(
                    f"Error: Figure {relative_to_root(figure_path, root)} referenced in "
                    f"{relative_to_root(qmd_file.resolve(), root)} not found in figure files.",
                    style="bold red",
                )
                error_count += 1

    # Print the results
    console.rule("Figures not referenced in any Quarto documents:")
    console.print("These are figures that exist in the project but are not used in any Quarto documents.")
    for figure_path, count in figure_ref_count.items():
        if count == 0:
            if "OBSOLETE" in figure_path.stem:
                continue

            # Check if its referenced wtih another extension:
            for ext in sorted(ALLOWED_EXTENSIONS):
                alt_figure_path = figure_path.with_suffix(ext)
                if (
                    alt_figure_path in figure_ref_count
                    and figure_ref_count[alt_figure_path] > 0
                ):
                    console.print(
                        f"Figure {relative_to_root(figure_path, root)} is not "
                        f"referenced, but {relative_to_root(alt_figure_path, root)} "
                        "is referenced.",
                        style="bold yellow",
                    )
                    break
            else:
                console.print(
                    f"Figure {relative_to_root(figure_path, root)} is not referenced "
                    "in any .qmd file.",
                    style="bold yellow",
                )

    return 1 if error_count else 0


def main() -> None:
    raise SystemExit(check_figures())

if __name__ == "__main__":
    main()
