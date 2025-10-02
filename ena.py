from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess

with SB(uc=True, test=True) as yyw45:
    url = "https://www.ipleak.net"
    yyw45.uc_open_with_reconnect(url, 4)
    yyw45.sleep(4)
