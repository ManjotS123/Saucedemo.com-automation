import pytest
from playwright.sync_api import sync_playwright 
from test_login import login

@pytest.fixture
def cart(login):
    page = login
    page.click('[data-test="shopping-cart-link"]')
    yield page

def test_cart(cart):
    page = cart
    assert 'https://www.saucedemo.com/cart.html' in page.url, 'Cart did not open'

#always set to fail
def test_checkout_button(cart):
    page = cart
    cart_items = page.locator('[data-test="inventory-item-name"]')
    item_count = cart_items.count()                    

    if item_count < 1 :
        page.click('[data-test="checkout"]')
        page.wait_for_url('https://www.saucedemo.com/checkout-step-one.html')
        pytest.fail('Can not checkout when cart is empty')

def test_continueshopping_button(cart):
    page = cart
    page.click('[data-test="continue-shopping"]')
    


