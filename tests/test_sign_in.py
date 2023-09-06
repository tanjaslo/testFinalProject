from test_utils import *
from selenium import webdriver
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

        print(f"User {email_password[0]} is signed in successfully")
