import os
import shutil
import subprocess
from pathlib import Path


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


def check_script(pymol_bin: str, script_path: Path) -> bool:
    try:
        output = subprocess.run([pymol_bin, "-c", str(script_path)], check=True, capture_output=True, text=True)

        if "Error" in output.stdout:
            print(f"Script '{script_path.name}' has syntax errors")
            for line in output.stdout.splitlines():
                print(f"\t{line}")
            return False

        print(f"Script '{script_path.name}' is valid.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Script '{script_path.name}' has syntax errors:\n{e.stderr}")
        return False


def main(args):
    pymol_bin = find_pymol_executable()
    if pymol_bin is None:
        print("Could not find PyMOL executable.")
        print("Install PyMOL or set PYMOL_BIN to the full executable path.")
        raise SystemExit(1)

    print(f"Using PyMOL executable: {pymol_bin}")

    if args.file:
        scripts = [Path(args.file)]
    else:
        script_dir = Path(args.directory) if args.directory else Path(".")
        scripts = list(sorted(script_dir.glob("*.pml"))) + list(sorted(script_dir.glob("*.pse")))

    if not scripts:
        print(f"No .pml or .pse files found in: {script_dir}")
        return
    
    scripts = [s.resolve() for s in scripts]
    
    # Go to a temporary directory to avoid any side effects from running the scripts.
    with subprocess.Popen(["mktemp", "-d"], stdout=subprocess.PIPE, text=True) as proc:
        temp_dir = proc.stdout.read().strip()
    os.chdir(temp_dir)

    failed_scripts = []
    for script in scripts:
        if not check_script(pymol_bin, script):
            failed_scripts.append(script)

    print(f"Checked {len(scripts)} scripts, {len(failed_scripts)} failed.")
    if failed_scripts:
        print("Failed scripts:")
        for script in failed_scripts:
            print(f"\t{script}")


    if failed_scripts:
        raise SystemExit(1)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Check PyMOL scripts for syntax errors.")
    parser.add_argument("--directory", "-d", type=str, default=None, help="Directory to search for .pml files (default: current directory)")
    parser.add_argument("--file", "-f", type=str, help="Specific .pml file to check (overrides --directory)", default=None)
    args = parser.parse_args()

    main(args)