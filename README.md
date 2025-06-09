# Lumen Automation Answer - MyCounter App - Mobile Automation Testing

## Setup Instructions

1. Install dependencies:<br>
pip install -r requirements.txt

2. Install Allure:<br>
brew install allure

3. Start Appium server:<br>
appium
4. Add the apk under root folder as app-debug.apk
5. Prepare your Android device/emulator.
6. Edit proper Appium capabilities in conftest.py    

## Run Tests <br>
pytest --alluredir=allure-results <br>
allure serve allure-results

## Structure
- Page Object Model (POM)
- Allure reports
- Designed for emulator and real device testing

