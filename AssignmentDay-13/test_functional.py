import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_open_website(setup):
    setup.get("https://example.com")
    assert "Example Domain" in setup.title


def test_page_content(setup):
    setup.get("https://example.com")
    heading = setup.find_element(By.TAG_NAME, "h1").text
    assert heading == "Example Domain"
