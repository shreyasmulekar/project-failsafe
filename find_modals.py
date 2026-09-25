import re

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

modals = set(re.findall(r'id=["\'](modal-[a-zA-Z0-9_-]+)["\']', text))
for m in sorted(modals):
    print(m)
