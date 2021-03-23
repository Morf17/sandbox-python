from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class UserCardPage(BasePage):
    LOCATOR_FULLNAME_LABEL = (By.CSS_SELECTOR, '.m-card-user__name')
    LOCATOR_EMAIL_LABEL = (By.CSS_SELECTOR, '.m-card-user__email')

    def get_fullname_label_text(self):
        return self.wait_for_element_visible(self.LOCATOR_FULLNAME_LABEL).text

    def get_email_label_text(self):
        return self.wait_for_element_visible(self.LOCATOR_EMAIL_LABEL).text
