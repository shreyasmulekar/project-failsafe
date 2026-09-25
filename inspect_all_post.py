import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('server.py', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'def do_POST\s*\(', text)
if m:
    start = m.start()
    lines = text[start:].splitlines()
    for i, l in enumerate(lines):
        if 'if path' in l or 'elif path' in l:
            print(f'{i}: {l.strip()}')
        if 'def do_' in l and i > 10:
            break
