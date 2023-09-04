import pytest

from api.api_client import ApiClient


@pytest.fixture
def api():
    return ApiClient()
