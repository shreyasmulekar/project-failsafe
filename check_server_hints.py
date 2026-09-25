import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('server.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('/api/hints/request')
print(text[idx+2200:idx+3200])
