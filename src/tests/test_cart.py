from playwright.async_api import expect

from pages.cart import Cart


async def test_cart(cart):
    page = cart
    assert 'https://www.saucedemo.com/cart.html' in page.url, 'Cart did not open'
    await expect(page.locator('[data-test="title"]')).to_have_text("Your Cart")


async def test_checkout_button(cart):
    page = cart
    checkout_button = Cart(page)

    await checkout_button.cart_checkout_button()
    assert 'https://www.saucedemo.com/checkout-step-one.html' in page.url, 'Can not checkout'
    await expect(page.locator('[data-test="title"]')).to_have_text("Checkout: Your Information")


async def test_continueshopping_button(cart):
    page = cart
    return_button = Cart(page)
    await return_button.cart_return_button()

    assert 'https://www.saucedemo.com/inventory.html' in page.url, 'Did not return to products page'
    await expect(page.locator('[data-test="inventory-list"]')).to_be_visible()
