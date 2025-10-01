from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
geo_data = requests.get("http://ip-api.com/json/").json()

latitude = geo_data["lat"]
longitude = geo_data["lon"]
timezone_id = geo_data["timezone"]
language_code = geo_data["countryCode"].lower()

with SB(uc=True, test=True,locale=f"{language_code.upper()}") as yyw45:
    yyw45.execute_cdp_cmd(
        "Emulation.setGeolocationOverride",
        {
            "latitude": latitude,
            "longitude": longitude,
            "accuracy": 100
        }
    )
    yyw45.execute_cdp_cmd(
        "Emulation.setTimezoneOverride",
        {"timezoneId": timezone_id}
    )
    url = "https://www.youtube.com/@Raeyei/live"
    yyw45.uc_open_with_reconnect(url, 4)
    yyw45.sleep(4)
    yyw45.uc_gui_click_captcha()
    yyw45.sleep(1)
    yyw45.uc_gui_handle_captcha()
    yyw45.sleep(4)
    if yyw45.is_element_present('button:contains("Accept")'):
        yyw45.uc_click('button:contains("Accept")', reconnect_time=4)
    if yyw45.is_element_visible('#injected-channel-player'):
        gsyhey = yyw45.get_new_driver(undetectable=True)
        gsyhey.uc_open_with_reconnect(url, 5)
        gsyhey.uc_gui_click_captcha()
        gsyhey.uc_gui_handle_captcha()
        yyw45.sleep(10)
        if gsyhey.is_element_present('button:contains("Accept")'):
            gsyhey.uc_click('button:contains("Accept")', reconnect_time=4)
        while yyw45.is_element_visible('#injected-channel-player'):
            yyw45.sleep(10)
        yyw45.quit_extra_driver()
    yyw45.sleep(30)
    yyw45.save_screenshot("aaa2.png")
