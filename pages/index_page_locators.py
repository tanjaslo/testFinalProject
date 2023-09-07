from selenium.webdriver.common.by import By

from resources.constants import CITIES


class IndexPageLocators:
    def __init__(self, city_name):
        self.CITY = (By.XPATH, f"//*[@id='root']/div/main/div[1]/section/ul/li[{CITIES.index(city_name) + 1}]/a/span")
        self.ACTIVE_LINK = (By.XPATH, f"//ul[@class='locations__list tabs__list']/li[{CITIES.index(city_name) + 1}]//a[contains(@class, 'locations__item-link') and contains(@class, 'tabs__item--active')]")

    SIGN_IN_LINK = (By.XPATH, "//span[@class='header__login' and text()='Sign in']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SIGN_OUT_LINK = (By.XPATH, "//span[@class='header__signout' and text()='Sign out']")
    NUMBER_OF_CITIES = (By.CSS_SELECTOR, "ul.locations__list.tabs__list>li")
    # ACTIVE_LINK = f"//a[contains(@class, 'locations__item-link') and contains(@class, 'tabs__item--active') and span[text()='{city_name}']]"
    # ACTIVE_LINK = (By.XPATH, f"//ul[@class='locations__list tabs__list']/li[{city_index}]//a[contains(@class, 'locations__item-link') and contains(@class, 'tabs__item--active')]")
