import json
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="session")
def driver():
    # Load capabilities from JSON
    with open('config/Capabilities.json') as f:
        caps = json.load(f)

    # Convert JSON dict to UiAutomator2Options
    options = UiAutomator2Options()
    for key, value in caps.items():
        # Convert string booleans/integers if needed
        if isinstance(value, str):
            if value.lower() == "true":
                value = True
            elif value.lower() == "false":
                value = False
            # elif value.isdigit():
            #     value = int(value)
        options.set_capability(key, value)

    # Initialize Appium driver with options
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
