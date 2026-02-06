# utils/base_page.py

from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(By.XPATH, locator).click()

    def enter_text(self, locator, text):
        self.driver.find_element(By.XPATH, locator).send_keys(text)

    def get_text(self, locator):
        return self.driver.find_element(By.XPATH, locator).text
