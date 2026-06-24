import pytest

from pages.item_home import ItemHome
from utils.selectors import INVENTORY_ADD_TO_CART_SELECTORS


@pytest.mark.parametrize('selector', INVENTORY_ADD_TO_CART_SELECTORS)
async def test_add_to_cart_from_listing(login, selector):
    page = login
    items = ItemHome(page)
    await items.click_cart(selector)

    assert await items.cart_count() > 0, "Item was not added to the cart"
