import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'function runChecksumScan\s*\(', text)
if m:
    start = m.start()
    print("Found runChecksumScan at char", start)
    print(text[start:start+1800])
