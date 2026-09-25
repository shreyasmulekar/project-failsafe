with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

modals = [
    (1, 'modal-origin'),
    (2, 'modal-memory'),
    (3, 'modal-incident-logs'),
    (4, 'modal-security-audit'),
    (5, 'modal-acrostic'),
    (6, 'modal-font'),
    (7, 'modal-version-hist'),
    (8, 'modal-spectro'),
    (9, 'modal-stego'),
    (10, 'modal-honeypot'),
    (11, 'modal-clearance'),
]

for st, mid in modals:
    idx = text.find(f'id="{mid}"')
    if idx == -1:
        print(f"Stage {st}: {mid} NOT FOUND!")
        continue
    # find next modal or 3000 chars
    chunk = text[idx:idx+3500]
    
    # search for submitStageDirectKey(X, ...)
    keys = re.findall(r'submitStageDirectKey\((\d+)', chunk)
    # search for input-stage-X
    inputs = re.findall(r'id=["\']input-stage-(\d+)["\']', chunk)
    # search for STAGE XX
    stages_hdr = re.findall(r'STAGE\s+(\d+)', chunk, re.IGNORECASE)
    
    print(f"Stage {st:2d} ({mid:22s}): submitDirectKey={keys} | input-stage={inputs} | headers={stages_hdr[:3]}")
