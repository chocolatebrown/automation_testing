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


class TestSample():
    @pytest.fixture()
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_login(self, setUp):
        self.driver.get(demo_url)
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id("user-name").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("login-button").click()
        time.sleep(1)
        assert login_sucess == self.driver.current_url

    def test_logout(self, setUp):
        self.driver.get(demo_url)
        self.driver.find_element_by_id("user-name").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("login-button").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id("react-burger-menu-btn").click()
        self.driver.find_element_by_id("logout_sidebar_link").click()
        signout = self.driver.find_element_by_id("login-button")
        assert signout.get_attribute('value') == "Login"


