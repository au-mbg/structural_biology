from pathlib import Path

try:
    from .helpers import QMDDocument, ROOT
except ImportError:
    from helpers import QMDDocument, ROOT
from rich.console import Console


def all_downloadable_files(root: Path = ROOT) -> list[Path]:
    paths = (root / "files").glob("*")
    return list(paths)


def check_downloads(root: Path = ROOT, console: Console | None = None) -> int:
    console = console or Console()

    total_downloads = 0
    valid_downloads = []
    error_count = 0

    for qmd_file in root.rglob("*.qmd"):
        qmd_document = QMDDocument(qmd_file)
        downloads = qmd_document.find_downloads()

        for download in downloads:
            total_downloads += 1
            if not download.exists():
                console.print(
                    f"Download link {download} in {qmd_file} does not exist.",
                    style="bold red",
                )
                error_count += 1
            else:
                valid_downloads.append(download)

    console.print(
        f"Found {len(valid_downloads)} valid download links out of "
        f"{total_downloads} total download links.",
        style="bold green",
    )

    # Check for any files in the downloads folder that are not linked in any qmd file
    all_files = set(all_downloadable_files(root))
    linked_files = set(valid_downloads)
    unlinked_files = all_files - linked_files
    if unlinked_files:
        console.print(
            f"Found {len(unlinked_files)} unlinked files in the downloads folder:",
            style="bold yellow",
        )
        for file in sorted(unlinked_files):
            console.print(f"- {file}", style="yellow")
    else:
        console.print(
            "All files in the downloads folder are linked in a qmd file.",
            style="bold green",
        )

    return 1 if error_count else 0


def main() -> None:
    raise SystemExit(check_downloads())


if __name__ == "__main__":
    main()
