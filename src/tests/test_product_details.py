import pytest

from pages.items import Items
from utils.selectors import PRODUCT_TITLE_SELECTORS


@pytest.mark.parametrize('selector', PRODUCT_TITLE_SELECTORS)
async def test_add_to_cart_from_details(login, selector):
    page = login
    items = Items(page)
    await items.click_items(selector)

    await page.wait_for_timeout(3000)

    await items.add_to_cart()

    assert await items.cart_count() > 0, 'item was not added to the cart'
