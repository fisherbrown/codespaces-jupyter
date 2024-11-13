# Fisher Brown
# Lab Section: 10
# 12 Nov 24
# Jayden Robison

from pathlib import Path
path = Path('prompt.txt')
contents = path.read_text()
lines = contents.splitlines()
way = Path('out.txt')
all_content = ''
for line in lines:
  to_write = ''
  row = line.split('\t')
  for i in row:
    if 'w' in i:
      mult = i.split('w:')
      to_write += int(mult[1])*' '
    elif '*' in i:
      mult = i.split('*:')
      to_write += int(mult[1])*'*'
  to_write += '\n'
  all_content += to_write
way.write_text(all_content)