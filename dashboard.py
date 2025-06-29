import os
import logging
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from appium.options.common import AppiumOptions
from appium.options.android import UiAutomator2Options
from selenium.common.exceptions import NoSuchElementException , TimeoutException

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[
                        logging.FileHandler("D:/Automation/BlackGhost/blackghost.log"),   # Logs to a file
                        logging.StreamHandler()           # Logs to the terminal
                    ])

# Define the options for Appium
options = UiAutomator2Options()
options = AppiumOptions()
options.platform_name = "Android"
options.device_name = "Lenovo Tab M9"
options.app = "/data/app/~~GoNsHJzeMORc-hy7nq3ymQ==/com.app.equivital-bJVKep1ALtrx3h3MVh-TjA==/base.apk=com.app.equivital"  # Path to your APK
options.automation_name = "UiAutomator2"
options.set_capability("appium:appPackage", "com.app.equivital")
options.set_capability("appium:appActivity", "com.app.equivital.view.activity.DashboardActivity") 
options.set_capability("appium:noReset", True)  # Prevents Appium from clearing app data
options.set_capability("appium:dontStopAppOnReset", True)  # Keeps the app running

# Connect to Appium server
driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4723",  # Appium server URL
    options=options,  
)
logging.info("Connected to device successfully!")

driver.activate_app("com.app.equivital")
# logging.info("Application launched!")
# logging.info("Blackghost: v3.0.0")
logging.info("Application launched! " + "Blackghost: v3.0.0")

# data = {
 
#         "CTE_text": "//android.widget.TextView[@resource-id='com.app.equivital:id/txtCTELbl' and @text = 'CTE']",
#         "Skin_text": "//android.widget.TextView[@resource-id='com.app.equivital:id/txtSkinLbl']",
#         "Ambient_text":"//android.widget.TextView[@resource-id='com.app.equivital:id/txtAmbientLbl']",
                
#         "Heart_Rate_text": "//android.widget.TextView[@resource-id='com.app.equivital:id/txtHeartRateLbl']",
#         "Heart_Rate_Avg_text": "//android.widget.TextView[@resource-id='com.app.equivital:id/txtHeartRateAvgLbl']",
#         "Calories_text": "//android.widget.TextView[@resource-id='com.app.equivital:id/txtCaloriesLbl']",
            
#         "Activity_text": "//android.widget.TextView[@resource-id='com.app.equivital:id/txtActivityModeLbl']",
#         "Total_steps_text": "//android.widget.TextView[@resource-id='com.app.equivital:id/txtTotalStepsLbl']",
#         "Distance_text": "//android.widget.TextView[@resource-id='com.app.equivital:id/txtDistanceLbl']"
              
# }
Available_Devices = {
#     "D5:80:D9:71:8D:17", "D5:80:B2:CA:5A:5A", "C6:97:B2:CA:5A:5A", "C4:76:8F:28:A1:CD",     
#                     "C6:971:8F:28:A1:CD", "CD:98F:28:A1:CD", "C6:F1:E6:1C:3A:42", "C1:C8:95:FC:BE:93", "D5:80:CF:FC:AC:6D",
                    "eq_24022055", "eq_12345678", "eq_C697B2CA5A5A"
    }
Scanning_page_elements = {
        "eq_icon": "//android.widget.ImageView[@resource-id='com.app.equivital:id/ivIcon']",
        "BLE_icon": "//android.widget.ImageButton[@resource-id='com.app.equivital:id/ivSync']",   
        "text_header": "//android.widget.TextView[@resource-id='com.app.equivital:id/txtHeaderTitle']", 
        "Scanning_btn": "//android.widget.Button[@resource-id='com.app.equivital:id/btnStartScan']"
    }
elements_to_check = [
    ("Back_btn", "xpath", "//android.widget.ImageButton[@resource-id='com.app.equivital:id/ivBack']"),
    ("Armband Text", "xpath", "//android.widget.TextView[@resource-id='com.app.equivital:id/txtArmbandLbl']"),
    ("info", "xpath", "//android.widget.ImageButton[@resource-id='com.app.equivital:id/ivInfo']"),
    ("Battery Percentage", "xpath", "//android.widget.TextView[@resource-id='com.app.equivital:id/txtBatteryPercentage']"),
    ("BLE connection", "xpath", "//android.widget.TextView[@resource-id='com.app.equivital:id/txtBleConnection']"),
    ("Body status", "xpath", "//android.widget.TextView[@resource-id='com.app.equivital:id/txtArmBeltStatus']"),
    ("Session time", "xpath", "//android.widget.TextView[@resource-id='com.app.equivital:id/txtTimer']"),
    ("Start button", "xpath", "//android.widget.Button[@resource-id='com.app.equivital:id/btnStart']"),
    ("CTE_text", "xpath", "//android.widget.TextView[@resource-id='com.app.equivital:id/txtCTELbl' and @text = 'CTE']"),
    ("Skin_text", "xpath", "//android.widget.TextView[@resource-id='com.app.equivital:id/txtSkinLbl']"),
    ("Ambient_text", "xpath", "//android.widget.TextView[@resource-id='com.app.equivital:id/txtAmbientLbl']"),
    ("Heart_Rate_text ", "xpath", "//android.widget.TextView[@resource-id='com.app.equivital:id/txtHeartRateLbl']"),
    ("Heart_Rate_Avg_text", "xpath", "//android.widget.TextView[@resource-id='com.app.equivital:id/txtHeartRateAvgLbl']"),
    ("Calories_text", "xpath", "//android.widget.TextView[@resource-id='com.app.equivital:id/txtCaloriesLbl']"),

    ("Activity_text", "xpath", "//android.widget.TextView[@resource-id='com.app.equivital:id/txtActivityModeLbl']"),
    ("Total_steps_text", "xpath", "//android.widget.TextView[@resource-id='com.app.equivital:id/txtTotalStepsLbl']"),
    ("Distance_text", "xpath", "//android.widget.TextView[@resource-id='com.app.equivital:id/txtDistanceLbl']"),
       
]

# Function to wait for an element
# def get_element(driver, element_name, timeout=5):
#     return WebDriverWait(driver, timeout).until(
#         EC.element_to_be_clickable((AppiumBy.XPATH, Scanning_page_elements[element_name]))
#     )
    
def get_element_bypath(driver, xpath, timeout=5):
    """Wait for an element to be visible and return it."""
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((AppiumBy.XPATH, xpath))
        )
    except Exception as e:
        logging.error(f"Element not found: {xpath} - {e}")
        return None

def get_element(driver, element_name, timeout=5):
    """Fetch an element from the scanning page or the elements_to_check list."""
    
    # Check in Scanning_page_elements dictionary
    if element_name in Scanning_page_elements:
        xpath = Scanning_page_elements[element_name]
    
    # Check in elements_to_check list
    else:
        xpath = None  # Default value if element not found
        for name, locator_type, path in elements_to_check:
            if name == element_name:
                xpath = path
                break  # Stop searching once found
    
    # If element was found in either list, return it
    if xpath:
        return WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, xpath))
        )
    
    # Raise an error if the element was not found in any list
    raise ValueError(f"Element '{element_name}' not found in defined lists.")

def get_element_presence(driver, element_xpath, timeout=5):
    """
    Check if an element is present on the screen.

    :param driver: Appium WebDriver instance
    :param element_xpath: The XPath of the element to check
    :param timeout: Time (seconds) to wait for element
    :return: True if element exists, False otherwise
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((AppiumBy.XPATH, element_xpath))
        )
        # logging.info(f" Element found:")
        return True
        # return element
    except TimeoutException:
        logging.error(f" Element NOT found: {element_xpath}")
        return False
    
def verify_elements(driver, elements_to_check):
    scrolling_required = False  # Flag to track if scrolling is needed

    for index, (element_name, locator_type, locator_value) in enumerate(elements_to_check):

        element_found = get_element_presence(driver, locator_value)

        # if not element_found:
        if element_name == "Calories_text":  # Enable scrolling when reaching this element
            logging.info(f"Element found: {element_name}")
            scrolling_required = True
            if scrolling_required:
                # scroll_and_find_element(driver, "com.app.equivital:id/txtActivityModeLbl")
                scroll_and_find_element(driver, "com.app.equivital:id/txtDistanceLbl")
                logging.info("scrolled successfully.............")
            else:
                logging.error("Scrolling is not enabled.")
        # /*****/
        # elif locator_type == "xpath":
        
        #     element_text = element_found.text  # Extract text from the element
        #     logging.info(f"Element found: {element_name} | Text: '{element_text}'")
        
        else:
            logging.info(f"Element found: {element_name}")

    logging.info("Element verification completed!")

def scan_for_devices(driver):
    """Scan for available devices and return a list of detected MAC addresses."""
    BLE_icon = get_element(driver, "BLE_icon").click()
    logging.info("Refreshed Scanning!")
    time.sleep(3)
    detected_devices = []
    
    serial_devices = driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.app.equivital:id/txtDeviceName']")
    if serial_devices:
        logging.info(f"Found {len(serial_devices)} device(s).")
    else:
        logging.error("No devices found.")

    serial_IDs = []
    for element in serial_devices:
        try:
            serial_text = element.find_element(AppiumBy.XPATH, ".//android.widget.TextView").text.strip()
            serial_IDs.append(serial_text)
        except Exception as e:
            logging.error(f"Could not extract text from device element: {e}")
    logging.info("Extracted Serial IDs: %s", serial_IDs)

    # Check each extracted serial_ID individually
    for serial_ID in serial_IDs:
        if serial_ID in Available_Devices:
            detected_devices.append(serial_ID)  # Append only valid ones

    return detected_devices  # Return filtered list

def select_and_connect_device(driver):
    WebDriverWait(driver , 3)
    """Automatically connect to the first detected device."""
    detected_devices = scan_for_devices(driver)

    if not detected_devices:
        print("No known devices found. Exiting...")
        return
    
    # Select the first detected device
    selected_ID = detected_devices[0]
    print(f"Auto-selecting device: {selected_ID}")

    # Construct the XPath to locate and click the device
    serial_xpath = f"//android.widget.TextView[@resource-id='com.app.equivital:id/txtDeviceName' and @text='{selected_ID}']"
    # selected_element = get_element(driver, serial_xpath)
    selected_element = get_element_bypath(driver, serial_xpath)

    if selected_element:
        selected_element.click()
        print(f"Connected to {selected_ID}")
    else:
        print(f"Failed to locate the selected device: {selected_ID}")
    return True

def back_btn_functionality(driver, timeout=5):
    success = True
    options_to_select = [("Yes", "xpath", "//android.widget.Button[@resource-id='com.app.equivital:id/btnYes']"),
                         ("No", "xpath", "//android.widget.Button[@resource-id='com.app.equivital:id/btnNo']"),
                         ("Text", "xpath", "//android.widget.TextView[@resource-id='com.app.equivital:id/txtMessage' and @text = 'Are you sure you want to go back and select another device?']")
    ]
    back_btn = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.ImageButton[@resource-id='com.app.equivital:id/ivBack']"))
    )
    back_btn.click()
    logging.info("Back button is tapped!")

    verify_elements(driver, options_to_select)
    try:
        # Wait until the 'No' button is clickable
        no_button_xpath = next(item[2] for item in options_to_select if item[0] == "No")
        no_button = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, no_button_xpath))
            ).click()
            
        logging.info("No button successful!")
        WebDriverWait(driver, 2)
        back_btn.click()
    except Exception as e:
        logging.error(f"error in tapping No: {e}")
        success = False

    try:
        #wait until 'Yes' button is clickable
        yes_button_xpath = next(item[2] for item in options_to_select if item[0] == "Yes")

        # Wait for the 'Yes' button to be clickable
        yes_button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, yes_button_xpath))
        ).click()
        logging.info("Yes button successful!")
        select_and_connect_device(driver)

    except Exception as e:
        logging.error(f"error in tapping Yes: {e}")
        success = False
    return success

def info_btn_functionality(driver, timeout=5):
    elements_to_check = [("Information_text", "xpath", "//android.widget.TextView[@resource-id='com.app.equivital:id/txtTitle']"),
                        ("App_version", "xpath", "//android.widget.TextView[@resource-id='com.app.equivital:id/txtAppVersionLbl']"),
                        ("Version_value", "xpath", "//android.widget.TextView[@resource-id='com.app.equivital:id/txtAppVersionVal']"),
                        ("Device_Name", "xpath", "//android.widget.TextView[@resource-id='com.app.equivital:id/txtDeviceNameLbl']"),
                        ("Device_serialID", "xpath", "//android.widget.TextView[@resource-id='com.app.equivital:id/txtDeviceNameVal']"), 
                        ("Device_FW_text", "xpath", "//android.widget.TextView[@resource-id='com.app.equivital:id/txtDeviceFirmwareLbl']"),
                        ("FW_Version", "xpath", "//android.widget.TextView[@resource-id='com.app.equivital:id/txtDeviceFirmwareVal']"),
                        ("Blackgost_Ecosystem_text", "xpath", "//android.widget.TextView[@resource-id='com.app.equivital:id/txtPartOfEquivital']"),
                        ("Close_info", "xpath", "//android.widget.ImageButton[@resource-id='com.app.equivital:id/ivClose']")
        ]
    info_btn =  WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.ImageButton[@resource-id='com.app.equivital:id/ivInfo']"))
    ).click()
    logging.info("Info button is tapped!")

    verify_elements(driver, elements_to_check)
    try:
        # Wait until the 'close info' button is clickable
        close_info_button_xpath = next(item[2] for item in elements_to_check if item[0] == "Close_info")
        close_info_button = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, close_info_button_xpath))
            ).click()
            
        logging.info("Close info button successful!")
    except Exception as e:
        logging.error(f"error in closing the info button: {e}")

    return True


def scroll_and_find_element(driver, locator, timeout=5):
    """
    Scrolls and finds an element using XPath or Resource ID with UiScrollable.

    :param driver: Appium WebDriver instance
    :param locator: Either an XPath string or a resource ID string
    :param timeout: Time (seconds) to wait for the element
    :return: WebElement if found, None otherwise
    """
    try:
        if locator.startswith("//"):  # If XPath
            scrollable_command = f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().xpath("{locator}"));'
            by = AppiumBy.XPATH
        else:  # If Resource ID
            scrollable_command = f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("{locator}"));'
            by = AppiumBy.ID

        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scrollable_command)  # Perform scrolling
        
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )
        return element
    except TimeoutException:
        logging.error(f"Element NOT found: {locator}")
        return None

if driver:
        if (get_element_bypath(driver, "//android.widget.TextView[@resource-id='com.app.equivital:id/txtArmbandLbl']")):
            logging.info("dashboard is active..............")
            verify_elements(driver, elements_to_check)
            scroll_and_find_element(driver, "com.app.equivital:id/txtTempLbl")
            logging.info("scrolled back to the top!")

            try:
                info_btn_functionality(driver)
                logging.info("Info button functionality verified!")
            except Exception as e:
                logging.error(f"info button functionality fails: {e}")
            try: 
                success = back_btn_functionality(driver)
                if success:
                    logging.info("Back button functionality is verified!")
                else:
                    logging.error("Back button functionality fails!")
            
            except Exception as e:  
                logging.error(f"Back button functionality fails: {e}")

        else:
            logging.error("make sure the dashboard tab is running!")

else:
    logging.error("Driver not initialized, skipping element interactions.")

logging.info("--------------------------------------------------------------------------------------------")
driver.quit()