from playwright.async_api import expect

from pages.filters import Filters


async def test_product_sorting(login):
    sort = Filters(login)
    select = sort.page.locator(sort.select_box)

    await sort.sort_atoz()
    await expect(select).to_have_value('az')
    assert await select.input_value() == 'az', 'filter not found'

    await sort.sort_ztoa()
    await expect(select).to_have_value('za')
    assert await select.input_value() == 'za', 'filter not found'

    await sort.sort_lohi()
    await expect(select).to_have_value('lohi')
    assert await select.input_value() == 'lohi', 'filter not found'

    await sort.sort_hilo()
    await expect(select).to_have_value('hilo')
    assert await select.input_value() == 'hilo', 'filter not found'
