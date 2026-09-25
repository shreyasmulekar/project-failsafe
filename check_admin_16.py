import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = list(re.finditer(r'(?:16|current_stage)', text))
print("Occurrences:", len(matches))
seen = set()
for m in matches:
    idx = m.start()
    line = text[max(0, idx-40):min(len(text), idx+60)].replace('\n', ' ')
    if line not in seen and any(k in line for k in ['current_stage >=', 'current_stage ==', 'current_stage >', 'stage >= 16', '/ 16', '/16', 'of 16']):
        seen.add(line)
        print("  ", line)
