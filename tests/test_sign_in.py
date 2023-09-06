from test_utils import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from pages.index_page import IndexPage
from resources.constants import SITE_URL


class TestSignIn:

    # Test Case 1: User Signin with valid credentials
    def test_user_sign_in(self, driver, email_password):
        # Test Case: User Login
        # Initialize the IndexPage class
        index_page = IndexPage(driver)
        # Navigate to the website
        index_page.navigate_to(SITE_URL)
        # Click on the "Sign in" link
        index_page.wait_and_click_sign_in_link()
        # Perform user login
        index_page.signin_user(email_password[0], email_password[1])
        # Verify that the user is signed in successfully
        assert index_page.verify_successful_signin(), "User is not signed in successfully"
        index_page.sign_out_user()
        time.sleep(1)
        print(f"User {email_password[0]} is signed in successfully and signed out")

    # Test Case 2: User Log out
    def test_user_sign_out(self, driver, email_password):
        index_page = IndexPage(driver)
        index_page.navigate_to(SITE_URL)
        index_page.wait_and_click_sign_in_link()
        index_page.signin_user(email_password[0], email_password[1])
        time.sleep(1)
        index_page.sign_out_user()
        # Check if the "Sign in" link is visible after signing out
        sign_in_link_visible = index_page.is_sign_in_link_visible()
        assert sign_in_link_visible, "Sign in link is not visible after signing out"
        print("User is signed out successfully")

    # Test Case 3: User Signin with invalid credentials
    def test_user_sign_in_with_invalid_credentials(self, driver, email_password):
        index_page = IndexPage(driver)
        index_page.navigate_to(SITE_URL)
        time.sleep(1)
        index_page.wait_and_click_sign_in_link()
        email_input = driver.find_element(By.NAME, 'email')
        email_input.send_keys("invalid")
        index_page.wait_and_click_sign_in_button()
        # Retrieve the validation message
        validation_message = email_input.get_attribute("validationMessage")
        # Check if the validation message matches the expected message
        expected_message = "Please provide correct email"
        assert validation_message == expected_message, f"Validation message mismatch. Expected: {expected_message}, Actual: {validation_message}"
        print("Sign In failed with invalid credentials")
