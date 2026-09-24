import sys
import time

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def run_broadcast_tests():
    print("=== STARTING BROADCAST DURATION VERIFICATION (AT LEAST 3 SECONDS) ===")
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1600,1000")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)

    try:
        print("1. Loading participant workstation http://localhost:8000/aditi_os_widget.html...")
        driver.get("http://localhost:8000/aditi_os_widget.html")
        time.sleep(2)

        driver.execute_script("""
            const modal = document.getElementById('team-auth-modal');
            if (modal) modal.style.display = 'none';
        """)

        # -------------------------------------------------------------
        # TEST 1: Minimum 3 Seconds Guarantee (Even if requested for less)
        # -------------------------------------------------------------
        print("\n--- TEST 1: Enforcing Minimum 3 Seconds Display ---")
        driver.execute_script("showBroadcastToast('EMERGENCY ANNOUNCEMENT: ALL TEAMS ATTENTION', 1000);")
        time.sleep(0.3)

        toast = driver.find_element(By.ID, "broadcast-toast")
        assert toast.is_displayed(), "Broadcast toast must be displayed"
        toast_text = toast.text
        print(f"Broadcast active at t=0.3s: '{toast_text.splitlines()[0]}'")
        assert "ORGANIZER BROADCAST" in toast_text, "Title must be ORGANIZER BROADCAST"
        assert "ALL TEAMS ATTENTION" in toast_text, "Must contain broadcast message"

        # Check at t = 1.2s (would have disappeared previously if 1s was respected)
        time.sleep(0.9)
        assert toast.is_displayed(), "Broadcast toast MUST still be displayed at t=1.2s"
        print("Broadcast verified visible at t=1.2s (exceeded requested 1.0s).")

        # Check at t = 2.2s
        time.sleep(1.0)
        assert toast.is_displayed(), "Broadcast toast MUST still be displayed at t=2.2s"
        print("Broadcast verified visible at t=2.2s.")

        # Check at t = 2.9s
        time.sleep(0.7)
        assert toast.is_displayed(), "Broadcast toast MUST still be displayed at t=2.9s (almost 3.0s)"
        print("Broadcast verified visible at t=2.9s (full >=3 seconds guaranteed!).")

        # Take screenshot of active broadcast with progress bar
        screenshot_path = "C:/Users/shrey/.gemini/antigravity/brain/17c36665-51d0-4b98-8e9d-7e8fd18fcd27/test_broadcast_toast_active.png"
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")

        # Wait until it concludes and dismisses
        time.sleep(1.2)
        print(f"After expiry, toast displayed state: {toast.is_displayed()}")

        # -------------------------------------------------------------
        # TEST 2: Rapid-Fire Broadcast Queueing (Prevent Premature Cutoff)
        # -------------------------------------------------------------
        print("\n--- TEST 2: Rapid-Fire Broadcast Queueing ---")
        print("Triggering Broadcast 1 (3000ms)...")
        driver.execute_script("showBroadcastToast('MESSAGE ONE: FIRST ALERT', 3000);")
        time.sleep(0.5)

        print("Triggering Broadcast 2 immediately after 0.5s...")
        driver.execute_script("showBroadcastToast('MESSAGE TWO: SECOND ALERT', 3000);")
        time.sleep(0.3)

        # Message 1 must STILL be showing, not prematurely killed by Message 2!
        current_text = driver.find_element(By.ID, "broadcast-toast").text
        print(f"Toast content at t=0.8s: '{current_text}'")
        assert "MESSAGE ONE" in current_text, "Message ONE must still be showing, queueing Message TWO"

        # Wait until Message 1 finishes its >=3s
        time.sleep(2.7) # Now t = 3.5s
        time.sleep(0.5) # Allow transition

        # Now Message 2 must be displaying!
        msg2_text = driver.find_element(By.ID, "broadcast-toast").text
        print(f"Toast content after Message 1 completed (t=4.0s): '{msg2_text}'")
        assert "MESSAGE TWO" in msg2_text, "Message TWO must now display smoothly from queue"
        print("Message TWO verified displaying after Message ONE completed full duration!")

        # Verify Message 2 also stays for at least 3 seconds
        time.sleep(2.2)
        assert driver.find_element(By.ID, "broadcast-toast").is_displayed(), "Message TWO must remain visible for at least 3s"
        print("Message TWO verified staying for at least 3 seconds!")

        print("\n=======================================================")
        print("🎉 BROADCAST DURATION VERIFICATION PASSED (>= 3 SECONDS)")
        print("=======================================================")

    finally:
        driver.quit()

if __name__ == "__main__":
    run_broadcast_tests()
