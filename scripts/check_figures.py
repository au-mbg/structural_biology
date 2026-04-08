from pathlib import Path
from helpers import QMDDocument, ROOT
from rich.console import Console

EXTENSIONS = [".png", ".jpg", ".jpeg", ".svg"]
EXCLUDE = ['_site', '.quarto']

def relative_to_root(path: Path) -> Path:
    return path.relative_to(ROOT.resolve())

def find_figures(directory: Path) -> list[Path]:
    paths = []
    for path in directory.rglob("*"):
        if path.suffix in EXTENSIONS and not any(exclude in path.parts for exclude in EXCLUDE):
            paths.append(path.resolve())
    return paths

def main():    
    console = Console()

    figure_files = find_figures(ROOT)
    figure_ref_count = {path: 0 for path in figure_files}

    # Loop over all .qmd files and count references to each figure
    for qmd_file in ROOT.rglob("*.qmd"):
        qmd_document = QMDDocument(qmd_file)
        for figure_path in qmd_document.find_figures():
            if figure_path in figure_ref_count:
                figure_ref_count[figure_path] += 1
            else:
                console.print(f"Warning: Figure {relative_to_root(figure_path)} referenced in {relative_to_root(qmd_file.resolve())} not found in figure files.", style="bold yellow")

    # Print the results
    for figure_path, count in figure_ref_count.items():
        if count == 0:
            if "OBSOLETE" in figure_path.stem:
                continue

            # Check if its referenced wtih another extension:
            for ext in EXTENSIONS:
                alt_figure_path = figure_path.with_suffix(ext)
                if alt_figure_path in figure_ref_count and figure_ref_count[alt_figure_path] > 0:
                    console.print(f"Figure {relative_to_root(figure_path)} is not referenced, but {relative_to_root(alt_figure_path)} is referenced.", style="bold yellow")
                    break
            else:                
                console.print(f"Figure {relative_to_root(figure_path)} is not referenced in any .qmd file.", style="bold red")

if __name__ == "__main__":
    main()