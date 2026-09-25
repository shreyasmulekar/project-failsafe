import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'function requestTacticalClue\s*\(', text)
if m:
    start = m.start()
    print("Found requestTacticalClue at char", start)
    print(text[start:start+2500])
