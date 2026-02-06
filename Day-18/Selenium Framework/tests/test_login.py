# tests/test_login.py

from selenium import webdriver
from pages.login_page import LoginPage
from config.config import URL, USERNAME, PASSWORD
import time

def test_login():

    # Launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)

    # Create object of LoginPage
    login = LoginPage(driver)

    # Perform login
    login.enter_username(USERNAME)
    login.enter_password(PASSWORD)
    login.click_login()

    time.sleep(2)

    # Get success message
    msg = login.get_success_message()
    print("Login Result:", msg)

    driver.quit()
