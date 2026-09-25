with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

modals = [
    'modal-recovery',
    'modal-origin',
    'modal-incident-logs',
    'modal-security-audit',
    'modal-acrostic',
    'modal-font',
    'modal-version-hist',
    'modal-stego',
    'modal-clearance'
]

for mid in modals:
    pattern = rf'<div[^>]*id=["\']{mid}["\'][\s\S]*?(?=<div[^>]*class=["\']nexus-modal["\']|<div[^>]*class=["\']modal["\']|\Z)'
    m = re.search(pattern, text)
    if m:
        block = m.group(0)
        print(f"=== {mid} (Length: {len(block)}) ===")
        # Print first 500 chars and last 200 chars
        print(block[:300].encode('ascii', 'replace').decode())
        print("...")
        print(block[-200:].encode('ascii', 'replace').decode())
        print("\n")
    else:
        print(f"=== {mid} NOT FOUND ===")
