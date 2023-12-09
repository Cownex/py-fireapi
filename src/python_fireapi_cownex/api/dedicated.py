import requests

from src.python_fireapi_cownex import exception, constants, utils
from src.python_fireapi_cownex.api.base import FireAPI


class Dedicated(FireAPI):
    """Class for interacting with the Dedicated Endpoints"""
    def get_marketplace(self):
        """List all available Dedicated Servers"""
        return self.request("dedicated/available", "GET")

    def is_available(self, identifier):
        """
        Check if Dedicated-Server available
        :param identifier: Dedicated-Identifier
        """
        return self.request(f"dedicated/available/{identifier}", "GET")

    def purchase_dedicated(self, identifier, webhook=None, connect=None):
        """
        Purchase the Dedicated-Server
        :param identifier: identifier: Dedicated-Identifier
        :param webhook: optional - URL to send Webhook when Dedicated-Server is ready.
        :param connect: optional - If Customer has an Dedicated-Server you can add this ID here.
        """
        if webhook or connect:
            data = {}
            utils.update_json(data, "webhook", webhook)
            utils.update_json(data, "connect", connect)
        else:
            data = None
        return self.request(f"dedicated/{identifier}/purchase", "POST", data)

    def dedicated_info(self, identifier):
        return self.request(f"dedicated/{identifier}/info", "GET")

    def get_dedicated_list(self):
        """List bought Dedicated-Server"""
        return self.request(f"dedicated/list", "GET")

    def delete_dedicated(self, identifier):
        """
        Delete Dedicated-Server
        :param identifier: Dedicated-Identifier
        """
        return self.request(f"dedicated/{identifier}/delete", "DELETE")

    def undelete_dedicated(self, identifier):
        """
        Undelete Dedicated-Server
        :param identifier: Dedicated-Identifier
        """
        return self.request(f"dedicated/{identifier}/undelete", "POST")



