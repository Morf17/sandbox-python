from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class UserCardPage(BasePage):
    FULLNAME_LABEL = (By.CSS_SELECTOR, '.m-card-user__name')
    EMAIL_LABEL = (By.CSS_SELECTOR, '.m-card-user__email')

    def get_fullname_label_text(self):
        return self.wait_for_element_visible(self.FULLNAME_LABEL).text

    def get_email_label_text(self):
        return self.wait_for_element_visible(self.EMAIL_LABEL).text
