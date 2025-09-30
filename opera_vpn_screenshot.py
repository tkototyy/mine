import time
from selenium import webdriver
from selenium.webdriver.opera.options import Options
import pyautogui

# === CONFIGURATION ===
OPERA_DRIVER_PATH = "operadriver"  # Or full path to operadriver
OPERA_BINARY_PATH = None  # Set if Opera is not in PATH
PROFILE_PATH = None  # Set to your Opera profile with VPN enabled, or leave as None
TARGET_URL = "https://example.com"

# === Setup Selenium for Opera ===
options = Options()
if OPERA_BINARY_PATH:
    options.binary_location = OPERA_BINARY_PATH
if PROFILE_PATH:
    options.add_argument(f"--user-data-dir={PROFILE_PATH}")

driver = webdriver.Opera(executable_path=OPERA_DRIVER_PATH, options=options)
driver.maximize_window()
time.sleep(1)

# === Open VPN Settings ===
driver.get("opera://settings/vpn")
time.sleep(5)

# === Find Coordinates with pyautogui ===
print("Move your mouse to the VPN toggle switch in Opera's settings window.")
input("Press Enter to capture the mouse position...")

x, y = pyautogui.position()
print(f"Mouse coordinates are: x={x}, y={y}")

# === (Optional) Click the toggle ===
click_it = input("Do you want to auto-click the VPN toggle now? (y/n): ").lower()
if click_it == "y":
    pyautogui.click(x, y)
    print("Clicked the VPN toggle.")
    time.sleep(2)

# === Go to target page and screenshot ===
driver.get(TARGET_URL)
time.sleep(5)
driver.save_screenshot("opera_vpn_screenshot.png")
print("Screenshot saved as opera_vpn_screenshot.png")

driver.quit()
