import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'function requestTacticalClue|requestHint|active-clue-banner', text)
if m:
    start = max(0, m.start() - 50)
    print("Found in html at char", start)
    print(text[start:start+1500])
