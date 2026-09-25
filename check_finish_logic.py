import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('server.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('team["round_2_finish_time_str"] = elapsed_str')
print(text[idx:idx+2000])
