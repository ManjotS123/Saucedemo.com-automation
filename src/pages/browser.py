from utils.config import BASE_URL


class BrowserPage:
    def __init__(self, page):
        self.page = page

    async def open(self):
        await self.page.goto(BASE_URL)
