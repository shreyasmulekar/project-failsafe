"""
verify_round1_to_round2_flow.py
Verifies end-to-end organizer control for promoting participants from Round 1 to Round 2
after completing all puzzles in Round 1.
"""
import time
import os
import sys
import json
import urllib.request
from selenium import webdriver
from selenium.webdriver.edge.options import Options

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

SERVER_URL = "http://localhost:8000"
ARTIFACT_DIR = r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27"

def run_round1_to_round2_verification():
    edge_options = Options()
    edge_options.add_argument("--headless=new")
    edge_options.add_argument("--disable-gpu")
    edge_options.add_argument("--window-size=1920,1080")
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Edge(options=edge_options)

    try:
        unique_suffix = str(int(time.time()))[-4:]
        team_id = f"PHANTOM-{unique_suffix}"
        team_name = f"Phantom Squad {unique_suffix}"
        pin = "wie-admin-2026"
        print(f"[1/6] Initializing Test Team [{team_id}] and marking Round 1 as Cleared...")

        # Register and complete Round 1 via API
        req_data = json.dumps({
            "team_id": team_id,
            "team_name": team_name,
            "members": "Dr. Miller, Cmdr. Shepard",
            "password": "CYBER-PASS-2026",
            "current_stage": 16,
            "is_finished": True,
            "finish_time_str": "42m 15s",
            "action": "🏆 Cleared all 16 Round 1 Stages! Standing by for Round 2."
        }).encode("utf-8")
        req = urllib.request.Request(f"{SERVER_URL}/api/teams/activity", data=req_data, headers={"Content-Type": "application/json"})
        urllib.request.urlopen(req)

        # Also register finish
        finish_data = json.dumps({
            "team_id": team_id,
            "team_name": team_name,
            "members": "Dr. Miller, Cmdr. Shepard",
            "password": "CYBER-PASS-2026",
            "elapsed_seconds": 2535,
            "elapsed_str": "42m 15s"
        }).encode("utf-8")
        finish_req = urllib.request.Request(f"{SERVER_URL}/api/teams/finish", data=finish_data, headers={"Content-Type": "application/json"})
        urllib.request.urlopen(finish_req)
        print("  ✓ Team registered and marked as finished Round 1.")

        print("[2/6] Loading Organizer Command Center...")
        driver.get(f"{SERVER_URL}/admin.html")
        time.sleep(1.5)

        driver.execute_script("""
            sessionStorage.setItem("failsafe_admin_authenticated", "true");
            sessionStorage.setItem("admin_pin", "wie-admin-2026");
            const modal = document.getElementById("admin-login-modal");
            if (modal) modal.style.display = "none";
            fetchLeaderboardData();
        """)
        time.sleep(2)

        # Verify Top Action Bar has the new [🚀 SEND FINISHED TO R2] button
        send_all_btn = driver.execute_script("""
            const btn = document.getElementById('btn-send-finished-r2');
            return btn ? btn.innerText : '';
        """)
        print(f"  Top Action Bar Button: '{send_all_btn}'")
        assert "SEND FINISHED TO R2" in send_all_btn, f"Expected SEND FINISHED TO R2 in top bar, got: {send_all_btn}"

        # Inspect table rows for team_id
        table_text = driver.execute_script("""
            const tbody = document.getElementById('teams-table-body');
            return tbody ? tbody.innerText : '';
        """)
        assert team_id in table_text, f"Expected {team_id} in leaderboard table"
        assert "R1 CLEARED (READY FOR R2)" in table_text, "Expected 'R1 CLEARED (READY FOR R2)' stage badge"
        print(f"  ✓ Stage badge for [{team_id}] shows '🏆 R1 CLEARED (READY FOR R2)'!")

        # Screenshot admin showing team ready for Round 2
        p1 = os.path.join(ARTIFACT_DIR, "live_admin_r1_completed_ready_for_r2.png")
        driver.save_screenshot(p1)
        print("  ✓ Saved Admin Screenshot (Ready for R2):", p1)

        print(f"[3/6] Promoting [{team_id}] to Round 2 via Organizer Action...")
        # Call the endpoint to promote team
        promote_res = driver.execute_script(f"""
            let done = false;
            fetch('/api/admin/send_to_round_2', {{
                method: 'POST',
                headers: {{ 'Content-Type': 'application/json' }},
                body: JSON.stringify({{ pin: 'wie-admin-2026', team_id: '{team_id}' }})
            }}).then(r => r.json()).then(data => {{
                window.__promoteData = data;
                fetchLeaderboardData();
            }});
        """)
        time.sleep(2.5)

        post_table_text = driver.execute_script("""
            const tbody = document.getElementById('teams-table-body');
            return tbody ? tbody.innerText : '';
        """)
        print("  Post-promotion Table Preview snippet:")
        for line in post_table_text.split("\n")[:10]:
            print(f"    {line}")

        assert "R2 PUZZLE 01" in post_table_text, "Expected 'R2 PUZZLE 01' stage badge"
        assert "IN ROUND 2" in post_table_text, "Expected 'IN ROUND 2' button for promoted team"
        print("  ✓ Leaderboard reflects: '🎯 R2 PUZZLE 01: ACTIVE' and '🎯 IN ROUND 2'!")

        # Screenshot admin post-promotion
        p2 = os.path.join(ARTIFACT_DIR, "live_admin_promoted_to_round2_verified.png")
        driver.save_screenshot(p2)
        print("  ✓ Saved Admin Screenshot (Promoted to R2):", p2)

        print(f"[4/6] Navigating to Participant Workstation for [{team_id}]...")
        driver.get(f"{SERVER_URL}/aditi_os_widget.html")
        time.sleep(1)

        # Authenticate participant workstation as team_id
        driver.execute_script(f"""
            const team = {{
                team_id: '{team_id}',
                team_name: '{team_name}',
                password: 'CYBER-PASS-2026',
                members: 'Dr. Miller, Cmdr. Shepard'
            }};
            localStorage.setItem('failsafe_auth_team', JSON.stringify(team));
            localStorage.setItem('failsafe_current_stage', '16');
            localStorage.setItem('failsafe_mission_completed', 'true');
            currentTeam = team;
            currentStage = 16;
            const authModal = document.getElementById('team-auth-modal');
            if (authModal) authModal.style.display = 'none';

            // Start telemetry sync
            startTelemetryHeartbeat();
            if (typeof reportTelemetryAction === 'function') {{
                reportTelemetryAction('Checking for Round 2 promotion');
            }}
        """)
        time.sleep(3)

        print("[5/6] Verifying Live Automatic Transition into Round 2 Arena...")
        r2_state = driver.execute_script("""
            const r1Ws = document.getElementById('nexus-r1-workspace');
            const r2Ws = document.getElementById('nexus-r2-workspace');
            const btnSwitch = document.getElementById('btn-switch-r2');
            const currentR = typeof currentRound !== 'undefined' ? currentRound : 1;
            return {
                currentRound: currentR,
                r1Display: r1Ws ? window.getComputedStyle(r1Ws).display : '',
                r2Display: r2Ws ? window.getComputedStyle(r2Ws).display : '',
                switchBtnDisplay: btnSwitch ? window.getComputedStyle(btnSwitch).display : '',
                switchBtnText: btnSwitch ? btnSwitch.innerText : ''
            };
        """)
        print("  Participant Workstation State:", json.dumps(r2_state, indent=2))

        assert r2_state["currentRound"] == 2, f"Expected currentRound == 2, got {r2_state['currentRound']}"
        assert r2_state["r2Display"] == "block", f"Expected r2Display == 'block', got {r2_state['r2Display']}"
        assert r2_state["r1Display"] == "none", f"Expected r1Display == 'none', got {r2_state['r1Display']}"
        assert "ROUND 1" in r2_state["switchBtnText"], f"Expected switch button to allow viewing Round 1, got {r2_state['switchBtnText']}"

        # Screenshot participant workstation live in Round 2
        p3 = os.path.join(ARTIFACT_DIR, "live_workstation_in_round2_arena_verified.png")
        driver.save_screenshot(p3)
        print("  ✓ Saved Workstation Screenshot (In Round 2):", p3)

        print("[6/6] Verifying SEND ALL FINISHED TO R2 Bulk Promotion...")
        # Register a second finished team PHANTOM-8
        team_id_2 = "PHANTOM-8"
        req_data_2 = json.dumps({
            "team_id": team_id_2,
            "team_name": "Phantom Bravo",
            "members": "Lt. Vance",
            "password": "BRAVO-PASS-2026",
            "current_stage": 16,
            "is_finished": True,
            "finish_time_str": "49m 02s",
            "action": "🏆 Stage 16 Completed"
        }).encode("utf-8")
        req2 = urllib.request.Request(f"{SERVER_URL}/api/teams/activity", data=req_data_2, headers={"Content-Type": "application/json"})
        urllib.request.urlopen(req2)

        # Call bulk promote
        bulk_data = json.dumps({ "pin": pin, "team_id": "ALL_FINISHED" }).encode("utf-8")
        bulk_req = urllib.request.Request(f"{SERVER_URL}/api/admin/send_to_round_2", data=bulk_data, headers={"Content-Type": "application/json"})
        bulk_res = json.loads(urllib.request.urlopen(bulk_req).read().decode("utf-8"))
        print(f"  Bulk Promotion Result: {bulk_res}")
        assert bulk_res["success"] == True
        assert "PHANTOM-8" in bulk_res["promoted_teams"]
        print("  ✓ Bulk promotion successfully sent all finished teams to Round 2!")

        print("\n🎉 ALL ROUND 1 TO ROUND 2 FLOW TESTS PASSED WITH 100% SUCCESS!")

    finally:
        driver.quit()

if __name__ == "__main__":
    run_round1_to_round2_verification()
