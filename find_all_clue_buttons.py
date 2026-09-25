import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# Check all buttons with text containing CLUE or HINT
matches = list(re.finditer(r'<button[^>]*>[^<]*(?:CLUE|HINT)[^<]*</button>', text, re.IGNORECASE))
print(f"Total buttons containing CLUE or HINT: {len(matches)}")
for m in matches:
    print(m.group(0))
