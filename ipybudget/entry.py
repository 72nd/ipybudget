"""
The entry module contains all income/expense entry related stuff.
"""

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
    amount: Money
    code: str = ""
    currency: str = "EUR"

    def __init__(self, name: str):
        self.name = name


    @classmethod
    def set_currency(cls, currency: str):
        """
        Alter the currency for all following entries (defaults to EUR).
        Currencies are expressed in a three lettered code as stated in the
        ISO 4217 standard.
        """
        cls.currency = currency
