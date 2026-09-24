import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    # Check for Ethan in text between > and < or in strings
    text_between = re.findall(r'>([^<]*\bethan\b[^<]*)<', line, re.IGNORECASE)
    quotes = re.findall(r'["\']([^"\']*\bethan\b[^"\']*)["\']', line, re.IGNORECASE)
    items = text_between + quotes
    filtered = []
    for x in items:
        # Ignore selectors, css classes, element IDs
        if x.startswith('.') or x.startswith('#') or 'class' in x or 'id=' in x:
            continue
        if x in ['ethan', 'ethan-hunt-box', 'canvas-ethan-entity', 'canvas-ethan-avatar']:
            continue
        filtered.append(x)
    if filtered:
        print(f"Line {i+1}: {filtered}")
