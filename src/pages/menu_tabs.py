class MenuTabs:
    def __init__(self, page):
        self.page = page

    async def click_inventory(self):
        await self.page.click('[data-test="inventory-sidebar-link"]')

    async def click_logout(self):
        await self.page.click('[data-test="logout-sidebar-link"]')

    async def click_resetappstate(self):
        await self.page.click('[data-test="reset-sidebar-link"]')
