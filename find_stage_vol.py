import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('VOLUNTEER_PUZZLE_GUIDE.md', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'(?:#+.*Stage|Stage\s*0?1)', text, re.IGNORECASE):
    start = max(0, m.start() - 30)
    end = min(len(text), m.end() + 100)
    print(text[start:end])
    print("="*40)
    if start > 5000:
        break
