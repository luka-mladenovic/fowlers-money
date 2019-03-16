from __future__ import annotations
from .currency_bag import CurrencyBag


class Currency:

    def __init__(self, code: str):
        currency_data = CurrencyBag.load(code)

        if(currency_data is None):
            raise ValueError('Currency ' + code + ' is not supported')

        self.__currency = currency_data

    def equals(self, currency: Currency) -> bool:
        """
        Check if given currency is of same type
        """
        return self.code == currency.code

    @property
    def code(self) -> str:
        """
        Return currency alphabetical code
        """
        return self.__currency['code']

    @property
    def name(self) -> str:
        """
        Return currency name
        """
        return self.__currency['name']

    @property
    def iso_code(self) -> int:
        """
        Return currency iso code
        """
        return self.__currency['iso_code']

    @property
    def minor_unit(self) -> int:
        """
        Return currency minor unit
        """
        return self.__currency['minor_unit']
