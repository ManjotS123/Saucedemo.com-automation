class Menu:
    def __init__(self, page):
        self.page = page

    async def open_menu(self):
        await self.page.get_by_role("button", name="Open Menu").click()

    async def close_menu(self):
        await self.page.get_by_role("button", name="Close Menu").click()
