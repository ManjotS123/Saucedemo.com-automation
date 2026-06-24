import pytest

from pages.cart import Cart


async def test_cart(cart):
    page = cart
    assert 'https://www.saucedemo.com/cart.html' in page.url, 'Cart did not open'


async def test_checkout_button(cart):
    page = cart
    checkout_button = Cart(page)

    if await checkout_button.item_count() < 1:
        pytest.skip("Cart is empty, needs at least one item to checkout")
    else:
        await checkout_button.cart_checkout_button()
        assert 'https://www.saucedemo.com/checkout-step-one.html' in page.url, 'Can not checkout'


async def test_continueshopping_button(cart):
    page = cart
    return_button = Cart(page)
    await return_button.cart_return_button()

    assert 'https://www.saucedemo.com/inventory.html' in page.url, 'Did not return to products page'
