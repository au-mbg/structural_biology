import os
import shutil
import subprocess
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.highlighter import Highlighter

import tempfile


class ErrorHighlighter(Highlighter):
    def check(self, text: Text) -> bool:
        if "Error" in text.plain:
            return True
        if "Traceback" in text.plain:
            return True
        return False

    def highlight(self, text: Text) -> None:
        # Highlight lines that contain "Error" in red.
        character_index = 0
        for line in text.split():
            if self.check(line):
                text.stylize("bold red", character_index, character_index + len(line))
            character_index += len(line) + 1  # +1 for the newline character


def find_pymol_executable() -> str | None:
    # Allow users/collaborators to override executable path explicitly.
    env_bin = os.environ.get("PYMOL_BIN")
    if env_bin:
        return env_bin

    on_path = shutil.which("pymol")
    if on_path:
        return on_path

    mac_app_bin = "/Applications/PyMOL.app/Contents/MacOS/PyMOL"
    if Path(mac_app_bin).is_file():
        return mac_app_bin

    return None


def find_scripts(
    file: str | None = None,
    directory: str | None = None,
    skip_pse: bool = False,
) -> list[Path]:
    if file:
        return [Path(file)]

    script_dir = Path(directory) if directory else Path(".")
    scripts = list(sorted(script_dir.rglob("*.pml")))
    if not skip_pse:
        scripts.extend(sorted(script_dir.rglob("*.pse")))
    return scripts


def check_script(pymol_bin: str, script_path: Path, console: Console) -> bool:
    try:
        with console.status(f"Checking {script_path.name}...", spinner="dots"):
            with tempfile.TemporaryDirectory() as tmp:
                # Symlink every sibling file into the temp dir
                for f in script_path.parent.iterdir():
                    os.symlink(f.resolve(), Path(tmp) / f.name)

                output = subprocess.run(
                    [pymol_bin, "-cqk", str(script_path)],
                    check=True,
                    capture_output=True,
                    text=True,
                    cwd=tmp,
                )

        if "Error" in output.stdout:
            panel = Panel(
                ErrorHighlighter()("\n".join(output.stdout.splitlines())),
                title=f"Syntax Errors in {script_path.name}",
            )
            console.print(panel)
            return False

        console.print(f"Script '{script_path.name}' is valid.", style="bold green")
        return True
    except subprocess.CalledProcessError as e:
        console.print(
            f"Script '{script_path.name}' has syntax errors:\n{e.stderr}",
            style="bold red",
        )
        return False


def main(args):
    console = Console()

    pymol_bin = find_pymol_executable()
    if pymol_bin is None:
        console.print("Could not find PyMOL executable.", style="bold red")
        console.print(
            "Install PyMOL or set PYMOL_BIN to the full executable path.",
            style="bold red",
        )
        raise SystemExit(1)

    console.print("Checking PyMOL scripts for syntax errors...", style="bold green")
    console.print(
        "Checking: {}".format(
            args.file
            if args.file
            else (args.directory if args.directory else "current directory")
        ),
        style="bold green",
    )
    console.print(f"Using PyMOL executable: {pymol_bin}", style="bold green")

    scripts = find_scripts(args.file, args.directory, args.skip_pse)

    if not scripts:
        script_dir = Path(args.directory) if args.directory else Path(".")
        extensions = ".pml" if args.skip_pse else ".pml or .pse"
        console.print(
            f"No {extensions} files found in: {script_dir}", style="bold yellow"
        )
        return

    scripts = [s.resolve() for s in scripts]
    failed_scripts = []
    for script in scripts:
        if not check_script(pymol_bin, script, console):
            failed_scripts.append(script)

    console.print(
        f"Checked {len(scripts)} scripts, {len(failed_scripts)} failed.",
        style="bold green",
    )
    if failed_scripts:
        console.print("Failed scripts:", style="bold red")
        for script in failed_scripts:
            console.print(f"\t{script}", style="bold red")

    if failed_scripts:
        raise SystemExit(1)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Check PyMOL scripts for syntax errors."
    )
    parser.add_argument(
        "--directory",
        "-d",
        type=str,
        default=None,
        help="Directory to search for .pml files (default: current directory)",
    )
    parser.add_argument(
        "--file",
        "-f",
        type=str,
        help="Specific .pml file to check (overrides --directory)",
        default=None,
    )
    parser.add_argument(
        "--skip-pse",
        action="store_true",
        help="Skip .pse session files during directory searches.",
    )
    args = parser.parse_args()

    main(args)
