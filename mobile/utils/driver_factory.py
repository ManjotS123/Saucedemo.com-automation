from appium.options.android import UiAutomator2Options
from appium import webdriver

def driver_instance():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Pixel 6"
    options.automation_name = "UiAutomator2"
    options.browser_name = "Chrome"
    options.chromedriver_executable = "C:/chromedriver-win64/chromedriver-win64/chromedriver.exe"

    url = "http://127.0.0.1:4723"
        
    driver = webdriver.Remote(command_executor=url, options = options)

    return driver