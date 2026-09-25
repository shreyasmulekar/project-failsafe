import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find renderRound2NexusGrid function definition
m = re.search(r'function renderRound2NexusGrid\(\)\s*\{', text)
if m:
    start = m.start()
    print("Found renderRound2NexusGrid at char", start)
    print(text[start:start+2500])
else:
    print("renderRound2NexusGrid not found")
