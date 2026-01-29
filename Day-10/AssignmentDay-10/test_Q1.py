
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b



# Pytest Test Cases
import pytest

# Test addition
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

# Test subtraction
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(2, 4) == -2

# Test multiplication
def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 10) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

# Test division by zero raises exception
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
