import re

with open("aditi_os_widget.html", "r", encoding="utf-8") as f:
    html = f.read()

# Map of Stage numbers to Modal IDs and Card IDs based on NEXUS_STAGES_META
stages_meta = {
    1: {"card": "card-recovery-term", "modal": "modal-recovery", "name": "ISHAAN_Recovery.term"},
    2: {"card": "card-memory", "modal": "modal-memory", "name": "ISHAAN_Memory.core"},
    3: {"card": "card-acrostic", "modal": "modal-acrostic", "name": "Aditi_Memo.doc"},
    4: {"card": "card-packet", "modal": "modal-packet", "name": "Packet_Capture.pcap"},
    5: {"card": "card-b64", "modal": "modal-b64", "name": "Base64_Payload.enc"},
    6: {"card": "card-metadata", "modal": "modal-metadata", "name": "System_Diagnostics.doc"},
    7: {"card": "card-typography", "modal": "modal-typography", "name": "AUTHENTIC_LOG.doc"},
    8: {"card": "card-caesar", "modal": "modal-caesar", "name": "ISHAAN_Audio_Intercept.wav"},
    9: {"card": "card-binary", "modal": "modal-binary", "name": "Failsafe_Git_Commit.log"},
    10: {"card": "card-logic", "modal": "modal-logic", "name": "Primary_Directive.auth"},
    11: {"card": "card-radar", "modal": "modal-radar", "name": "Core_Values_Security.dossier"},
    12: {"card": "card-whiteout", "modal": "modal-whiteout", "name": "Emergency_Log.doc"},
    13: {"card": "card-rot4", "modal": "modal-rot4", "name": "ROT-4 Cipher Intercept"},
    14: {"card": "card-atbash", "modal": "modal-atbash", "name": "Atbash Inversion Stream"},
    15: {"card": "card-polybius", "modal": "modal-polybius", "name": "Polybius Matrix Cache"},
    16: {"card": "card-freq", "modal": "modal-freq", "name": "Frequency Distribution Analysis"}
}

print(f"{'STAGE':<8} | {'CARD ID':<22} | {'MODAL ID':<18} | {'CLICK DIR':<10} | {'SUBMIT DIR':<10} | {'INPUT ELEM':<10}")
print("-" * 90)

for s, info in stages_meta.items():
    modal_id = info["modal"]
    start = html.find(f'id="{modal_id}"')
    if start == -1:
        start = html.find(f"id='{modal_id}'")
    
    if start == -1:
        print(f"Stage {s:02d} | {info['card']:<22} | {modal_id:<18} | NOT FOUND!")
        continue
    
    # take next 4000 characters
    chunk = html[start:start+4500]
    has_click = "WHERE TO CLICK" in chunk
    has_submit = "WHERE TO SUBMIT" in chunk
    has_input = ("<input" in chunk or "submitStageDirectKey" in chunk or "type=\"text\"" in chunk or "prompt-input" in chunk or "TRANSMIT" in chunk)
    print(f"Stage {s:02d} | {info['card']:<22} | {modal_id:<18} | {str(has_click):<10} | {str(has_submit):<10} | {str(has_input):<10}")
