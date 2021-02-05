"""
The group module contains all income/expense group related stuff.
"""
from ipybudget import DEFAULT_CURRENCY
from ipybudget.entry import Entry
from ipybudget.rates import RatesNotInstalled

from typing import List, Union, Optional

from money import Money
from money.exceptions import ExchangeBackendNotInstalled
from vdom import helpers as v


class Group:
    """A Group groups one or more income or expense entries. It's also possible
    to nest multiple groups into each other (sub groups). This can be used to
    structure complex income or expense records like for example personnel
    expenses. The group implements the needed IPython repl formatting methods
    for outputting HTML, Mardkown and LaTeX. This is the intended way of
    displaying the data for the report. Use Jupyter's Markdown blocks to
    further structure and formate the budget and adding remarks for entries.
    """

    name: str
    """Name of the Group."""
    items: List[Union[Entry, "Group"]]
    """All income/expense entries of this group. Each group can also contain
    sub-groups itself to express more complex budgets."""
    code: str = ""
    """Optional short identifier for the group. Defaults to an empty string."""
    comment: str = ""
    """Brief remarks on this group. It's advised to keep this comments rather
    short as they have the tendency to break the table layout. Use Markdown
    blocks in the Jupyter notebook instead. Defaults to an empty string.
    """
    currency: str = DEFAULT_CURRENCY
    """
    ISO 4217 currency code for the group. Defaults to `EUR`. Can be changed by
    calling the ipybudget.budget.Budget.set_currency method. Attention: Entries
    of the group created with ipybudget.entry.Entry.__init__ will **not**
    automatically inherit this currency.
    """

    def __init__(
            self,
            name: str,
            items: List[Union[Entry, "Group"]],
            code: str = "",
            comment: str = "",
            currency: Optional[str] = None,
    ):
        """
        Initializes a Group instance. Needs at least a name for the group.
        """
        self.name = name
        self.items = items
        self.code = code
        self.comment = comment
        if currency:
            self.currency = currency

    @classmethod
    def _set_currency(cls, currency: str):
        """
        Alter the currency for all following entries (defaults to EUR).
        Currencies are expressed in a three lettered code as stated in the
        ISO 4217 standard.

        This method shouldn't be called directly use the ipybudget.set_currency
        method instead.
        """
        cls.currency = currency

    def total(self) -> Money:
        """
        Calculates the total sum of all entries in the group and it's
        subgroups. The items have to be a Entry or a Group otherwise a
        exception will be thrown.
        """
        rsl = Money(0, self.currency)

        for item in self.items:
            if isinstance(item, Entry):
                try:
                    rsl += item.amount_by_currency(self.currency)
                except ExchangeBackendNotInstalled:
                    raise RatesNotInstalled
                continue
            if isinstance(item, Group):
                try:
                    rsl += item.total().to(self.currency)
                except ExchangeBackendNotInstalled:
                    raise RatesNotInstalled
                continue
            raise TypeError(
                "Group item has to be a Entry/Group, got {} instead".format(
                    type(item))
            )
        return rsl

    def _repr_html_(self):
        """Output for the Jupyter notebook."""
        layout = v.table(
            v.tr(
                v.th("Pos.", style={"text-align": "right"}),
                v.th("Bezeichnung", style={"text-align": "left"}),
                v.th("Betrag", style={"text-align": "right"}),
                v.th("Anmerkung", style={"text-align": "left"})
            ),
            v.tr(
                v.td(v.b(self.code), style={"text-align": "right"}),
                v.td(v.b(self.name), style={"text-align": "left"}),
                v.td(),
                v.td(),
            ),
            *[x.vdom() for x in self.items],
            v.tr(
                v.td(),
                v.td(v.b(
                    "Total {}".format(self.name)),
                    style={"text-align": "left"}
                ),
                v.td(v.b(str(self.total())), style={"text-align": "right"}),
                v.td(),
            )
        )
        return layout.to_html()
