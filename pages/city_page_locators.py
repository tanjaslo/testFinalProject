from selenium.webdriver.common.by import By


class CityPageLocators:
    NUMBER_OF_PLACES = (By.CSS_SELECTOR, "#root>div>main>div.cities>div>section>b")
    PLACE_CARD = (By.CSS_SELECTOR, '.cities__place-card.place-card')