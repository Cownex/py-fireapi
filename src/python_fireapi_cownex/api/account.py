import requests

from src.python_fireapi_cownex import exception, constants
from src.python_fireapi_cownex.api.base import FireAPI


class Account(FireAPI):
    """Class for interacting with the Account Endpoints"""
    def list_all_requests(self, offset: int = None):
        """
        List all Requests
        :param offset: Offset of the List
        """
        if offset:
            data = {"offset": offset}
        else:
            data = None
        return self.request("account/requests", "POST", data)
