
import pytest

# Common reusable fixture for test data
@pytest.fixture
def numbers():
    return 10, 5

# Common reusable fixture for resource
@pytest.fixture
def resource():
    print("\nSetting up resource")
    data = {"status": "active"}
    yield data
    print("\nTearing down resource")

def test_addition(numbers):
    a, b = numbers
    assert a + b == 15

def test_subtraction(numbers):
    a, b = numbers
    assert a - b == 5

def test_resource_usage(resource):
    assert resource["status"] == "active"
