import time
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opts = Options()
opts.add_argument("--headless=new")
opts.add_argument("--window-size=1600,1050")
opts.add_argument("--disable-web-security")
opts.add_argument("--user-data-dir=C:/Users/shrey/AppData/Local/Temp/chrome_test_profile_" + str(int(time.time())))

driver = webdriver.Chrome(options=opts)

try:
    print("Navigating to http://127.0.0.1:8000/aditi_os_widget.html...")
    driver.get("http://127.0.0.1:8000/aditi_os_widget.html")
    time.sleep(2)

    # Initialize test state
    driver.execute_script("""
        localStorage.clear();
        sessionStorage.clear();
        localStorage.setItem('failsafe_stage', '1');
        localStorage.setItem('failsafe_penalty_seconds', '0');
        const auth = document.getElementById('team-auth-modal');
        if (auth) auth.style.display = 'none';
        if (typeof updateNexusDashboard === 'function') updateNexusDashboard();
    """)
    time.sleep(0.5)

    print("\n--- TEST 1: STAGE 1 TRANSMIT KEY ---")
    driver.execute_script("openModal('modal-origin');")
    time.sleep(0.5)

    res1 = driver.execute_script("""
        const inp = document.getElementById('input-stage-1');
        const btn = inp ? inp.nextElementSibling : null;
        if (!inp || !btn) return { error: 'elements missing' };
        inp.value = 'ORIGIN';
        btn.click();
        return {
            typed: inp.value,
            fb: (document.getElementById('fb-stage-1') || {}).innerText
        };
    """)
    print("Stage 1 click result:", res1)
    time.sleep(0.6)

    after1 = driver.execute_script("""
        return {
            stage: currentStage,
            fb1: (document.getElementById('fb-stage-1') || {}).innerText
        };
    """)
    print("Stage 1 after 600ms:", after1)
    assert after1["stage"] == 2, f"Expected Stage 2, got {after1['stage']}"
    print("✓ Stage 1 Transmit Key PASSED!")

    print("\n--- TEST 2: STAGE 4 MURDER MYSTERY (22:45) ---")
    driver.execute_script("""
        setStage(4);
        openModal('modal-security-audit');
    """)
    time.sleep(0.5)

    res4 = driver.execute_script("""
        const inp = document.getElementById('input-stage-4');
        const btn = inp ? inp.nextElementSibling : null;
        if (!inp || !btn) return { error: 'elements missing' };
        inp.value = '22:45';
        btn.click();
        return {
            typed: inp.value,
            fb: (document.getElementById('fb-stage-4') || {}).innerText
        };
    """)
    print("Stage 4 click result:", res4)
    time.sleep(0.6)

    after4 = driver.execute_script("""
        return {
            stage: currentStage,
            fb4: (document.getElementById('fb-stage-4') || {}).innerText
        };
    """)
    print("Stage 4 after 600ms:", after4)
    assert after4["stage"] == 5, f"Expected Stage 5, got {after4['stage']}"
    print("✓ Stage 4 Transmit Key (22:45) PASSED!")

    print("\n--- TEST 3: STAGE 6 FONT SIZE (11pt) & SPACING (1.15) & TRANSMIT KEY ---")
    driver.execute_script("""
        setStage(6);
        openModal('modal-font');
    """)
    time.sleep(0.5)

    font_check = driver.execute_script("""
        const authLog = document.getElementById('tab-content-auth-log');
        const decoyLog = document.getElementById('tab-content-decoy-log');
        return {
            authStyle: authLog ? authLog.getAttribute('style') : null,
            decoyStyle: decoyLog ? decoyLog.getAttribute('style') : null
        };
    """)
    print("Font style attributes:", json.dumps(font_check, indent=2))
    assert "11pt" in font_check["authStyle"] and "1.15" in font_check["authStyle"], "Auth log missing 11pt/1.15"
    assert "11pt" in font_check["decoyStyle"] and "1.15" in font_check["decoyStyle"], "Decoy log missing 11pt/1.15"
    print("✓ Both logs verified with 11pt and 1.15 spacing!")

    res6 = driver.execute_script("""
        const inp = document.getElementById('input-stage-6');
        const btn = inp ? inp.nextElementSibling : null;
        if (!inp || !btn) return { error: 'elements missing' };
        inp.value = 'ARIAL';
        btn.click();
        return {
            typed: inp.value,
            fb: (document.getElementById('fb-stage-6') || {}).innerText
        };
    """)
    print("Stage 6 click result:", res6)
    time.sleep(0.6)

    after6 = driver.execute_script("""
        return {
            stage: currentStage,
            fb6: (document.getElementById('fb-stage-6') || {}).innerText
        };
    """)
    print("Stage 6 after 600ms:", after6)
    assert after6["stage"] == 7, f"Expected Stage 7, got {after6['stage']}"
    print("✓ Stage 6 Transmit Key (ARIAL) PASSED!")

    print("\n--- TEST 4: STAGE 10 HONEYPOT (+5 MIN PENALTY ON OPEN & ADVANCE) ---")
    driver.execute_script("""
        setStage(10);
        localStorage.setItem('failsafe_penalty_seconds', '0');
        sessionStorage.clear();
    """)
    pen_before = driver.execute_script("return parseInt(localStorage.getItem('failsafe_penalty_seconds') || '0', 10);")
    print("Penalty seconds before opening honeypot:", pen_before)

    # Opening modal-honeypot
    driver.execute_script("openModal('modal-honeypot');")
    time.sleep(0.5)

    pen_after = driver.execute_script("return parseInt(localStorage.getItem('failsafe_penalty_seconds') || '0', 10);")
    print("Penalty seconds immediately upon opening honeypot:", pen_after)
    assert pen_after >= 300, f"Expected penalty >= 300s (+5m), got {pen_after}"
    print("✓ Immediate +5 minute (+300s) penalty on honeypot open verified!")

    # Verify bypass input is gone
    bypass_exists = driver.execute_script("return !!document.getElementById('input-honeypot-bypass');")
    print("Old bypass input exists?", bypass_exists)
    assert not bypass_exists, "Old bypass input should be removed!"

    # Click [⚡ ACKNOWLEDGE PENALTY & ADVANCE TO STAGE 11 →]
    driver.execute_script("submitHoneypotAdvance();")
    time.sleep(0.6)

    after10 = driver.execute_script("""
        return {
            stage: currentStage,
            fb10: (document.getElementById('fb-stage-10') || {}).innerText
        };
    """)
    print("Stage 10 after advance:", after10)
    assert after10["stage"] == 11, f"Expected Stage 11, got {after10['stage']}"
    print("✓ Stage 10 Honeypot Penalty & Advance to Stage 11 PASSED!")

    print("\n🎉 ALL USER REQUIREMENTS VERIFIED AND PASSING 100%!")

finally:
    driver.quit()
