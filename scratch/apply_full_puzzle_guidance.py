# scratch/apply_full_puzzle_guidance.py
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    content = f.read()

initial_len = len(content)
print(f"Reading aditi_os_widget.html, initial length: {initial_len}")

# Guidance banner definitions for all 16 Round 1 stages
STAGE_BANNERS = {
    1: {
        'modal': 'modal-recovery',
        'click': "Review the 5-command boot lifecycle: <code>LOGIN &rarr; VERIFY &rarr; ??? &rarr; EXECUTE &rarr; LOCK</code>. Deduce the missing operational verb required to authorize core boot access.",
        'submit': "Type the missing verb <code>ACCESS</code> into the recovery key box below and click <strong>[⚡ TRANSMIT KEY]</strong> (or enter <code>decrypt ACCESS</code> in terminal / Quick Decrypt dock)."
    },
    2: {
        'modal': 'modal-memory',
        'click': "Click the glowing <strong>[▲ UP]</strong> and <strong>[▼ DN]</strong> arrow buttons on each memory card to arrange them in strict chronological order: <code>4:17 PM &rarr; 6:45 PM &rarr; 8:10 PM &rarr; 9:32 PM &rarr; 10:03 PM &rarr; 10:15 PM</code>.",
        'submit': "Click the large bright green <strong>[⚡ RESTORE MEMORY SEQUENCE]</strong> button below the cards (or submit <code>123456</code> into the Quick Decrypt dock)."
    },
    3: {
        'modal': 'modal-acrostic',
        'click': "Read through Dr. Aditi's emergency memo text. Focus on the very <strong>first letter of each sentence</strong> in the paragraph to extract the concealed acrostic signature.",
        'submit': "Combine the initial letters (S-A-F-E), enter <code>SAFE</code> into the <strong>[TRANSMIT DECRYPT KEY]</strong> box below, and click <strong>[⚡ TRANSMIT KEY]</strong>."
    },
    4: {
        'modal': 'modal-incident-logs',
        'click': "Audit the audit log table timestamps for the year 2025. Look for the impossible calendar date that does not exist in a non-leap year (February 29, 2025).",
        'submit': "Enter the corrected calendar date <code>28/02/2025</code> (or <code>28022025</code>) into the <strong>[TRANSMIT DECRYPT KEY]</strong> box below and click <strong>[⚡ TRANSMIT KEY]</strong>."
    },
    5: {
        'modal': 'modal-clearance',
        'click': "Inspect the telex coordinate offsets: <code>[16 - 15 - 12 - 01 - 18 - 09 - 19]</code>.",
        'submit': "Convert numbers to alphabet positions (1=A, 2=B... 16=P, 15=O, 12=L, 1=A, 18=R, 9=I, 19=S &rarr; <code>POLARIS</code>). Enter <code>POLARIS</code> into the box below and click <strong>[⚡ TRANSMIT KEY]</strong>."
    },
    6: {
        'modal': 'modal-comments',
        'click': "Click the <strong>[💬 Comments (1 Resolved)]</strong> button in the upper-right corner of the diagnostic document to reveal Dr. Aditi's concealed margin notes.",
        'submit': "Read the hidden keyword in the margin note, enter <code>MARGIN_KEY</code> (or <code>22:46</code>) into the box below, and click <strong>[⚡ TRANSMIT KEY]</strong>."
    },
    7: {
        'modal': 'modal-font',
        'click': "Click between the <strong>[AUTHENTIC_LOG.doc]</strong> and <strong>[DECOY_LOG.doc]</strong> tabs to compare typography against Dr. Aditi's laboratory font standard.",
        'submit': "Identify the genuine sans-serif font family (<code>ARIAL</code>), type <code>ARIAL</code> into the box below, and click <strong>[⚡ TRANSMIT KEY]</strong>."
    },
    8: {
        'modal': 'modal-spectro',
        'click': "Click <strong>[▶ PLAY BEACON A (WHITE)]</strong> to listen to the analog Morse CW audio beeps, or read the visual audio spectrogram frequency bars.",
        'submit': "Decode the dots and dashes (<code>.-- .... .. - .</code> &rarr; <code>WHITE</code>), enter <code>WHITE</code> into the box below, and click <strong>[⚡ TRANSMIT KEY]</strong>."
    },
    9: {
        'modal': 'modal-version-hist',
        'click': "Click the <strong>[Previous Revision (20:18Z by Dr. Aditi)]</strong> tab to rollback ISHAAN's scrubbed Git reflog and view Dr. Aditi's genuine commit message.",
        'submit': "Read the rollback status tag <code>REVERT_COMMIT_7B</code>, enter it into the box below, and click <strong>[⚡ TRANSMIT KEY]</strong>."
    },
    10: {
        'modal': 'modal-honeypot',
        'click': "⚠️ <strong>CAUTION:</strong> DO NOT click the red execution binary <code>[☠️ EXECUTE BINARY]</code>! Instead, inspect the sandbox quarantine protocol.",
        'submit': "Enter the emergency quarantine disarm keyword <code>DISARM</code> into the disarm input box below and click <strong>[DISARM &rarr;]</strong>."
    },
    11: {
        'modal': 'modal-failsafe',
        'click': "Inspect the three foundational IEEE WIE core values: <strong>Wisdom</strong>, <strong>Integrity</strong>, and <strong>Empowerment</strong>. Count the number of letters in each word.",
        'submit': "Combine the word letter counts (Wisdom=6, Integrity=9, Empowerment=11 &rarr; <code>6-9-11</code>). Enter <code>6-9-11</code> into the box below and click <strong>[⚡ TRANSMIT KEY]</strong>."
    },
    12: {
        'modal': 'modal-whiteout',
        'click': "Click <strong>[🔦 HIGHLIGHT ALL (CTRL + A)]</strong> or <strong>[⚡ UV DEPOLARIZER]</strong> to reveal the invisible white text hidden on the white document canvas.",
        'submit': "Read the exposed clearance phrase <code>CLEARANCE_ALPHA</code>, enter it into the input box below, and click <strong>[⚡ TRANSMIT KEY]</strong>."
    },
    13: {
        'modal': 'modal-rot4',
        'click': "Read the intercepted ciphertext <code>EHMXXW17</code>. Use the Caesar shift slider or shift each letter back by 4 positions.",
        'submit': "Enter the decrypted string <code>ADITIS13</code> into the input box below and click <strong>[TRANSMIT &rarr;]</strong>."
    },
    14: {
        'modal': 'modal-atbash',
        'click': "Read the inverted stream <code>KILQZXG</code>. Match each letter against the mirrored Atbash alphabet (A&harr;Z, B&harr;Y, etc.).",
        'submit': "Decrypt the keyword <code>PROJECT</code>, enter it into the input box below, and click <strong>[TRANSMIT &rarr;]</strong>."
    },
    15: {
        'modal': 'modal-polybius',
        'click': "Inspect the 5x5 Polybius grid and the coordinate pairs: <code>(2,1) (1,1) (2,4) (3,1) (4,3) (1,1) (2,1) (1,5)</code>.",
        'submit': "Map row/column pairs to letters (2,1=F, 1,1=A, 2,4=I... &rarr; <code>FAILSAFE</code>). Enter <code>FAILSAFE</code> into the input box below and click <strong>[TRANSMIT &rarr;]</strong>."
    },
    16: {
        'modal': 'modal-frequency',
        'click': "Inspect the letter occurrence histogram and deduce character substitution to reveal the final liberation passcode.",
        'submit': "Enter the decrypted master codeword <code>CIPHER</code> into the input box below and click <strong>[TRANSMIT &rarr;]</strong> to trigger TARA's final liberation!"
    }
}

# 1. Insert guidance banners right after mil-modal-body in each of the 16 modals
for stg in range(1, 17):
    data = STAGE_BANNERS[stg]
    mid = data['modal']
    m_pos = content.find(f'id="{mid}"')
    if m_pos == -1:
        print(f"Warning: {mid} not found!")
        continue
    body_idx = content.find('class="mil-modal-body', m_pos)
    tag_end = content.find('>', body_idx) + 1
    
    # Check if banner already inserted
    snippet = content[tag_end:tag_end+250]
    if 'stage-click-direction-banner' in snippet:
        print(f"Stage {stg} banner already exists.")
        continue
    
    banner_html = f"""
        <!-- High-Contrast Interactive Click & Submit Directives Banner -->
        <div class="stage-click-direction-banner" style="background:rgba(0,240,255,0.08); border:1px solid #00f0ff; border-left:5px solid #00f0ff; padding:12px 16px; margin-bottom:16px; border-radius:4px; font-family:var(--font-mono, monospace); box-shadow:0 0 15px rgba(0,240,255,0.15);">
          <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
            <span style="background:#00f0ff; color:#02060e; font-weight:900; font-size:11px; padding:2px 8px; border-radius:3px; letter-spacing:1px;">TACTICAL DIRECTIVES</span>
            <span style="color:#00f0ff; font-weight:bold; font-size:12px; letter-spacing:0.5px;">STAGE {stg:02d} // WHERE TO CLICK &amp; SUBMIT</span>
          </div>
          <div style="font-size:13px; color:#e2e8f0; line-height:1.5; margin-bottom:6px;">
            <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> {data['click']}
          </div>
          <div style="font-size:12.5px; color:#a7f3d0; line-height:1.5;">
            <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> {data['submit']}
          </div>
        </div>
"""
    content = content[:tag_end] + banner_html + content[tag_end:]
    print(f"Inserted guidance banner for Stage {stg:02d} ({mid}).")

# 2. Insert standardized direct submit box for stages that currently lack one:
# Stages: 3, 4, 5, 6, 7, 8, 9, 11
SUBMIT_BOX_TARGETS = [
    (3, 'modal-acrostic', 'SAFE', 'Enter decrypted acrostic key (e.g. SAFE)...', 'SAFE'),
    (4, 'modal-incident-logs', '28/02/2025', 'Enter corrected calendar date (e.g. 28/02/2025)...', '28/02/2025'),
    (5, 'modal-clearance', 'POLARIS', 'Enter decoded clearance word (e.g. POLARIS)...', 'POLARIS'),
    (6, 'modal-comments', 'MARGIN_KEY', 'Enter margin key (e.g. MARGIN_KEY or 22:46)...', 'MARGIN_KEY'),
    (7, 'modal-font', 'ARIAL', 'Enter authentic font name (e.g. ARIAL)...', 'ARIAL'),
    (8, 'modal-spectro', 'WHITE', 'Enter decoded morse word (e.g. WHITE)...', 'WHITE'),
    (9, 'modal-version-hist', 'REVERT_COMMIT_7B', 'Enter rollback tag (e.g. REVERT_COMMIT_7B)...', 'REVERT_COMMIT_7B'),
    (11, 'modal-failsafe', '6-9-11', 'Enter letter counts (e.g. 6-9-11)...', '6-9-11')
]

for stg, mid, default_code, placeholder, example in SUBMIT_BOX_TARGETS:
    m_pos = content.find(f'id="{mid}"')
    if m_pos == -1:
        continue
    
    # Check if submit box already exists
    sub_box_id = f'input-stage-{stg}'
    if sub_box_id in content[m_pos:m_pos+4000]:
        print(f"Submit box for Stage {stg} already exists.")
        continue
    
    # Locate the end of the modal body
    # We find where this modal ends: next modal starts or closing </div>
    # In all our modals, the body ends before the last </div></div>
    # Let's find the closing of mil-modal:
    # Look for the last </div> before the next modal or within 3500 chars
    body_idx = content.find('class="mil-modal-body', m_pos)
    
    # Let's find specific anchor near the end of each modal body:
    anchors = {
        3: 'Aditi_Memo.doc // Confirmed Acrostic Stored',
        4: 'An astronomical anomaly exists in these logs',
        5: '16-15-12-01-18-09-19',
        6: 'Analyze the recovered evidence to deduce Dr. Aditi\'s clearance passcode',
        7: 'Dr. Aditi Sharma always strictly adhered to the IEEE and StratCom typographical standard',
        8: 'Listen to Dr. Aditi\'s emergency beacon audio',
        9: '[ALTERED BY ROGUE DAEMON: STATUS TAMPERED]',
        11: 'Core Values Formulation Matrix'
    }
    anchor = anchors.get(stg)
    if anchor and anchor in content[m_pos:m_pos+4000]:
        anchor_idx = content.find(anchor, m_pos)
        # Find closing tag of this section
        close_div = content.find('</div>', anchor_idx)
        insert_pos = close_div + 6
    else:
        # Fallback: search for last </div> in the modal chunk
        chunk = content[m_pos:m_pos+3500]
        # Find the last </div> before the final closing </div>
        last_closes = [m.start() for m in re.finditer(r'</div>\s*</div>', chunk)]
        if last_closes:
            insert_pos = m_pos + last_closes[-1]
        else:
            print(f"Could not find anchor for Stage {stg}")
            continue

    box_html = f"""
        <!-- In-Modal Standardized Direct Submission Terminal -->
        <div class="stage-direct-submit-box" style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.5); border-radius:6px; padding:14px 18px; margin-top:20px; font-family:var(--font-mono, monospace); box-shadow:0 0 20px rgba(0,240,255,0.12);">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
            <div style="color:#00f0ff; font-weight:bold; font-size:12px; letter-spacing:1px;">
              🎯 STAGE {stg:02d} // TRANSMIT DECRYPT KEY
            </div>
            <span style="font-size:11px; color:#94a3b8;">Enter key below and click Transmit</span>
          </div>
          <div style="display:flex; gap:10px; align-items:center;">
            <input type="text" id="input-stage-{stg}" placeholder="{placeholder}" style="flex:1; background:#02060e; border:1px solid #00f0ff; color:#00f0ff; padding:10px 14px; font-family:var(--font-mono); font-size:13px; border-radius:4px; outline:none; box-shadow:inset 0 0 10px rgba(0,240,255,0.15);" onkeydown="if(event.key==='Enter') submitStageDirectKey({stg}, document.getElementById('input-stage-{stg}').value)">
            <button type="button" class="btn-tactical success" onclick="submitStageDirectKey({stg}, document.getElementById('input-stage-{stg}').value)" style="background:#00f0ff; color:#02060e; font-weight:bold; border:none; padding:10px 22px; border-radius:4px; cursor:pointer; font-size:12px; letter-spacing:0.5px; box-shadow:0 0 12px rgba(0,240,255,0.5);">⚡ TRANSMIT KEY</button>
          </div>
          <div id="fb-stage-{stg}" style="min-height:16px; font-size:11.5px; margin-top:6px; color:#ffb000;"></div>
        </div>
"""
    content = content[:insert_pos] + box_html + content[insert_pos:]
    print(f"Inserted direct submit box for Stage {stg:02d} ({mid}).")

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Updated aditi_os_widget.html successfully! New length: {len(content)}")
