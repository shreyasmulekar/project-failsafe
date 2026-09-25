from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opts = Options()
opts.add_argument("--headless=new")
d = webdriver.Chrome(options=opts)
d.get("http://localhost:8000/aditi_os_widget.html")
print("Before click:", len(d.find_elements(By.ID, "btn-trap-honeypot")))
onclick = d.execute_script("return document.getElementById('card-trap').getAttribute('onclick');")
print("card-trap onclick attribute:", onclick)
d.execute_script("document.getElementById('card-trap').click();")
print("After click:", len(d.find_elements(By.ID, "btn-trap-honeypot")))
print("Current URL:", d.current_url)
d.quit()
