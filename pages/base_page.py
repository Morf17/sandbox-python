from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    __timeout = 5

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver

    def find_element(self, locator, timeout=__timeout):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                                                         message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, timeout=__timeout):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator),
                                                         message=f"Can't find element by locator {locator}")

    def wait_for_element_visible(self, locator, timeout=__timeout):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element_not_visible(self, locator, timeout=__timeout) -> None:
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def wait_for(self, lambda_expression, timeout=__timeout) -> None:
        WebDriverWait(self.driver, timeout).until(lambda_expression)
