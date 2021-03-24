from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_FIELD = (By.NAME, '_username')
    PASSWORD_FIELD = (By.ID, 'password')
    ENTER_BUTTON = (By.CSS_SELECTOR, 'input[value=\'Войти\']')
    CREDENTIALS_ERROR = (By.XPATH, "//*[@class='m-login__signin']//div[text()='Invalid credentials.']")

    def fill_login_field(self, login: str):
        self.find_element(self.LOGIN_FIELD).send_keys(login)
        return self

    def get_login_field_text(self) -> str:
        return self.find_element(self.LOGIN_FIELD).get_attribute('value')

    def fill_password_field(self, password: str):
        self.find_element(self.PASSWORD_FIELD).send_keys(password)
        return self

    def get_password_field_text(self) -> str:
        return self.find_element(self.PASSWORD_FIELD).get_attribute('value')

    def click_enter_button(self):
        self.find_element(self.ENTER_BUTTON).click()

    def is_displayed_credentials_error(self) -> bool:
        try:
            return self.driver.find_element(*self.CREDENTIALS_ERROR).is_displayed()
        except NoSuchElementException:
            return False
