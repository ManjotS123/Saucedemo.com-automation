class Checkout:
    def __init__(self,page):
        self.page = page
        self.first_name_locator = '[data-test="firstName"]'
        self.last_name_locator =  '[data-test="lastName"]'
        self.postal_code_locator = '[data-test="postalCode"]'
        self.checkout_button = '[data-test="checkout"]'
        self.cancel_button = '[data-test="cancel"]'
        self.continue_button = '[data-test="continue"]'
        self.finish_button = '[data-test="finish"]'
        self.back_to_home_button = '[data-test="back-to-products"]'
        self.checkout_one_url = 'https://www.saucedemo.com/checkout-step-one.html'
        self.checkout_two_url = 'https://www.saucedemo.com/checkout-step-two.html'
        self.checkout_complete_url = 'https://www.saucedemo.com/checkout-complete.html'

    def  checkout_info(self,fname,lname,pcode )  :
        self.page.click(self.checkout_button)
        self.page.fill(self.first_name_locator, fname) 
        self.page.fill(self.last_name_locator, lname)
        self.page.fill(self.postal_code_locator, pcode)

    def cancel_checkout(self):
        self.page.click(self.cancel_button)

    def continue_checkout(self):
        self.page.click(self.continue_button) 

    def finish_checkout(self):
        self.page.click(self.finish_button)    

    def home(self):
        self.page.click(self.back_to_home_button)              