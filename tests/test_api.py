# Test Scenario: API Testing for https://six-cities-7.vercel.app/ website

from api.api_common import validate_response, parse_as_json
from resources.constants import BASE_URL, EXPECTED_FIELDS


def fetch_and_validate_data(api, endpoint):
    response = api.get(endpoint)
    validate_response(response)
    return parse_as_json(response)


class TestAPI:
    # Test Case 1: Verify Successful API Connection
    def test_successful_api_connection(self, api):
        fetch_and_validate_data(api, "hotels")
        print("API connection successful!")

    # Test Case 2: Verify Data Consistency and Accuracy
    def test_data_consistency_and_accuracy(self, api):
        places = fetch_and_validate_data(api, "hotels")

        for place in places:
            # Check if all expected fields are present in the place
            assert all(field in place for field in EXPECTED_FIELDS), "Place data is inconsistent"
        print("Data consistency and accuracy verified successfully!")

    # Test Case 3: Verify Places Titles
    def test_place_titles(self, api):
        places = fetch_and_validate_data(api, "hotels")

        # Validate that each place has a title
        for place in places:
            assert "title" in place, "Place does not have a title field"
        print("Place titles verified successfully!")

    # Test Case 4: Verify Place Ratings are within the valid range (0.0 - 5.0)
    def test_place_ratings_valid_range(self, api):
        places = fetch_and_validate_data(api, "hotels")

        for place in places:
            rating = place.get("rating")
            assert 0.0 <= rating <= 5.0, f"Place rating {rating} is not within the valid range (0.0 - 5.0)"
        print("Place ratings are within the valid range (0.0 - 5.0)")

    # Test Case 5: Verify Place Prices Are Positive
    def test_place_prices_positive(self, api):
        places = fetch_and_validate_data(api, "hotels")

        for place in places:
            price = place.get("price")
            assert price >= 0, f"Place price {price} is not positive"
        print("Place prices are positive.")
