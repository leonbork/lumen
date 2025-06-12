from pages.base_page import BasePage
import allure

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting current counter value")
    def get_counter_value(self):
        return int(self.get_text_by_key("Counter value"))

    @allure.step("Clicking 'Reset Counter' button")
    def click_reset_counter(self):
        self.click_by_key("Reset Counter button")

    @allure.step("Clicking 'Logout' button")
    def click_logout(self):
        self.click_by_key("Logout button")

    @allure.step("Navigating to Messages tab")
    def navigate_to_messages(self):
        self.click_by_key("Messages tab")

    @allure.step("Navigating to Profile tab")
    def navigate_to_profile(self):
        self.click_by_key("Profile tab")

    @allure.step("Navigating to Home tab")
    def navigate_to_home(self):
        self.click_by_key("Home tab")

    @allure.step("Checking if Home tab is displayed")
    def is_home_tab_displayed(self):
        return self.is_displayed_by_key("Home tab")
