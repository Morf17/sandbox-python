from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.user_card_page import UserCardPage


class MainPage(BasePage):
    AVATAR_BUTTON = (By.CSS_SELECTOR, '.m-topbar__user-profile')

    def click_profile_button(self) -> UserCardPage:
        self.find_element(self.AVATAR_BUTTON).click()
        return UserCardPage(self.driver)
