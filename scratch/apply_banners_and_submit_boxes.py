# scratch/apply_banners_and_submit_boxes.py
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Verify initial length
print(f"Initial length: {len(content)}")

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

# Stages that need a direct submit box inserted before closing of mil-modal-body
NEEDS_SUBMIT_BOX = {
    3: ("SAFE", "Enter decrypted acrostic key (e.g. SAFE)..."),
    4: ("28/02/2025", "Enter corrected calendar date (e.g. 28/02/2025)..."),
    5: ("POLARIS", "Enter decoded clearance word (e.g. POLARIS)..."),
    6: ("MARGIN_KEY", "Enter margin key (e.g. MARGIN_KEY or 22:46)..."),
    7: ("ARIAL", "Enter authentic font name (e.g. ARIAL)..."),
    8: ("WHITE", "Enter decoded morse word (e.g. WHITE)..."),
    9: ("REVERT_COMMIT_7B", "Enter rollback tag (e.g. REVERT_COMMIT_7B)..."),
    11: ("6-9-11", "Enter letter counts (e.g. 6-9-11)...")
}

# 1. Insert banners right after <div class="mil-modal-body"...>
for stg, data in STAGE_BANNERS.items():
    mid = data['modal']
    m_pos = content.find(f'id="{mid}"')
    if m_pos == -1:
        print(f"Warning: {mid} not found!")
        continue
    
    body_idx = content.find('class="mil-modal-body', m_pos)
    tag_end = content.find('>', body_idx) + 1
    
    # Check if banner already inserted
    snippet = content[tag_end:tag_end+200]
    if 'stage-click-direction-banner' in snippet or 'WHERE TO CLICK & SUBMIT' in snippet:
        print(f"Stage {stg} banner already exists, skipping insertion.")
        continue
    
    banner_html = f"""
        <!-- High-Contrast Interactive Click & Submit Directives Banner -->
        <div class="stage-click-direction-banner" style="background:rgba(0,240,255,0.07); border:1px solid #00f0ff; border-left:5px solid #00f0ff; padding:12px 16px; margin-bottom:16px; border-radius:4px; font-family:var(--font-mono, monospace);">
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

# 2. Insert standardized direct submit box for stages that need one
for stg, (default_key, placeholder) in NEEDS_SUBMIT_BOX.items():
    mid = STAGE_BANNERS[stg]['modal']
    m_pos = content.find(f'id="{mid}"')
    if m_pos == -1:
        continue
    
    # Find modal end: find next modal or closing divs
    # Let's locate the closing </div> of mil-modal-body
    # We can search for the closing </div> of the modal by counting
    body_idx = content.find('class="mil-modal-body', m_pos)
    # Search from body_idx for the end of the modal body
    # An easy unique anchor is right before the </div> that closes mil-modal-body
    # Let's inspect each modal's ending individually
print("Stage banners inserted. Now inserting submit boxes...")
