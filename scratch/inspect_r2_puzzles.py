import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const ROUND2_PUZZLE_DATA = \{', text)
if m:
    data_str = text[m.start():m.start()+50000]
    # Find all puzzle keys
    for pz_num in range(1, 16):
        pz_m = re.search(rf'\b{pz_num}:\s*\{{', data_str)
        if pz_m:
            chunk = data_str[pz_m.start():pz_m.start()+2500]
            title = re.search(r'title:\s*"([^"]+)"', chunk)
            prompt = re.search(r'passwordPrompt:\s*"([^"]+)"', chunk)
            tara = re.search(r'taraPointerHint:\s*"([^"]+)"', chunk)
            ishaan = re.search(r'ishaanTaunt:\s*"([^"]+)"', chunk)
            print(f"=== PUZZLE {pz_num:02d} ===")
            print(f"  Title: {title.group(1) if title else 'N/A'}")
            print(f"  Prompt: {prompt.group(1) if prompt else 'N/A'}")
            print(f"  TARA Hint: {tara.group(1)[:70] if tara else 'N/A'}...")
            print(f"  ISHAAN Taunt: {ishaan.group(1)[:70] if ishaan else 'N/A'}...")
