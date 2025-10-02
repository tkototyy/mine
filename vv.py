from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess

def is_stream_online(username):
    """
    Returns True if the Twitch stream is online, False otherwise.
    Uses the public frontend Client-ID (no OAuth).
    """
    url = f"https://www.twitch.tv/{username}"
    headers = {
        "Client-ID": "kimne78kx3ncx6brgo4mv6wki5h1ko",  # Publicly known Client-ID
    }
    resp = requests.get(url, headers=headers)
    return "isLiveBroadcast" in resp.text

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
    url = "https://www.twitch.tv/jokergotyou_69"
    yyw45.uc_open_with_reconnect(url, 4)
    yyw45.sleep(4)
    yyw45.uc_gui_click_captcha()
    yyw45.sleep(1)
    yyw45.uc_gui_handle_captcha()
    yyw45.sleep(4)
    if yyw45.is_element_present('button:contains("Accept")'):
        yyw45.uc_click('button:contains("Accept")', reconnect_time=4)
    if True:
        gsyhey = yyw45.get_new_driver(undetectable=True)
        gsyhey.uc_open_with_reconnect(url, 5)
        gsyhey.uc_gui_click_captcha()
        gsyhey.uc_gui_handle_captcha()
        yyw45.sleep(10)
        if gsyhey.is_element_present('button:contains("Accept")'):
            gsyhey.uc_click('button:contains("Accept")', reconnect_time=4)
        while is_stream_online("jokergotyou_69"):
            yyw45.sleep(10)
        yyw45.quit_extra_driver()
    yyw45.sleep(10)
    yyw45.save_screenshot("aaa2.png")
