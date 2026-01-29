
import pytest

# Shared fixture for all test files
@pytest.fixture
def numbers():
    return 8, 4


def test_addition(numbers):
    a, b = numbers
    assert a + b == 12

def test_subtraction(numbers):
    a, b = numbers
    assert a - b == 4

def test_multiplication(numbers):
    a, b = numbers
    assert a * b == 32

def test_division(numbers):
    a, b = numbers
    assert a / b == 2
