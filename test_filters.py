import pytest
from playwright.sync_api import sync_playwright 
from test_login import login

def test_menu_tabs(login):
    page = login
    
    #selects different filters
    page.select_option('[data-test="product-sort-container"]', value='az', timeout= 1000)

    page.select_option('[data-test="product-sort-container"]', value='za', timeout= 1000)
    
    page.select_option('[data-test="product-sort-container"]', value='lohi', timeout= 1000)
    
    page.select_option('[data-test="product-sort-container"]', value='hilo', timeout = 1000)

    