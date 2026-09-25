import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Lines around 10779 in aditi_os_widget.html:")
print(''.join(lines[10770:10800]))
