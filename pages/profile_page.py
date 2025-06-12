from pages.base_page import BasePage
import allure

class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Checking if Profile screen is displayed")
    def is_profile_screen_displayed(self):
        return self.is_displayed_by_key("Profile tab")
