import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('admin.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(''.join(lines[1740:1785]))
