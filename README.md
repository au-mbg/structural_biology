# Strukturbiologi

Repository for course notes for *Strukturbiologi* at the Department of Molecular Biology & Genetics at Aarhus University. 

## Installation

The site is build using [Quarto](https://quarto.org/) a Markdown-based publishing system 
and uses `git` for version control with the remote repository hosted on Github.com.

### Git 

To work on the site locally you will need to clone the repository, you can do so 
for a HTTPS setup with

```
git clone https://github.com/au-mbg/structural_biology.git
```

or for SSH (requires setting up an [SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent), which can be a little tricky) with 
```
git clone https://github.com/au-mbg/structural_biology.git
```
This requires having `git` installed, if you do not then you can first install `pixi`
like described below and then use that to install git. 


### Pixi

Pixi is a package manager that can install all the required programs to render the site. 

The first step is to install `pixi` this can be installed on **MacOS** and **Linux** with 
the command

```bash
curl -fsSL https://pixi.sh/install.sh | sh
```

On **Windows** it can be installed either through the installer available from the [`pixi` website](https://pixi.prefix.dev/latest/installation/#__tabbed_1_2) or with the command 

```powershell
powershell -ExecutionPolicy Bypass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```

After the installation finishes you will need to open a new terminal for the `pixi`-command to 
be available.

### Installing `git` with `pixi`

If you do not have git installed, you can use `pixi` to install git, like so

```bash
pixi global install git
```

After this open a new terminal/shell and `git` will be available. 

Then the `git clone` commands listed above will work. 

### `git` authentication

To help with git setup you can run 

```
pixi run github-auth
```
This will ask a few questions and eventually open a browser to login to github. 
You will only need to do this once per machine. 

### Basic git operations 

Before making any updates it's a good idea to make sure you have the latest version

```bash
git pull
```

When you've made an update you can run 

```bash
git status
```
This will list all the files that have been changed, for example 

```
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   course_notes/exercises/te_01_i_gang_med_pymol.qmd

no changes added to commit (use "git add" and/or "git commit -a")
```

Then you add the files you want to commit 

```bash
git add course_notes/exercises/te_01_i_gang_med_pymol.qmd
```
Write a commit message

```bash
git commit -m "Update the exercises for the first TØ session."
```

And then push to the remote 

```bash
git push
```

For slightly more detailed instructions see [git - the simple guide](https://rogerdudler.github.io/git-guide/).

### Using `pixi` for site rendering

With `pixi` installed the site can be rendered or previewed using the commands 

- `pixi run preview-exercise`: Opens a live preview of the student facing version of the site.
- `pixi run preview-solution`: Opens a live preview of the instructor facing version of the site.
- `pixi run render`: Renders the entire site (not live).
- `pixi run clean`: Cleans up any site artifacts. 

### Manual installation

If instead opting to not use `pixi` this requires installing 

- `quarto`: See [Quarto Get Started](https://quarto.org/docs/get-started/)
- A Python 3.12 environment with appropriate packages.

This installation path is not recommended unless you're comfortable tinkering a bit. 

## Publishing 

The site is automatically rendered and published when commits are pushed to the `main`-branch 
of the repository. 

This is configured through Github Actions, see [publish.yml](.github/workflows/publish.yml).

## Authoring

For authoring instructions see [AUTHORING.md](AUTHORING.md)




