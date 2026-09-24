# scratch/find_modals.py
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Find all divs with modal or dossier in class or id
for line_idx, line in enumerate(text.splitlines()):
    if '<div' in line and ('class="mil-modal' in line or 'class="modal' in line or 'class="dossier-modal' in line or 'id="modal-' in line):
        print(f"Line {line_idx+1}: {line.strip()[:100]}")
