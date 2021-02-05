import unittest

from ipybudget.entry import Entry
from ipybudget.group import Group
from ipybudget.rates import Rates

from money import Money


class TestRates(unittest.TestCase):
    """
    Tests all the currency related stuff. Especially working with different
    currencies.
    """

    def test_simple_sum(self):
        """
        Tests the total of a group consisting of two entries with different
        currencies.
        """
        rates = Rates()
        rates.add_currency("USD", 2)
        group = Group(
            "Set Design",
            [
                Entry("Expense 1", 100),
                Entry("Expense 2", 200, currency="USD"),
            ]
        )
        self.assertEqual(group.total(), Money(200, "EUR"))

    def test_complex_sum(self):
        """Some more currencies."""
        rates = Rates()
        rates.add_currency("USD", 2)
        rates.add_currency("CHF", 0.5)
        group = Group(
            "Set Design",
            [
                Entry("Expense 1", 100),
                Entry("Expense 2", 200, currency="USD"),
                Entry("Expense 3", 100, currency="CHF"),
            ]
        )
        self.assertEqual(group.total(), Money(400, "EUR"))
