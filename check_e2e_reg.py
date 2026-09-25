import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('test_e2e_all_stages.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('team')
print(text[:1000])
