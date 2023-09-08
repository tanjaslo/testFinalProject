from pages.base_page import BasePage
from pages.city_page_locators import CityPageLocators


class CityPage(BasePage):

    # Get the number of places to stay by counting the place card elements
    def get_place_card_elements_count(self):
        place_card_elements = self.find_elements(*CityPageLocators.PLACE_CARD)
        return len(place_card_elements)

    # Get the text of the element (e.g., "17 places to stay in Paris")
    def display_number_of_places_to_stay(self):
        # Wait for the element indicating the number of places to stay to be visible
        places_element = self.explicitly_wait_and_find_element(10, CityPageLocators.NUMBER_OF_PLACES)
        places_text = places_element.text
        return places_text

