from test_utils import *
import pytest as pytest
from selenium import webdriver

from api.api_client import ApiClient


@pytest.fixture
def api():
    return ApiClient()


@pytest.fixture(scope="module")
def driver():
    _driver = webdriver.Chrome()
    _driver.maximize_window()  # Maximize the browser window
    yield _driver  # Yield the WebDriver instance to the test
    _driver.quit()  # After the test, close the WebDriver
