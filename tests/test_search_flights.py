import pytest
from pages.flight_search_page import FlightSearchPage
# from pages.home_page import HomePage
from utils.excel_reader import read_excel_data

# Read all test data from Excel
test_data = read_excel_data("test_data/flight_data.xlsx", "flight_data")

@pytest.mark.parametrize("data", test_data)
def test_flight_search(driver, data):
    # home_page = HomePage(driver)

    search_page = FlightSearchPage(driver)
    search_page.go_to_flights()

    # home_page.go_to_flights()

    from_city = data["FromCity"]
    to_city = data["ToCity"]
    date = data["Date"]

    search_page.search_flight(from_city, to_city, date)

    # Add your verification step (like checking search results)
    assert True  # placeholder for now
