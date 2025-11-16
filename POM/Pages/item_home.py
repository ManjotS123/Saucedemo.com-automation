class Item_home:
    def __init__(self,page):
        self.page = page
    
    def click_cart(self,selector):
         self.page.click(selector)

    def cart_count(self):
        cart = self.page.locator('[data-test="shopping-cart-badge"]')     

        if cart.count() <1 :
            return 0
        return int(cart.inner_text())