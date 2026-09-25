import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('const ROUND2_PUZZLE_DATA = {')
idx_end = text.find('\n    const R2_CARD_DEFINITIONS = [', idx)
if idx_end == -1:
    idx_end = text.find('const R2_CARD_DEFINITIONS = [', idx)

print("ROUND2_PUZZLE_DATA length:", idx_end - idx)
# Print list of keys in ROUND2_PUZZLE_DATA
import re
keys = re.findall(r'\n  ([0-9]+):\s*\{', text[idx:idx_end])
print("Existing keys in ROUND2_PUZZLE_DATA:", keys)
