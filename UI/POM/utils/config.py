import os

BASE_URL = os.getenv("SAUCEDEMO_BASE_URL", "https://www.saucedemo.com")
USERNAME = os.getenv("SAUCEDEMO_USERNAME", "standard_user")
PASSWORD = os.getenv("SAUCEDEMO_PASSWORD", "secret_sauce")

HEADLESS = os.getenv("HEADLESS", "true").strip().lower() not in ("false", "0", "no")
