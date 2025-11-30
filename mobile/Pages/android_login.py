from  appium.webdriver.common.appiumby import AppiumBy

class LoginPage:
   def __init__(self, driver):
      self.driver = driver
      self.username = (AppiumBy.CSS_SELECTOR,  '[data-test="username"]')
      self.password = (AppiumBy.CSS_SELECTOR, '[data-test="password"]')
      self.submit = (AppiumBy.CSS_SELECTOR, '[data-test="login-button"]')
   

   def login(self):
      self.driver.get("https://www.saucedemo.com/") 
      self.driver.find_element(*self.username).send_keys("standard_user")
      self.driver.find_element(*self.password).send_keys("secret_sauce")
      self.driver.find_element(*self.submit).click()
      