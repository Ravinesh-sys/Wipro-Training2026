
import pytest

# Function-scoped fixture (runs before every test)
@pytest.fixture(scope="function")
def function_data():
    print("\nFunction-scoped fixture setup")
    return 5

@pytest.fixture(scope="module")
def module_data():
    print("\nModule-scoped fixture setup")
    return 10



def test_using_function_scope(function_data):
    assert function_data == 5

def test_using_function_scope_again(function_data):
    assert function_data == 5

def test_using_module_scope(module_data):
    assert module_data == 10

def test_using_module_scope_again(module_data):
    assert module_data == 10
