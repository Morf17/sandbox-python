import allure

from pages.login_page import LoginPage
from tests.base_test import BaseTest


class TestsLoginNegative(BaseTest):

    @allure.description('Проверка авторизации с неправильным логином и паролем')
    def test_incorrect_username_and_password(self, init_web_driver):
        self.driver = init_web_driver
        login_page = LoginPage(self.driver)
        login = 'TestUser'
        password = 'Password'
        login_page.fill_login_field(login).fill_password_field(password)
        assert login_page.is_displayed_credentials_error() is False
        login_page.click_enter_button()
        assert login_page.is_displayed_credentials_error() is True
        assert login_page.get_login_field_text() == login
        assert login_page.get_password_field_text() == ''

    @allure.description('Проверка авторизации с пустым логином и паролем')
    def test_empty_username_and_password(self, init_web_driver):
        self.driver = init_web_driver
        login_page = LoginPage(self.driver)
        login_page.click_enter_button()
        assert login_page.is_displayed_credentials_error() is False
        assert self.driver.current_url == 'https://tt-develop.quality-lab.ru/login'
