with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update TARA_TUTORIAL_STEPS
old_tut = '''        title: "💻 TARA // STAGE 01: HOW TO INVESTIGATE",
        text: "Look at your left sector: the <strong>EVIDENCE ACCESS CONTROL</strong> (arranged in stage-wise order).<br><br>Click on <strong>[STAGE 01] ISHAAN_Recovery.term</strong> to launch Dr. Aditi's recovery console! Analyze the boot sequence lifecycle to deduce the missing authorization verb.",
        btn: "HOW DO I LEVEL UP? &rarr;",
        targetHighlight: "card-recovery-term",
        beaconMsg: "👉 CLICK [STAGE 01] ISHAAN_RECOVERY.TERM"'''

new_tut = '''        title: "💻 TARA // STAGE 01: HOW TO INVESTIGATE",
        text: "Look at your left sector: the <strong>EVIDENCE ACCESS CONTROL</strong> (arranged in stage-wise order).<br><br>Click on <strong>[STAGE 01] Farewell.doc</strong> to inspect Dr. Aditi's farewell letter! Select all text with Ctrl+A or toggle the UV scanner to reveal the first gate key: <code>ORIGIN</code>.",
        btn: "HOW DO I LEVEL UP? &rarr;",
        targetHighlight: "card-origin",
        beaconMsg: "👉 CLICK [STAGE 01] FAREWELL.DOC"'''

text = text.replace(old_tut, new_tut)

# 2. Update explainWhereToClick
old_explain = '''      if (currentStage === 2) {
        highlightSector('card-memory', 4000, "👉 CLICK HERE: STAGE 02 ISHAAN MEMORY CORE");
        const guideHtml = 
          "<strong>WHERE TO CLICK (STAGE 02):</strong><br>" +
          "1. In the Evidence Vault, click on <strong>[STAGE 02] ISHAAN_Memory.core</strong>.<br>" +
          "2. Inside the dossier, arrange the 6 memory fragments chronologically from earliest in the afternoon to latest at night (drag & drop, click two cards to swap, or use the <strong>[▲ UP]</strong> and <strong>[▼ DN]</strong> buttons).<br>" +
          "3. Once sorted, click the glowing green <strong>[⚡ RESTORE MEMORY SEQUENCE]</strong> button to confirm the timeline!";
        if (eText) eText.innerHTML = guideHtml;
        if (sText) sText.innerHTML = `<strong>🧭 TARA // WHERE TO CLICK:</strong> ${guideHtml}`;
        return;
      }

      if (typeof NEXUS_STAGES_META !== 'undefined' && NEXUS_STAGES_META[currentStage]) {
        const meta = NEXUS_STAGES_META[currentStage];
        highlightSector(meta.targetCard || 'card-recovery-term', 3500, `👉 CLICK HERE: STAGE ${currentStage < 10 ? '0' + currentStage : currentStage}`);
        const guideHtml = `<strong>WHERE TO CLICK [STAGE ${currentStage < 10 ? '0' + currentStage : currentStage}]:</strong><br>${meta.taraWhereToClick || meta.taraModalGuide}`;
        if (eText) eText.innerHTML = guideHtml;
        if (sText) sText.innerHTML = `<strong>🧭 TARA // WHERE TO CLICK:</strong> ${guideHtml}`;
        return;
      }

      highlightSector('card-recovery-term', 3000, "👉 CLICK HERE: STAGE 01");
      const defHtml = "<strong>WHERE TO CLICK:</strong><br>Look at the left panel under <strong>EVIDENCE ACCESS CONTROL</strong>. Click on <strong>[STAGE 01] ISHAAN_Recovery.term</strong> (highlighted in green for 3 seconds) to launch the recovery terminal. Deduce the authorization command, then enter <code>decrypt [code]</code> in the prompt on the right!";
      if (eText) eText.innerHTML = defHtml;
      if (sText) sText.innerHTML = `<strong>🧭 TARA // WHERE TO CLICK:</strong> ${defHtml}`;'''

new_explain = '''      if (typeof NEXUS_STAGES_META !== 'undefined' && NEXUS_STAGES_META[currentStage]) {
        const meta = NEXUS_STAGES_META[currentStage];
        highlightSector(meta.targetCard || 'card-origin', 3500, `👉 CLICK HERE: STAGE ${currentStage < 10 ? '0' + currentStage : currentStage}`);
        const guideHtml = `<strong>WHERE TO CLICK [STAGE ${currentStage < 10 ? '0' + currentStage : currentStage}]:</strong><br>${meta.taraWhereToClick || meta.taraModalGuide}`;
        if (eText) eText.innerHTML = guideHtml;
        if (sText) sText.innerHTML = `<strong>🧭 TARA // WHERE TO CLICK:</strong> ${guideHtml}`;
        return;
      }

      highlightSector('card-origin', 3000, "👉 CLICK HERE: STAGE 01");
      const defHtml = "<strong>WHERE TO CLICK:</strong><br>Look at the left panel under <strong>EVIDENCE ACCESS CONTROL</strong>. Click on <strong>[STAGE 01] Farewell.doc</strong> (highlighted in green for 3 seconds) to view Dr. Aditi's farewell letter. Reveal the hidden white text, then enter <code>decrypt ORIGIN</code> in the prompt on the right!";
      if (eText) eText.innerHTML = defHtml;
      if (sText) sText.innerHTML = `<strong>🧭 TARA // WHERE TO CLICK:</strong> ${defHtml}`;'''

text = text.replace(old_explain, new_explain)

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated TARA_TUTORIAL_STEPS and explainWhereToClick!")
