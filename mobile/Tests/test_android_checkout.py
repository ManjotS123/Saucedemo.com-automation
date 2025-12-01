import pytest
from appium import webdriver
from Pages.android_checkout import Checkout
from UI.POM.utils.random_generator import first_name,last_name,postal_code
from .test_android_login  import login

def test_cart(login):
 driver = login
 cart = Checkout(driver)
 cart.cart()

def test_checkout(login):
 driver = login
 checkout = Checkout(driver)
 checkout.cart()
 checkout.checkout()

def test_continue_checkout(login):
 driver = login
 cont_checkout = Checkout(driver)
 cont_checkout.cart()
 cont_checkout.checkout()
 cont_checkout.checkout_info(first_name(3), last_name(3), postal_code(5))
 cont_checkout.continue_checkout()

def test_finish_checkout(login):
 driver = login
 finish = Checkout(driver)
 finish.cart()
 finish.checkout()
 finish.checkout_info(first_name(3), last_name(3), postal_code(5))
 finish.continue_checkout() 
 finish.finish_checkout()

def test_home_page(login):
 driver = login
 home = Checkout(driver)
 home.cart()
 home.checkout()
 home.checkout_info(first_name(3), last_name(3), postal_code(5))
 home.continue_checkout() 
 home.finish_checkout()
 home.home_page() 


