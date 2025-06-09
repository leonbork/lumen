from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
import allure

class LoginPage(BasePage):
    # Locators
    EMAIL_FIELD = (AppiumBy.ACCESSIBILITY_ID, "Email field")
    PASSWORD_FIELD = (AppiumBy.ACCESSIBILITY_ID, "Password field")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Login button")
    # Assuming this ID for the error message after validation
    LOGIN_ERROR_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, "Login error message")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Logging in with email '{email}' and password '{password}'")
    def login(self, email, password):
        self.send_keys_to_element(self.EMAIL_FIELD, email)
        self.send_keys_to_element(self.PASSWORD_FIELD, password)
        self.click_element(self.LOGIN_BUTTON)

    @allure.step("Getting login error message")
    def get_error_message(self):
        return self.get_element_text(self.LOGIN_ERROR_MESSAGE)

    @allure.step("Checking if Login button is displayed")
    def is_login_button_displayed(self):
        return self.is_element_displayed(self.LOGIN_BUTTON)