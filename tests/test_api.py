# Test Scenario: API Testing for https://six-cities-7.vercel.app/ website
import requests

from api.api_common import validate_response, parse_as_json
from resources.constants import BASE_URL


class TestAPI:
    # Test Case 1: Verify Successful API Connection
    def test_successful_api_connection(self, api):
        response = api.get("hotels")
        validate_response(response)
