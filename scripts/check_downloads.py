from helpers import QMDDocument, ROOT
from rich.console import Console

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


if __name__ == "__main__":
    main()