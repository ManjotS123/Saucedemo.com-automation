import pytest
from playwright.sync_api import sync_playwright 
from Pages.filters import Filters

def test_filters(login):
    page = login
    sort = Filters(page)
    
    sort.sort_atoz()
    assert sort.page.locator(sort.select_box).input_value() == 'az', 'filter not found'
    
    sort.sort_ztoa()
    assert sort.page.locator(sort.select_box).input_value() == 'za', 'filter not found'

    sort.sort_lohi()
    assert sort.page.locator(sort.select_box).input_value() == 'lohi', 'filter not found'
    
    sort.sort_hilo()
    assert sort.page.locator(sort.select_box).input_value() == 'hilo', 'filter not found'


    