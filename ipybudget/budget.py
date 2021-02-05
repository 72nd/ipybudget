"""
The Budget module contains all budget class related stuff.
"""
from ipybudget.entry import Entry
from ipybudget.group import Group
from ipybudget.rates import Rates

from typing import List, Union


class Budget:
    """
    The Budget class is the main class for every ipybudget based budget. It
    contains the different expense and income groups and provides export
    functionality for the whole budget. For displaying the each entry it's
    advised to use the display functionality of the Groups and using Jupyter's
    markdown blocks to express the structure of the budget.

    To accommodate multiple currencies in one budget you can define fixed
    exchanged rates for your budget.
    """

    expenses = List[Union[Entry, Group]]
    """
    All groups and/or entries (also known as Item) which create some financial
    obligation for the project/company.
    """
    incomes = List[Union[Entry, Group]]
    """
    All groups and/or entries (also known as Item) which create some financial
    income for the project/company.
    """
    __rates: Rates = Rates()
    """
    Contains the currency exchange rates. The functionality is outsourced from
    the budget class to offer the separate rendering of exchange rates in the
    Jupyter notebooks and it's exported documents.
    """

    def __init__(
        self,
        expenses: List[Union[Entry, Group]] = [],
        incomes: List[Union[Entry, Group]] = [],
        rates: Rates = Rates()
    ):
        self.expenses = expenses
        self.incomes = incomes
        self.__rates = rates

    @classmethod
    def set_currency(cls, currency: str):
        """
        Alter the currency for all following budget elements (defaults to EUR).
        Currencies are expressed in a three lettered code as stated in the
        ISO 4217 standard.
        """
        Group.set_currency(currency)
        Entry.set_currency(currency)
        Rates.set_currency(currency)
