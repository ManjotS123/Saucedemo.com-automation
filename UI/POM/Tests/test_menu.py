import pytest
from Pages.menu import Menu


def test_menu_button(login):
    page = login
    
    menu = Menu(page)
    menu.open_menu()
    menu.close_menu()
    