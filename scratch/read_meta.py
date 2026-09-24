# scratch/read_meta.py
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('const NEXUS_STAGES_META = {')
if pos != -1:
    end_pos = text.find('    };', pos)
    chunk = text[pos:end_pos+6]
    print(chunk[:3000])
    if len(chunk) > 3000:
        print("\n--- NEXT 3000 ---")
        print(chunk[3000:6000])
    if len(chunk) > 6000:
        print("\n--- NEXT 3000 ---")
        print(chunk[6000:9000])
