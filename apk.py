import time
import logging
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

'''
import os
print(os.path.exists("D:/Downloads/amazon.apk"))  # Should return True
'''
options = UiAutomator2Options()
options.set_capability("app", "D:\\Downloads\\com.amazon.mShop.android.shopping_26.18.0.100-1241256011_minAPI26(arm64-v8a)(nodpi)_apkmirror.com.apk")
options.set_capability("platformName", "Android")
options.set_capability("deviceName", "Lenovo Tab M9")
# options.set_capability("appium:appPackage", "com.amazon.mShop.android.shopping")
options.set_capability("appium:appPackage", "com.amazon.mShop.android.shopping")
# options.set_capability("appium:appActivity", "com.amazon.mShop.navigation.MainActivity")
options.set_capability("appium:appActivity", "com.amazon.mShop.home.HomeActivity")

driver = webdriver.Remote('http://localhost:4723', options=options)