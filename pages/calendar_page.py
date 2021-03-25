import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CalendarPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.__loader = lambda: self.find_element((By.ID, 'schedule-overlay'))
        self.__month_title = lambda: self.find_element((By.ID, 'schedule-month-title'))
        self.__employee_selector = lambda: self.find_element((By.ID, 'select2--container'))
        self.__apply_button = lambda: self.find_element((By.CSS_SELECTOR, '.btn_do_filter'))
        self.__working_days = lambda: self.find_elements((By.CSS_SELECTOR, '.schedule-badge--default'))
        self.__weekends = lambda: self.find_elements((By.CSS_SELECTOR, '.schedule-badge--no-event'))
        self.__date_selector = lambda: self.find_element((By.CSS_SELECTOR, '.date-filter'))
        self.__next_month = lambda: self.find_element((By.CSS_SELECTOR, '.datepicker-months td .active +*'))
        self.__employee_search_field = lambda: self.find_element((By.CSS_SELECTOR, '.select2-dropdown '
                                                                                   '.select2-search__field'))

    @allure.step('Дождаться загрузки страницы')
    def wait_for_page_load(self):
        self.wait_for(lambda driver: self.__loader().get_attribute('style') == 'display: none;')
        return self

    @allure.step('Получить выбранный месяц и год')
    def get_month_title_text(self) -> str:
        return self.__month_title().text

    @allure.step('Выбрать сотрудника: {full_name}')
    def select_employee(self, full_name: str):
        self.__employee_selector().click()
        self.__employee_search_field().send_keys(full_name)
        xpath = f"//*[contains(@class, 'select2-results__option') and text()='{full_name}']"
        self.find_element((By.XPATH, xpath)).click()
        self.__apply_button().click()
        return self

    @allure.step('Получить наличие рабочих дней')
    def have_working_days(self) -> bool:
        return len(self.__working_days()) > 0

    @allure.step('Получить наличие выходных дней')
    def have_weekends(self) -> bool:
        return len(self.__weekends()) > 0

    @allure.step('Выбрать следующий месяц')
    def select_next_month(self):
        self.__date_selector().click()
        self.__next_month().click()
        self.__apply_button().click()
        return self
