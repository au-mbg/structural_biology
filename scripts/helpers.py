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
    
    def find_downloads(self) -> list[str]:
        pattern = r'{{<\s*download-button\s+path="(.*?)"(?:\s+filename=".*?")?\s*>}}'
        matches = re.findall(pattern, self.content)
        download_paths = []
        for match in matches:
            print(match)
            download_path = (self.path.resolve().parent / match).resolve()
            download_paths.append(download_path)
        return download_paths

