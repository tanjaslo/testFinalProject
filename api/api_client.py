import requests

from resources.constants import BASE_URL


class ApiClient:
    def __init__(self):
        self.base_url = BASE_URL

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params)
        return response
