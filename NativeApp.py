import time
import logging
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC


options = UiAutomator2Options()
options.set_capability("appium:appPackage", "com.google.android.dialer")
options.set_capability("appium:appActivity", "com.google.android.dialer.extensions.GoogleDialtactsActivity")  # update as per your main activity
options.set_capability("platformName", "Android")
options.set_capability("deviceName", "Lenovo Tab M9")

driver = webdriver.Remote('http://localhost:4723', options=options)
driver.activate_app("com.google.android.dialer")
print("Google Dialer app launched successfully!")

scan_elements = {
    "DialPad": "//com.google.android.material.floatingactionbutton.FloatingActionButton[@content-desc='key pad']",
    "search_bar": "//android.widget.TextView[@resource-id='com.google.android.dialer:id/open_search_bar_text_view']",
    "voice_search": "//android.widget.Button[@content-desc='Start voice search']",
    "options": "//android.widget.ImageView[@content-desc='More options']",
    "favourites": "//android.view.View[@resource-id='com.google.android.dialer:id/navigation_bar_item_active_indicator_view']",
    "Recents": "(//android.widget.ImageView[@resource-id='com.google.android.dialer:id/navigation_bar_item_icon_view'])[2]",
    "contacts": "(//android.widget.ImageView[@resource-id='com.google.android.dialer:id/navigation_bar_item_icon_view'])[3]"

}
Keypad = [
    ("1", "xpath", "//android.widget.FrameLayout[@content-desc='1,']"),
    ("2", "xpath", "//android.widget.FrameLayout[@content-desc='2,ABC']"),
    ("3", "xpath", "//android.widget.FrameLayout[@content-desc='3,DEF']"),
    ("4", "xpath", "//android.widget.FrameLayout[@content-desc='4,GHI']"),
    ("5", "xpath", "//android.widget.FrameLayout[@content-desc='5,JKL']"),
    ("6", "xpath", "//android.widget.FrameLayout[@content-desc='6,MNO']"),
    ("7", "xpath", "//android.widget.FrameLayout[@content-desc='7,PQRS']"),
    ("8", "xpath", "//android.widget.FrameLayout[@content-desc='8,TUV']"),
    ("9", "xpath", "//android.widget.FrameLayout[@content-desc='9,WXYZ']"),
    ("0", "xpath", "//android.widget.FrameLayout[@content-desc='0']"),
    ("*", "xpath", "//android.widget.FrameLayout[@content-desc='*']"),
    ("#", "xpath", "//android.widget.FrameLayout[@content-desc='#']"),
    ("call", "xpath", "//android.widget.Button[@content-desc='dial']"),
]

# self.driver.hide_keyboard()   
def get_element(driver, element_name, timeout=5):
    """Fetch an element from the page"""
    
    # Check in Scanning_page_elements dictionary
    if element_name in scan_elements:
        xpath = scan_elements[element_name]
    
    else:
        xpath = None  # Default value if element not found
        for name, locator_type, path in Keypad:
            if name == element_name:
                xpath = path
                break  
    
    # If element was found in either list, return it
    if xpath:
        return WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, xpath))
        )
    
    # Raise an error if the element was not found in any list
    raise ValueError(f"Element '{element_name}' not found in defined lists.")

if driver:
    try:
        DialPad = get_element(driver, "DialPad").click()
        print("dial pad clicked!")
        try:
            phone_number = "1234567890"
            if '*' in phone_number or '#' in phone_number:
                print("Invalid character in phone number. Please enter a valid number.")
            else:
                for digit in phone_number:
                    digit_button = get_element(driver, digit)
                    digit_button.click()
                
                print("Phone number entered successfully!")
                call_button = get_element(driver, "call").click()
                print("call initialed!")

        except Exception as e:
            print(f"error in dialing the mobile number: {e}")

    except Exception as e:
        print(f"error in initializing the dial pad button : {e}")

    time.sleep(2)
    driver.quit()
else:
    print("Driver not initialized.")
