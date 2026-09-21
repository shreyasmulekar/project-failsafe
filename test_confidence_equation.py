import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_confidence_test():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1280,900")
    
    html_path = os.path.abspath(r"C:\Users\shrey\.gemini\antigravity\scratch\project-failsafe\confidence_equation.html")
    file_url = f"file:///{html_path.replace(os.sep, '/')}"
    
    print(f"Launching Edge to test: {file_url}")
    driver = webdriver.Edge(options=options)
    
    try:
        driver.get(file_url)
        wait = WebDriverWait(driver, 10)
        
        # 1. SCREEN 1: OPENING SCREEN
        print("\n--- STEP 1: OPENING SCREEN ---")
        h1 = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'ADI // INCIDENT ANALYSIS')]")))
        print(f"[PASS] Found title: {h1.text}")
        
        body_text = driver.find_element(By.ID, "screen-stage-1").text
        assert "05 predictions detected." in body_text, "Missing '05 predictions detected.'"
        assert "01 confidence value corrupted." in body_text, "Missing '01 confidence value corrupted.'"
        assert "Trace the mathematical model." in body_text, "Missing 'Trace the mathematical model.'"
        print("[PASS] Opening text lines verified.")
        
        begin_btn = driver.find_element(By.ID, "btn-begin-investigation")
        begin_btn.click()
        time.sleep(0.5)
        
        # 2. SCREEN 2: EVIDENCE SCREEN
        print("\n--- STEP 2: EVIDENCE SCREEN ---")
        wait.until(EC.visibility_of_element_located((By.ID, "screen-stage-2")))
        cards = driver.find_elements(By.CSS_SELECTOR, ".evidence-card")
        assert len(cards) == 5, f"Expected 5 cards, got {len(cards)}"
        print(f"[PASS] Rendered {len(cards)} evidence cards.")
        
        evidence_text = driver.find_element(By.ID, "screen-stage-2").text
        for letter, conf in [('A', '100%'), ('B', '56.25%'), ('C', '6.25%'), ('D', '0%'), ('E', '30%')]:
            assert f"PREDICTION {letter}" in evidence_text
            assert conf in evidence_text
        print("[PASS] All 5 predictions and ADI confidence values verified on cards.")
        
        driver.save_screenshot(r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27\screenshot_step2_evidence.png")
        
        proceed_btn = driver.find_element(By.ID, "btn-proceed-formula")
        proceed_btn.click()
        time.sleep(0.5)
        
        # 3. SCREEN 3: FORMULA DISCOVERY SCREEN
        print("\n--- STEP 3: FORMULA DISCOVERY SCREEN ---")
        wait.until(EC.visibility_of_element_located((By.ID, "screen-stage-3")))
        prompt_el = driver.find_element(By.ID, "formula-prompt-text")
        assert "ADI claims its confidence is calculated from sensor evidence. Reconstruct the equation." in prompt_el.text
        print(f"[PASS] Prompt text: {prompt_el.text}")
        
        # Test incorrect submission with exp=1
        submit_btn = driver.find_element(By.ID, "btn-calculate-formula")
        submit_btn.click()
        time.sleep(0.4)
        feedback = driver.find_element(By.ID, "formula-feedback-box")
        assert "EQUATION MISMATCH" in feedback.text or "REJECTED" in feedback.text
        print(f"[PASS] Incorrect formula rejected with hint: {feedback.text[:60]}...")
        
        # Select exp = 2 (Quadratic)
        exp2_btn = driver.find_element(By.CSS_SELECTOR, "button[data-exp='2']")
        exp2_btn.click()
        time.sleep(0.3)
        print("[PASS] Selected exponent ^2.")
        
        driver.save_screenshot(r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27\screenshot_step3_formula.png")
        
        # Submit correct formula
        submit_btn.click()
        time.sleep(0.5)
        feedback = driver.find_element(By.ID, "formula-feedback-box")
        assert "MODEL RECONSTRUCTED" in feedback.text
        print(f"[PASS] Formula confirmed: {feedback.text[:50]}...")
        
        # 4. SCREEN 4: VERIFICATION TABLE SCREEN
        print("\n--- STEP 4: VERIFICATION TABLE SCREEN ---")
        wait.until(EC.visibility_of_element_located((By.ID, "screen-stage-4")))
        # Wait for audit animation to finish (at least 5 rows * 350ms ~ 2.5s)
        time.sleep(3.0)
        
        rows = driver.find_elements(By.CSS_SELECTOR, "#verification-table-body tr")
        assert len(rows) == 5, f"Expected 5 table rows, got {len(rows)}"
        print("[PASS] 5 audit rows rendered.")
        
        table_text = driver.find_element(By.ID, "verification-table-body").text
        print("Audit Table Content:\n" + table_text)
        assert "100%" in table_text and "MATCH" in table_text
        assert "56.25%" in table_text
        assert "6.25%" in table_text
        assert "0%" in table_text
        assert "30%" in table_text and "25%" in table_text and "CORRUPTED" in table_text
        print("[PASS] Audit comparison table matches expected data (E flagged as CORRUPTED).")
        
        driver.save_screenshot(r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27\screenshot_step4_verification.png")
        
        isolate_btn = wait.until(EC.element_to_be_clickable((By.ID, "btn-proceed-isolation")))
        isolate_btn.click()
        time.sleep(0.5)
        
        # 5. SCREEN 5: IDENTIFICATION SCREEN
        print("\n--- STEP 5: ANOMALY IDENTIFICATION SCREEN ---")
        wait.until(EC.visibility_of_element_located((By.ID, "screen-stage-5")))
        question_text = driver.find_element(By.CSS_SELECTOR, "#screen-stage-5 .panel-lead-text").text
        assert "Which prediction contains the corrupted confidence value?" in question_text
        print(f"[PASS] Question: {question_text}")
        
        # Click choice E — SYSTEM SHUTDOWN
        choice_e = driver.find_element(By.ID, "anomaly-choice-E")
        choice_e.click()
        print("[PASS] Clicked option 'E — SYSTEM SHUTDOWN'.")
        time.sleep(1.2)
        
        # 6. SCREEN 6: CONFIRMATION SCREEN
        print("\n--- STEP 6: CONFIRMATION SCREEN ---")
        wait.until(EC.visibility_of_element_located((By.ID, "screen-stage-6")))
        conf_card_text = driver.find_element(By.CSS_SELECTOR, ".confirmation-card").text
        print("Confirmation Dossier:\n" + conf_card_text)
        assert "30%" in conf_card_text
        assert "25%" in conf_card_text
        assert "5 percentage points" in conf_card_text
        print("[PASS] Confirmation values verified.")
        
        driver.save_screenshot(r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27\screenshot_step6_confirmation.png")
        
        story_btn = driver.find_element(By.ID, "btn-proceed-story")
        story_btn.click()
        time.sleep(0.5)
        
        # 7. SCREEN 7: STORY REVEAL & CLIMAX SCREEN
        print("\n--- STEP 7: STORY REVEAL SCREEN ---")
        wait.until(EC.visibility_of_element_located((By.ID, "screen-stage-7")))
        reveal_box = driver.find_element(By.CSS_SELECTOR, ".story-reveal-container").text
        print("Story Reveal Output:\n" + reveal_box)
        assert "YOU FOUND THE ERROR." in reveal_box
        assert "BUT YOU DIDN'T FIND WHO CREATED IT." in reveal_box
        assert "TRACE CONTINUES..." in reveal_box
        print("[PASS] Story reveal text lines verified.")
        
        driver.save_screenshot(r"C:\Users\shrey\.gemini\antigravity\brain\17c36665-51d0-4b98-8e9d-7e8fd18fcd27\screenshot_step7_reveal.png")
        
        continue_btn = driver.find_element(By.ID, "btn-continue-stage")
        assert continue_btn.is_displayed()
        continue_btn.click()
        time.sleep(0.5)
        print("[PASS] Clicked CONTINUE button successfully!")
        
        print("\n==================================================")
        print("TEST SUCCESS: 100% COMPLETE FLOW VERIFIED!")
        print("==================================================")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    run_confidence_test()
