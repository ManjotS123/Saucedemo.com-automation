import pytest
from playwright.async_api import expect

from pages.items import Items
from utils.selectors import PRODUCT_TITLE_SELECTORS


@pytest.mark.parametrize('selector', PRODUCT_TITLE_SELECTORS)
async def test_add_to_cart_from_details(login, selector):
    page = login
    items = Items(page)
    await items.click_items(selector)

    await items.add_to_cart()

    await expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text("1")
    assert await items.cart_count() > 0, 'item was not added to the cart'
