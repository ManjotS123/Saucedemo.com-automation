import pytest
from playwright.sync_api import sync_playwright 
from test_login import login


def test_item1(login):
    page = login
    page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    cart = page.locator('[data-test="shopping-cart-badge"]')

    page.screenshot(path= "C:/Users/manjo/OneDrive/Desktop/gen_Test/Screenshots/cart.png" )
    
    assert int(cart.inner_text()) > 0, 'item was not added to the cart'

    page.close()

def test_item2(login):
    page = login
    page.click('[data-test="add-to-cart-sauce-labs-bike-light"]')
    cart = page.locator('[data-test="shopping-cart-badge"]')

    page.screenshot(path= "C:/Users/manjo/OneDrive/Desktop/gen_Test/Screenshots/cart2.png" )

    assert int(cart.inner_text()) > 0, 'item was not added to the cart'

    page.close()



    
def test_item3(login):   
    page = login
    page.click('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')
    cart = page.locator('[data-test="shopping-cart-badge"]')

    page.screenshot(path= "C:/Users/manjo/OneDrive/Desktop/gen_Test/Screenshots/cart3.png" )

    assert int(cart.inner_text()) > 0, 'item was not added to the cart'

    page.close()



def test_item4(login):
    page = login
    page.click('[data-test="add-to-cart-sauce-labs-fleece-jacket"]')
    cart = page.locator('[data-test="shopping-cart-badge"]')

    page.screenshot(path= "C:/Users/manjo/OneDrive/Desktop/gen_Test/Screenshots/cart4.png" )

    assert int(cart.inner_text()) > 0, 'item was not added to the cart'

    page.close()

def test_item5(login):
    page = login    
    page.click('[data-test="add-to-cart-sauce-labs-onesie"]')
    cart = page.locator('[data-test="shopping-cart-badge"]')

    page.screenshot(path= "C:/Users/manjo/OneDrive/Desktop/gen_Test/Screenshots/cart5.png" )

    assert int(cart.inner_text()) > 0, 'item was not added to the cart'

    page.close()


def test_item6(login):
    page = login    
    page.click('[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]')
    cart = page.locator('[data-test="shopping-cart-badge"]')


    page.screenshot(path= "C:/Users/manjo/OneDrive/Desktop/gen_Test/Screenshots/cart6.png" )

    assert int(cart.inner_text()) > 0, 'item was not added to the cart'

    page.close()