from __future__ import annotations

from dataclasses import dataclass
import subprocess
from pathlib import Path

ROOT = Path("course_notes/_site/instructor/exercises/").resolve()


@dataclass()
class ProtectedPage:
    source: Path | str
    password: str
    output: Path | str | None = None
    overwrite: bool = False

    def __post_init__(self):
        self.source = Path(self.source).resolve()
        if not self.source.is_file():
            raise ValueError(
                f"Source file {self.source} does not exist or is not a file."
            )

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
        "false",
    ]

    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    MASTER_PASSWORD = "struktur2026"

    PAGES = [
        ProtectedPage(
            source=ROOT / "te_01_i_gang_med_pymol.qmd",
            password=MASTER_PASSWORD,
            overwrite=True,
        ),
        ProtectedPage(
            source=ROOT / "te_02_introduktion_til_tø.qmd",
            password=MASTER_PASSWORD,
            overwrite=True,
        ),
        ProtectedPage(
            source=ROOT / "te_03_pymol_scripting.qmd",
            password=MASTER_PASSWORD,
            overwrite=True,
        ),
        ProtectedPage(
            source=ROOT / "te_04_proteinstruktur_1.qmd",
            password=MASTER_PASSWORD,
            overwrite=True,
        ),
        ProtectedPage(
            source=ROOT / "te_05_proteinstruktur_2.qmd",
            password=MASTER_PASSWORD,
            overwrite=True,
        ),
        ProtectedPage(
            source=ROOT / "te_06_nukleinsyrestruktur_1.qmd",
            password=MASTER_PASSWORD,
            overwrite=True,
        ),
        ProtectedPage(
            source=ROOT / "te_07_nukleinsyrestruktur_2.qmd",
            password=MASTER_PASSWORD,
            overwrite=True,
        ),
        ProtectedPage(
            source=ROOT / "te_08_evolution_og_bioinformatik.qmd",
            password=MASTER_PASSWORD,
            overwrite=True,
        ),
        ProtectedPage(
            source=ROOT / "te_09_lø_forberedelse_1.qmd",
            password=MASTER_PASSWORD,
            overwrite=True,
        ),
        ProtectedPage(
            source=ROOT / "te_10_lø_forberedelse_2.qmd",
            password=MASTER_PASSWORD,
            overwrite=True,
        ),
        ProtectedPage(
            source=ROOT / "te_11_binding_og_genkendelse.qmd",
            password=MASTER_PASSWORD,
            overwrite=True,
        ),
        ProtectedPage(
            source=ROOT / "te_12_enzymmekanismer.qmd",
            password=MASTER_PASSWORD,
            overwrite=True,
        ),
        ProtectedPage(
            source=ROOT / "te_13_enzymregulering.qmd",
            password=MASTER_PASSWORD,
            overwrite=True,
        ),
        ProtectedPage(
            source=ROOT / "te_14_strukturmetoder.qmd",
            password=MASTER_PASSWORD,
            overwrite=True,
        ),
        ProtectedPage(
            source=ROOT / "te_15_ai_og_modellering.qmd",
            password=MASTER_PASSWORD,
            overwrite=True,
        ),
        ProtectedPage(
            source=ROOT / "te_16_kulhydrater_og_glykosylering_af_proteiner.qmd",
            password=MASTER_PASSWORD,
            overwrite=True,
        ),
        ProtectedPage(
            source=ROOT / "te_17_lipider_og_cellemembraner.qmd",
            password=MASTER_PASSWORD,
            overwrite=True,
        ),
        ProtectedPage(
            source=ROOT / "te_18_membranpumper.qmd",
            password=MASTER_PASSWORD,
            overwrite=True,
        ),
        ProtectedPage(
            source=ROOT / "te_19_kanaler_og_porer.qmd",
            password=MASTER_PASSWORD,
            overwrite=True,
        ),
        ProtectedPage(
            source=ROOT / "te_20_signaltransduktion.qmd",
            password=MASTER_PASSWORD,
            overwrite=True,
        ),
        ProtectedPage(
            source=ROOT / "te_21_eksamensopgaver.qmd",
            password=MASTER_PASSWORD,
            overwrite=True,
        ),
        ProtectedPage(
            source=ROOT / "te_22_eksamensopgaver.qmd",
            password=MASTER_PASSWORD,
            overwrite=True,
        ),
        ProtectedPage(
            source=ROOT / "te_23_eksamensopgaver.qmd",
            password=MASTER_PASSWORD,
            overwrite=True,
        ),
        ProtectedPage(
            source=ROOT / "te_24_eksamensopgaver.qmd",
            password=MASTER_PASSWORD,
            overwrite=True,
        ),
    ]

    for page in PAGES:
        encrypt_file(page)
