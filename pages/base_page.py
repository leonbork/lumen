from appium_flutter_finder.flutter_finder import FlutterFinder
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.finder = FlutterFinder()

    @allure.step("Finding Flutter element by key: {key}")
    def find_by_key(self, key):
        return self.driver.find_element_by_flutter(self.finder.by_value_key(key))

    @allure.step("Clicking Flutter element by key: {key}")
    def click_by_key(self, key):
        self.find_by_key(key).click()

    @allure.step("Sending keys '{text}' to Flutter element by key: {key}")
    def send_keys_by_key(self, key, text):
        el = self.find_by_key(key)
        el.clear()
        el.send_keys(text)

    @allure.step("Getting text from Flutter element by key: {key}")
    def get_text_by_key(self, key):
        return self.find_by_key(key).text

    @allure.step("Checking if Flutter element by key: {key} is displayed")
    def is_displayed_by_key(self, key):
        try:
            return self.find_by_key(key).is_displayed()
        except:
            return False
