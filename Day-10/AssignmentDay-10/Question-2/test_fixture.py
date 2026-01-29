# test_fixtures_example.py
import pytest

# Reusable fixture for test data
@pytest.fixture
def numbers():
    return 10, 5

# Reusable fixture for a resource (simulated setup/cleanup)
@pytest.fixture
def database_connection():
    print("\nConnecting to database")
    connection = {"status": "connected"}
    yield connection
    print("\nClosing database connection")

# Tests using fixtures
def test_addition(numbers):
    a, b = numbers
    assert a + b == 15

def test_subtraction(numbers):
    a, b = numbers
    assert a - b == 5

def test_resource(database_connection):
    assert database_connection["status"] == "connected"
