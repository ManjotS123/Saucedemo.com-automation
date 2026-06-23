import os

from appium.options.android import UiAutomator2Options
from appium import webdriver


def driver_instance():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = os.getenv("ANDROID_DEVICE_NAME", "Pixel 6")
    options.automation_name = "UiAutomator2"
    options.browser_name = "Chrome"
    # Path to the local chromedriver and the Appium server are environment
    # specific, so keep them overridable instead of hardcoded.
    options.chromedriver_executable = os.getenv(
        "CHROMEDRIVER_PATH",
        "C:/chromedriver-win64/chromedriver-win64/chromedriver.exe",
    )

    url = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")

    driver = webdriver.Remote(command_executor=url, options=options)

    return driver
