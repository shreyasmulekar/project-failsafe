import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="modal-clue-confirm"')
print(text[idx+2400:idx+3600])
