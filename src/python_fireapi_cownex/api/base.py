import requests

from src.python_fireapi_cownex import exception, constants


class FireAPI(object):
    """Base Class for interacting with the FireAPI"""
    url = ""
    api_key = ""

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key

    def request(self, endpoint, methode, data=None):
        if not endpoint or not methode:
            raise Exception("Endpoint and Methode required.")
        if not methode in constants.HTTP_METHODS:
            raise Exception("Endpoint and Methode required.")
        headers = {
            "X-FIRE-APIKEY": f"{self.api_key}",
            'Content-Type': 'application/x-www-form-urlencoded',
            "Accept": "application/json",
        }
        return requests.request(methode, url=self.url + endpoint, data=data, headers=headers, verify=True)
