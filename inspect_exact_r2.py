import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx_d = text.find('const R2_CLICK_DIRECTIVES = {')
if idx_d != -1:
    idx_d_end = text.find('};', idx_d) + 2
    print("Found R2_CLICK_DIRECTIVES snippet:")
    print(text[idx_d:idx_d+400])

idx_c = text.find('const R2_CARD_DEFINITIONS = [')
if idx_c != -1:
    idx_c_end = text.find('];', idx_c) + 2
    print("Found R2_CARD_DEFINITIONS snippet:")
    print(text[idx_c:idx_c+400])
