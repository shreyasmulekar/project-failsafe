import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('server.py', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'16|15|TOTAL_STAGES|len\(STAGES\)|range\(1,\s*1[0-9]\)', text):
    start = max(0, m.start() - 40)
    end = min(len(text), m.end() + 40)
    print(text[start:end])
    print("-" * 30)
