import pytest
from tests.base_test import BaseTest
import allure

@allure.feature("Navigation Functionality")
class TestNavigation(BaseTest):
    # The login is handled by the autouse fixture in BaseTest.

    @allure.story("Tab Navigation")
    @allure.title("Test navigation to Messages tab and back to Home")
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigate_to_messages_and_back(self):
        """
        Tests navigation to the Messages tab and back to Home.
        """
        with allure.step("Navigating to Messages tab"):
            self.home_page.navigate_to_messages()
            # If there was a unique element on messages screen, we'd verify it here
        with allure.step("Navigating back to Home tab"):
            self.home_page.navigate_to_home()
            assert self.home_page.is_home_tab_displayed(), "Did not return to Home screen after navigating from Messages."
        allure.attach("Successfully navigated to Messages and back to Home.", name="Messages Nav Test Result", attachment_type=allure.attachment_type.TEXT)

    @allure.story("Tab Navigation")
    @allure.title("Test navigation to Profile tab and back to Home")
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigate_to_profile_and_back(self):
        """
        Tests navigation to the Profile tab and back to Home.
        """
        with allure.step("Navigating to Profile tab"):
            self.home_page.navigate_to_profile()
            assert self.profile_page.is_profile_screen_displayed(), "Profile screen was not displayed."
        with allure.step("Navigating back to Home tab"):
            self.home_page.navigate_to_home()
            assert self.home_page.is_home_tab_displayed(), "Did not return to Home screen after navigating from Profile."
        allure.attach("Successfully navigated to Profile and back to Home.", name="Profile Nav Test Result", attachment_type=allure.attachment_type.TEXT)


    @allure.story("Logout Functionality")
    @allure.title("Test that Logout returns to the login screen")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_logout_returns_to_login_screen(self):
        """
        Tests that clicking logout returns to the login screen.
        """
        with allure.step("Clicking 'Logout' button"):
            self.home_page.click_logout()
            assert self.login_page.is_login_button_displayed(), "Did not return to Login screen after logout."
        allure.attach("Successfully logged out and returned to login screen.", name="Logout Test Result", attachment_type=allure.attachment_type.TEXT)