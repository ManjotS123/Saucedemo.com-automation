import pytest
from playwright.sync_api import sync_playwright 
from .conftest import Item_home_selectors
from Pages.item_home import Item_home

@pytest.mark.parametrize('selectors', Item_home_selectors)
def test_home_items(login, selectors):
    page = login
    items = Item_home(page)
    items.click_cart(selectors)
    
    assert items.cart_count() > 0, "Item was not added to the cart"
    
