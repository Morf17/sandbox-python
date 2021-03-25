import allure
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.calendar_page import CalendarPage
from pages.login_page import LoginPage
from settings import Settings


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        try:
            if 'init_web_driver' in item.fixturenames:
                web_driver = item.funcargs['init_web_driver']
            else:
                return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))


@pytest.fixture(scope='function')
def init_web_driver():
    options = Options()
    settings = Settings()
    options.add_argument('--window-size=500x500')
    driver = webdriver.Chrome(options=options, executable_path=settings.get_driver_path())
    driver.set_window_size('200', '100')
    driver.get(settings.get_url())
    driver.maximize_window()
    driver.implicitly_wait(2)
    yield driver
    driver.quit()


@allure.step("Авторизоваться на сайте")
@pytest.fixture(scope='function')
def auth(init_web_driver):
    driver = init_web_driver
    settings = Settings()
    if settings.get_use_api_auth():
        body = {'_csrf_token': None, '_username': settings.get_login(), '_password': settings.get_password(),
                '_submit': 'Войти'}
        headers = {'cookie': 'PHPSESSID=2fe672133d32a47c8b079908a847abfe; side-menu=minimized'}
        api_session = requests.session().post('https://tt-develop.quality-lab.ru/login_check', body, headers=headers)
        cookie_name = 'PHPSESSID'
        session_id: str = api_session.history.pop(0).cookies.get(cookie_name)
        cookie = {'name': cookie_name, 'value': session_id, 'domain': 'tt-develop.quality-lab.ru', 'path': '/',
                  'httpOnly': True, 'secure': False}
        driver.delete_all_cookies()
        driver.add_cookie(cookie)
        driver.get(settings.get_url())
    else:
        login_page = LoginPage(driver)
        login_page \
            .fill_login_field(settings.get_login()) \
            .fill_password_field(settings.get_password()) \
            .click_enter_button()
    assert driver.current_url == 'https://tt-develop.quality-lab.ru/report/group/edit'
    yield driver


@allure.step("Открыть календарь")
@pytest.fixture(scope='function')
def open_calendar(auth):
    driver = auth
    driver.get('https://tt-develop.quality-lab.ru/calendar/')
    CalendarPage(driver) \
        .wait_for_page_load() \
        .select_employee('Абдулин Ринат') \
        .wait_for_page_load()
    yield auth
