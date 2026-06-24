import pytest
from playwright.async_api import expect

from pages.item_home import ItemHome
from utils.selectors import INVENTORY_ADD_TO_CART_SELECTORS


@pytest.mark.parametrize('selector', INVENTORY_ADD_TO_CART_SELECTORS)
async def test_add_to_cart_from_listing(login, selector):
    page = login
    items = ItemHome(page)
    await items.click_cart(selector)

    await expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text("1")
    assert await items.cart_count() > 0, "Item was not added to the cart"
