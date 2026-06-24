class Cart:
    def __init__(self, page):
        self.page = page

    async def cart_button(self):
        await self.page.click('[data-test="shopping-cart-link"]')

    async def cart_checkout_button(self):
        await self.page.click('[data-test="checkout"]')

    async def cart_return_button(self):
        await self.page.click('[data-test="continue-shopping"]')

    async def item_count(self):
        return await self.page.locator('[data-test="inventory-item-name"]').count()
