from selenium.common import TimeoutException, NoSuchElementException

from pages.base_page import BasePage
from pages.index_page_locators import IndexPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class IndexPage(BasePage):

        def wait_and_click_sign_in_link(self):
            self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.SIGN_IN_LINK).click()

        # def wait_and_type_user_email(self, email):
        #     self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.EMAIL_INPUT).send_keys(email)
        #
        # def wait_and_type_user_password(self, password):
        #     self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.PASSWORD_INPUT).send_keys(password)

        def wait_and_type_user_field(self, locator, text):
            self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, locator).send_keys(text)

        def wait_and_click_sign_in_button(self):
            self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.SIGN_IN_BUTTON).click()

        # def signin_user(self, email, password):
        #     self.wait_and_type_user_email(email)
        #     self.wait_and_type_user_password(password)
        #     self.wait_and_click_sign_in_button()

        def sign_in_user(self, email, password):
            self.wait_and_type_user_field(IndexPageLocators.EMAIL_INPUT, email)
            self.wait_and_type_user_field(IndexPageLocators.PASSWORD_INPUT, password)
            self.wait_and_click_sign_in_button()

        def sign_out_user(self):
            self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.SIGN_OUT_LINK).click()

        def verify_successful_sign_in(self):
            try:
                sign_out_element = self.explicitly_wait_and_find_element(
                    MAX_WAIT_INTERVAL, IndexPageLocators.SIGN_OUT_LINK
                )
                return sign_out_element.is_displayed()
            except TimeoutException:
                return False

        def is_sign_in_link_visible(self):
            try:
                sign_in_element = self.explicitly_wait_and_find_element(
                    MAX_WAIT_INTERVAL, IndexPageLocators.SIGN_IN_LINK
                )
                return sign_in_element.is_displayed()
            except TimeoutException:
                return False

        def click_city_link(self, city_locator):
            self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, city_locator).click()

        def is_city_link_active(self, active_link_locator):
            try:
                active_city_link = self.driver.find_element(*active_link_locator)
                print(f"Active city link is found: {active_city_link.text}")
                return True
            except NoSuchElementException:
                return False

        def get_number_of_cities(self):
            try:
                self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.NUMBER_OF_CITIES)
                city_elements = self.find_elements(*IndexPageLocators.NUMBER_OF_CITIES)
                displayed_cities = [element for element in city_elements if element.is_displayed()]
                return len(displayed_cities)
            except (TimeoutException, NoSuchElementException):
                return 0
