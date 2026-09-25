from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opts = Options()
opts.add_argument("--headless=new")
opts.add_argument("--disable-application-cache")
opts.add_argument("--disk-cache-size=0")
d = webdriver.Chrome(options=opts)
d.get("http://localhost:8000/aditi_os_widget.html")
els = d.find_elements(By.ID, "btn-trap-honeypot")
print("Found by ID count:", len(els))
btns = d.find_elements(By.XPATH, "//button[contains(text(), 'DO NOT CLICK')]")
print("Found by text count:", len(btns))
d.quit()
