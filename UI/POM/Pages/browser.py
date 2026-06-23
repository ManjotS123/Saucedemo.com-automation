from utils.config import BASE_URL


class BrowserPage:
    def __init__(self, page):
        self.page = page
        self.page.goto(BASE_URL)
