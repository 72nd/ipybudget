"""
The entry module contains all income/expense entry related stuff.
"""
from ipybudget import DEFAULT_CURRENCY

from typing import Union
from decimal import Decimal

from money import Money


class Entry:
    """
    A Entry represents a income or expense entry in your budget. They are
    grouped by the Group objects. All amounts are handled using a appropriate
    money object. Each entry defines at least a name and a amount. The effect
    of a given amount is defined by the group, so use negative amounts
    cautious for such stuff as yield reductions.
    """

    name: str
    """Short concise name for an income/expense entry."""
    amount: Money
    """Defines the amount of the entry."""
    code: str = ""
    """Optional short identifier for the entry. Defaults to an empty string."""
    comment: str = ""
    """Brief remarks on this entry. It's advised to keep this comments rather
    short as they have the tendency to break the table layout. Use Markdown
    blocks in the Jupyter notebook instead. Defaults to an empty string.
    """
    currency: str = DEFAULT_CURRENCY
    """ISO 4217 currency code for the group. Defaults to `EUR`."""

    def __init__(
        self,
        name: str,
        amount: Money,
        code: str = "",
        comment: str = "",
    ):
        self.name = name
        self.amount = amount
        self.code = code
        self.command = comment

    @classmethod
    def defaults(
        cls,
        name: str,
        amount: Union[str, int, Decimal],
        code: str = "",
        comment: str = "",
    ):
        """
        Initializes a Entry instance with the default currency. This is a
        additional method for your convenience.
        """
        return Entry(
            name,
            Money(amount, currency=cls.currency),
            code=code,
            comment=comment,
        )

    @ classmethod
    def set_currency(cls, currency: str):
        """
        Alter the currency for all following entries (defaults to EUR).
        Currencies are expressed in a three lettered code as stated in the
        ISO 4217 standard.
        """
        cls.currency = currency
