import sys
sys.stdout.reconfigure(encoding='utf-8')

# ==========================================
# 1. PATCH SERVER.PY
# ==========================================
with open('server.py', 'r', encoding='utf-8') as f:
    server_code = f.read()

# Replace current_stage: 15 with 21 in default finish team object
server_code = server_code.replace(
    '"current_stage": 15,\n                    "unlocked_stages": list(range(1, 16)),',
    '"current_stage": 21,\n                    "unlocked_stages": list(range(1, 22)),'
)

# Replace round_2_stage = 15 with 17
server_code = server_code.replace(
    'team["round_2_stage"] = 15',
    'team["round_2_stage"] = 17\n                    team["round_2_unlocked_stages"] = list(range(1, 18))'
)

# Replace current_stage = 15 with 21 for round 1 finish
server_code = server_code.replace(
    'team["current_stage"] = 15',
    'team["current_stage"] = 21\n                    team["unlocked_stages"] = list(range(1, 22))'
)

with open('server.py', 'w', encoding='utf-8') as f:
    f.write(server_code)
print("Updated server.py finish endpoint stage numbers (R1: 21, R2: 17)")


# ==========================================
# 2. PATCH ADMIN.HTML
# ==========================================
with open('admin.html', 'r', encoding='utf-8') as f:
    admin_code = f.read()

admin_code = admin_code.replace(
    'const isR1Finished = !!t.is_finished || (parseInt(t.current_stage || 1, 10) >= 16);',
    'const isR1Finished = !!t.is_finished || (parseInt(t.current_stage || 1, 10) >= 21);'
)

admin_code = admin_code.replace(
    'const isFinished = t ? (t.is_finished || t.current_stage >= 16) : true;',
    'const isFinished = t ? (t.is_finished || t.current_stage >= 21) : true;'
)

admin_code = admin_code.replace(
    'const finishedTeams = cachedTeams.filter(t => t.is_finished || t.current_stage >= 16);',
    'const finishedTeams = cachedTeams.filter(t => t.is_finished || t.current_stage >= 21);'
)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_code)
print("Updated admin.html R1 finish thresholds to >= 21")


# ==========================================
# 3. PATCH ADITI_OS_WIDGET.HTML
# ==========================================
with open('aditi_os_widget.html', 'r', encoding='utf-8') as f:
    widget_code = f.read()

# A. Current stage bounds
widget_code = widget_code.replace(
    'if (isNaN(currentStage) || currentStage < 1 || currentStage > 16) currentStage = 1;',
    'if (isNaN(currentStage) || currentStage < 1 || currentStage > 21) currentStage = 1;'
)

# B. recordStageCleared nextStage bounds
widget_code = widget_code.replace(
    'const nextStage = stageNum + 1;\n      if (nextStage <= 16) {',
    'const nextStage = stageNum + 1;\n      if (nextStage <= 21) {'
)

# C. renderStageTimeBreakdownHTML loop
widget_code = widget_code.replace(
    'for (let s = 1; s <= 16; s++) {\n        const item = stageTimes[s];',
    'for (let s = 1; s <= 21; s++) {\n        const item = stageTimes[s];'
)

# D. applyAuthenticatedTeam stage bound
widget_code = widget_code.replace(
    'if (team.current_stage && team.current_stage >= 1 && team.current_stage <= 16) {',
    'if (team.current_stage && team.current_stage >= 1 && team.current_stage <= 21) {'
)

# E. handleUnlockAllLevelsTriggered loop and r2 array
widget_code = widget_code.replace(
    'for (let s = 1; s <= 16; s++) {\n        const meta = NEXUS_STAGES_META[s];',
    'for (let s = 1; s <= 21; s++) {\n        const meta = NEXUS_STAGES_META[s];'
)
widget_code = widget_code.replace(
    'round2StagesCleared = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15];',
    'round2StagesCleared = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17];'
)

# F. r1FullyFinished check
widget_code = widget_code.replace(
    'const r1FullyFinished = (storedR1Stage >= 16 && localStorage.getItem(\'failsafe_r1_done\') === \'true\');',
    'const r1FullyFinished = (storedR1Stage >= 21 && localStorage.getItem(\'failsafe_r1_done\') === \'true\');'
)

# G. handleMissionVictorySequence strings and flags
widget_code = widget_code.replace(
    'logTerm(`🏆 ALL 16 FORENSIC STAGES RESOLVED IN ${elapsedStr}!`, "green");',
    'logTerm(`🏆 ALL 21 FORENSIC STAGES RESOLVED IN ${elapsedStr}!`, "green");'
)
widget_code = widget_code.replace(
    'reportTelemetryAction(`🏆 Solved all 16 stages in ${elapsedStr}! Awaiting TARA liberation.`);',
    'reportTelemetryAction(`🏆 Solved all 21 stages in ${elapsedStr}! Awaiting TARA liberation.`);'
)
widget_code = widget_code.replace(
    'localStorage.setItem("failsafe_mission_completed", "true");',
    'localStorage.setItem("failsafe_mission_completed", "true");\n      localStorage.setItem("failsafe_r1_done", "true");\n      localStorage.setItem("failsafe_stage", "21");\n      localStorage.setItem("failsafe_current_stage", "21");'
)

# H. handleRound2GrandVictory string
widget_code = widget_code.replace(
    'logTerm("👑 ALL 15 ORBITAL OLYMPIAD CIPHERS MASTERED. ISHAAN PURGED FROM SATELLITE ARRAY.", "green");',
    'logTerm("👑 ALL 17 ORBITAL OLYMPIAD CIPHERS MASTERED. ISHAAN PURGED FROM SATELLITE ARRAY.", "green");'
)

with open('aditi_os_widget.html', 'w', encoding='utf-8') as f:
    f.write(widget_code)
print("Updated aditi_os_widget.html track completion logic for R1 (21) & R2 (17)")
