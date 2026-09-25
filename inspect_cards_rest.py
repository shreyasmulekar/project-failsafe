import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'id=["\']nexus-cards-grid["\']', text)
if m:
    start = m.start()
    print(text[start+3000:start+7500])
