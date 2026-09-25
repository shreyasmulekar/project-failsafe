import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('server.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('/api/teams/finish')
print(text[idx-50:idx+2500])
