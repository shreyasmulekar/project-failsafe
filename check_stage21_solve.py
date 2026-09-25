import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('// Stage 21:')
if idx == -1:
    idx = text.find('Stage 21')
print(text[idx-50:idx+2500])
