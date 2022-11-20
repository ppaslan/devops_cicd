from shop_app.calculator import Calculator

class TestCalculator:
    
    def test_class(self):
        calc = Calculator()
        assert calc

    def test_add(self):
        calc = Calculator()
        assert calc.add(1, 1) == 2

    def test_add_negative_ones(self):
        calc = Calculator()
        assert calc.add(-1, -1) == -2

    def test_subtract(self):
        calc = Calculator()
        assert calc.subtract(10, 10) == 0
        
    def test_subtract_negative_ones(self):
        calc = Calculator()
        assert calc.subtract(-10, -10) == 0
    
    
