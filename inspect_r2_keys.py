import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Inspect submitRound2Key to see how it validates
idx = html.find('function submitRound2Key')
if idx != -1:
    print("Found submitRound2Key:")
    print(html[idx:idx+1200])

# Inspect R2_CLICK_DIRECTIVES
idx2 = html.find('const R2_CLICK_DIRECTIVES')
if idx2 != -1:
    print("Found R2_CLICK_DIRECTIVES:")
    print(html[idx2:idx2+1200])
