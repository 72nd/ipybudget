"""
The Budget module contains all budget class related stuff.
"""
from ipybudget.entry import Entry
from ipybudget.group import Group

from typing import List


class Budget:
    """
    The Budget class is the main class for every ipybudget based budget. It
    contains the different expense and income groups and provides export
    functionality for the whole budget. For displaying the each entry it's
    advised to use the display functionality of the Groups and using Jupyter's
    markdown blocks to express the structure of the budget.
    """
    expenses = List[Group]

    @classmethod
    def set_currency(cls, currency: str):
        """
        Alter the currency for all following budget elements (defaults to EUR).
        Currencies are expressed in a three lettered code as stated in the
        ISO 4217 standard.
        """
        Group.set_currency(currency)
        Entry.set_currency(currency)
