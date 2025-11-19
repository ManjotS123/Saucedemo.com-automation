import pytest
from playwright.sync_api import sync_playwright 

    
def test_login (login):
    page = login
    assert 'https://www.saucedemo.com/inventory' in page.url, "Login has failed"

   
     
    
     