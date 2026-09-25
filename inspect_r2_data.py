import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const ROUND2_PUZZLE_DATA\s*=', text)
if m:
    start = m.start()
    print("Found ROUND2_PUZZLE_DATA at char", start)
    print(text[start:start+1500])
else:
    print("ROUND2_PUZZLE_DATA not found")

m2 = re.search(r'const R2_CARD_DEFINITIONS\s*=', text)
if m2:
    start = m2.start()
    print("Found R2_CARD_DEFINITIONS at char", start)
    print(text[start:start+1000])
