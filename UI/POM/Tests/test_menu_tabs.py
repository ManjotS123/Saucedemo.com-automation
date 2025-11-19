import pytest
from playwright.sync_api import sync_playwright 
from Pages.menu_tabs import Menu_tabs
from Pages.menu import Menu

def test_menu_tabs(login):
    page = login
    
    menu = Menu(page)
    menu.open_menu()
    
    menu_tabs = Menu_tabs(page)
    menu_tabs.click_inventory()
    menu_tabs.click_resetappstate()
    menu_tabs.click_logout()

    #'About' external site page
    #page.click('[data-test="about-sidebar-link"]')

    page.wait_for_timeout(3000)