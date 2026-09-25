import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('server.py', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'def do_POST\s*\(', text)
if m:
    start = m.start()
    lines = text[start:].splitlines()
    for l in lines[:100]:
        if 'if path' in l or 'elif path' in l or 'data =' in l:
            print(l)
