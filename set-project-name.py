#!/usr/bin/env python3

# Quick and dirty script for quickly changing project name from the terminal

import re, sys
from pathlib import Path

target = Path('./project.godot')
template_name_line = re.compile("config/name=\"(.*)\"")
text = open(target).read()
result = template_name_line.search(text)

start: str = text[:result.start(1)]
end: str = text[result.end(1):]
current_name: str = result.group(1)
new_name: str = None

print(f'Original project name: {current_name}')
if len(sys.argv) > 1:
    new_name = sys.argv[1]
else:
    print(f'To change: {sys.argv[0]} [new project name]')
    exit(1)

if current_name == new_name:
    print(f'Names are identical. Change skipped.')
    exit(0)

open(target, 'w').write(start + new_name + end)

print(f'Project name has now been changed to {new_name}')
