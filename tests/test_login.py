import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestLogin:

    @pytest.fixture(scope='function')
    def init_web_driver(self):
        options = Options()
        options.add_argument('--window-size=500x500')
        driver = webdriver.Chrome(options=options, executable_path='C:\webdrivers\chrome\chromedriver.exe')
        driver.set_window_size('200', '100')
        driver.get('https://tt-develop.quality-lab.ru')
        driver.maximize_window()
        driver.implicitly_wait(2)
        yield driver
        driver.quit()

    def test_incorrect_username_and_password(self, init_web_driver):
        driver = init_web_driver
        driver.find_element(By.NAME, '_username').send_keys('TestUser')
        driver.find_element(By.ID, 'password').send_keys('Password')
        xpath = "//*[@class='m-login__signin']//div[text()='Invalid credentials.']"
        error_message = lambda: driver.find_element(By.XPATH, xpath)
        with pytest.raises(NoSuchElementException):
            error_message()
        driver.find_element(By.CSS_SELECTOR, "input[value='Войти']").click()
        assert error_message().is_displayed() is True, "Не отображается ошибка о неправильном логине/пароле"
