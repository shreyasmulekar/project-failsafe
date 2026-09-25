import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('🎯 STAGE 01 // TRANSMIT DECRYPT KEY')
print(text[idx:idx+1500])
