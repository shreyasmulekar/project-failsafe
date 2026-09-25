import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('max="16"', 'max="21"')
html = html.replace('max="15"', 'max="17"')
html = html.replace('clear Stage 16', 'clear Stage 21')
html = html.replace('Stage 16', 'Stage 21')

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated admin.html")
