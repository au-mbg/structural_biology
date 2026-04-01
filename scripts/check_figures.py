from pathlib import Path
import re

EXTENSIONS = [".png", ".jpg", ".jpeg", ".svg"]
EXCLUDE = ['_site']

ROOT = Path.cwd() / 'course_notes'

class QMDDocument:
    def __init__(self, path: Path):
        self.path = path
        self.content = path.read_text()

    def find_figures(self) -> list[Path]:
        pattern = r"!\[.*?\]\((.*?)\)"
        matches = re.findall(pattern, self.content)
        figure_paths = []
        for match in matches:
            figure_path = self.path.resolve().parent / match
            figure_paths.append(figure_path)
        return figure_paths


def relative_to_root(path: Path) -> Path:
    return path.relative_to(ROOT.resolve())

def find_figures(directory: Path) -> list[Path]:
    paths = []
    for path in directory.rglob("*"):
        if path.suffix in EXTENSIONS and not any(exclude in path.parts for exclude in EXCLUDE):
            paths.append(path.resolve())
    return paths

def main():    
    figure_files = find_figures(ROOT)
    figure_ref_count = {path: 0 for path in figure_files}

    # Loop over all .qmd files and count references to each figure
    for qmd_file in ROOT.rglob("*.qmd"):
        qmd_document = QMDDocument(qmd_file)
        for figure_path in qmd_document.find_figures():
            if figure_path in figure_ref_count:
                figure_ref_count[figure_path] += 1
            else:
                print(f"Warning: Figure {relative_to_root(figure_path)} referenced in {relative_to_root(qmd_file.resolve())} not found in figure files.")

    # Print the results
    for figure_path, count in figure_ref_count.items():
        if count == 0:

            # Check if its referenced wtih another extension:
            for ext in EXTENSIONS:
                alt_figure_path = figure_path.with_suffix(ext)
                if alt_figure_path in figure_ref_count and figure_ref_count[alt_figure_path] > 0:
                    print(f"Figure {relative_to_root(figure_path)} is not referenced, but {relative_to_root(alt_figure_path)} is referenced.")
                    break
            else:
                print(f"Figure {relative_to_root(figure_path)} is not referenced in any .qmd file.")





if __name__ == "__main__":
    main()