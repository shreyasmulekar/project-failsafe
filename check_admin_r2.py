import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function sendAllFinishedToRound2')
print(text[idx:idx+1500])
