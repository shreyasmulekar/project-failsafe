import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'(?:16|15|stage|Stage)', text):
    start = max(0, m.start() - 30)
    end = min(len(text), m.end() + 30)
    snippet = text[start:end].replace('\n', ' ')
    if any(k in snippet for k in ['/ 16', '/ 15', 'Stage 16', 'Stage 15', 'max="16"', 'max="15"']):
        print(snippet)
