import requests

from src.python_fireapi_cownex import exception, constants
from src.python_fireapi_cownex.api.base import FireAPI


class Accounting(FireAPI):
    """Class for interacting with the Accounting Endpoints"""

    def get_all_invoices(self):
        """List all Invoices"""
        return self.request("accounting/invoices", "GET")

    def get_invoice_details(self, invoice_id):
        """
        Get Details of the given Invoice
        :param invoice_id: ID of the Invoice
        :return:
        """
        return self.request(f"accounting/invoices/{invoice_id}", "GET")

    def get_current_invoices(self):
        """Get current Invoice state"""
        return self.request("accounting/invoices/current", "GET")

    def get_pricing(self):
        """Get current pricing for vms and domains."""
        return self.request("accounting/pricings", "GET")

    def get_sales(self):
        """Get current sales."""
        return self.request("accounting/sales", "GET")



