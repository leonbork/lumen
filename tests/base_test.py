import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.profile_page import ProfilePage # Import ProfilePage
from tests.test_data import TestData
import allure

class BaseTest:
    """
    Base class for all test cases, providing common setup (like login)
    and access to page objects.
    """
    @pytest.fixture(autouse=True)
    def setup_method(self, appium_driver):
        """
        Fixture to set up common test prerequisites, such as logging in.
        This fixture will run automatically before each test method in classes
        that inherit from BaseTest.
        """
        self.driver = appium_driver
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.profile_page = ProfilePage(self.driver) # Initialize ProfilePage here as well

        # Perform login for tests that require it using VALID_USER from TestData
        with allure.step(f"Performing login with valid credentials: {TestData.VALID_USER['email']}"):
            self.login_page.login(TestData.VALID_USER["email"], TestData.VALID_USER["password"])
            assert self.home_page.is_home_tab_displayed(), "Login failed: Home screen was not displayed."