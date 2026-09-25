with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find locations
pos_stage_nav = text.find('const STAGE_NAVIGATION_DATA = {')
pos_stage_titles = text.find('const STAGE_TITLES = {')
pos_checksum = text.find('function runChecksumScan(passcode) {')
pos_cards_grid = text.find('<div class="nexus-cards-grid" id="nexus-cards-grid">')
pos_stages_meta = text.find('const NEXUS_STAGES_META = {')

print("STAGE_NAVIGATION_DATA:", pos_stage_nav)
print("STAGE_TITLES:", pos_stage_titles)
print("runChecksumScan:", pos_checksum)
print("nexus-cards-grid:", pos_cards_grid)
print("NEXUS_STAGES_META:", pos_stages_meta)
