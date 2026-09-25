import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
modals = re.findall(r'<div[^>]*id=["\'](modal-[^"\']+)["\']', text)
print("Modals found:", modals)
