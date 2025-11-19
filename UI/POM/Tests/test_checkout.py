import pytest
from playwright.sync_api import sync_playwright 
from utils.random_generator import first_name, last_name, postal_code
from Pages.checkout import Checkout


def test_checkout_one(checkout):
    page = checkout
    
    assert 'https://www.saucedemo.com/checkout-step-one.html' in page.url, 'checkout not successful'

def test_cancel(checkout):
    page = checkout
    cancel = Checkout(page)
    cancel.cancel_checkout()

    
    assert 'https://www.saucedemo.com/cart.html' in page.url, 'checkout not successful'

def test_checkout_two(checkout):
    page = checkout
    step_two = Checkout(page)
    step_two.continue_checkout()

    assert 'https://www.saucedemo.com/checkout-step-two.html' in page.url, 'checkout not successful'


def test_checkout_complete(checkout):
    page = checkout
    complete = Checkout(page)
    complete.continue_checkout() 
    complete.finish_checkout()

    assert 'https://www.saucedemo.com/checkout-complete.html' in page.url, 'checkout not successful'

def test_home_page(checkout):
    page = checkout
    finish = Checkout(page)
    finish.continue_checkout() 
    finish.finish_checkout()
    finish.home() 

    assert 'https://www.saucedemo.com/inventory.html' in page.url, 'could not return to home page'

