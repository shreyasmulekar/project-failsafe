with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'class="mil-modal"' in line or 'class="nexus-modal"' in line:
        print(f"Line {i+1}: {line.strip()[:100]}")
