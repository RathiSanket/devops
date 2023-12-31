"""

Unit test for the calculator library

"""

import calculator


class TestCalculator:
    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_addition2(self):
        assert 5 == calculator.add(2, 3)

    def test_sub(self):
        assert 2 == calculator.sub(4, 2)

    def test_mul(self):
        assert 100 == calculator.mul(10, 10)

    def test_mul2(self):
        assert 20 == calculator.mul(2, 10)
