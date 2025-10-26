from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # ✅ creates self.wait

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find_element(locator).click()

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    def wait_and_click(self, by, locator):
        element = self.wait.until(EC.element_to_be_clickable((by, locator)))
        element.click()

    def is_displayed(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False
