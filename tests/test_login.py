import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_login_mmt(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    # Handle first screen popups if any
    try:
        driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()
        driver.find_element_by_id("com.makemytrip:id/headerWidgetV2").click()
    except:
        pass

    login_page.enter_credentials("9149782783")
    login_page.click_confirm()
    login_page.submit_OTP()

    assert home_page.is_user_logged_in(), "Login failed!"
