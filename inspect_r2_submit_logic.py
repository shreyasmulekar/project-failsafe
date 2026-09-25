import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'round2.*submit|submit.*round2|/api/stage/unlock', text, re.IGNORECASE):
    start = max(0, m.start() - 50)
    end = min(len(text), m.end() + 250)
    print(text[start:end])
    print("="*40)
