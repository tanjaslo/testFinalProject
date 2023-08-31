import html
import json


def validate_response(response, expected_status_code=200):
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
    print("The status code is: " + str(response.status_code))


def parse_as_json(response):
    encoded_data = response.text

    # Decode HTML entities
    decoded_data = html.unescape(encoded_data)

    # Parse as JSON
    json_data = json.loads(decoded_data)

    return json_data
