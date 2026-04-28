from calculator.operations import Calculator

calc = Calculator()
print("Running tests...")
print(calc)

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_subtract():
    calc = Calculator()
    assert calc.subtract(10, 5) == 5

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5
