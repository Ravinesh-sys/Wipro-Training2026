# pages/login_page.py

from utils.base_page import BasePage

class LoginPage(BasePage):

    # Locators (XPATH)
    username_box = "//input[@id='username']"
    password_box = "//input[@id='password']"
    login_btn = "//button[@type='submit']"
    success_msg = "//div[@class='flash success']"

    def enter_username(self, username):
        self.enter_text(self.username_box, username)

    def enter_password(self, password):
        self.enter_text(self.password_box, password)

    def click_login(self):
        self.click(self.login_btn)

    def get_success_message(self):
        return self.get_text(self.success_msg)
