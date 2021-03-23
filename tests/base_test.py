import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseTest:

    @pytest.fixture(scope='function')
    def init_web_driver(self):
        options = Options()
        options.add_argument('--window-size=500x500')
        driver = webdriver.Chrome(options=options, executable_path='C:\\webdrivers\\chrome\\chromedriver.exe')
        driver.set_window_size('200', '100')
        driver.get('https://tt-develop.quality-lab.ru')
        driver.maximize_window()
        driver.implicitly_wait(2)
        yield driver
        driver.quit()
