import re

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

keys = set(re.findall(r'localStorage\.(?:getItem|setItem)\([\'"]([a-zA-Z0-9_-]+)[\'"]', text))
for k in sorted(keys):
    print(k)
