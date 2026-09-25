import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('CLASSIFIED EVIDENCE ACCESS DIRECTORY // 21 STAGES')
print(text[idx+700:idx+1500])
