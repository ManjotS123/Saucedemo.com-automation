import pytest
import os
import re
from playwright.sync_api import sync_playwright, Page
from Pages.login import Login_page
from Pages.cart import Cart
from Pages.checkout import Checkout
from utils.random_generator import first_name, last_name, postal_code

# Log in fixture
@pytest.fixture 
def login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        login_page = Login_page(page)
        login_page.login()

        yield page

#cart page fixture
@pytest.fixture
def cart(login):
    page = login
    cart = Cart(page)
    cart.cart_button()

    yield page

#checkout page fixture
@pytest.fixture
def checkout(cart):
    page = cart
    checkout = Checkout(page)
    
    fname = first_name(3)
    lname = last_name(3)
    pcode = postal_code(5)
    
    checkout.checkout_info(fname, lname, pcode)
    
    yield page   

#item selectors on the home page
Item_home_selectors = [
    '[data-test="add-to-cart-sauce-labs-backpack"]',
    '[data-test="add-to-cart-sauce-labs-bike-light"]',
    '[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]',
    '[data-test="add-to-cart-sauce-labs-fleece-jacket"]',
    '[data-test="add-to-cart-sauce-labs-onesie"]',
    '[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]'

]

#item selectors on their respective page i.e after clicking the item

item_selectors = [
    
    '[data-test="item-4-title-link"]',
    '[data-test="item-0-title-link"]',
    '[data-test="item-1-title-link"]',
    '[data-test="item-5-title-link"]',
    '[data-test="item-2-title-link"]',
    '[data-test="item-3-title-link"]'
]

def sanitize_filename(name: str) -> str:
    # Removes characters illegal in Windows filenames
    return re.sub(r'[<>:"/\\|?*\[\]= ]+', "_", name)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Only take screenshots at the end of the test (not setup/teardown)
    if report.when == "call":
        page = None

        # Find the Playwright Page object in fixtures
        for fixture_val in item.funcargs.values():
            if isinstance(fixture_val, Page):
                page = fixture_val
                break

        if page:
            # Create screenshot folder
            screenshot_dir = os.path.join("Screenshots", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
             
            status = "PASSED" if report.passed else "FAILED"
            
            safe_test_name = sanitize_filename(item.name)
            
            screenshot_path = os.path.join(
                screenshot_dir,
                f"{item.name}_{status}.png"
            )

             
            try:
                page.wait_for_load_state('networkidle')
                page.screenshot(path=screenshot_path, full_page=True)
            except Exception as e:
                print(f"[HOOK] Screenshot failed: {e}")

            # Attach screenshot path into JUnit XML file
            report.sections.append(("screenshot", screenshot_path))