with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="modal-clue-confirm"')
if idx != -1:
    print(text[idx:idx+1500].encode('ascii', 'replace').decode())
