import locale
from datetime import datetime

import allure

from pages.calendar_page import CalendarPage


class TestCalendar:

    @allure.description('Проверка текущего месяца')
    def test_current_month(self, open_calendar):
        calendar_page = CalendarPage(open_calendar)
        locale.setlocale(locale.LC_ALL, "ru")
        current_data = datetime.today()
        current_month = current_data.strftime('%B').lower()
        assert calendar_page.get_month_title_text() == f'{current_month} {current_data.year}'
        assert calendar_page.have_working_days() is True, 'Отсутствуют рабочие дни'
        assert calendar_page.have_weekends() is True, 'Отсутствуют выходные дни'

    @allure.description('Проверка переключения месяца')
    def test_next_month(self, open_calendar):
        calendar_page = CalendarPage(open_calendar)
        calendar_page.select_next_month().wait_for_page_load()
        assert calendar_page.have_working_days() is True, 'Отсутствуют рабочие дни'
        assert calendar_page.have_weekends() is True, 'Отсутствуют выходные дни'

    @allure.description('Проверка графика другого сотрудника')
    def test_another_employee(self, open_calendar):
        calendar_page = CalendarPage(open_calendar)
        assert calendar_page.have_working_days() is True, 'Отсутствуют рабочие дни'
        assert calendar_page.have_weekends() is True, 'Отсутствуют выходные дни'
