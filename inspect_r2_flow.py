import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("Searching for round 2 occurrences in aditi_os_widget.html...")

for m in re.finditer(r'(?:current_round\s*===?\s*2|initRound2|renderRound2|round2_stage|ROUND2_STAGES)', text):
    start = max(0, m.start() - 100)
    end = min(len(text), m.end() + 250)
    print("Match:", m.group(0))
    print(text[start:end])
    print("-" * 60)
