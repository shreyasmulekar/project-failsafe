from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opts = Options()
opts.add_argument("--headless=new")
d = webdriver.Chrome(options=opts)
d.get("http://localhost:8000/aditi_os_widget.html")
d.execute_script("currentStage = 10; localStorage.setItem('failsafe_stage', '10'); document.getElementById('card-trap').click();")
btn = d.find_element(By.ID, "btn-trap-honeypot")
safe_text = btn.text.encode("ascii", "ignore").decode()
print("Safe button text:", safe_text)
assert "DO NOT CLICK" in btn.text and "+5 MIN PENALTY" in btn.text
print("Assertion Passed!")
d.quit()
