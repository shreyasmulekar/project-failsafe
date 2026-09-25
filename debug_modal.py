from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument("--headless=new")
d = webdriver.Chrome(options=opts)
d.get("http://localhost:8000/aditi_os_widget.html")
html = d.execute_script("return document.getElementById('modal-honeypot') ? document.getElementById('modal-honeypot').innerHTML : 'NULL';")
print("Has btn-trap-honeypot:", "btn-trap-honeypot" in html)
print("Has DO NOT CLICK:", "DO NOT CLICK" in html)
btns = d.execute_script("return Array.from(document.querySelectorAll('#modal-honeypot button')).map(b => b.outerHTML);")
print("Buttons inside modal-honeypot:", btns)
d.quit()
