import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
for m in re.finditer(r'#modal-clue-confirm|\.mil-modal\s*\{', text):
    start = max(0, m.start() - 20)
    end = min(len(text), m.start() + 300)
    print(text[start:end])
    print('---')
