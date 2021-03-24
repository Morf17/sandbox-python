import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage
from settings import Settings


class BaseTest:

    @pytest.fixture(scope='function')
    def init_web_driver(self):
        options = Options()
        options.add_argument('--window-size=500x500')
        driver = webdriver.Chrome(options=options, executable_path=Settings().get_driver_path())
        driver.set_window_size('200', '100')
        driver.get(Settings().get_url())
        driver.maximize_window()
        driver.implicitly_wait(2)
        yield driver
        driver.quit()

    @pytest.fixture(scope='function')
    def auth(self, init_web_driver):
        driver = init_web_driver
        login_page = LoginPage(driver)
        login_page \
            .fill_login_field(Settings().get_login()) \
            .fill_password_field(Settings().get_password()) \
            .click_enter_button()
        assert driver.current_url == 'https://tt-develop.quality-lab.ru/report/group/edit'
        yield init_web_driver
