from pathlib import Path
import re
from dataclasses import dataclass

@dataclass
class CodeBlock:
    index_start: int
    index_end: int
    div_class: str = None


def find_code_blocks(lines):
    code_blocks = []
    in_code_block = False
    
    for i, line in enumerate(lines):

        if re.match(r'```', line) and not in_code_block:
            in_code_block = True
            index_start = i
        elif line.strip() == '```' and in_code_block:
            in_code_block = False
            index_end = i
            code_blocks.append(CodeBlock(index_start=index_start, index_end=index_end, div_class=lines[index_start]))
    
    return code_blocks


def find_files():
    directories = ['exercises', 'other_notes', 'videos']
    paths = []
    for directory in directories:
        path = Path(f'../../{directory}/').glob('*.qmd')
        paths.extend(list(path))
    return paths

def read_qmd(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

def write_qmd(filename, lines):
    with open(filename, 'w') as f:
        f.writelines(lines)

def replace_div(lines, code_block):
    if code_block.div_class not in [r'```python', r'```default', r'```{python}']:
        lines[code_block.index_start] = '```default\n'

def main():
    paths = find_files()
    for path in paths:
        lines = read_qmd(path)
        code_blocks = find_code_blocks(lines)
        print(f"File: {path}")
        for block in code_blocks:
            replace_div(lines, block)
        write_qmd(path, lines)



if __name__ == "__main__":
    main()
