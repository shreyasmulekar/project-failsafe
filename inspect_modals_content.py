with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

modals = ['modal-incident-logs', 'modal-security-audit', 'modal-acrostic', 'modal-font', 'modal-version-hist', 'modal-stego', 'modal-clearance']
for m in modals:
    idx = text.find(f'id="{m}"')
    if idx != -1:
        print(f"=== {m} ===")
        chunk = text[idx:idx+800].replace('\n', ' ')
        safe_str = chunk[:650].encode('ascii', 'replace').decode()
        print(safe_str)
        print()
