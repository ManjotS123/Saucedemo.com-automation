import pytest
from playwright.sync_api import sync_playwright 
from test_login import login


def test_item1(login):
    page = login
    page.click('[data-test="item-4-title-link"]')
    page.click('[data-test="add-to-cart"]')
    cart = page.locator('[data-test="shopping-cart-badge"]')

    page.screenshot(path= "C:/Users/manjo/OneDrive/Desktop/gen_Test/Screenshots/items/item.png" )
    
    assert int(cart.inner_text()) > 0, 'item was not added to the cart'

    page.close()

def test_item2(login):
    page = login
    page.click('[data-test="item-0-title-link"]')
    page.click('[data-test="add-to-cart"]')
    cart = page.locator('[data-test="shopping-cart-badge"]')

    page.screenshot(path= "C:/Users/manjo/OneDrive/Desktop/gen_Test/Screenshots/items/item2.png" )

    assert int(cart.inner_text()) > 0, 'item was not added to the cart'

    page.close()



    
def test_item3(login):   
    page = login
    page.click('[data-test="item-1-title-link"]')
    page.click('[data-test="add-to-cart"]')
    cart = page.locator('[data-test="shopping-cart-badge"]')

    page.screenshot(path= "C:/Users/manjo/OneDrive/Desktop/gen_Test/Screenshots/items/item3.png" )

    assert int(cart.inner_text()) > 0, 'item was not added to the cart'

    page.close()



def test_item4(login):
    page = login
    page.click('[data-test="item-5-title-link"]')
    page.click('[data-test="add-to-cart"]')
    cart = page.locator('[data-test="shopping-cart-badge"]')

    page.screenshot(path= "C:/Users/manjo/OneDrive/Desktop/gen_Test/Screenshots/items/item4.png" )

    assert int(cart.inner_text()) > 0, 'item was not added to the cart'

    page.close()

def test_item5(login):
    page = login    
    page.click('[data-test="item-2-title-link"]')
    page.click('[data-test="add-to-cart"]')
    cart = page.locator('[data-test="shopping-cart-badge"]')

    page.screenshot(path= "C:/Users/manjo/OneDrive/Desktop/gen_Test/Screenshots/items/item5.png" )

    assert int(cart.inner_text()) > 0, 'item was not added to the cart'

    page.close()


def test_item6(login):
    page = login    
    page.click('[data-test="item-3-title-link"]')
    page.click('[data-test="add-to-cart"]')
    cart = page.locator('[data-test="shopping-cart-badge"]')


    page.screenshot(path= "C:/Users/manjo/OneDrive/Desktop/gen_Test/Screenshots/items/item6.png" )

    assert int(cart.inner_text()) > 0, 'item was not added to the cart'

    page.close()

#[data-test="back-to-products"]