# test_xunit_style.py

# xUnit-style setup and teardown (pytest)

def setup_module():
    print("\nSetup before entire module")

def teardown_module():
    print("\nTeardown after entire module")

def setup_function():
    print("\nSetup before each test")

def teardown_function():
    print("\nTeardown after each test")


# Sample test cases
def test_addition():
    assert 2 + 3 == 5

def test_subtraction():
    assert 5 - 2 == 3
