import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Search for stage count references in round 1
for m in re.finditer(r'(?:/ 16|/ 15|/ 12|16 CLEARED|15 CLEARED|totalStages|TOTAL_STAGES)', text):
    start = max(0, m.start() - 60)
    end = min(len(text), m.end() + 60)
    print("Match:", m.group(0), "at char", m.start())
    print(text[start:end])
    print("-" * 50)
