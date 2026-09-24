import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const ROUND2_PUZZLE_DATA = \{', text)
if m:
    print(text[m.start():m.start()+1500])
