import pytest
from playwright.sync_api import sync_playwright 
from .conftest import item_selectors
from Pages.items import Items

@pytest.mark.parametrize('item_selectors', item_selectors)
def test_items(item_selectors, login):
    page = login
    items = Items(page)
    items.click_items(item_selectors)
    
    page.wait_for_timeout(3000)
          
    items.add_to_cart()
    
    assert items.cart_count() > 0, 'item was not added to the cart'


    
    
