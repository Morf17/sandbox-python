import allure
import pytest
import softest


class TestFirst(softest.TestCase):

    @pytest.fixture(scope='class', autouse=True)
    def setup_class(self):
        print('FirstTest class started')
        yield
        print('All tests in FirstTest finished')

    @pytest.fixture(scope='function', autouse=True)
    def setup_function(self):
        print('Test start')
        yield
        print('Test finished')

    @allure.description('Test №1')
    def test1(self):
        print('Test №1')
        assert 2 + 2 == 4

    @allure.description('Test №2')
    def test2(self):
        print('Test №2')
        assert 2 + 2 == 5

    @allure.description('Test №3')
    def test3(self):
        print('Test №3')
        self.soft_assert(self.assertEqual, 2 + 2, 4)
        self.soft_assert(self.assertEqual, 2 + 2, 5, 'Ошибка при сложении')
        self.assert_all()

    @allure.description('Test №4')
    def test4(self):
        print('Test №4')
        assert 1 / 0 == 1

    @allure.description('Test №5')
    def test5(self):
        print('Test №5')
