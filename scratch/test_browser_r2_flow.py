# scratch/test_browser_r2_flow.py
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

def test_r2_flow():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1600,1050")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Edge(options=options)
    try:
        print("=== 1. LOADING APP FOR ROUND 2 INTERACTION TEST ===")
        driver.get(URL)
        time.sleep(1.0)
        for _ in range(20):
            if driver.execute_script("return typeof renderRound2Arena === 'function';"):
                break
            time.sleep(0.5)

        # Authenticate and switch to Round 2
        driver.execute_script("""
            localStorage.setItem('failsafe_auth_team', JSON.stringify({
                team_id: 'R2-BROWSER-CHAMPION',
                team_name: 'Cyber Olympians',
                password: 'wie2026',
                members: 'Alpha, Beta'
            }));
            const m = document.getElementById('team-auth-modal');
            if (m) m.style.display = 'none';
            
            // Switch to Round 2 Arena
            const r2Cont = document.getElementById('round2-arena-container');
            const r1Left = document.querySelector('.forensic-sector');
            const vault = document.querySelector('.nexus-vault-section');
            const hero = document.querySelector('.nexus-hero-section');
            if (r2Cont) r2Cont.style.display = 'block';
            if (r1Left) r1Left.style.display = 'none';
            if (vault) vault.style.display = 'none';
            if (hero) hero.style.display = 'none';

            round2CurrentStage = 1;
            renderRound2Arena();
        """)
        time.sleep(1.0)

        # Test answers for all 15 questions
        r2_answers = [
            "C", "BL", "5", "CIPHER", "SQUARES",
            "011", "CLEARANCE", "SE", "NONE", "RLRCK",
            "NODC", "102", "3-EMPTY", "FINALS", "ECLIPSE"
        ]

        print("=== 2. SUBMITTING ANSWERS IN-APP FROM QUESTION 1 TO 15 ===")
        for i, ans in enumerate(r2_answers, 1):
            res = driver.execute_script(f"""
                const pzBefore = round2CurrentStage;
                submitRound2Code('{ans}');
                return {{
                    submitted: '{ans}',
                    stageBefore: pzBefore,
                    clearedList: round2StagesCleared
                }};
            """)
            print(f"  [OK] Question {i:02d}: Submitted '{ans}' -> Cleared stages: {res.get('clearedList')}")
            time.sleep(1.0)

        # After question 15, verify Grand Victory celebration modal
        time.sleep(2.0)
        victory_res = driver.execute_script("""
            const vModal = document.getElementById('victory-celebration-modal');
            const isVisible = vModal && (vModal.style.display === 'flex' || window.getComputedStyle(vModal).display === 'flex');
            const prizeContainer = document.getElementById('podium-prize-badge-container');
            const congratsTitle = document.getElementById('victory-congrats-title');
            const aditiVideo = document.getElementById('dr-aditi-video-feed');
            const subtitle = document.getElementById('victory-aditi-subtitle');

            return {
                modalVisible: isVisible,
                prizeText: prizeContainer ? prizeContainer.innerText : '',
                titleText: congratsTitle ? congratsTitle.innerText : '',
                videoLoaded: !!aditiVideo,
                subtitleText: subtitle ? subtitle.innerText : ''
            };
        """)

        assert victory_res.get("modalVisible"), "Victory celebration modal did not open after Question 15!"
        print("\n=== 3. GRAND VICTORY CELEBRATION MODAL VERIFIED ===")
        print(f"  [OK] Modal Active: {victory_res.get('modalVisible')}")
        print(f"  [OK] Podium Prize: {victory_res.get('prizeText')}")
        print(f"  [OK] Victory Title: {victory_res.get('titleText')}")
        print(f"  [OK] Dr. Aditi Video Element Present: {victory_res.get('videoLoaded')}")
        print(f"  [OK] Dr. Aditi Decrypted Message: {victory_res.get('subtitleText')[:80]}...")

        print("\n=======================================================")
        print("ALL 15 ROUND 2 PUZZLES AND GRAND VICTORY MODAL PASSED!")
        print("=======================================================")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_r2_flow()
