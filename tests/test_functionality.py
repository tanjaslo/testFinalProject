# Test Scenario: Interaction with UI Elements and Functionality Testing for https://six-cities-7.vercel.app/ website

from test_utils import *
import time
from pages.index_page import IndexPage
from pages.city_page import CityPage
from pages.offer_page import OfferPage
from pages.index_page_locators import IndexPageLocators
from resources.constants import SITE_URL, CHOSEN_CITY_NAME

city_locator = IndexPageLocators(CHOSEN_CITY_NAME).CITY_LINK
active_city_locator = IndexPageLocators(CHOSEN_CITY_NAME).ACTIVE_CITY_LINK


class TestFunctionality:

    # Test Case 1: Verify that the page displays the expected number of cities
    def test_number_of_cities(self, driver):
        index_page = IndexPage(driver)
        index_page.navigate_to(SITE_URL)
        time.sleep(1)
        cities_count = index_page.get_number_of_cities()
        expected_count = 6
        assert cities_count == expected_count, f"Expected number of cities: {expected_count}, Actual number of cities: {cities_count}"
        print(f"Verified: {cities_count} cities are displayed on the index page")

    # Test Case 2: Click on the city link and verify that the city link is active
    def test_click_city_link(self, driver):
        index_page = IndexPage(driver)
        index_page.navigate_to(SITE_URL)
        index_page.click_city_link(city_locator)
        time.sleep(1)
        is_active = index_page.is_city_link_active(active_city_locator)
        time.sleep(1)
        assert is_active, f"City link is not active"
        print(f"Verified: City link is active")

    # Test Case 3: Click on the city link and verify that the city-specific page is loaded
    # by displaying the message with number of places to stay
    def test_display_number_of_places_to_stay(self, driver):
        index_page = IndexPage(driver)
        index_page.navigate_to(SITE_URL)
        time.sleep(1)
        index_page.click_city_link(city_locator)
        time.sleep(1)
        city_page = CityPage(driver)
        places_count = city_page.get_place_card_elements_count()
        print(f" {places_count} place_card_elements are found")
        expected_message = f"{places_count} places to stay in {CHOSEN_CITY_NAME}"
        actual_message = city_page.display_number_of_places_to_stay()
        assert actual_message == expected_message, f"Expected message: '{expected_message}', Actual message: '{actual_message}'"
        print(f"Verified: {actual_message}")
