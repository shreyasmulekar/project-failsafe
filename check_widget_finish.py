import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = list(re.finditer(r'/api/teams/finish', text))
print("Occurrences of /api/teams/finish:", len(matches))
for m in matches:
    idx = m.start()
    print(text[idx-50:idx+250])
    print('---')
