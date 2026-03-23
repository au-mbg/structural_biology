# Strukturbiologi

Repository for course notes for *Strukturbiologi* at the Department of Molecular Biology & Genetics at Aarhus University. 

## Installation

The site is build using [Quarto](https://quarto.org/) a Markdown-based publishing system. 
The simplest installation is using `pixi`. 

### Pixi

Pixi is a package manager that can install all the required programs to render the site. 

The first step is to install `pixi` this can be installed on **MacOS** and **Linux** with 
the command

```bash
curl -fsSL https://pixi.sh/install.sh | sh
```

On **Windows** it can be installed either through the installer available from the [`pixi` website](https://pixi.prefix.dev/latest/installation/#__tabbed_1_2) or with the command 

```
powershell -ExecutionPolicy Bypass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```

#### Using Pixi 

With `pixi` installed the site can be rendered or previewed using the commands 

- `pixi run preview-exercise`: Opens a live preview of the student facing version of the site.
- `pixi run preview-solution`: Opens a live preview of the instructor facing version of the site.
- `pixi run render`: Renders the entire site (not live).
- `pixi run clean`: Cleans up any site artifacts. 

### Manual installation

If instead opting to not use `pixi` this requires installing 

- `quarto`: See [Quarto Get Started](https://quarto.org/docs/get-started/)
- A Python 3.12 environment with appropriate packages.

This installation path is not recommended. 






