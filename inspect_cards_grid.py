import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'id=["\']nexus-cards-grid["\']', text)
if m:
    start = m.start()
    print("Found nexus-cards-grid at char", start)
    print(text[start:start+4000])
else:
    print("nexus-cards-grid not found")
