from Pages.browser import BrowserPage
from utils.config import BASE_URL


def test_open_browser(browser_page):
    BrowserPage(browser_page)

    assert browser_page.url == f"{BASE_URL}/", 'Browser did not open the website'
