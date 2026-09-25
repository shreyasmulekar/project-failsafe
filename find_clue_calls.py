import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'requestTacticalClue', text)]
print(f"Total occurrences of requestTacticalClue: {len(matches)}")
for idx in matches:
    start = max(0, idx - 150)
    end = min(len(text), idx + 250)
    print("--- OCCURRENCE ---")
    print(text[start:end])
    print()
