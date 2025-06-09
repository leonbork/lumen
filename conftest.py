import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
import os
from datetime import datetime
import allure

# Optional: Load environment variables from .env file
# from dotenv import load_dotenv
# load_dotenv()

@pytest.fixture(scope="session")
def appium_driver():
    """
    Fixture to set up and tear down the Appium driver.
    """
    # Get Appium server URL from environment variable or use default
    appium_server_url = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")

    options = AppiumOptions()
    options.set_capability("platformName", "Android")
    options.set_capability("automationName", "UiAutomator2")
    options.set_capability("deviceName", "emulator-5554")  # Replace with your device name or emulator ID
    options.set_capability("appPackage", "com.example.mycounter.mycounter")
    options.set_capability("appActivity", ".MainActivity")
    options.set_capability("app", os.path.abspath(os.path.join(os.path.dirname(__file__), 'app-debug.apk')))
    options.set_capability("noReset", False)  # Reset app state before each session
    options.set_capability("newCommandTimeout", 300) # Increased timeout for slow operations (e.g., 5 minutes)

    driver = None
    try:
        driver = webdriver.Remote(appium_server_url, options=options)
        driver.implicitly_wait(15) # Set implicit wait for elements to appear (increased from 10)
        yield driver
    except Exception as e:
        pytest.fail(f"Failed to start Appium driver: {e}")
    finally:
        if driver:
            driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to take a screenshot on test failure and attach it to Allure reports.
    """
    outcome = yield
    rep = outcome.get_result()

    # Capture screenshot only if the test call failed
    if rep.when == "call" and rep.failed:
        driver = None
        # Try to get the driver from the fixture (if available)
        for fixture_name in item.fixturenames:
            if fixture_name == "appium_driver":
                driver = item.funcargs[fixture_name]
                break

        if driver:
            try:
                screenshot_name = f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                screenshot_bytes = driver.get_screenshot_as_png()
                allure.attach(screenshot_bytes, name=screenshot_name, attachment_type=allure.attachment_type.PNG)
                print(f"\nScreenshot attached to Allure report for failed test: {item.name}")
            except Exception as e:
                print(f"Failed to take screenshot or attach to Allure: {e}")