from playwright.async_api import expect

from pages.browser import BrowserPage
from utils.config import BASE_URL


async def test_open_site(browser_page):
    await BrowserPage(browser_page).open()
    assert browser_page.url == f"{BASE_URL}/", 'Browser did not open the website'
    await expect(browser_page.locator('[data-test="login-button"]')).to_be_visible()


async def test_login(login):
    page = login
    assert 'https://www.saucedemo.com/inventory' in page.url, "Login has failed"
    await expect(page.locator('[data-test="inventory-list"]')).to_be_visible()
