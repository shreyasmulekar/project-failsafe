import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('server.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

m_start = 0
for i, l in enumerate(lines):
    if 'def do_POST' in l:
        m_start = i
        break

for i in range(m_start + 1380, m_start + 1445):
    if i < len(lines):
        print(f'{i+1}: {lines[i]}', end='')
