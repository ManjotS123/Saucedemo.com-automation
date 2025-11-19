class Login_page:
    def __init__(self, page):
        self.page = page
        self.page.goto("https://www.saucedemo.com")
        self.username = '[data-test="username"]'
        self.password = '[data-test="password"]'
        self.submit = '[data-test="login-button"]'
    

    def login(self):
        self.page.fill(self.username, 'standard_user')
        self.page.fill(self.password, 'secret_sauce')
        self.page.click(self.submit)

