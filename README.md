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

- `pixi run preview student`: Opens a live preview of the scheduled student version.
- `pixi run preview solution`: Opens a live preview of the scheduled public solution version.
- `pixi run preview instructor`: Opens the complete instructor version locally without password protection.
- `pixi run preview-rebuild student`: Rebuilds the student-facing HTML before opening its preview.
- `pixi run preview-rebuild solution`: Rebuilds the solution HTML before opening its preview.
- `pixi run preview-rebuild instructor`: Rebuilds the complete instructor HTML before opening its preview.
- `pixi run render student`: Renders only the student-facing version (also the default for `pixi run render`).
- `pixi run render solution`: Renders only the public solution version using its own release calendar.
- `pixi run render instructor`: Renders the complete, HTML-only instructor version without local encryption.
- `pixi run render-all`: Renders all three site versions (not live).
- `pixi run clean`: Removes publication and authoring-preview artifacts.

Direct publication commands are also supported. From the repository root, use
`quarto render course_notes --profile student,publish`,
`quarto render course_notes --profile solution,publish`, or
`quarto render course_notes --profile instructor,publish`; from `course_notes/`,
omit the project path. The scheduling extension selects the applicable calendar
or bypasses scheduling for the instructor profile.

`pixi run preview` combines the selected content profile with the `author`
profile and writes to a persistent authoring site under `course_notes/_preview`.
The student preview uses `_preview`, the solution preview uses
`_preview/solution`, and the instructor preview uses `_preview/instructor`.
They reuse existing output for fast startup. Run the corresponding
`preview-rebuild` command after cleaning or whenever the cached preview needs
to be refreshed. Publication renders write to `course_notes/_site` and do not
invalidate this authoring cache.

Release behaviour must be checked with a complete render and the generated
`_site` directory. The `publish` profile hides drafts and registers the final
cleanup of unreleased HTML, PDF, and Word outputs. Only complete project renders
perform that cleanup; the `author` profile must not be used for publication.
Scheduling and cleanup are disabled for the complete instructor profile.

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

The course uses `scheduled-docs-profiles` 1.1.0, an MIT-licensed derivative of
`qmd-lab/scheduled-docs` 0.6.0 maintained in
[`au-mbg/quarto-teaching-tools`](https://github.com/au-mbg/quarto-teaching-tools/tree/main/extensions/scheduled-docs-profiles).
The original extension was created by Andrew Bray; its license and attribution
are included with the vendored extension. The editable release calendars are:

- `course_notes/_schedule.yml` for student exercises.
- `course_notes/_schedule-solution.yml` for the public solution profile.

For each active profile the extension looks for `_schedule-<profile>.yml` and
falls back to `_schedule.yml`. Thus the student profile uses the base calendar,
the solution profile uses `_schedule-solution.yml`, and the instructor profile
bypasses calendars.

Dates use ISO `YYYY-MM-DD` notation and UTC. In the provisional 2026 calendar,
each pair of exercises is released to students one week before its course-plan
week and in the solution profile one week afterward. Edit the dates in both files
when the authoritative timetable is known. A page can be forced on or off by
adding `draft: false` or `draft: true` to its calendar entry.

The extension controls pages and generated HTML/PDF/Word documents. The homepage
is an always-visible overview with plain-text exercise titles; links to released
exercises appear in the sidebar. Files under `course_notes/files/` remain public,
and the scheduled solution site is published under `/solution/`. The complete
instructor site is published under `/instructor/`; GitHub Actions encrypts its
HTML with StatiCrypt, while local renders and previews remain unencrypted. The
instructor profile is HTML-only. Because the repository source is public, the
password prompt is a convenience gate rather than protection for confidential
source material.

For reproducible date testing, temporarily replace `draft-after: "system-time"`
with an ISO date in the relevant calendar, run the corresponding Pixi render,
inspect `_site`, and restore `system-time` before committing.

## Authoring

For authoring instructions see [AUTHORING.md](AUTHORING.md)
