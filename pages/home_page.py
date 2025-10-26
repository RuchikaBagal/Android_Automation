from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    HOME_ICON = (AppiumBy.ID, "bottom_bar_HOME_title")

    def is_user_logged_in(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.HOME_ICON))
            return True
        except:
            return False
        # return self.is_displayed(self.HOME_ICON)


