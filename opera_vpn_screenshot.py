import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# --- Setup Selenium ---
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # run without opening browser window
# For Ubuntu: Ensure chromedriver is in your PATH, and Chrome/Chromium is installed
driver = webdriver.Chrome(options=options)

# --- Target site (replace with the actual site you want to scrape) ---
url = "https://openproxylist.com/openvpn/"  
driver.get(url)
time.sleep(5)
download_links = []
wait = WebDriverWait(driver, 10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# --- Handle consent popup if present ---
try:
    consent_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Accept') or contains(., 'Consent')]"))
    )
    consent_btn.click()
    print("Consent accepted.")
except TimeoutException:
    print("No consent button found, continuing...")
time.sleep(5)

while True:
    # 1. Collect all download links on current page
    anchors = driver.find_elements(By.XPATH, "//a[contains(@href, '.ovpn')]")
    for a in anchors:
        href = a.get_attribute("href")
        if href and href not in download_links:
            download_links.append(href)

    # 2. Try to click the Next button
    try:
        next_button = driver.find_element(By.XPATH, "//span[contains(@class, 'page-link') and text()='Next']")
        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(4)  # wait for page to load
    except NoSuchElementException:
        break  # no more Next button, exit loop

driver.quit()

print(f"Collected {len(download_links)} links.")

# --- Download and modify files ---
# For Ubuntu, OpenVPN config dir is typically /etc/openvpn
openvpn_config_dir = "vpn-configs/"

# Make sure the directory exists
os.makedirs(openvpn_config_dir, exist_ok=True)

for link in download_links:
    try:
        filename = os.path.basename(link)
        local_path = os.path.join(openvpn_config_dir, filename)  # save directly here
        r = requests.get(link, timeout=15)
        if r.status_code == 200:
            content = r.text
            content = content.replace("cipher AES-128-CBC", "data-ciphers AES-128-CBC")

            with open(local_path, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"Saved directly to: {local_path}")
        else:
            print(f"Failed to download {link} (status {r.status_code})")
    except PermissionError:
        print(f"Permission denied: run this script as root (e.g., with sudo) to write into {openvpn_config_dir}")
    except Exception as e:
        print(f"Error downloading {link}: {e}")
