import pytest
from appium import webdriver
import json
import time

def test_launch_app(driver):
    # Just check if app launches
    current_package = driver.current_package
    assert current_package == "com.makemytrip"
    print("✅ MakeMyTrip launched successfully")

