# Test Scenario: API Testing for https://six-cities-7.vercel.app/ website
import requests

from api.api_common import validate_response, parse_as_json
from resources.constants import BASE_URL


class TestAPI:
    # Test Case 1: Verify Successful API Connection
    def test_successful_api_connection(self, api):
        response = api.get("hotels")
        validate_response(response)

    # Test Case 2: Verify Data Consistency and Accuracy
    def test_data_consistency_and_accuracy(self, api):
        response = api.get("hotels")
        validate_response(response)

        events = parse_as_json(response)

        # Validate data consistency and accuracy for each event
        for event in events:
            assert "city" in event
            assert "title" in event
            assert "rating" in event
            assert "price" in event
        print("Data consistency and accuracy verified successfully!")
