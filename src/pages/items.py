class Items:
    def __init__(self, page):
        self.page = page

    async def click_items(self, selector):
        await self.page.click(selector)

    async def add_to_cart(self):
        await self.page.click('[data-test="add-to-cart"]')

    async def cart_count(self):
        cart = self.page.locator('[data-test="shopping-cart-badge"]')

        if await cart.count() < 1:
            return 0
        return int(await cart.inner_text())
