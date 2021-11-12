#!/usr/bin/env python3

# Quick and dirty script for quickly changing project name from the terminal

import re, sys
from pathlib import Path

def pexit(string: str, code: int):
    print(string)
    exit(code)

target: Path = Path('./project.godot')
template_name_line: re.Pattern = re.compile("config/name=\"(.*)\"")
text: str = open(target).read()
result = template_name_line.search(text)

if result is None:
    pexit(f'Incorrect file format in: {target}', 1)
    
start: str = text[:result.start(1)]
end: str = text[result.end(1):]
current_name: str = result.group(1)
new_name: str = ''

print(f'Original project name: {current_name}')
if len(sys.argv) > 1:
    new_name = sys.argv[1]
else:
    pexit(f'To change: {sys.argv[0]} [new project name]', 1)

if current_name == new_name:
    pexit(f'Names are identical. Change skipped.', 0)

open(target, 'w').write(start + new_name + end)

pexit(f'Project name has now been changed to {new_name}', 0)
