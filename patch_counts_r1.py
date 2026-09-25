import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace 16 with 21 in UI displays for total stages
replaces = [
    ('16 / 16', '21 / 21'),
    ('16 CHRONOLOGICAL STAGES', '21 CHRONOLOGICAL STAGES'),
    ('CLASSIFIED EVIDENCE ACCESS DIRECTORY // 16 STAGES', 'CLASSIFIED EVIDENCE ACCESS DIRECTORY // 21 STAGES'),
    ('16 / 16 STAGES RESOLVED', '21 / 21 STAGES RESOLVED'),
    ('ALL 16 STAGES CLEARED', 'ALL 21 STAGES CLEARED'),
    ('ALL 16 STAGES SOLVED', 'ALL 21 STAGES SOLVED'),
    ('All 16 Stages Cleared', 'All 21 Stages Cleared'),
    ('(totalSec || 1800) / 16', '(totalSec || 1800) / 21'),
    ('clearedStages.length / 16', 'clearedStages.length / 21'),
    ('Math.min(100, (currentStage / 16) * 100)', 'Math.min(100, (currentStage / 21) * 100)'),
    ('Math.min(100, ((currentStage - 1) / 16) * 100)', 'Math.min(100, ((currentStage - 1) / 21) * 100)')
]

for old, new in replaces:
    count = text.count(old)
    if count > 0:
        text = text.replace(old, new)
        print(f"Replaced '{old}' -> '{new}' ({count} times)")

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated stage counts in aditi_os_widget.html")
