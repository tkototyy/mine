from seleniumbase import BaseCase

class OperaVPNTest(BaseCase):
    def test_enable_vpn_and_screenshot(self):
        # Launch Opera browser
        self.open("opera://settings/vpn")
        self.sleep(5)  # Wait for settings page to load

        # Try to enable VPN (the settings page is Shadow DOM, so this is tricky)
        # We'll attempt to click the toggle by JS; this may need adjustment for Opera updates.
        # If the selector changes, inspect the page and adjust.
        try:
            self.execute_script("""
                let shadowRoot = document.querySelector('settings-ui').shadowRoot;
                let main = shadowRoot.querySelector('#main');
                let settingsPage = main.shadowRoot.querySelector('settings-basic-page');
                let vpnPage = settingsPage.shadowRoot.querySelector('settings-privacy-page');
                let vpnToggle = vpnPage.shadowRoot.querySelector('#enableVpn');
                if (vpnToggle && !vpnToggle.checked) {
                    vpnToggle.click();
                }
            """)
            self.sleep(2)
        except Exception as e:
            print("Could not enable VPN automatically: ", e)

        # Now go to the target page (replace with your target)
        target_url = "https://example.com"
        self.open(target_url)
        self.sleep(6)  # Wait for VPN to connect and page to load

        # Take screenshot
        self.save_screenshot("opera_vpn_screenshot.png")
