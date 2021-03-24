import locale
from datetime import datetime

import pytest

from pages.calendar_page import CalendarPage
from tests.base_test import BaseTest


class TestCalendar(BaseTest):

    @pytest.fixture(scope='function')
    def open_calendar(self, auth):
        self.driver = auth
        self.driver.get('https://tt-develop.quality-lab.ru/calendar/')
        CalendarPage(self.driver) \
            .wait_for_page_load() \
            .select_employee('Абдулин Ринат') \
            .wait_for_page_load()
        yield auth

    def test_current_month(self, open_calendar):
        calendar_page = CalendarPage(self.driver)
        locale.setlocale(locale.LC_ALL, "ru")
        current_data = datetime.today()
        current_month = current_data.strftime('%B').lower()
        assert calendar_page.get_month_title_text() == f'{current_month} {current_data.year}'
        assert calendar_page.get_working_days_amount() > 0, 'Отсутствуют рабочие дни'
        assert calendar_page.get_weekends_amount() > 0, 'Отсутствуют выходные дни'

    def test_next_month(self, open_calendar):
        calendar_page = CalendarPage(self.driver)
        calendar_page.select_next_month().wait_for_page_load()
        assert calendar_page.get_working_days_amount() > 0, 'Отсутствуют рабочие дни'
        assert calendar_page.get_weekends_amount() > 0, 'Отсутствуют выходные дни'

    def test_another_employee(self, open_calendar):
        calendar_page = CalendarPage(self.driver)
        assert calendar_page.get_working_days_amount() > 0, 'Отсутствуют рабочие дни'
        assert calendar_page.get_weekends_amount() > 0, 'Отсутствуют выходные дни'
