"""
The rates module handles the usage of multiple currencies in one budget. This
is accomplished by implementing the BackendBase object of the money package.
"""
from ipybudget import DEFAULT_CURRENCY

from decimal import Decimal
from typing import Dict, Union

from money import xrates
from money.exchange import BackendBase


class Rates(BackendBase):
    """
    The Rates class handles the conversion when using multiple currencies in
    one budget. The rates are expressed in relation to the base currency
    (change this by using the ipybudget.budget.Budget.set_currency method).
    As transparency is important for budgets "hard-coded" values set by the
    user are favorable than using dynamic Internet based approaches. This class
    implements all IPython repl methods, thus can be used to output a formatted
    overview over the used exchange rates in Jupyter. Add currencies by using
    the Rates.add_currency method.

    The conversion is archived by implementing the BackendBase class from the
    money package. By instantiating a new Rates instance, this will get
    automatically registered as the default backend for *all* currency
    calculations. 
    """
    __base_currency: str = DEFAULT_CURRENCY
    """
    Defines the base currency which is used to express the exchange rate for
    additional currencies relative to this base. Using the set_currency method
    will also adjust the base currency. Defaults `EUR`.
    """
    __rates: Dict[str, Union[int, float]] = {}
    """
    Used to store additional exchange rates expressed relative to the
    base_currency. You can add a rate by using the add_rate method.
    """

    def __init__(self):
        """
        Returns a new instance of the Rates and register this as the new
        default for currency conversion for *all* calculations.
        """
        xrates.install(self)

    @classmethod
    def set_currency(cls, currency: str):
        """
        Alter the base currency for all following budget elements (defaults to
        `EUR`). Currencies are expressed in a three lettered code as stated in
        the ISO 4217 standard.
        """
        cls.__base_currency = currency

    def add_currency(self, currency: str, rate: Union[int, float]):
        """
        Add an additional currency with a given name (following the ISO 4217
        standard) and a exchange rate relative to the base currency.
        """
        self.__rates[currency] = rate

    def base(self):
        """
        Returns the base currency. Implements the abstract method base()
        from BackendBase.
        """
        return self.__base_currency

    def rate(self, currency):
        """
        Implements the abstract method rate() of the BackendBase.
        """
        if currency == self.__base_currency:
            return Decimal(1)
        return self.__rates.get(currency, None)

    def quotation(self, origin, target):
        """
        Implements the abstract method quotation() of the BackendBase by
        calling it's implementation.
        """
        return super(Rates, self).quotation(origin, target)


class RatesNotInstalled(Exception):
    """
    This class wraps the money.exceptions.ExchangeBackendNotInstalled for
    a more understandable error. In the case of ipybudget the raise the user
    wants to do some currency conversions without having defined the rates by
    instantiate a Rates object.
    """

    def __init__(self):
        msg = "you tried to use multiple currencies without defining " \
            "the exchange rates by instantiate a Rates instance."
        super(Exception, self).__init__(msg)
