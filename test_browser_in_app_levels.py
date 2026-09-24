# test_browser_in_app_levels.py
import sys
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

URL = "http://127.0.0.1:8000/aditi_os_widget.html"

def test_levels():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1600,1050")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Edge(options=options)
    try:
        print("=== 1. LOADING APPLICATION ===")
        driver.get(URL)
        time.sleep(1.5)

        # Authenticate and dismiss login
        driver.execute_script("""
            localStorage.setItem('failsafe_auth_team', JSON.stringify({
                team_id: 'TEST-BROWSER',
                team_name: 'In-App Verifier',
                password: 'wie2026',
                members: 'Unit Tester'
            }));
            const m = document.getElementById('team-auth-modal');
            if (m) m.style.display = 'none';
            window.__testBypassSequentialLock = true;
            if (typeof updateNexusDashboard === 'function') updateNexusDashboard();
        """)
        time.sleep(1)
        print("[OK] Application loaded and authenticated.")

        print("\n=== 2. VERIFYING ALL 16 STAGES OF ROUND 1 OPEN IN-APP ===")
        for stg in range(1, 17):
            res = driver.execute_script(f"""
                currentStage = {stg};
                if (typeof updateNexusDashboard === 'function') updateNexusDashboard();
                openActiveStageModal();
                const meta = NEXUS_STAGES_META[{stg}];
                if (!meta) return {{ success: false, error: 'No meta for stage {stg}' }};
                const modalEl = document.getElementById(meta.modal);
                if (!modalEl) return {{ success: false, error: 'Modal element not found: ' + meta.modal }};
                const isActive = modalEl.classList.contains('active-modal') || window.getComputedStyle(modalEl).display !== 'none';
                
                // Close modal for next iteration
                closeAllModals();
                return {{
                    success: true,
                    modalId: meta.modal,
                    isActive: isActive,
                    title: meta.title
                }};
            """)
            assert res.get("success"), f"Stage {stg} failed: {res.get('error')}"
            assert res.get("isActive"), f"Stage {stg} modal {res.get('modalId')} was not active/visible!"
            print(f"  [OK] Round 1 Stage {stg:02d} ({res.get('title')}): Modal [{res.get('modalId')}] opened cleanly in-app!")

        print("\n=== 3. VERIFYING ALL 15 PUZZLES OF ROUND 2 OPEN IN-APP ===")
        # Switch to Round 2 arena
        driver.execute_script("""
            const r2Cont = document.getElementById('round2-arena-container');
            const r1Left = document.querySelector('.forensic-sector');
            const vault = document.querySelector('.nexus-vault-section');
            const hero = document.querySelector('.nexus-hero-section');
            if (r2Cont) r2Cont.style.display = 'block';
            if (r1Left) r1Left.style.display = 'none';
            if (vault) vault.style.display = 'none';
            if (hero) hero.style.display = 'none';
        """)

        for pz_num in range(1, 16):
            pz_res = driver.execute_script(f"""
                round2CurrentStage = {pz_num};
                renderRound2Arena();
                const viewport = document.getElementById('r2-puzzle-viewport');
                const pzData = ROUND2_PUZZLE_DATA[{pz_num}];
                if (!pzData) return {{ success: false, error: 'No puzzle data for {pz_num}' }};
                const hasContent = viewport && viewport.innerHTML.trim().length > 20;
                const hasInput = !!document.getElementById('r2-passcode-input');
                const badge = document.getElementById('r2-current-stage-badge');
                return {{
                    success: true,
                    hasContent: hasContent,
                    hasInput: hasInput,
                    title: pzData.title,
                    badgeText: badge ? badge.innerText : ''
                }};
            """)
            assert pz_res.get("success"), f"Round 2 Puzzle {pz_num} failed: {pz_res.get('error')}"
            assert pz_res.get("hasContent"), f"Round 2 Puzzle {pz_num} viewport was empty!"
            assert pz_res.get("hasInput"), f"Round 2 Puzzle {pz_num} had no passcode input!"
            print(f"  [OK] Round 2 Puzzle {pz_num:02d} ({pz_res.get('title')}): Rendered in-app viewport ({pz_res.get('badgeText')})")

        print("\n=======================================================")
        print("ALL 16 ROUND 1 LEVELS AND ALL 15 ROUND 2 LEVELS")
        print("OPEN AND RENDER DIRECTLY INSIDE THE APPLICATION!")
        print("=======================================================")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_levels()
