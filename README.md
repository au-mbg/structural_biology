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

- `pixi run preview exercise`: Opens a live preview of the student facing version of the site.
- `pixi run preview solution`: Opens a live preview of the public instructor/solution version of the site.
- `pixi run render exercise`: Renders only the student-facing version (also the default for `pixi run render`).
- `pixi run render solution`: Renders only the public solution version using its own release calendar.
- `pixi run render-all`: Renders both public site versions (not live).
- `pixi run clean`: Cleans up any site artifacts. 

Direct `quarto render` from `course_notes/` is also a supported student-default
render. Use the Pixi commands for previews and solution builds: they safely select
the appropriate calendar and restore the student calendar even if Quarto fails.
`pixi run preview` shows drafts deliberately, so release behaviour must be checked
with a render and the generated `_site` directory. Direct `quarto preview` is not
supported because it bypasses the preview-mode safeguards in the Pixi wrapper.

### Manual installation

If instead opting to not use `pixi` this requires installing 

- `quarto`: See [Quarto Get Started](https://quarto.org/docs/get-started/)
- A Python 3.12 environment with appropriate packages.

This installation path is not recommended unless you're comfortable tinkering a bit. 

## Publishing 

The site is automatically rendered and published when commits are pushed to the `main`-branch 
of the repository. It can also be started manually and is rebuilt daily at 03:17
UTC so scheduled material can become visible without a new commit. GitHub may
start scheduled workflows later than their nominal time.

This is configured through Github Actions, see [publish.yml](.github/workflows/publish.yml).

### Scheduled exercise releases

The course uses the unmodified `scheduled-docs` extension. The editable release
calendars are:

- `course_notes/_schedule.yml` for student exercises.
- `course_notes/_schedule-solution.yml` for the public solution profile.

Dates use ISO `YYYY-MM-DD` notation and UTC. In the provisional 2026 calendar,
each pair of exercises is released to students one week before its course-plan
week and in the solution profile one week afterward. Edit the dates in both files
when the authoritative timetable is known. A page can be forced on or off by
adding `draft: false` or `draft: true` to its calendar entry.

The extension controls pages and generated HTML/PDF/Word documents. The homepage
is an always-visible overview with plain-text exercise titles; links to released
exercises appear in the sidebar. Files under `course_notes/files/` remain public,
as does the linked `/instructor/` site; profiles and schedules are content
separation, not access control.

For reproducible date testing, temporarily replace `draft-after: "system-time"`
with an ISO date in the relevant calendar, run the corresponding Pixi render,
inspect `_site`, and restore `system-time` before committing.

## Authoring

For authoring instructions see [AUTHORING.md](AUTHORING.md)
