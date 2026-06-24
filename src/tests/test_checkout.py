from playwright.async_api import expect

from pages.checkout import Checkout


async def test_checkout_one(checkout):
    page = checkout
    assert 'https://www.saucedemo.com/checkout-step-one.html' in page.url, 'checkout not successful'
    await expect(page.locator('[data-test="title"]')).to_have_text("Checkout: Your Information")


async def test_cancel(checkout):
    page = checkout
    cancel = Checkout(page)
    await cancel.cancel_checkout()

    assert 'https://www.saucedemo.com/cart.html' in page.url, 'checkout not successful'
    await expect(page.locator('[data-test="title"]')).to_have_text("Your Cart")


async def test_checkout_two(checkout):
    page = checkout
    step_two = Checkout(page)
    await step_two.continue_checkout()

    assert 'https://www.saucedemo.com/checkout-step-two.html' in page.url, 'checkout not successful'
    await expect(page.locator('[data-test="title"]')).to_have_text("Checkout: Overview")


async def test_checkout_complete(checkout):
    page = checkout
    complete = Checkout(page)
    await complete.continue_checkout()
    await complete.finish_checkout()

    assert 'https://www.saucedemo.com/checkout-complete.html' in page.url, 'checkout not successful'
    await expect(page.locator('[data-test="complete-header"]')).to_have_text("Thank you for your order!")


async def test_home_page(checkout):
    page = checkout
    finish = Checkout(page)
    await finish.continue_checkout()
    await finish.finish_checkout()
    await finish.home()

    assert 'https://www.saucedemo.com/inventory.html' in page.url, 'could not return to home page'
    await expect(page.locator('[data-test="inventory-list"]')).to_be_visible()
