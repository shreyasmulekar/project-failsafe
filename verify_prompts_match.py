import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

modals = [
    'modal-polybius-shift',
    'modal-clock-loop',
    'modal-status-check',
    'modal-shift-matrix',
    'modal-audit-timeline'
]

for m in modals:
    idx = text.find(f'id="{m}"')
    print(f"Modal {m}: {'FOUND' if idx != -1 else 'MISSING'}")

# Also check Round 2 Stage 17 (The Failsafe Logic Tree)
idx_f = text.find("The Failsafe Logic Tree")
print(f"Failsafe Logic Tree in R2: {'FOUND' if idx_f != -1 else 'MISSING'}")
