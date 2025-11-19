import pytest
from playwright.sync_api import sync_playwright 
from Pages.cart import Cart

def test_cart(cart):
    page = cart
    
    assert 'https://www.saucedemo.com/cart.html' in page.url, 'Cart did not open'

#skip test if the cart is empty
def test_checkout_button(cart):
    page = cart
    checkout_button = Cart(page)
    
    if checkout_button.item_count() < 1 :
        pytest.skip("Cart is empty, needs at least one item to checkout")
        
    
    else :
        checkout_button.cart_checkout_button()  
        assert page('https://www.saucedemo.com/checkout-step-one.html') in page.url, 'Can not checkout'


def test_continueshopping_button(cart):
    page = cart
    return_button = Cart(page)
    return_button.cart_return_button
    


