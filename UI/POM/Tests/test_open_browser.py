import pytest
from playwright.sync_api import sync_playwright
from Pages.browser import Browser_page 


def test_open_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = True)
        page = browser.new_page()
        open_browser = Browser_page(page)

        assert page.url == "https://www.saucedemo.com/", 'Browser did not open the website' 
    
