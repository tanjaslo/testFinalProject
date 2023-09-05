from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

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
        #
        # def wait_and_click_sign_in_button(self):
        #     self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.SIGN_IN_LINK).click()

        def signin_user(self, email, password):
            # Find email and password input fields and enter valid credentials
            email_field = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.EMAIL_INPUT)
            password_field = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.PASSWORD_INPUT)

            email_field.send_keys(email)
            password_field.send_keys(password)

            # Submit the signin form
            self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.SIGN_IN_BUTTON).click()

        def verify_successful_signin(self):
            try:
                sign_out_element = self.explicitly_wait_and_find_element(
                    MAX_WAIT_INTERVAL, IndexPageLocators.SIGN_OUT_LINK
                )
                return sign_out_element.is_displayed()
            except TimeoutException:
                return False
