import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update STAGE_TITLES
old_titles = '''      15: "Ch 15: The Polybius Coordinate Trail",
      16: "Ch 16: Frequency Override Count"
    };'''

new_titles = '''      15: "Ch 15: The Polybius Coordinate Trail",
      16: "Ch 16: Frequency Override Count",
      17: "Ch 17: Rogue Chatbot Polybius Shift",
      18: "Ch 18: The Modular Clock Loop",
      19: "Ch 19: The Anomaly Checklist",
      20: "Ch 20: The Shift Cipher Matrix",
      21: "Ch 21: The Log Anomaly Timeline"
    };'''

if old_titles in html:
    html = html.replace(old_titles, new_titles)
    print("STAGE_TITLES updated")
else:
    print("Warning: old_titles not found")

# 2. Update STAGE_REQUIRED_MODAL_MAP
old_modal_map = '''      'card-polybius': 15,
      'modal-polybius': 15,
      'card-frequency': 16,
      'modal-frequency': 16
    };'''

new_modal_map = '''      'card-polybius': 15,
      'modal-polybius': 15,
      'card-frequency': 16,
      'modal-frequency': 16,
      'card-polybius-shift': 17,
      'modal-polybius-shift': 17,
      'card-clock-loop': 18,
      'modal-clock-loop': 18,
      'card-status-check': 19,
      'modal-status-check': 19,
      'card-shift-matrix': 20,
      'modal-shift-matrix': 20,
      'card-audit-timeline': 21,
      'modal-audit-timeline': 21
    };'''

if old_modal_map in html:
    html = html.replace(old_modal_map, new_modal_map)
    print("STAGE_REQUIRED_MODAL_MAP updated")
else:
    print("Warning: old_modal_map not found")

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved stage titles & modal map changes!")
