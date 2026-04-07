import os
import shutil
import subprocess
from pathlib import Path

from rich.console import Console
from rich.panel import Panel

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


def check_script(pymol_bin: str, script_path: Path, console: Console) -> bool:
    try:
        output = subprocess.run([pymol_bin, "-c", str(script_path)], check=True, capture_output=True, text=True)

        if "Error" in output.stdout:
            panel = Panel(output.stdout, title=f"Syntax Errors in {script_path.name}", style="bold red")
            console.print(panel)

            # console.print(f"Script '{script_path.name}' has syntax errors", style="bold red")
            # for line in output.stdout.splitlines():
            #     console.print(f"\t{line}", style="bold red")
            return False

        console.print(f"Script '{script_path.name}' is valid.", style="bold green")
        return True
    except subprocess.CalledProcessError as e:
        console.print(f"Script '{script_path.name}' has syntax errors:\n{e.stderr}", style="bold red")
        return False


def main(args):
    console = Console()

    pymol_bin = find_pymol_executable()
    if pymol_bin is None:
        console.print("Could not find PyMOL executable.", style="bold red")
        console.print("Install PyMOL or set PYMOL_BIN to the full executable path.", style="bold red")
        raise SystemExit(1)

    console.print(f"Using PyMOL executable: {pymol_bin}", style="bold green")

    if args.file:
        scripts = [Path(args.file)]
    else:
        script_dir = Path(args.directory) if args.directory else Path(".")
        scripts = list(sorted(script_dir.glob("*.pml"))) + list(sorted(script_dir.glob("*.pse")))

    if not scripts:
        console.print(f"No .pml or .pse files found in: {script_dir}", style="bold yellow")
        return
    
    scripts = [s.resolve() for s in scripts]
    
    # Go to a temporary directory to avoid any side effects from running the scripts.
    with subprocess.Popen(["mktemp", "-d"], stdout=subprocess.PIPE, text=True) as proc:
        temp_dir = proc.stdout.read().strip()
    os.chdir(temp_dir)

    failed_scripts = []
    for script in scripts:
        if not check_script(pymol_bin, script, console):
            failed_scripts.append(script)

    console.print(f"Checked {len(scripts)} scripts, {len(failed_scripts)} failed.", style="bold green")
    if failed_scripts:
        console.print("Failed scripts:", style="bold red")
        for script in failed_scripts:
            console.print(f"\t{script}", style="bold red")


    if failed_scripts:
        raise SystemExit(1)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Check PyMOL scripts for syntax errors.")
    parser.add_argument("--directory", "-d", type=str, default=None, help="Directory to search for .pml files (default: current directory)")
    parser.add_argument("--file", "-f", type=str, help="Specific .pml file to check (overrides --directory)", default=None)
    args = parser.parse_args()

    main(args)