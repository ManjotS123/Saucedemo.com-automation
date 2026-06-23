from utils.config import BASE_URL, USERNAME, PASSWORD


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.page.goto(BASE_URL)
        self.username = '[data-test="username"]'
        self.password = '[data-test="password"]'
        self.submit = '[data-test="login-button"]'

    def login(self, username=USERNAME, password=PASSWORD):
        self.page.fill(self.username, username)
        self.page.fill(self.password, password)
        self.page.click(self.submit)
