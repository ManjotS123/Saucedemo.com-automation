import pytest
from  appium import webdriver
from  appium.webdriver.common.appiumby import AppiumBy
from Pages.android_login import LoginPage
from utils.driver_factory import driver_instance


@pytest.fixture(scope="function")
def login():
    driver = driver_instance()
    login = LoginPage(driver)
    login.login()

    yield driver

def test_login(login):
    login
    
    button = login.find_element(AppiumBy.CSS_SELECTOR, 'button')
    assert button.text == "button",'Login has failed' 


    

    
