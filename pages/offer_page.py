from pages.offer_page_locators import OfferPageLocators
from pages.base_page import BasePage


class OfferPage(BasePage):

    def get_place_name(self):
        place_name_element = self.driver.find_element(*OfferPageLocators.PLACE_NAME)
        return place_name_element.text

    # More methods will be added to interact with other elements on the offer page
