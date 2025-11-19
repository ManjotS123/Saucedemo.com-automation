class Filters:
    def __init__(self,page):
       self.page = page
       self.select_box = '[data-test="product-sort-container"]'

    def sort_atoz(self):
        self.page.select_option(self.select_box, value='az', timeout= 1000)

    def sort_ztoa(self):
        self.page.select_option(self.select_box, value='za', timeout= 1000)

    def sort_lohi(self):
        self.page.select_option(self.select_box, value='lohi', timeout= 1000)

    def sort_hilo(self):
        self.page.select_option(self.select_box, value='hilo', timeout = 1000)       
