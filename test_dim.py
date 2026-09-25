from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless=new')
options.add_argument('--window-size=1366,768')
driver = webdriver.Chrome(options=options)
driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', {'width': 1366, 'height': 768, 'deviceScaleFactor': 1, 'mobile': False})
driver.get('http://localhost:8000/aditi_os_widget.html')
import time
time.sleep(1.0)
driver.find_element("id", "auth-login-id").send_keys("T-ALPHA")
driver.find_element("id", "auth-login-pass").send_keys("Password123!")
driver.find_element("id", "auth-login-form").submit()
import time
time.sleep(1.5)
res = driver.execute_script('''
    const r1 = document.querySelector("#nexus-r1-workspace .nexus-top-row");
    const r2 = document.querySelector("#nexus-r2-workspace .nexus-top-row");
    const r1_vis = document.querySelector("#nexus-r1-workspace")?.style.display;
    const r2_vis = document.querySelector("#nexus-r2-workspace")?.style.display;
    return {
        innerW: window.innerWidth,
        innerH: window.innerHeight,
        r1_vis,
        r2_vis,
        r1_cols: r1 ? getComputedStyle(r1).gridTemplateColumns : null,
        r2_cols: r2 ? getComputedStyle(r2).gridTemplateColumns : null
    };
''')
print("Logged in state:", res)
driver.quit()
