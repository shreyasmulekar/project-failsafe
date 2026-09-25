import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('const ROUND2_PUZZLE_DATA = {')
print(text[idx:idx+1500])
