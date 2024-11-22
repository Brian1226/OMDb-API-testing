import os
import pytest
import requests
from dotenv import load_dotenv
from api_client import ApiClient

load_dotenv()

@pytest.fixture
def api_client():
    base_url = os.getenv("BASE_URL")
    api_key = os.getenv("API_KEY")
    return ApiClient(base_url, api_key)

def test_search_by_title(api_client):
    response = api_client.search_by_title("The Batman")
    assert response["status_code"] == 200, f"Expected status code 200, but got {response['status_code']}"
    assert response["data"]["Response"] == "True", f"Expected response 'True', but got {response['data']['Response']}"
    assert response["data"]["Title"] == "The Batman", f"Expected title 'The Batman', but got {response['data']['Title']}"

def test_search_by_invalid_title(api_client):
    response = api_client.search_by_title("Invalid Movie Title")
    assert response["status_code"] == 200, f"Expected status code 200, but got {response['status_code']}"
    assert response["data"]["Response"] == "False", f"Expected response 'False', but got {response['data']['Response']}"
    assert response["data"]["Error"] == "Movie not found!", f"Expected error message 'Movie not found!', but got {response['data']['Error']}"

def test_search_by_title_without_api_key():
    base_url = os.getenv("BASE_URL")
    api_client_without_api_key = ApiClient(base_url, "")
    response = api_client_without_api_key.search_by_title("The Batman")
    assert response["status_code"] == 401, f"Expected status code 401, but got {response['status_code']}"
    assert response["data"]["Response"] == "False", f"Expected response 'False', but got {response['data']['Response']}"
    assert response["data"]["Error"] == "No API key provided.", f"Expected error message 'No API key provided.', but got {response['data']['Error']}"
