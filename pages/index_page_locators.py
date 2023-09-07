from selenium.webdriver.common.by import By


class IndexPageLocators:
    def __init__(self, city_name):
        # Defining CITY and ACTIVE_LINK as instance variables based on the city_name
        # provided as a parameter to the constructor,
        # allows to create different instances of IndexPageLocators for different cities,
        # and each instance will have its own CITY_LINK and ACTIVE_LINK attributes based on the specified city_name.
        self.CITY_LINK = (By.XPATH, f"//a[contains(@class, 'locations__item-link') and contains(@class, 'tabs__item false') and span[text()='{city_name}']]")
        self.ACTIVE_CITY_LINK = (By.XPATH, f"//a[contains(@class, 'locations__item-link') and contains(@class, 'tabs__item--active') and span[text()='{city_name}']]")

    SIGN_IN_LINK = (By.XPATH, "//span[@class='header__login' and text()='Sign in']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SIGN_OUT_LINK = (By.XPATH, "//span[@class='header__signout' and text()='Sign out']")
    NUMBER_OF_CITIES = (By.CSS_SELECTOR, "ul.locations__list.tabs__list>li")
