from pathlib import Path

from helpers import QMDDocument, ROOT
from rich.console import Console


def all_downloadable_files() -> list[Path]:
    paths = (ROOT / "files").glob("*")
    return list(paths)

def main():
    console = Console()

    total_downloads = 0
    valid_downloads = []

    for qmd_file in ROOT.rglob("*.qmd"):
        qmd_document = QMDDocument(qmd_file)
        downloads = qmd_document.find_downloads()


        for download in downloads:
            total_downloads += 1
            if not download.exists():
                console.print(f"Download link {download} in {qmd_file} does not exist.", style="bold red")
            else:
                valid_downloads.append(download)

    console.print(f"Found {len(valid_downloads)} valid download links out of {total_downloads} total download links.", style="bold green")

    ## Check for any files in the downloads folder that are not linked in any qmd file
    all_files = set(all_downloadable_files())
    linked_files = set(valid_downloads)
    unlinked_files = all_files - linked_files
    if unlinked_files:
        console.print(f"Found {len(unlinked_files)} unlinked files in the downloads folder:", style="bold yellow")
        for file in unlinked_files:
            console.print(f"- {file}", style="yellow")
    else:
        console.print("All files in the downloads folder are linked in a qmd file.", style="bold green")


if __name__ == "__main__":
    main()