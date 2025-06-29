import os
import logging
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from appium.options.common import AppiumOptions
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.keys import Keys

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

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[
                        logging.FileHandler("D:/Automation/BlackGhost/app.log"),   # Logs to a file
                        logging.StreamHandler()           # Logs to the terminal
                    ])

scanning_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.app.equivital:id/txtHeaderTitle']"))
    )
if scanning_btn:
    # print("scanning tab is active......")
    logging.info("scanning tab is active............")
else:
    print("scanning section is not active......")
# Define MAC addresses to check
Available_Devices = {
    # "D5:80:D9:71:8D:17", "D5:80:B2:CA:5A:5A", "C6:97:B2:CA:5A:5A",
    # "C4:76:8F:28:A1:CD", "C6:971:8F:28:A1:CD", "CD:98F:28:A1:CD",
    # "C6:F1:E6:1C:3A:42", "C1:C8:95:FC:BE:93", "D5:80:CF:FC:AC:6D"
    "eq_24022055", "eq_12345678" , "eq_C697B2CA5A5A"
}
Scanning_page_elements = {
        "eq_icon": "//android.widget.ImageView[@resource-id='com.app.equivital:id/ivIcon']",
        "BLE_icon": "//android.widget.ImageButton[@resource-id='com.app.equivital:id/ivSync']",   
        "text_header": "//android.widget.TextView[@resource-id='com.app.equivital:id/txtHeaderTitle']", 
        "Scanning_btn": "//android.widget.Button[@resource-id='com.app.equivital:id/btnStartScan']"
    }
def get_element(driver, xpath, timeout=5):
    """Wait for an element to be visible and return it."""
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((AppiumBy.XPATH, xpath))
        )
    except Exception as e:
        print(f"Element not found: {xpath} - {e}")
        return None
    
def search_Device_ID(driver, search_key):
    
    """Check if a device starting with the given search key is present in the scanned list."""
    try:
        # Locate the search bar and enter the search key
        search_bar = get_element(driver, "//android.widget.EditText[@resource-id='com.app.equivital:id/edtSearch']")
        search_bar.click()
        search_bar.clear()
        search_bar.send_keys(search_key)
        # search_bar.send_keys(Keys.RETURN)  # Press Enter
        # search_bar.send_keys(Keys.ENTER)  # Press Enter to trigger search
        logging.info(f"Searching for devices with '{search_key}'...")
    except Exception as e:
        logging.error(f"Error interacting with search bar: {e}")
        return False

    # Wait for the search results to update
    driver.implicitly_wait(3)
    # WebDriverWait(driver, 2)

    # Scan for devices after updating the search
    detected_devices = scan_for_devices(driver)

    # Check if any detected device starts with the search_key
    matching_devices = [device for device in detected_devices if device.startswith(search_key)]

    if matching_devices:
        print(f"Devices found starting with '{search_key}': {matching_devices}")
        logging.info("")
        return True
    else:
        No_Device = get_element(driver, "//android.widget.TextView[@resource-id='com.app.equivital:id/tvMsg']")
        print(f"No devices found starting with '{search_key}'.")
        if No_Device:
            logging.info("Text found : No Device found")
        else:
            logging.error("No devices found text not found!")
        return False

# def scan_for_devices(driver):
    # """Scan for available devices and return a list of detected MAC addresses."""
    # # BLE_icon = get_element(driver, "BLE_icon").click()
    # # print("Refreshed Scanning!")
    # # WebDriverWait(driver, 5)
    # detected_devices = []
    
    # # Find all elements that contain a serial ID (modify the XPath if needed)
    # # serial_devices = driver.find_elements(AppiumBy.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.app.equivital:id/rvDevices']")   #path of the available devices text
    # serial_devices = driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.app.equivital:id/txtDeviceName']")
    # if serial_devices:
    #     print(f"Found {len(serial_devices)} devices.")
    # else:
    #     print("No devices found.")

    # serial_IDs = []
    # for element in serial_devices:
    #     try:
    #         serial_text = element.find_element(AppiumBy.XPATH, ".//android.widget.TextView").text.strip()
    #         serial_IDs.append(serial_text)
    #     except Exception as e:
    #         print(f"Could not extract text from device element: {e}")
    # print("Extracted Serial IDs:", serial_IDs)

    # # Check each extracted serial_ID individually
    # for serial_ID in serial_IDs:
    #     if serial_ID in Available_Devices:
    #         detected_devices.append(serial_ID)  # Append only valid ones

    # return detected_devices  # Return filtered list

def scan_for_devices(driver):
    """Scan for available devices and return a list of detected MAC addresses."""
    max_attempts = 3  # Maximum refresh attempts
    attempt = 0
    detected_devices = []


    while attempt < max_attempts:
        logging.info(f"Scanning attempt {attempt + 1}...")

        # Click BLE icon to refresh scanning
        try:
            BLE_icon = get_element(driver, "BLE_icon")
            BLE_icon.click()
            logging.info("Refreshed Scanning!")
            time.sleep(3)  # Wait for scanning to complete
        except Exception as e:
            logging.error(f"Failed to click BLE icon: {e}")
            return []

        serial_devices = driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.app.equivital:id/txtDeviceName']")
        
        if serial_devices:
            logging.info(f"Found {len(serial_devices)} device(s).")
        else:
            logging.warning("No devices found.")

        serial_IDs = []
        for element in serial_devices:
            try:
                serial_text = element.find_element(AppiumBy.XPATH, ".//android.widget.TextView").text.strip()
                serial_IDs.append(serial_text)
            except Exception as e:
                logging.error(f"Could not extract text from device element: {e}")

        logging.info("Extracted Serial IDs: %s", serial_IDs)

        # Check each extracted serial_ID individually
        detected_devices = [serial_ID for serial_ID in serial_IDs if serial_ID in Available_Devices]

        if detected_devices:  # If devices are found, return them
            return detected_devices
        
        attempt += 1  # Increment attempt counter

    logging.error("No devices found after 3 attempts.")
    return []  # Return empty list if no devices are found

def select_and_connect_device(driver):
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
    selected_element = get_element(driver, serial_xpath)

    if selected_element:
        selected_element.click()
        print(f"Connected to {selected_ID}")
    else:
        print(f"Failed to locate the selected device: {selected_ID}")
    return True

if driver:
    try:
        # detected_devices = scan_for_devices(driver)
        # print("Scanning for devices done and the detected devices are found............")
        # print("detected device : ", detected_devices)
        search_Device_ID(driver, "eq_C697")
        if select_and_connect_device(driver):
            print("Device connection successful!")
        else:
            print("Device connection failed.")

    except Exception as e:
        print(f"Error in initializing the scanning: {e}")
else:
    print("error....")
