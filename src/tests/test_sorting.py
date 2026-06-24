from pages.filters import Filters


async def test_product_sorting(login):
    sort = Filters(login)

    await sort.sort_atoz()
    assert await sort.page.locator(sort.select_box).input_value() == 'az', 'filter not found'

    await sort.sort_ztoa()
    assert await sort.page.locator(sort.select_box).input_value() == 'za', 'filter not found'

    await sort.sort_lohi()
    assert await sort.page.locator(sort.select_box).input_value() == 'lohi', 'filter not found'

    await sort.sort_hilo()
    assert await sort.page.locator(sort.select_box).input_value() == 'hilo', 'filter not found'
