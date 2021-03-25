import allure
import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage
from settings import Settings
from tests.base_test import BaseTest


class TestLoginPositive(BaseTest):

    @pytest.mark.parametrize('login,password', [(Settings().get_login(), Settings().get_password()), ('Тест', 'Тест')])
    @allure.description('Авторизация с правильным логином и паролем')
    def test_correct_username_and_password(self, init_web_driver, login, password):
        self.driver = init_web_driver
        login_page = LoginPage(self.driver)
        login_page \
            .fill_login_field(login) \
            .fill_password_field(password) \
            .click_enter_button()
        expected_url = 'https://tt-develop.quality-lab.ru/report/group/edit'
        assert self.driver.current_url == expected_url, 'Не удалось авторизоваться'
        user_card_page = MainPage(self.driver).click_profile_button()
        assert 'Сальников' in user_card_page.get_fullname_label_text(), 'Неправильное ФИО сотрудника'
        email = user_card_page.get_email_label_text()
        assert 'fake+' in email and '@quality-lab.ru' in email, f"Отображается неправильный email: {email}"
