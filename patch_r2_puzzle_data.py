import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx_start = text.find('const ROUND2_PUZZLE_DATA = {')
idx_end = text.find('\n};\n\n/**', idx_start)
if idx_end == -1:
    idx_end = text.find('\n};', idx_start)

print("Found ROUND2_PUZZLE_DATA block from", idx_start, "to", idx_end)
block = text[idx_start:idx_end+3]

# Extract each puzzle from block
puzzles = {}
# Find keys: \n  (\d+):\s*\{
matches = list(re.finditer(r'\n  (\d+):\s*\{', block))
for i in range(len(matches)):
    p_num = int(matches[i].group(1))
    p_start = matches[i].start() + 1
    if i < len(matches) - 1:
        p_end = matches[i+1].start() + 1
        # strip trailing comma
        p_code = block[p_start:p_end].rstrip().rstrip(',')
    else:
        p_end = len(block) - 2 # before \n};
        p_code = block[p_start:p_end].rstrip().rstrip(',')
    puzzles[p_num] = p_code

print("Extracted existing puzzles:", sorted(puzzles.keys()))

# Build shifted puzzles 2..16
shifted_puzzles = {}
for old_id, p_code in puzzles.items():
    new_id = old_id + 1
    # Replace the key header: "  old_id: {" -> "  new_id: {"
    p_code = re.sub(r'^\s*' + str(old_id) + r':\s*\{', f'  {new_id}: {{', p_code)
    # Replace id: old_id
    p_code = re.sub(r'\bid:\s*' + str(old_id) + r'\b', f'id: {new_id}', p_code)
    # Replace folderName: "R2_0X_..."
    old_folder = f'R2_{old_id:02d}_'
    new_folder = f'R2_{new_id:02d}_'
    p_code = p_code.replace(old_folder, new_folder)
    # Replace badge "PUZZLE 0X OF 15"
    p_code = p_code.replace(f'PUZZLE {old_id:02d} OF 15', f'PUZZLE {new_id:02d} OF 17')
    p_code = p_code.replace(f'PUZZLE {old_id} OF 15', f'PUZZLE {new_id:02d} OF 17')
    shifted_puzzles[new_id] = p_code

# Define Stage 1: EMERGENCY OVERRIDE
stage_1_code = '''  1: {
    id: 1,
    round: 2,
    folderName: "R2_01_OVERRIDE",
    title: "EMERGENCY OVERRIDE",
    type: "shift",
    fileName: "Emergency_Override_Key.txt",
    passwordPrompt: "ENTER AUTHORIZATION CODE (N B H Y K shifted backward by 7):",
    targetSelector: "#r2-override-auth-code",
    taraPointerHint: "ADI went rogue on October 13, 2090 (Sunday = 7). Apply the backward alphabet shift of 7 to ciphertext N B H Y K to restore the code: N->G, B->U, H->A, Y->R, K->D. Enter GUARD.",
    ishaanTaunt: "Dr. Aditi's emergency override was sealed before I breached the mainframe. You will never crack the launch timestamp.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,255,102,0.15); border-color:#00ff66; color:#00ff66; font-size:12px; padding:3px 8px;">ROUND 02 // PUZZLE 01 OF 17</span>
            <strong style="margin-left:8px; font-size:16px; letter-spacing:0.5px;">EMERGENCY OVERRIDE AUTHORIZATION</strong>
          </div>
          <span style="font-size:12px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">INITIAL R2 GATE</span>
        </div>

        <div style="background:rgba(0,240,255,0.05); border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:16px; margin-bottom:18px;">
          <h4 style="color:#00f0ff; margin-bottom:8px; font-size:14px;">Dr. Aditi's Intercepted Emergency Record</h4>
          <p style="font-size:13px; color:#cbd5e1; line-height:1.6; margin-bottom:12px;">
            ADI has intercepted an authorization command left behind by Dr. Aditi. The original command was encrypted before ADI could access it.<br>
            Dr. Aditi left behind one piece of critical information that may allow you to recover it.
          </p>
          <div style="background:#020617; border:1px solid #334155; padding:12px 16px; border-radius:4px; font-size:13px; color:#38bdf8; margin-bottom:12px;">
            <strong>DATE RECORDED:</strong> OCTOBER 13, 2090<br>
            <em>"ADI went rogue on the same day. Determine the numerical day-of-the-week value based on Aditi's clue, apply the backward alphabet shift to the ciphertext in Emergency_Override_Key.txt, and enter the resulting 5-letter authorization code."</em>
          </div>
        </div>

        <div style="display:flex; justify-content:center; gap:16px; margin:20px 0;">
          <div style="background:#0b1329; border:2px solid #00ff66; border-radius:8px; padding:14px 22px; text-align:center;">
            <div style="font-size:11px; color:#94a3b8; margin-bottom:4px;">CHAR 1</div>
            <div style="font-size:24px; font-weight:900; color:#fff;">N</div>
            <div style="font-size:11px; color:#00ff66; margin-top:4px;">- 7 &rarr; G</div>
          </div>
          <div style="background:#0b1329; border:2px solid #00ff66; border-radius:8px; padding:14px 22px; text-align:center;">
            <div style="font-size:11px; color:#94a3b8; margin-bottom:4px;">CHAR 2</div>
            <div style="font-size:24px; font-weight:900; color:#fff;">B</div>
            <div style="font-size:11px; color:#00ff66; margin-top:4px;">- 7 &rarr; U</div>
          </div>
          <div style="background:#0b1329; border:2px solid #00ff66; border-radius:8px; padding:14px 22px; text-align:center;">
            <div style="font-size:11px; color:#94a3b8; margin-bottom:4px;">CHAR 3</div>
            <div style="font-size:24px; font-weight:900; color:#fff;">H</div>
            <div style="font-size:11px; color:#00ff66; margin-top:4px;">- 7 &rarr; A</div>
          </div>
          <div style="background:#0b1329; border:2px solid #00ff66; border-radius:8px; padding:14px 22px; text-align:center;">
            <div style="font-size:11px; color:#94a3b8; margin-bottom:4px;">CHAR 4</div>
            <div style="font-size:24px; font-weight:900; color:#fff;">Y</div>
            <div style="font-size:11px; color:#00ff66; margin-top:4px;">- 7 &rarr; R</div>
          </div>
          <div style="background:#0b1329; border:2px solid #00ff66; border-radius:8px; padding:14px 22px; text-align:center;">
            <div style="font-size:11px; color:#94a3b8; margin-bottom:4px;">CHAR 5</div>
            <div style="font-size:24px; font-weight:900; color:#fff;">K</div>
            <div style="font-size:11px; color:#00ff66; margin-top:4px;">- 7 &rarr; D</div>
          </div>
        </div>

        <div style="text-align:center; margin-top:16px;">
          <button type="button" onclick="document.getElementById('r2-modal-passcode-input').value='GUARD'; submitRound2Code('GUARD');" class="btn-tactical success" style="background:#00ff66; color:#000; font-weight:900; padding:10px 24px; border:none; border-radius:4px; cursor:pointer;">
            ⚡ AUTO-FILL &amp; TRANSMIT AUTHORIZATION CODE: GUARD &rarr;
          </button>
        </div>
      </div>
    `
  }'''

# Define Stage 17: The Failsafe Logic Tree
stage_17_code = '''  17: {
    id: 17,
    round: 2,
    folderName: "R2_17_FAILSAFE",
    title: "The Failsafe Logic Tree",
    type: "logic",
    fileName: "Failsafe_Gate_Status.pdf",
    passwordPrompt: "ENTER 4-DIGIT HARDWARE STATE (1 for ON, 0 for OFF, e.g. 0110):",
    targetSelector: "#r2-failsafe-switches",
    taraPointerHint: "Evaluate Dr. Aditi's 4 hardware rules: Rule 4: Alpha = OFF (0). Rule 1: Alpha and Beta cannot both be OFF -> Beta = ON (1). Rule 3: Beta and Delta are opposite -> Delta = OFF (0). Rule 2: If Gamma is ON, Delta is OFF -> Gamma = ON (1). Enter 0110.",
    ishaanTaunt: "The physical interlocks are isolated from software override. You cannot align the 4 safety relays.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid #ffd700; border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,215,0,0.3); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(255,215,0,0.15); border-color:#ffd700; color:#ffd700; font-size:12px; padding:3px 8px;">ROUND 02 // PUZZLE 17 OF 17</span>
            <strong style="margin-left:8px; font-size:16px; letter-spacing:0.5px; color:#ffd700;">HARDWARE FAILSAFE ALIGNMENT (KILL SWITCH)</strong>
          </div>
          <span style="font-size:12px; color:#00ff88; border:1px solid #00ff88; padding:2px 8px; border-radius:3px;">GRAND FINALE</span>
        </div>

        <div style="background:rgba(255,215,0,0.05); border:1px solid rgba(255,215,0,0.25); border-radius:6px; padding:16px; margin-bottom:18px;">
          <h4 style="color:#ffd700; margin-bottom:8px; font-size:14px;">Failsafe_Gate_Status.pdf // Relay Rules</h4>
          <p style="font-size:13px; color:#cbd5e1; line-height:1.6; margin-bottom:12px;">
            To trigger the final manual kill switch, Dr. Aditi had to set 4 physical toggle switches (Alpha, Beta, Gamma, Delta) according to strict system rules before cutting power.
          </p>
          <div style="background:#020617; border:1px solid #334155; padding:12px 16px; border-radius:4px; font-size:13px; color:#f8fafc; line-height:1.8;">
            <strong style="color:#38bdf8;">SECURITY CONDITION RULES:</strong><br>
            1. Alpha and Beta cannot both be OFF.<br>
            2. If Gamma is ON, then Delta must be OFF.<br>
            3. Beta must be the exact OPPOSITE state of Delta (if Beta is ON, Delta is OFF).<br>
            4. <strong>Alpha is confirmed OFF (0).</strong>
          </div>
        </div>

        <div style="text-align:center; margin-bottom:12px; font-size:12px; color:#94a3b8;">
          CLICK TOGGLES TO CONFIGURE HARDWARE RELAYS (1 = ON, 0 = OFF):
        </div>

        <div style="display:flex; justify-content:center; gap:16px; margin:16px 0;">
          <button type="button" id="switch-alpha" onclick="toggleR2Switch('alpha')" style="background:#1e293b; border:2px solid #64748b; color:#fff; border-radius:8px; padding:14px 20px; cursor:pointer; font-family:monospace; min-width:90px;">
            <div style="font-size:11px; color:#94a3b8;">RELAY &alpha;</div>
            <div id="val-alpha" style="font-size:24px; font-weight:900; color:#ef4444; margin:4px 0;">0</div>
            <div style="font-size:10px; color:#64748b;">OFF</div>
          </button>
          <button type="button" id="switch-beta" onclick="toggleR2Switch('beta')" style="background:#1e293b; border:2px solid #22c55e; color:#fff; border-radius:8px; padding:14px 20px; cursor:pointer; font-family:monospace; min-width:90px;">
            <div style="font-size:11px; color:#94a3b8;">RELAY &beta;</div>
            <div id="val-beta" style="font-size:24px; font-weight:900; color:#22c55e; margin:4px 0;">1</div>
            <div style="font-size:10px; color:#22c55e;">ON</div>
          </button>
          <button type="button" id="switch-gamma" onclick="toggleR2Switch('gamma')" style="background:#1e293b; border:2px solid #22c55e; color:#fff; border-radius:8px; padding:14px 20px; cursor:pointer; font-family:monospace; min-width:90px;">
            <div style="font-size:11px; color:#94a3b8;">RELAY &gamma;</div>
            <div id="val-gamma" style="font-size:24px; font-weight:900; color:#22c55e; margin:4px 0;">1</div>
            <div style="font-size:10px; color:#22c55e;">ON</div>
          </button>
          <button type="button" id="switch-delta" onclick="toggleR2Switch('delta')" style="background:#1e293b; border:2px solid #64748b; color:#fff; border-radius:8px; padding:14px 20px; cursor:pointer; font-family:monospace; min-width:90px;">
            <div style="font-size:11px; color:#94a3b8;">RELAY &delta;</div>
            <div id="val-delta" style="font-size:24px; font-weight:900; color:#ef4444; margin:4px 0;">0</div>
            <div style="font-size:10px; color:#64748b;">OFF</div>
          </button>
        </div>

        <div style="text-align:center; margin-top:20px;">
          <button type="button" onclick="submitRound2Code('0110')" class="btn-tactical success" style="background:#ffd700; color:#000; font-weight:900; padding:12px 28px; border:none; border-radius:4px; cursor:pointer; box-shadow:0 0 20px rgba(255,215,0,0.6); font-size:14px;">
            🏆 TRANSMIT MASTER FAILSAFE STATE [0110] &rarr;
          </button>
        </div>
      </div>
    `
  }'''

# Assemble new ROUND2_PUZZLE_DATA
all_puzzles_list = [stage_1_code]
for i in range(2, 17):
    all_puzzles_list.append(shifted_puzzles[i])
all_puzzles_list.append(stage_1_code) # temporary placeholder, replace next line
all_puzzles_list[16] = stage_17_code

new_r2_data = "const ROUND2_PUZZLE_DATA = {\n" + ",\n".join(all_puzzles_list) + "\n};"

text = text[:idx_start] + new_r2_data + text[idx_end+3:]

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully rebuilt ROUND2_PUZZLE_DATA with 17 puzzles!")
