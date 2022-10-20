import pytest

from main import add, subtract, multiply, divide


class TestClass:

    @pytest.fixture()         #ked chcem pouzivat tie iste cisla na testovanie, vytvorim si testovaciu sadu,overenie certifikatu
    def numbers(self):
        x = 10
        y = 20
        z = 25
        return [x, y, z]

    def test_add_2(self, numbers):
        x = numbers[0]
        y = numbers[1]
        assert add(x, y) == 30

    @pytest.mark.sucet              #zaregistroval som mark v pytest.ini aby nevyhadyovalo chybu
    @pytest.mark.parametrize("x, y, z", [(1, 1, 2), (1.5, 0.5, 2),
                                         (-5, -10, -15)])  # pouzivame parametry aby sme mohli vyskusat viac hodnot
    def test_add(self, x, y, z):
        assert add(x, y) == z  # assert ako if -> true or false

    @pytest.mark.parametrize("x, y, z", [(1, 1, 0), (1.5, 0.5, 1), (-5, -10, 5)])
    def test_subtract(self, x, y, z):
        assert subtract(x, y) == z

    @pytest.mark.parametrize("x, y, z", [(1, 1, 1), (1.5, 2, 3), (-5, -10, 50)])
    def test_multiply(self, x, y, z):
        assert multiply(x, y) == z

    @pytest.mark.xfail
    @pytest.mark.parametrize("x, y, z", [(0, 1, 0), (110, 100, 1.1), (5, -10, - 0.5), (2, 3, 0.67)])
    def test_divide(self, x, y, z):
        assert divide(x, y) == z

