from  appium.webdriver.common.appiumby import AppiumBy

class Checkout:
   def __init__(self, driver):
      self.driver = driver
      self.cart_button = (AppiumBy.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
      self.first_name = (AppiumBy.CSS_SELECTOR, '[data-test="firstName"]')
      self.last_name =  (AppiumBy.CSS_SELECTOR, '[data-test="lastName"]')
      self.postal_code = (AppiumBy.CSS_SELECTOR, '[data-test="postalCode"]')
      self.checkout_button = (AppiumBy.CSS_SELECTOR, '[data-test="checkout"]')
      self.cancel_button = (AppiumBy.CSS_SELECTOR, '[data-test="cancel"]')
      self.continue_button = (AppiumBy.CSS_SELECTOR, '[data-test="continue"]')
      self.finish_button = (AppiumBy.CSS_SELECTOR, '[data-test="finish"]')
      self.back_to_home_button = (AppiumBy.CSS_SELECTOR, '[data-test="back-to-products"]')

   def cart(self):
      self.driver.find_element(*self.cart_button).click()  

   def checkout_info(self, fname, lname, pcode):
      self.driver.find_element(*self.first_name).send_keys(fname)
      self.driver.find_element(*self.last_name).send_keys(lname)
      self.driver.find_element(*self.postal_code).send_keys(pcode)

   def checkout(self):
      self.driver.find_element(*self.checkout_button).click()

   def cancel(self):
      self.driver.find_element(*self.cancel_button).click()

   def continue_checkout(self):
      self.driver.find_element(*self.continue_button).click()

   def finish_checkout(self):
      self.driver.find_element(*self.finish_button).click()

   def home_page(self):
      self.driver.find_element(*self.back_to_home_button).click()           
