class Menu_tabs:
    def __init__(self, page):
        self.page = page

    def click_inventory(self):
        self.page.click('[data-test="inventory-sidebar-link"]') 

    def click_logout(self):
        self.page.click('[data-test="logout-sidebar-link"]')
    
    def click_resetappstate(self):
        self.page.click('[data-test="reset-sidebar-link"]')