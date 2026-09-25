import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'//\s*Stage 16:.*?(\}\s*else\s*if|\}\s*else\s*\{)', text, re.DOTALL)
if m:
    start = m.start()
    print("Found Stage 16 in runChecksumScan:")
    print(text[start:start+1200])
else:
    print("Not found by regex, searching literal 1400")
    idx = text.find('1400')
    while idx != -1:
        print(text[idx-50:idx+200])
        print("="*40)
        idx = text.find('1400', idx+1)
        if idx > 550000:
            break
