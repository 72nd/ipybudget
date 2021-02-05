from ipybudget.entry import Entry
from ipybudget.group import Group
from ipybudget.rates import Rates

DEFAULT_CURRENCY = "EUR"
"""The default currency for the package."""


def set_currency(cls, currency: str):
    """
    Alter the currency for all following budget elements (defaults to EUR).
    Currencies are expressed in a three lettered code as stated in the
    ISO 4217 standard.
    """
    Group._set_currency(currency)
    Entry._set_currency(currency)
    Rates._set_currency(currency)
