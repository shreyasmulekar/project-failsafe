import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx15 = text.find('\n  15: {')
if idx15 != -1:
    idx_end = text.find('\n};', idx15)
    print("Found 15 in ROUND2_PUZZLE_DATA:")
    print(text[idx_end-400:idx_end+10])
