import pytest
from tests.base_test import BaseTest
from tests.test_data import TestData
import allure

@allure.feature("Login Functionality")
class TestLogin(BaseTest):
    @allure.story("Successful Login")
    @allure.title("Test successful login with valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login(self):
        """
        Tests successful login with valid credentials.
        """
        with allure.step("Resetting app to ensure clean login state"):
            self.driver.reset()

        with allure.step(f"Attempting login with valid user: {TestData.VALID_USER['email']}"):
            self.login_page.login(TestData.VALID_USER["email"], TestData.VALID_USER["password"])
            assert self.home_page.is_home_tab_displayed(), "Home screen was not displayed after successful login."
        allure.attach("User successfully logged in and home page is displayed.", name="Login Success", attachment_type=allure.attachment_type.TEXT)


    @allure.story("Negative Login Scenarios")
    @allure.title("Test login with invalid credentials")
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_login_credentials(self):
        """
        Tests login with invalid credentials and verifies error message.
        """
        with allure.step("Resetting app to ensure clean login state"):
            self.driver.reset()

        with allure.step(f"Attempting login with invalid user: {TestData.INVALID_USER['email']}"):
            self.login_page.login(TestData.INVALID_USER["email"], TestData.INVALID_USER["password"])
            assert self.login_page.is_element_displayed(self.login_page.LOGIN_ERROR_MESSAGE), \
                "Login error message was not displayed for invalid credentials."
            allure.attach(self.login_page.get_error_message(), name="Login Error Message", attachment_type=allure.attachment_type.TEXT)
            assert "Invalid credentials" in self.login_page.get_error_message()
        allure.attach("Error message displayed for invalid credentials.", name="Invalid Credential Test Result", attachment_type=allure.attachment_type.TEXT)


    @allure.story("Negative Login Scenarios")
    @allure.title("Test login with another invalid user")
    @allure.severity(allure.severity_level.NORMAL)
    def test_another_invalid_login_scenario(self):
        """
        Tests another negative login scenario with different invalid credentials.
        """
        with allure.step("Resetting app to ensure clean login state"):
            self.driver.reset()

        with allure.step(f"Attempting login with another invalid user: {TestData.ANOTHER_INVALID_USER['email']}"):
            self.login_page.login(TestData.ANOTHER_INVALID_USER["email"], TestData.ANOTHER_INVALID_USER["password"])
            assert self.login_page.is_element_displayed(self.login_page.LOGIN_ERROR_MESSAGE), \
                "Login error message was not displayed for another invalid user."
            allure.attach(self.login_page.get_error_message(), name="Login Error Message", attachment_type=allure.attachment_type.TEXT)
            assert "Wrong email or password" in self.login_page.get_error_message()
        allure.attach("Error message displayed for another invalid user.", name="Another Invalid Credential Test Result", attachment_type=allure.attachment_type.TEXT)


    @allure.story("Negative Login Scenarios")
    @allure.title("Test login with empty email and password fields")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_empty_login_fields(self):
        """
        Tests login with empty email and password fields.
        """
        with allure.step("Resetting app to ensure clean login state"):
            self.driver.reset()

        with allure.step("Attempting login with empty fields"):
            self.login_page.login(TestData.EMPTY_USER["email"], TestData.EMPTY_USER["password"])
            assert self.login_page.is_login_button_displayed(), \
                "Login button should still be displayed if login failed with empty fields."
            # If there's a specific validation message for empty fields, verify that.
        allure.attach("Login button remained displayed, indicating validation for empty fields.", name="Empty Fields Test Result", attachment_type=allure.attachment_type.TEXT)