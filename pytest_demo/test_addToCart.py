import time
import pytest
import pytest_html
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

demo_url = "https://www.saucedemo.com/"

username = "standard_user"
password = "secret_sauce"
login_sucess = "https://www.saucedemo.com/inventory.html"


@pytest.fixture()
def setUp():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()

def test_addToCart(setUp):
    driver.get(demo_url)
    driver.find_element_by_id("user-name").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("login-button").click()
    driver.implicitly_wait(2)
    driver.find_elements_by_xpath('(//div[@id="inventory_container"]//button)')[0].click()
    driver.implicitly_wait(10)
    cart_value = driver.find_element_by_id("shopping_cart_container").text
    assert cart_value == '1'

def test_removeToCart(setUp):
    driver.get(demo_url)
    driver.find_element_by_id("user-name").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("login-button").click()
    driver.implicitly_wait(2)
    driver.find_elements_by_xpath('(//div[@id="inventory_container"]//button)')[0].click()
    driver.implicitly_wait(2)
    driver.find_element_by_id("remove-sauce-labs-backpack").click()
    buttons = driver.find_elements_by_xpath('//div[@class="inventory_item"]')
    assert len(buttons) == 6