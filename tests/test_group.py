import unittest

from ipybudget.entry import Entry
from ipybudget.group import Group

from money import Money


class TestGroup(unittest.TestCase):
    """Tests for the ipybudget Group class."""

    def test_default_init(self):
        """Test the default values for a Group instance."""
        group = Group("Set Design")
        self.assertEqual(group.name, "Set Design")
        self.assertEqual(group.items, [])
        self.assertEqual(group.code, "")
        self.assertEqual(group.comment, "")
        self.assertEqual(group.currency, "EUR")

    def test_init(self):
        """Test the initialziation of instance with all options."""
        name = "Set Design"
        items = []
        code = "2.1a"
        comment = "This is a comment"
        currency = "USD"
        group = Group(
            name,
            items=items,
            code=code,
            comment=comment,
            currency=currency,
        )
        self.assertEqual(group.name, name)
        self.assertEqual(group.items, items)
        self.assertEqual(group.code, code)
        self.assertEqual(group.comment, comment)
        self.assertEqual(group.currency, currency)

    def test_total_one_entry(self):
        """Test the total method with one entries."""
        group = Group(
            "Test Group",
            items=[
                Entry("Entry 1", 100),
                Entry("Entry 2", "23.5"),
            ]
        )
        self.assertEqual(group.total(), Money("123.5", "EUR"))
        self.assertNotEqual(group.total(), Money("123.5", "USD"))
        self.assertNotEqual(group.total(), Money(100, "EUR"))

    def test_total_one_entry_usd(self):
        """Test the total method while changing the global currency to USD."""
        Group.set_currency("USD")
        group = Group(
            "Test Group",
            items=[
                Entry("Entry 1", 100),
                Entry("Entry 2", "23.5"),
            ]
        )
        self.assertEqual(group.total(), Money("123.5", "USD"))
        self.assertNotEqual(group.total(), Money("123.5", "EUR"))
        self.assertNotEqual(group.total(), Money(100, "USD"))

