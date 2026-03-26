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
│  ├── editor
│  │  └── pymol.xml      # Optional editor syntax support for PyMOL
│  ├── quarto
│  │  ├── filters        # Controls what gets shown/hidden during rendering
│  │  ├── styling        # CSS/SCSS for the website
│  │  └── website.yml    # Main Quarto website/navigation configuration
│  └── tooling
│     └── Makefile       # Render/preview commands used by the root Makefile
├── _extensions          # Quarto extensions (kept at the top level for Quarto)
├── _quarto-exercise.yml # Exercise profile configuration
├── _quarto-solution.yml # Solution profile configuration
├── _quarto.yml          # Small Quarto entry point that loads config/quarto/website.yml
├── _site                # Rendered site / The product of a render/preview command
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

## Exercise vs. solution

The project uses a set of *filters* in `config/quarto/filters/` to control the visibility of solutions - specifically 
callout blocks which are specified with 

```
::: {.solution-callout}
Content...
:::
```

This content will only be visible when viewing the instructor/solution version of the site, 
but the content is contained in the same document as the exercise. This makes it much simpler to 
keep exercises and solutions up to date. 

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

The script Python script `course_notes/exercises/pymol_scripts/check_scripts.py` checks that all PyMOL scripts in the `course_notes/exercises/pymol_scripts/`-directory are syntactically correct. To run this you use 

```
pixi run check-pymol-scripts
```

This requires having PyMOL installed and discoverable.

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

```
<a href="../files/script_te4_e7.pml" download="Tu.pml">
  📥 Click to download script.
</a>
```

Here the `href`-path should is the relative path from the `.qmd` to the fil. The `download`-path specifies the file name of the downloaded file. 