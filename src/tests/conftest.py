import os
import re
from pathlib import Path

import pytest
from playwright.async_api import async_playwright

from pages.login import LoginPage
from pages.item_home import ItemHome
from pages.cart import Cart
from pages.checkout import Checkout
from utils.random_generator import first_name, last_name, postal_code
from utils.config import HEADLESS, DEVICES
from utils.selectors import INVENTORY_ADD_TO_CART_SELECTORS

REPO_ROOT = Path(__file__).resolve().parents[2]
REPORTS_DIR = REPO_ROOT / "reports"
SCREENSHOTS_DIR = REPO_ROOT / "Screenshots" / "screenshots"


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    if not config.option.xmlpath:
        config.option.xmlpath = str(REPORTS_DIR / "results.xml")


def sanitize_filename(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*\[\]= ]+', "_", name)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)


async def capture_screenshot(page, node):
    report = getattr(node, "rep_call", None)
    if report is None:
        return
    status = "PASSED" if report.passed else "FAILED"
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    path = os.path.join(str(SCREENSHOTS_DIR), f"{sanitize_filename(node.name)}_{status}.png")
    try:
        await page.wait_for_load_state("domcontentloaded")
        await page.screenshot(path=path, full_page=True)
    except Exception as e:
        print(f"[screenshot] failed: {e}")


# Browser fixture: parametrized across the desktop + mobile device matrix
# defined in config.py. "desktop" uses a default context; any other name is
# resolved through Playwright's built-in device descriptors for emulation.
@pytest.fixture(params=DEVICES, ids=DEVICES)
async def browser_page(request):
    device_name = request.param.strip()
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=HEADLESS)

        if device_name.lower() == "desktop":
            context = await browser.new_context()
        else:
            context = await browser.new_context(**p.devices[device_name])

        page = await context.new_page()

        try:
            yield page
        finally:
            await capture_screenshot(page, request.node)
            await context.close()
            await browser.close()


@pytest.fixture
async def login(browser_page):
    page = browser_page
    await LoginPage(page).login()
    yield page


@pytest.fixture
async def cart(login):
    page = login
    # Add a product so the cart is non-empty for downstream checkout steps.
    await ItemHome(page).click_cart(INVENTORY_ADD_TO_CART_SELECTORS[0])
    await Cart(page).cart_button()
    yield page


@pytest.fixture
async def checkout(cart):
    page = cart
    checkout = Checkout(page)
    await checkout.checkout_info(first_name(3), last_name(3), postal_code(5))
    yield page
