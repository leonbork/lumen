from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
import allure

class HomePage(BasePage):
    # Locators
    HOME_TAB = (AppiumBy.ACCESSIBILITY_ID, "Home tab")
    MESSAGES_TAB = (AppiumBy.ACCESSIBILITY_ID, "Messages tab")
    PROFILE_TAB = (AppiumBy.ACCESSIBILITY_ID, "Profile tab")
    COUNTER_VALUE = (AppiumBy.ACCESSIBILITY_ID, "Counter value")
    RESET_COUNTER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Reset Counter button")
    LOGOUT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Logout button")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting current counter value")
    def get_counter_value(self):
        return int(self.get_element_text(self.COUNTER_VALUE))

    @allure.step("Clicking 'Reset Counter' button")
    def click_reset_counter(self):
        self.click_element(self.RESET_COUNTER_BUTTON)

    @allure.step("Clicking 'Logout' button")
    def click_logout(self):
        self.click_element(self.LOGOUT_BUTTON)

    @allure.step("Navigating to Messages tab")
    def navigate_to_messages(self):
        self.click_element(self.MESSAGES_TAB)

    @allure.step("Navigating to Profile tab")
    def navigate_to_profile(self):
        self.click_element(self.PROFILE_TAB)

    @allure.step("Navigating to Home tab")
    def navigate_to_home(self):
        self.click_element(self.HOME_TAB)

    @allure.step("Checking if Home tab is displayed")
    def is_home_tab_displayed(self):
        return self.is_element_displayed(self.HOME_TAB)