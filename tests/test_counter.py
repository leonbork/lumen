import pytest
from tests.base_test import BaseTest
import allure

@allure.feature("Counter Functionality")
class TestCounter(BaseTest):

    @allure.story("Counter Reset")
    @allure.title("Test counter initial value and reset functionality")
    @allure.severity(allure.severity_level.NORMAL)
    def test_counter_initial_value_and_reset(self):
        """
        Verifies the initial counter value and tests the reset functionality.
        """
        with allure.step("Ensuring counter starts at 0 for this test"):
            self.home_page.click_reset_counter()
            initial_counter_value = self.home_page.get_counter_value()
            assert initial_counter_value == 0, f"Expected initial counter value to be 0, but got {initial_counter_value}"

        with allure.step("Navigating away and back to increment counter"):
            self.home_page.navigate_to_messages()
            self.home_page.navigate_to_home()
            assert self.home_page.get_counter_value() == 1, "Counter did not increment after navigation."

        with allure.step("Clicking 'Reset Counter' button"):
            self.home_page.click_reset_counter()
            assert self.home_page.get_counter_value() == 0, "Counter did not reset to 0."
        allure.attach("Counter value verified after navigation and reset.", name="Counter Reset Test Result", attachment_type=allure.attachment_type.TEXT)

    @allure.story("Counter Increment")
    @allure.title("Test counter increments on tab navigation")
    @allure.severity(allure.severity_level.NORMAL)
    def test_counter_increments_on_navigation(self):
        """
        Verifies that the counter increments when navigating between tabs.
        """
        with allure.step("Ensuring counter starts at 0"):
            self.home_page.click_reset_counter()

        with allure.step("Navigating multiple times and verifying counter increment"):
            for i in range(1, 4):
                self.home_page.navigate_to_messages()
                self.home_page.navigate_to_home()
                expected_counter = i
                actual_counter = self.home_page.get_counter_value()
                assert actual_counter == expected_counter, \
                    f"Expected counter to be {expected_counter} after {i} navigations, but got {actual_counter}"
                allure.attach(f"Counter value after {i} navigations: {actual_counter}", name=f"Counter after {i} navigations", attachment_type=allure.attachment_type.TEXT)

            self.home_page.navigate_to_profile()
            self.home_page.navigate_to_home()
            assert self.home_page.get_counter_value() == 4, "Counter did not increment after another navigation."
        allure.attach("Counter value verified after multiple navigations.", name="Counter Increment Test Result", attachment_type=allure.attachment_type.TEXT)