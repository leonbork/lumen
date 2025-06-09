from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
import allure

class ProfilePage(BasePage):
    PROFILE_SCREEN_TITLE = (AppiumBy.ACCESSIBILITY_ID, "Profile tab")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Checking if Profile screen is displayed")
    def is_profile_screen_displayed(self):
        return self.is_element_displayed(self.PROFILE_SCREEN_TITLE)