class Items:
    def __init__(self,page):
        self.page = page

    def click_items(self, selector):
        self.page.click(selector)

    def add_to_cart(self):
        self.page.click('[data-test="add-to-cart"]')

    def cart_count(self):
        cart = self.page.locator('[data-test="shopping-cart-badge"]')     

        if cart.count() <1 :
            return 0
        return int(cart.inner_text())        