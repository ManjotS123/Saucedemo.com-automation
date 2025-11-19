class Menu:
    def __init__(self, page):
        self.page = page
        
    def open_menu(self):
        self.page.get_by_role("button", name="Open Menu").click()

    def close_menu(self):
        self.page.get_by_role("button", name="Close Menu").click()





