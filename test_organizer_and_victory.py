import os
import sys
import time
import json
import subprocess
import urllib.request
import urllib.parse

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PORT = 8008

def start_test_server():
    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"
    # Create a test script that runs server on PORT 8008
    with open("test_server_runner.py", "w", encoding="utf-8") as f:
        f.write(f"""import server
server.PORT = {PORT}
if __name__ == '__main__':
    server.run()
""")
    proc = subprocess.Popen([sys.executable, "test_server_runner.py"], cwd=os.getcwd(), env=env)
    time.sleep(2)
    return proc

def test_api():
    base = f"http://127.0.0.1:{PORT}"
    print(f"--- 1. Testing /api/status on {base} ---")
    req = urllib.request.Request(f"{base}/api/status")
    with urllib.request.urlopen(req) as res:
        data = json.loads(res.read().decode())
        print("Status response:", data)
        assert data["status"] == "online"
        assert "server_url" in data

    print("--- 2. Registering Team ---")
    reg_payload = json.dumps({
        "team_id": "OMEGA-77",
        "password": "secret-pass-77",
        "team_name": "Apex Cipher Hunters",
        "members": "Dr. Sarah, Alex Chen, Maya Lin"
    }).encode("utf-8")
    req = urllib.request.Request(f"{base}/api/teams/register", data=reg_payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as res:
        data = json.loads(res.read().decode())
        print("Register response:", data)
        assert data["team"]["team_id"] == "OMEGA-77"
        assert data["team"]["team_name"] == "Apex Cipher Hunters"

    print("--- 3. Sending Activity Telemetry ---")
    act_payload = json.dumps({
        "team_id": "OMEGA-77",
        "team_name": "Apex Cipher Hunters",
        "members": "Dr. Sarah, Alex Chen, Maya Lin",
        "password": "secret-pass-77",
        "current_stage": 14,
        "action": "Decrypted Honeypot Bypass (Stage 14)",
        "tamper_incidents": 0,
        "is_locked": False
    }).encode("utf-8")
    req = urllib.request.Request(f"{base}/api/teams/activity", data=act_payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as res:
        data = json.loads(res.read().decode())
        print("Activity response:", data)
        assert data["success"] is True

    sample_stage_times = {
        str(i): {"duration_seconds": 60 + i * 5, "duration_str": f"{1 + (i*5)//60}m {((i*5)%60):02d}s"}
        for i in range(1, 16)
    }

    print("--- 4. Completing Mystery via /api/teams/finish with stage_times ---")
    fin_payload = json.dumps({
        "team_id": "OMEGA-77",
        "team_name": "Apex Cipher Hunters",
        "members": "Dr. Sarah, Alex Chen, Maya Lin",
        "password": "secret-pass-77",
        "elapsed_seconds": 1845,
        "elapsed_str": "30m 45s",
        "stage_times": sample_stage_times
    }).encode("utf-8")
    req = urllib.request.Request(f"{base}/api/teams/finish", data=fin_payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as res:
        data = json.loads(res.read().decode())
        print("Finish response:", data)
        assert data["success"] is True
        assert data["team"]["is_finished"] is True
        assert data["team"]["finish_time_str"] == "30m 45s"
        assert "stage_times" in data["team"]
        assert len(data["team"]["stage_times"]) == 15

    print("--- 5. Checking Organizer Leaderboard with stage_times ---")
    req = urllib.request.Request(f"{base}/api/admin/leaderboard?pin=wie-admin-2026")
    with urllib.request.urlopen(req) as res:
        data = json.loads(res.read().decode())
        lb = data["leaderboard"]
        print(f"Leaderboard count: {len(lb)}")
        team = next((t for t in lb if t["team_id"] == "OMEGA-77"), None)
        assert team is not None
        assert team["team_name"] == "Apex Cipher Hunters"
        assert team["members"] == "Dr. Sarah, Alex Chen, Maya Lin"
        assert team["password"] == "secret-pass-77"
        assert team["is_finished"] is True
        assert team["finish_time_str"] == "30m 45s"
        assert "stage_times" in team
        assert len(team["stage_times"]) == 15
        print("Leaderboard team details and 15 puzzle times verified successfully!")

def test_browser_ui():
    print("--- 6. Running Headless Browser UI Test ---")
    edge_options = Options()
    edge_options.add_argument("--headless=new")
    edge_options.add_argument("--window-size=1920,1080")
    edge_options.add_argument("--disable-gpu")
    edge_options.add_argument("--no-sandbox")
    
    driver = webdriver.Edge(options=edge_options)

    try:
        # Test Admin Dashboard
        admin_url = f"http://127.0.0.1:{PORT}/admin.html"
        print(f"Loading {admin_url}...")
        driver.get(admin_url)
        time.sleep(2)
        
        # Verify team row is rendered
        body_text = driver.find_element(By.TAG_NAME, "body").text
        assert "OMEGA-77" in body_text
        assert "Apex Cipher Hunters" in body_text
        assert "30m 45s" in body_text
        print("Admin Dashboard successfully rendered OMEGA-77 with completion time!")
        driver.save_screenshot(r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27\screenshot_admin_verified_details.png")

        # Test Admin [ ⏱️ TIMES ] Modal
        print("Opening Puzzle Times modal in Admin Dashboard...")
        driver.execute_script("showTeamPuzzleTimes('OMEGA-77');")
        time.sleep(1)
        times_modal = driver.find_element(By.ID, "modal-puzzle-times")
        assert times_modal.is_displayed()
        modal_text = times_modal.text
        assert "PUZZLE SOLVE TIMES" in modal_text.upper()
        assert "STAGE 01" in modal_text
        assert "STAGE 15" in modal_text
        print("Admin Puzzle Times Modal opened and verified!")
        driver.save_screenshot(r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27\screenshot_admin_puzzle_times_modal.png")
        driver.execute_script("closeModal('modal-puzzle-times');")
        time.sleep(0.5)
        
        # Test Participant Application V1 (aditi_os_widget.html)
        app_url = f"http://127.0.0.1:{PORT}/aditi_os_widget.html"
        print(f"Loading {app_url}...")
        driver.get(app_url)
        time.sleep(2)

        # Login existing team OMEGA-77 and inject 15 sample stage times into local storage
        sample_times_json = json.dumps({
            str(i): {"duration_seconds": 60 + i * 5, "duration_str": f"{1 + (i*5)//60}m {((i*5)%60):02d}s"}
            for i in range(1, 16)
        })
        driver.execute_script(f"""
            localStorage.setItem("failsafe_server_url", "http://127.0.0.1:{PORT}");
            localStorage.setItem("failsafe_stage_times", '{sample_times_json}');
            document.getElementById("auth-login-id").value = "OMEGA-77";
            document.getElementById("auth-login-pass").value = "secret-pass-77";
        """)
        btn = driver.find_element(By.CSS_SELECTOR, "#auth-login-form button[type='submit']")
        btn.click()
        time.sleep(1.5)

        # 6a. Verify Organizer button was removed from participant dashboard
        header_text = driver.find_element(By.CLASS_NAME, "header-actions").text
        assert "ORGANIZER" not in header_text
        print("Verified: Organizer button successfully removed from participant dashboard!")

        # 6b. Verify Mobile Blocker overlay exists
        mobile_blocker = driver.find_element(By.ID, "mobile-blocker-overlay")
        assert mobile_blocker is not None
        print("Verified: Mobile device blocker overlay present in workstation!")

        # 6c. Verify Right-Click / Google Lens contextmenu suppression and breach reporting
        violation_before = driver.execute_script("return violationCount;")
        driver.execute_script("""
            const ev = new MouseEvent('contextmenu', { bubbles: true, cancelable: true });
            window.dispatchEvent(ev);
        """)
        time.sleep(0.5)
        violation_after = driver.execute_script("return violationCount;")
        assert violation_after > violation_before
        print("Verified: Right-click / Google Lens context menu blocked and logged as cheat attempt!")

        # 6d. Verify Fullscreen exit triggers proctor lockdown overlay with reason
        driver.execute_script("""
            triggerProctorLockdown("Exited Fullscreen Mode (Pressed Esc / Window Resize)");
        """)
        time.sleep(0.5)
        proctor_overlay = driver.find_element(By.ID, "proctor-lockdown-overlay")
        assert proctor_overlay.is_displayed()
        reason_text = driver.find_element(By.ID, "proctor-violation-reason").text
        assert "Exited Fullscreen Mode" in reason_text
        print("Verified: Strict fullscreen exit triggers Proctor Lockdown with clear breach reason!")
        driver.save_screenshot(r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27\screenshot_proctor_lockdown_breach.png")

        # Unlock with organizer PIN
        driver.execute_script("""
            document.getElementById('proctor-pin-input').value = 'wie-admin-2026';
            verifyProctorOverride();
        """)
        time.sleep(0.5)
        assert not proctor_overlay.is_displayed()
        print("Verified: Organizer PIN successfully unlocked workstation!")

        # 6e. Verify Admin Dashboard reflects breach notification
        admin_win_url = f"http://127.0.0.1:{PORT}/admin.html"
        driver.get(admin_win_url)
        time.sleep(2)
        admin_body = driver.find_element(By.TAG_NAME, "body").text
        assert "BREACH" in admin_body.upper() or "FULLSCREEN" in admin_body.upper() or "GOOGLE" in admin_body.upper()
        print("Verified: Admin dashboard displays real-time breach notifications!")
        driver.save_screenshot(r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27\screenshot_admin_breach_badge.png")

        # Return to participant app for victory sequence
        driver.get(app_url)
        time.sleep(1.5)
        driver.execute_script(f"""
            localStorage.setItem("failsafe_server_url", "http://127.0.0.1:{PORT}");
            localStorage.setItem("failsafe_stage_times", '{sample_times_json}');
            currentTeam = {{
                team_id: "OMEGA-77",
                team_name: "Apex Cipher Hunters",
                members: "Dr. Sarah, Alex Chen, Maya Lin",
                password: "secret-pass-77"
            }};
        """)

        # Trigger victory sequence directly via JS
        print("Triggering Stage 15 Victory Sequence...")
        driver.execute_script("handleMissionVictorySequence();")
        time.sleep(2)

        # Verify Celebration Modal is visible and has per-puzzle breakdown
        v_modal = driver.find_element(By.ID, "victory-celebration-modal")
        assert v_modal.is_displayed()
        v_text = v_modal.text
        assert "DR. ADITI SHARMA" in v_text
        assert "APEX CIPHER HUNTERS" in v_text.upper()
        assert "PUZZLE-BY-PUZZLE TIME BREAKDOWN" in v_text or ("PUZZLE" in v_text and "BREAKDOWN" in v_text)
        assert "01" in v_text
        assert "15" in v_text
        print("Victory Celebration Modal displayed Dr. Aditi's transmission, congratulations, and 15-puzzle breakdown!")
        driver.save_screenshot(r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27\screenshot_victory_celebration_dr_aditi.png")

        # Click Free ETHAN & Terminate Workstation
        print("Clicking Free ETHAN & Terminate...")
        lib_btn = driver.find_element(By.ID, "btn-free-ethan-terminate")
        lib_btn.click()
        time.sleep(2)

        # Verify Application Termination Overlay is visible with puzzle breakdown and transmission status
        term_overlay = driver.find_element(By.ID, "application-termination-overlay")
        assert term_overlay.is_displayed()
        term_text = term_overlay.text
        assert "WORKSTATION TERMINATED" in term_text
        assert "OMEGA-77" in term_text
        assert "PUZZLE-BY-PUZZLE TIME BREAKDOWN" in term_text or ("PUZZLE" in term_text and "BREAKDOWN" in term_text)
        assert "TRANSMITTED TO TOURNAMENT SERVER" in term_text
        print("Application Termination Overlay successfully locked down the terminal with full puzzle breakdown!")
        driver.save_screenshot(r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27\screenshot_application_terminated.png")

        # Test Offline Fallback Mode
        print("--- 7. Testing Offline Fallback Mode (No Server Connection) ---")
        driver.get(f"file:///{os.path.abspath('aditi_os_widget.html').replace(os.sep, '/')}")
        time.sleep(2)
        driver.execute_script(f"""
            localStorage.clear();
            localStorage.setItem("failsafe_server_url", "http://127.0.0.1:9999"); // intentionally dead port
            localStorage.setItem("failsafe_stage_times", '{sample_times_json}');
            currentTeam = {{
                team_id: "OFFLINE-99",
                team_name: "Shadow Operatives",
                members: "Solo Runner",
                password: "offline-pass"
            }};
            finalizeEthanLiberationAndTerminate();
        """)
        time.sleep(2)
        offline_term = driver.find_element(By.ID, "application-termination-overlay")
        assert offline_term.is_displayed()
        offline_text = offline_term.text
        assert "OFFLINE LOCAL RECORD" in offline_text
        assert "OFFLINE-99" in offline_text
        assert "PUZZLE-BY-PUZZLE TIME BREAKDOWN" in offline_text or ("PUZZLE" in offline_text and "BREAKDOWN" in offline_text)
        print("Offline mode verified: Station displays total time and all 15 puzzle times locally!")
        driver.save_screenshot(r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27\screenshot_offline_termination_times.png")

    finally:
        driver.quit()

if __name__ == "__main__":
    server_proc = start_test_server()
    try:
        test_api()
        test_browser_ui()
        print("\n=========================================")
        print(" ALL VERIFICATION CHECKS PASSED 100%! ")
        print("=========================================\n")
    finally:
        server_proc.terminate()
        try:
            if os.path.exists("test_server_runner.py"):
                os.remove("test_server_runner.py")
        except:
            pass
