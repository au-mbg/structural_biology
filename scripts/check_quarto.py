from helpers import ROOT
from rich.console import Console
import yaml

def find_all_qmd(config):
    references_files = []

    def find_qmd_files(config):
        if isinstance(config, dict):
            for key, value in config.items():
                if key == "href" and isinstance(value, str) and value.endswith(".qmd"):
                    references_files.append(ROOT / value)
                else:
                    find_qmd_files(value)
        elif isinstance(config, list):
            for item in config:
                find_qmd_files(item)
        elif isinstance(config, str) and config.endswith(".qmd"):
            references_files.append(ROOT / config)

    find_qmd_files(config)
    return references_files

def main():
    console = Console()
    console.print(f"Root directory is: {ROOT}")

    # Find all .qmd files referenced in the website configuration
    with open(ROOT / "config" / "quarto" / "website.yml") as f:
        website_config = yaml.safe_load(f)
    references_files = find_all_qmd(website_config)

    # Find all .qmd files in the project directory
    all_qmd_files = list(ROOT.glob("**/*.qmd"))

    # Compare referenced .qmd files with all .qmd files in the project
    missing_files = [f for f in references_files if f not in all_qmd_files]

    for f in missing_files:
        console.print(f"Missing referenced .qmd file: {f}")

    if not missing_files:
        console.print("All referenced .qmd files are present.")

    # Report any .qmd files in the project that are not referenced in the website configuration
    unreferenced_files = [f for f in all_qmd_files if f not in references_files]
    for f in unreferenced_files:
        console.print(f"Unreferenced .qmd file: {f}")
    if not unreferenced_files:
        console.print("All .qmd files in the project are referenced.")


if __name__ == "__main__":
    main()