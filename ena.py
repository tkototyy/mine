from seleniumbase import BaseCase
import time

class IPLeakScreenshot(BaseCase):
    def test_ipleak_screenshot(self):
        # Navigate to ipleak.net
        self.open("https://ipleak.net")

        # Wait 15 seconds to allow all checks to run
        time.sleep(15)

        # Save screenshot
        self.save_screenshot("ipleak_screenshot.png")

# To run directly:  python ipleak_screenshot.py
if __name__ == "__main__":
    from seleniumbase import run_command
    run_command("ipleak_screenshot.py IPLeakScreenshot.test_ipleak_screenshot")
