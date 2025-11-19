
class Browser_page:
    def __init__(self, page):
        self.page = page
        self.page.goto("https://www.saucedemo.com/")  
        