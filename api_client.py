import requests
from utils.logger import Logger
import logging


class ApiClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key
        self.logger = Logger().logger(logging.DEBUG)

    def search_by_title(self, title):
        param = {
            "t": title,
            "apikey": self.api_key
        }

        try:
            response = requests.get(self.base_url, params=param, timeout=10)
            self.logger.debug(f"Response status code: {response.status_code}")
            self.logger.debug(f"Response data: {response.json()}")
            return {"status_code": response.status_code, "data": response.json()}
        except requests.exceptions.Timeout as timeout_error:
            self.logger.error(f"Timeout error occurred: {timeout_error}")
            return {"status_code": 408, "data": {"Response": "False", "Error": "Request timed out."}}
        except requests.exceptions.ConnectionError as connection_error:
            self.logger.error(f"Connection error occurred: {connection_error}")
            return {"status_code": 500, "data": {"Response": "False", "Error": "Connection error."}}
