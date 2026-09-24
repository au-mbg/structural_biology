# Authoring 

Content is written in Quarto flavoured markdown `.qmd`-files. The basic syntax 
is regular Markdown a guide for which can be found [here](https://quarto.org/docs/authoring/markdown-basics.html). 

These files are plain text, so what you see is exactly what the document contains, 
unlike `.pdf` or `.docx` which carry various metadata and the viewing experience is 
program and platform specific. Additionally, version control is much easier for 
raw text rather than more complex formats. 

The goal of this document is not to list every detail of Markdown, those are already 
listed in the guide linked above - but rather to describe a few extra features.

## Repository layout 

The site is generated from a number of documents, the layout looks like so

```
course_notes
├── config               # Most configuration lives here
│  ├── quarto
│  │  ├── styling        # CSS/SCSS for the website
│  │  └── website.yml    # Main Quarto website/navigation configuration
├── _extensions          # Quarto extensions (kept at the top level for Quarto)
├── _quarto-student.yml  # Scheduled student profile configuration
├── _quarto-author.yml   # Authoring settings that make drafts visible
├── _quarto-author-*.yml # Profile-specific preview output locations
├── _quarto-instructor.yml # Complete instructor profile with PDF/Word downloads
├── _quarto-publish.yml  # Publication settings and release cleanup
├── _quarto-solution.yml # Solution profile configuration
├── _quarto.yml          # Small Quarto entry point that loads config/quarto/website.yml
├── _preview             # Persistent local authoring preview
├── _site                # Publication output
├── exercises            # Directory with the exercise files
│  ├── index.qmd 
│  ├── media             # Contains figures
│  ├── te_01_....qmd     # An exercise .qmd file
│  ├── ...
├── exercises            # Directory with downloadable files
│  ├── file.pml
│  ├── ...
├── index.qmd            # Landing page 
├── other_notes          # Directory for guides/installation
│  ├── installation.qmd  # An installation guide .qmd file
│  ├── ...
├── videos               # Directory containing .qmd files for the videos
│  ├── videor.qmd        # Videos overview page
│  ├── videor_1.qmd      # For video 1
├── ...
```

Most contributors will only need to work in `exercises/`, `other_notes/`, `videos/`, or occasionally `index.qmd`. The files in `config/`, plus the `_quarto...` files, mainly control how the site is rendered.

## Previewing changes

Start the student-facing preview with:

```sh
pixi run preview student
```

Use `pixi run preview solution` for the scheduled public solutions and
`pixi run preview instructor` for all content and solutions. Instructor previews
are not password protected. Preview output is kept in `course_notes/_preview`,
so restarting a preview normally reuses the existing HTML. After
`pixi run clean`, use the corresponding `preview-rebuild` command. Publication
output is separate in `course_notes/_site`, and publishing does not remove the
preview cache.

Use `pixi run render student`, `pixi run render solution`,
`pixi run render instructor`, or `pixi run render-all` when checking release
builds. Student and solution renders hide scheduled drafts and remove unreleased
files. Instructor renders include everything and emit HTML, PDF, and Word files.
Only the HTML is encrypted later in the GitHub Actions publication workflow;
the PDF and Word downloads remain directly accessible.

## Student, solution, and instructor profiles

The project uses a set of *filters* in `_extensions` to control the visibility of solutions - specifically 
callout blocks which are specified with 

```
::: {.callout-solution}
Content...
:::
```

This content is hidden from the student profile and visible in both the solution
and instructor profiles. The public solution profile follows its release
calendar. The instructor profile always includes all pages and solutions; its
published HTML is processed by StatiCrypt in CI, while its PDF and Word files
remain directly downloadable. The source content remains in the same document,
making exercises and solutions easier to keep synchronized.

## Figures

Figures are included using 

```md
![Caption](path/to/figure.png)
```

Additionally [settings](https://quarto.org/docs/authoring/figures.html) are provided by Quarto, 
for example setting the width/height in pixels, inches or percentage of screen space

```md
![Caption](path/to/figure.png){width=300}
![Caption](path/to/figure.png){width=4in}
![Caption](path/to/figure.png){width=80%}

```

### Subfigures

Figures can be arranged using a figure div, 

```md
::: {#fig-elephants layout-ncol=2}

![Surus](surus.png){#fig-surus}

![Hanno](hanno.png){#fig-hanno}

Famous Elephants
:::
```

### Floating / Aligned figures

To wrap text around a floating figure it can be wrapped in float div, like below

```md
::: {style="float: right; margin: 10px; width: 28%;"}
![Ray Tracing settings](pymol_guide_1_media/media/image10.png)
:::
```

### Checking figure references 

Run all local project checks and display a combined pass/fail summary with:

```sh
pixi run check-all
```

The individual checks below remain available when working on a specific type of
content.

The command 

```sh
pixi run check-figures
```
Produces an overview of the figure references in the documents and highlights any 
broken links or unlinked figures. 

## Code 

Markdown supports both inline code and code blocks. Inline code is written using single-backticks ``` `code` ```

Code blocks are created using triple backticks

````
```
Some code
```
````

Additionally, Quarto markdown can highlight a number of languages, for code blocks this is done by specifying the language 

```` 
```python
def my_func(x):
    return x
```
````
Will be rendered with Python highlighting. The majority of code shown in these course notes are PyMOL which doesn't have 
a proper highligther, however it is still useful to write them using the default highlighter, like so 

````
```default
# MY first PyMOL script

reinitialize

fetch 1BL8
```
````

For larger pieces of code, e.g. in solutions it's beneficial to include them directly from a file as this makes it easier to ensure
that the code is valid 
````
```default 
{{< include pymol_scripts/script_te1_e2.pml >}}
```
````
Here the path is relative to the current file, so the above path works for all the `exercises/te_*.qmd` files. 

### PyMOL Scripts

The Python script `scripts/check_scripts.py` checks that all PyMOL scripts in a directory are syntactically correct. The project has PyMOL files in two places: 

- `course_notes/files`: For downloadable scripts/session files. 
- `course_notes/exercises/pymol_scripts`: For exercise solution scripts. 

To run the check on both directories use

```sh
pixi run check-pymol-scripts
```
The checker displays a spinner with the file currently being processed. The comprehensive
`check-all` task checks only `.pml` scripts so that slow saved `.pse` sessions do not block
the other project checks. When running `check_scripts.py` directly, pass `--skip-pse` to
apply the same PML-only behavior to a directory.

This requires having PyMOL installed and discoverable. For checking just a single script one 
can use 

```sh
pixi run check-script <script_path.pml>
```

## Callout blocks

Callout blocks are very useful as way to make some content distinguishable, for example for hints. 

A callout for a hint can be created like so 

```
::: {.callout-tip}
My hint explanation here....

This can include any other content, such as figures, math or code.

:::
```

## Downloadable files

Downloadable files should be put in the `course_notes/files`-directory and then linked to using a block like

{{< download-button path="../files/TE6-TALE.pml" filename="TALE.pml" >}}


Here the `path` is the relative path from the `.qmd` to the file. The `filename` specifies the file name of the downloaded file. 

You can check that downloadable files are correctly linked using the command 

```sh
pixi run check-downloads
```

## Different formats 

*Note: This is regards to converting existing files to markdown, not outputting different formats from the website*

`quarto` uses the very powerful `pandoc` for converting between file formats internally, but 
sometimes it can also be useful for helping with converting a file while authoring, for example 

```
pixi r pandoc word_document.docx -o markdown.md -t markdown 
```

Will convert a Word `.docx` document to an `.md`-markdown while trying to preserve as much 
styling as possible. `pandoc` has a variety of settings and features, for example it can media/images 

```
pixi r pandoc word_document.docx -o markdown.md -t markdown --extract-media=media/
```

For a full list of options see [the pandoc manual](https://pandoc.org/MANUAL.html).
