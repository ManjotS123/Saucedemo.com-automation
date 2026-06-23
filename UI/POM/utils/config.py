import os

BASE_URL = os.getenv("SAUCEDEMO_BASE_URL", "https://www.saucedemo.com")
USERNAME = os.getenv("SAUCEDEMO_USERNAME", "standard_user")
PASSWORD = os.getenv("SAUCEDEMO_PASSWORD", "secret_sauce")

HEADLESS = os.getenv("HEADLESS", "true").strip().lower() not in ("false", "0", "no")

# Device matrix the suite runs against. "desktop" uses a default browser
# context; any other entry must match a Playwright device descriptor
# (e.g. "Pixel 5", "iPhone 13") and runs with mobile emulation.
# Override with PLAYWRIGHT_DEVICES="desktop,iPhone 13".
DEVICES = [
    d.strip()
    for d in os.getenv("PLAYWRIGHT_DEVICES", "desktop,Pixel 5").split(",")
    if d.strip()
]
