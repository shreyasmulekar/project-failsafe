import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('server.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = list(re.finditer(r'if path == [\'\"]/api/admin/', text))
for m in matches:
    idx = m.start()
    print(text[idx:idx+80])
