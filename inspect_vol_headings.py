import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('VOLUNTEER_PUZZLE_GUIDE.md', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'### Stage \d+.*|### Round 2.*|## Stage \d+.*', text)
for m in matches[:30]:
    print(m)
