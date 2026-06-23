from playwright.sync_api import sync_playwright
from Pages.browser import BrowserPage
from utils.config import BASE_URL, HEADLESS


def test_open_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        page = browser.new_page()
        BrowserPage(page)

        assert page.url == f"{BASE_URL}/", 'Browser did not open the website'

        browser.close()
