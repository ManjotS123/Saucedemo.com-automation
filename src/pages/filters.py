class Filters:
    def __init__(self, page):
        self.page = page
        self.select_box = '[data-test="product-sort-container"]'

    async def sort_atoz(self):
        await self.page.select_option(self.select_box, value='az', timeout=1000)

    async def sort_ztoa(self):
        await self.page.select_option(self.select_box, value='za', timeout=1000)

    async def sort_lohi(self):
        await self.page.select_option(self.select_box, value='lohi', timeout=1000)

    async def sort_hilo(self):
        await self.page.select_option(self.select_box, value='hilo', timeout=1000)
