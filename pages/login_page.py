from pages.base_page import BasePage
import allure

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Logging in with email '{email}' and password '{password}'")
    def login(self, email, password):
        self.send_keys_by_key("Email field", email)
        self.send_keys_by_key("Password field", password)
        self.click_by_key("Login button")

    @allure.step("Getting login error message")
    def get_error_message(self):
        return self.get_text_by_key("Login error message")

    @allure.step("Checking if Login button is displayed")
    def is_login_button_displayed(self):
        return self.is_displayed_by_key("Login button")
