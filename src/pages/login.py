from utils.config import BASE_URL, USERNAME, PASSWORD


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = '[data-test="username"]'
        self.password = '[data-test="password"]'
        self.submit = '[data-test="login-button"]'

    async def open(self):
        await self.page.goto(BASE_URL)

    async def login(self, username=USERNAME, password=PASSWORD):
        await self.open()
        await self.page.fill(self.username, username)
        await self.page.fill(self.password, password)
        await self.page.click(self.submit)
