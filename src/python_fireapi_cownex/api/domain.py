from src.python_fireapi_cownex.api.base import FireAPI


class Domain(FireAPI):
    """Class for interacting with the Dpmain Endpoints"""

    def list_all_domains(self):
        """List all purchased Domains"""
        pass

    def register_domain(self, domain, handle, authcode=None):
        """
        Register/Transfer a Domain
        :param domain: Domain (ex. fireapi.de)
        :param handle: Previously created handle
        :param authcode: If transfer, authcode
        """
        pass

    def delete_domain(self, domain):
        """
        Deletes the Domain
        :param domain: Domain (ex. fireapi.de)
        """
        pass

    def undelete_domain(self, domain):
        """
        Undeletes the Domain
        :param domain: Domain (ex. fireapi.de)
        """
        pass

    def get_authcode(self, domain):
        """
        Requests the Authcode
        :param domain: Domain (ex. fireapi.de)
        """
        pass

    def domain_info(self, domain):
        """
        List Info about Domain
        :param domain: Domain (ex. fireapi.de)
        """
        pass

    def check_domain_available(self, domain):
        """
        Check if Domain can be Register/Transfer
        :param domain: Domain (ex. fireapi.de)
        """
        pass

    def change_nameserver(self, domain, ns1, ns2, n3=None, ns4=None, ns5=None):
        """

        :param domain: Domain (ex. fireapi.de)
        :param ns1: Namserver 1 (required)
        :param ns2: Namserver 2 (required)
        :param n3: Namserver 3 (optional)
        :param ns4:  Namserver 4 (optional)
        :param ns5:  Namserver 5(optional)
        """
        pass

    def get_pricing(self):
        """Get Domain TLD Pricing"""
        pass

    # todo add handle & dns