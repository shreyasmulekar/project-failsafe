import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('async function submitStageDirectKey')
if idx == -1:
    idx = text.find('function submitStageDirectKey')
print(text[idx:idx+1500])
