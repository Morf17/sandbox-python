import pytest
import softest

from settings import Settings


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

    def test1(self):
        print('Test №1')
        assert 2 + 2 == 4

    def test2(self):
        print('Test №2')
        assert 2 + 2 == 5

    def test3(self):
        print('Test №3')
        self.soft_assert(self.assertEqual, 2 + 2, 4)
        self.soft_assert(self.assertEqual, 2 + 2, 5, 'Ошибка при сложении')
        self.assert_all()

    def test4(self):
        print('Test №4')
        assert 1 / 0 == 1

    def test5(self):
        print('Test №5')
        Settings()
