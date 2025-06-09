from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30) # Increased wait time for elements

    @allure.step("Finding element by {by} with value '{value}'")
    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    @allure.step("Clicking element by {by} with value '{value}'")
    def click_element(self, by, value):
        element = self.find_element(by, value)
        element.click()

    @allure.step("Sending keys '{text}' to element by {by} with value '{value}'")
    def send_keys_to_element(self, by, value, text):
        element = self.find_element(by, value)
        element.clear() # Clear existing text before sending new keys
        element.send_keys(text)

    @allure.step("Getting text from element by {by} with value '{value}'")
    def get_element_text(self, by, value):
        element = self.find_element(by, value)
        return element.text

    @allure.step("Checking if element by {by} with value '{value}' is displayed")
    def is_element_displayed(self, by, value):
        try:
            return self.find_element(by, value).is_displayed()
        except:
            return False

    @allure.step("Scrolling to text '{text}'")
    def scroll_to_text(self, text):
        """Scrolls until the specified text is visible."""
        # This is a generic Appium scroll.
        self.driver.execute_script('mobile: scrollGesture', {
            'left': 100, 'top': 100, 'width': 800, 'height': 800,
            'direction': 'down',
            'percent': 0.75,
            'speed': 1000,
            'text': text
        })