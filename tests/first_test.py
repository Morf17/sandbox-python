import pytest


class TestFirst:

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

    def test2(self):
        print('Test №2')

    def test3(self):
        print('Test №3')

    def test4(self):
        print('Test №4')

    def test5(self):
        print('Test №5')
