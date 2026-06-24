from pages.menu import Menu
from pages.menu_tabs import MenuTabs


async def test_menu_button(login):
    menu = Menu(login)
    await menu.open_menu()
    await menu.close_menu()


async def test_menu_tabs(login):
    page = login

    menu = Menu(page)
    await menu.open_menu()

    menu_tabs = MenuTabs(page)
    await menu_tabs.click_inventory()
    await menu_tabs.click_resetappstate()
    await menu_tabs.click_logout()

    await page.wait_for_timeout(3000)
