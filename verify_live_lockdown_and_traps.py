import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

ARTIFACT_DIR = r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27"
SERVER_URL = "http://localhost:8000"

def test_live_proctor_and_traps():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1600,1050")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Edge(options=options)
    try:
        print("[1/6] Navigating to Participant Workstation...")
        driver.get(f"{SERVER_URL}/aditi_os_widget.html")
        time.sleep(2)

        # Login as ALFA-1
        driver.execute_script("""
            localStorage.setItem('failsafe_auth_team', JSON.stringify({
                team_id: 'ALFA-1',
                team_name: 'gabe_itch',
                password: 'wie2026',
                members: 'Kirk'
            }));
            if (typeof currentTeam !== 'undefined') {
                currentTeam = {
                    team_id: 'ALFA-1',
                    team_name: 'gabe_itch',
                    password: 'wie2026',
                    members: 'Kirk'
                };
            }
            const authModal = document.getElementById('team-auth-modal');
            if (authModal) authModal.style.display = 'none';
            if (typeof applyAuthenticatedTeam === 'function') {
                applyAuthenticatedTeam(currentTeam);
            }
        """)
        time.sleep(1)

        # Initial timer check
        timer_text_before = driver.execute_script("""
            const el = document.getElementById('nexus-live-mission-timer');
            return el ? el.innerText : '';
        """)
        pen_before = driver.execute_script("""
            return parseInt(localStorage.getItem('failsafe_penalty_seconds') || '0', 10);
        """)
        print(f"  Initial Timer: {timer_text_before}, Stored Penalty: {pen_before}s")

        print("[2/6] Triggering DO_NOT_RUN.exe Honeypot Trap Live...")
        driver.execute_script("triggerLockdownTrap();")
        time.sleep(1.5)

        pen_after = driver.execute_script("""
            return parseInt(localStorage.getItem('failsafe_penalty_seconds') || '0', 10);
        """)
        traps_after = driver.execute_script("""
            return parseInt(localStorage.getItem('failsafe_traps_count') || '0', 10);
        """)
        timer_text_after = driver.execute_script("""
            const el = document.getElementById('nexus-live-mission-timer');
            return el ? el.innerText : '';
        """)
        badge_text = driver.execute_script("""
            const badge = document.getElementById('nexus-penalty-badge');
            return (badge && badge.style.display !== 'none') ? badge.innerText : '';
        """)
        print(f"  Post-Trap: Timer: {timer_text_after}, Badge: '{badge_text}', Penalty Secs: {pen_after}s, Traps Count: {traps_after}")
        assert pen_after >= pen_before + 300, f"Expected penalty to increase by at least 300s, got {pen_after}"
        assert traps_after >= 1, "Expected traps count to be >= 1"

        # Close trap overlay and verify Tara recovery
        driver.execute_script("closeLockdown();")
        time.sleep(1)

        tara_state = driver.execute_script("return typeof taraState !== 'undefined' ? taraState : '';")
        print(f"  Tara state after closing trap: {tara_state}")

        # Send telemetry ping
        driver.execute_script("reportTelemetryAction('Live Testing Honeypot & Exit FS');")
        time.sleep(1.5)

        # Screenshot participant workstation
        p1 = os.path.join(ARTIFACT_DIR, "live_workstation_trap_and_unlocked.png")
        driver.save_screenshot(p1)
        print("  ✓ Saved Workstation Screenshot:", p1)

        print("[3/6] Navigating to Organizer Command Center...")
        driver.get(f"{SERVER_URL}/admin.html")
        time.sleep(1.5)

        driver.execute_script("""
            sessionStorage.setItem("failsafe_admin_authenticated", "true");
            sessionStorage.setItem("admin_pin", "wie-admin-2026");
            const modal = document.getElementById("admin-login-modal");
            if (modal) modal.style.display = "none";
            fetchLeaderboardData();
        """)
        time.sleep(2.5)

        # Verify admin leaderboard table
        table_html = driver.execute_script("""
            const tbody = document.getElementById('teams-table-body');
            return tbody ? tbody.innerText : '';
        """)
        print("  Leaderboard Preview snippet:")
        for line in table_html.split("\n")[:8]:
            print(f"    {line}")

        # Verify Penalties column in table
        assert "Penalties:" in table_html, f"Expected 'Penalties:' to appear in table, got: {table_html}"

        # Check global fullscreen button
        global_btn_text = driver.execute_script("""
            const btn = document.getElementById('btn-global-fullscreen-exit');
            return btn ? btn.innerText : '';
        """)
        print(f"  Global FS Button: '{global_btn_text}'")

        print("[4/6] Executing Organizer Remote Unlock & Fullscreen Exit Approval...")
        driver.execute_script("""
            respondFullscreenExit('ALL', 'approve');
        """)
        time.sleep(2)

        # Also trigger remote-unlock for ALFA-1
        driver.execute_script("""
            fetch('/api/admin/remote-unlock', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ pin: 'wie-admin-2026', team_id: 'ALFA-1' })
            });
        """)
        time.sleep(2)
        driver.execute_script("fetchLeaderboardData();")
        time.sleep(2)

        # Screenshot Admin Dashboard
        p2 = os.path.join(ARTIFACT_DIR, "live_admin_clean_penalties_verified.png")
        driver.save_screenshot(p2)
        print("  ✓ Saved Admin Screenshot:", p2)

        print("[5/6] Verifying Participant Workstation Immunity to Focus Loss & Shortcuts...")
        driver.get(f"{SERVER_URL}/aditi_os_widget.html")
        time.sleep(2)

        is_fs_auth = driver.execute_script("return isFullscreenExitAuthorized();")
        print(f"  isFullscreenExitAuthorized on workstation: {is_fs_auth}")
        assert is_fs_auth == True, "Expected isFullscreenExitAuthorized to be True"

        # Simulate Alt+Tab, Windows Key, and document visibilitychange
        driver.execute_script("""
            // Dispatch Alt+Tab
            window.dispatchEvent(new KeyboardEvent('keydown', { key: 'Tab', keyCode: 9, altKey: true, bubbles: true }));
            // Dispatch Windows key
            window.dispatchEvent(new KeyboardEvent('keydown', { key: 'Meta', code: 'MetaLeft', keyCode: 91, bubbles: true }));
            // Dispatch visibilitychange
            document.dispatchEvent(new Event('visibilitychange'));
        """)
        time.sleep(1)

        lock_overlay_display = driver.execute_script("""
            const ov = document.getElementById('proctor-lockdown-overlay');
            return ov ? window.getComputedStyle(ov).display : 'none';
        """)
        proctor_active = driver.execute_script("return typeof proctorLockActive !== 'undefined' ? proctorLockActive : false;")
        violations = driver.execute_script("return typeof violationCount !== 'undefined' ? violationCount : 0;")
        print(f"  Lockdown overlay display: '{lock_overlay_display}'")
        print(f"  proctorLockActive: {proctor_active}")
        print(f"  violationCount: {violations}")

        assert lock_overlay_display == 'none', f"Lockdown overlay should NOT be displayed, was {lock_overlay_display}"
        assert proctor_active == False, "proctorLockActive should remain False"
        assert violations == 0, f"violationCount should remain 0, was {violations}"
        print("  ✓ Workstation is 100% immune to false lockouts while fullscreen exit is authorized!")

        print("[6/6] All Live Tests Passed Successfully!")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_live_proctor_and_traps()
