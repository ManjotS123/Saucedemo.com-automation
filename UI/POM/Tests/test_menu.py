import pytest
from playwright.sync_api import sync_playwright 
from Pages.menu import Menu


def test_menu_button(login):
    page = login
    
    menu = Menu(page)
    menu.open_menu()
    menu.close_menu()
    