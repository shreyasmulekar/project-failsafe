import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('server.py', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'/api/.*verify|/api/.*submit|stage_info\.get\(["\']keys["\']\)', text):
    start = max(0, m.start() - 50)
    end = min(len(text), m.end() + 300)
    print(text[start:end])
    print("="*50)
