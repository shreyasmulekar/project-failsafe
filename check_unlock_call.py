import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('test_e2e_all_stages.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('R1_STAGES')
if idx == -1:
    idx = text.find('Stage  1')
if idx == -1:
    idx = text.find('/api/stage/unlock')
print(text[idx-50:idx+800])
