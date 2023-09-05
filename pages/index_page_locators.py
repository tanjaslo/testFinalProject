from selenium.webdriver.common.by import By


class IndexPageLocators:
    SIGN_IN_LINK = (By.XPATH, "//span[@class='header__login' and text()='Sign in']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SIGN_OUT_LINK = (By.XPATH, "//span[@class='header__signout' and text()='Sign out']")
