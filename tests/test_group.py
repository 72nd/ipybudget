import unittest

from ipybudget import DEFAULT_CURRENCY
from ipybudget.entry import Entry
from ipybudget.group import Group
from ipybudget.rates import Rates

from money import Money


class TestGroup(unittest.TestCase):
    """Tests for the ipybudget Group class."""

    def test_default_init(self):
        """Test the default values for a Group instance."""
        group = Group("Set Design", [])
        self.assertEqual(group.name, "Set Design")
        self.assertEqual(group.items, [])
        self.assertEqual(group.code, "")
        self.assertEqual(group.comment, "")
        self.assertEqual(group.currency, DEFAULT_CURRENCY)

    def test_init(self):
        """Test the initialziation of instance with all options."""
        name = "Set Design"
        items = []
        code = "2.1a"
        comment = "This is a comment"
        group = Group(
            name,
            items,
            code=code,
            comment=comment,
        )
        self.assertEqual(group.name, name)
        self.assertEqual(group.items, items)
        self.assertEqual(group.code, code)
        self.assertEqual(group.comment, comment)
        self.assertEqual(group.currency, DEFAULT_CURRENCY)

    def test_total_two_entries(self):
        """Test the total method with one entries."""
        group = Group(
            "Test Group",
            [
                Entry("Entry 1", 100),
                Entry("Entry 2", "23.5"),
            ]
        )
        self.assertEqual(group.total(), Money("123.5", "EUR"))

    def test_total_two_entries_usd(self):
        """Test the total method while having one entry in USD."""
        rates = Rates()
        rates.add_currency("USD", 2)

        group = Group(
            "Test Group",
            [
                Entry("Entry 1", 100),
                Entry.from_money("Entry 2", Money(200, "USD")),
            ]
        )
        self.assertEqual(group.total(), Money(200, "EUR"))
        self.assertNotEqual(group.total(), Money(300, "EUR"))
        self.assertNotEqual(group.total(), Money(200, "USD"))
        self.assertNotEqual(group.total(), Money(300, "USD"))

    @unittest.expectedFailure
    def test_failure_on_no_rates(self):
        """
        Tests if a exception is thrown when multiple currencies are used by no
        Rates object was instantiated.
        """
        group = Group(
            "Test Group",
            [
                Entry("Entry 1", 100),
                Entry("Entry 2", "23.5"),
            ]
        )
        self.assertEqual(group.total(), Money("123.5", "USD"))
        self.assertNotEqual(group.total(), Money("123.5", "EUR"))
        self.assertNotEqual(group.total(), Money(100, "USD"))
