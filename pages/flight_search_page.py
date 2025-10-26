from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class FlightSearchPage(BasePage):

    Flights_section = (AppiumBy.ACCESSIBILITY_ID, "primary_lob_FLT_icon")
    FROM_FIELD = (AppiumBy.ID, "com.makemytrip:id/selected_from_city_text_layout")
    TO_FIELD = (AppiumBy.ID, "com.makemytrip:id/selected_to_city_text_layout")
    Departure_DATE_FIELD = (AppiumBy.ID, "com.makemytrip:id/tv_from_date")
    SEARCH_BUTTON = (AppiumBy.ID, "com.makemytrip:id/search_button_flat")


    def go_to_flights(self):
        """Click on the Flights tab from home screen"""
        self.wait_and_click(*self.Flights_section)

    def search_flight(self, from_city, to_city, date):

        
        self.wait_and_click(*self.FROM_FIELD)
        self.send_keys(self.FROM_FIELD, from_city)

        self.wait_and_click(*self.TO_FIELD)
        self.send_keys(self.TO_FIELD, to_city)

        self.wait_and_click(*self.Departure_DATE_FIELD)
        self.send_keys(self.Departure_DATE_FIELD, date)

        self.wait_and_click(*self.SEARCH_BUTTON)
