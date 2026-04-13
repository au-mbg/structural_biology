from __future__ import annotations

from dataclasses import dataclass
import subprocess
from pathlib import Path

ROOT = Path("course_notes/_site/instructor/").resolve()

@dataclass()
class ProtectedPage:
    source: Path | str
    password: str
    output: Path | str | None = None
    overwrite: bool = False

    def __post_init__(self):
        self.source = Path(self.source).resolve()
        if not self.source.is_file():
            raise ValueError(f"Source file {self.source} does not exist or is not a file.")

        if self.output is None and not self.overwrite:
            raise ValueError("Output path must be specified if overwrite is False.")
        elif self.output is None and self.overwrite:
            self.output = self.source
        else:
            self.output = Path(self.output).resolve()

def encrypt_file(page: ProtectedPage) -> None:
    cmd = [
        "npx",
        "--no-install",
        "staticrypt",
        page.source.as_posix(),
        "-p",
        page.password,
        "-o",
        page.output.as_posix(),
        "-d",
        page.output.parent.as_posix(),
        "--short",
        "--config",
        "false"
    ]

    subprocess.run(cmd, check=True)

if __name__ == "__main__":

    PAGES = [
        ProtectedPage(source=ROOT / "exercises/te_01_i_gang_med_pymol.html", password="password1", overwrite=True),
        ProtectedPage(source=ROOT / "exercises/te_02_introduktion_til_tø.html", password="password2", overwrite=True),
        ProtectedPage(source=ROOT / "exercises/te_03_pymol_scripting.html", password="password3", overwrite=True),
        ProtectedPage(source=ROOT / "exercises/te_04_proteinstruktur_1.html", password="password4", overwrite=True),
        ProtectedPage(source=ROOT / "exercises/te_05_proteinstruktur_2.html", password="password5", overwrite=True),

    ]

    for page in PAGES:
        encrypt_file(page)


