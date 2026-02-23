.PHONY: all exercise solution clean preview-exercise preview-solution

all: exercise solution

exercise:
	quarto render --profile exercise

solution:
	quarto render --profile solution

preview-exercise:
	quarto preview --profile exercise

preview-solution:
	quarto preview --profile solution

clean:
	rm -rf _site
