from pages.login_page import LoginPage
from pages.main_page import MainPage
from settings import Settings
from tests.base_test import BaseTest


class TestLoginPositive(BaseTest):

    def test_correct_username_and_password(self, init_web_driver):
        self.driver = init_web_driver
        login_page = LoginPage(self.driver)
        login_page \
            .fill_login_field(Settings().get_login()) \
            .fill_password_field(Settings().get_password()) \
            .click_enter_button()
        assert self.driver.current_url == 'https://tt-develop.quality-lab.ru/report/group/edit'
        user_card_page = MainPage(self.driver).click_profile_button()
        assert 'Сальников' in user_card_page.get_fullname_label_text()
        email = user_card_page.get_email_label_text()
        assert 'fake+' in email and '@quality-lab.ru' in email, f"Отображается неправильный email: {email}"
