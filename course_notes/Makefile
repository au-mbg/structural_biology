.PHONY: all exercise solution clean preview-exercise preview-solution

# exercise → _site/  (student-facing, no solutions)
# solution → _site/instructor/  (instructor-facing, with solutions)

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
