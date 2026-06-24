from playwright.async_api import expect

from pages.menu import Menu
from pages.menu_tabs import MenuTabs
from utils.config import BASE_URL


async def test_menu_button(login):
    page = login
    menu = Menu(page)

    sidebar_link = page.locator('[data-test="inventory-sidebar-link"]')

    await menu.open_menu()
    await expect(sidebar_link).to_be_in_viewport()

    await menu.close_menu()
    await expect(sidebar_link).not_to_be_in_viewport()


async def test_menu_tabs(login):
    page = login
    menu = Menu(page)
    await menu.open_menu()

    menu_tabs = MenuTabs(page)
    await menu_tabs.click_inventory()
    await menu_tabs.click_resetappstate()
    await menu_tabs.click_logout()

    await expect(page.locator('[data-test="login-button"]')).to_be_visible()
    assert page.url.rstrip('/') == BASE_URL.rstrip('/'), 'Did not return to the login page after logout'
