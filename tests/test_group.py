import unittest

from ipybudget.group import Group


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
