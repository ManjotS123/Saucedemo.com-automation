class Cart:
    def __init__(self,page):
        self.page = page

    def cart_button(self):
        self.page.click('[data-test="shopping-cart-link"]')  

    def cart_checkout_button(self):
        self.page.click('[data-test="checkout"]')

    def cart_return_button(self):
        self.page.click('[data-test="continue-shopping"]')        

    def item_count(self):
        return self.page.locator('[data-test="inventory-item-name"]').count()

                   