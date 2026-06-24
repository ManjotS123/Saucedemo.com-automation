from utils.config import BASE_URL


class Checkout:
    def __init__(self, page):
        self.page = page
        self.first_name_locator = '[data-test="firstName"]'
        self.last_name_locator = '[data-test="lastName"]'
        self.postal_code_locator = '[data-test="postalCode"]'
        self.checkout_button = '[data-test="checkout"]'
        self.cancel_button = '[data-test="cancel"]'
        self.continue_button = '[data-test="continue"]'
        self.finish_button = '[data-test="finish"]'
        self.back_to_home_button = '[data-test="back-to-products"]'
        self.checkout_one_url = f'{BASE_URL}/checkout-step-one.html'
        self.checkout_two_url = f'{BASE_URL}/checkout-step-two.html'
        self.checkout_complete_url = f'{BASE_URL}/checkout-complete.html'

    async def checkout_info(self, fname, lname, pcode):
        await self.page.click(self.checkout_button)
        await self.page.fill(self.first_name_locator, fname)
        await self.page.fill(self.last_name_locator, lname)
        await self.page.fill(self.postal_code_locator, pcode)

    async def cancel_checkout(self):
        await self.page.click(self.cancel_button)

    async def continue_checkout(self):
        await self.page.click(self.continue_button)

    async def finish_checkout(self):
        await self.page.click(self.finish_button)

    async def home(self):
        await self.page.click(self.back_to_home_button)
