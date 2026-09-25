import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = list(re.finditer(r'(?:round_2_is_finished|stage_times|finish|completed|is_finished)', text, re.IGNORECASE))
print("Admin matches:", len(matches))
seen = set()
for m in matches:
    start = max(0, m.start() - 30)
    end = min(len(text), m.end() + 30)
    snippet = text[start:end].replace('\n', ' ')
    if snippet not in seen:
        seen.add(snippet)
        if len(seen) <= 12:
            print("  ", snippet)
