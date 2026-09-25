import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Mass_System_Log.txt')
while idx != -1:
    print(text[idx-50:idx+150])
    print("="*40)
    idx = text.find('Mass_System_Log.txt', idx+1)
