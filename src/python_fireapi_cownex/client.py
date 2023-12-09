import requests
from api import domain, dedicated, vm, accounting, account
from src.python_fireapi_cownex import exception, constants


class FireAPIClient(object):
    """Client for interact with the FireAPI"""
    url = "https://live.fireapi.de/"
    api_key = None

    def __init__(self, api_key=None):
        self.api_key = api_key

    @property
    def vm(self):
        return vm.VM(self.url, self.api_key)

    @property
    def domain(self):
        return domain.Domain(self.url, self.api_key)

    @property
    def dedicated(self):
        return dedicated.Dedicated(self.url, self.api_key)

    @property
    def accounting(self):
        return accounting.Accounting(self.url, self.api_key)

    @property
    def account(self):
        return account.Account(self.url, self.api_key)
