from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class LoginPage(BasePage):

    CONFIRM_BUTTON = (AppiumBy.ID, "com.makemytrip:id/btn_continue")
    PHONE_INPUT = (AppiumBy.ID, "com.makemytrip:id/inputFieldChild")
    SUBMIT_BUTTON = (AppiumBy.ID, "com.makemytrip:id/btn_continue")

    def __init__(self, driver):
        super().__init__(driver)  # ✅ This line initializes self.wait from BasePage

    def click_confirm(self):
        self.click(self.CONFIRM_BUTTON)

    # def enter_credentials(self, phone, password):
    def enter_credentials(self, phone):
        self.send_keys(self.PHONE_INPUT, phone)
        # self.send_keys(self.PASSWORD_INPUT, password)

    def submit_OTP(self):
        self.wait_and_click(*self.SUBMIT_BUTTON)
# com.gommt.gommt_auth.v2.b2c.presentation.LoginActivityV2
