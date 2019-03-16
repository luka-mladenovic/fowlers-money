from __future__ import annotations
from .currency import Currency
import operator
import math


class Money:

    def __init__(self, amount: int, currency: Currency):
        self.__assert_amount(amount)

        self.__amount = amount
        self.__currency = currency

    def instance(self, amount: int) -> Money:
        """
        Return new money object using the
        same currency and given amount
        """
        self.__assert_amount(amount)

        return self.__class__(
            amount, self.currency
        )

    def __assert_currency(self, money: Money):
        """
        Assert that given money has the same currency
        """
        if not self.currency.equals(money.currency):
            raise ValueError('Currencies do not match')

    @staticmethod
    def __assert_amount(amount):
        """
        Assert that given amount is an integer
        """
        if not isinstance(amount, int):
            raise ValueError('Amount must be an integer')

    @staticmethod
    def __assert_operand(operand):
        """
        Assert that given operand is a numeric type
        """
        if not isinstance(operand, (int, float)):
            raise ValueError('Operand must be a numeric value')

    @property
    def amount(self) -> int:
        """
        Return money amount
        """
        return self.__amount

    @property
    def currency(self) -> Currency:
        """
        Return currency object
        """
        return self.__currency

    def __add__(self, money: Money) -> Money:
        """
        Return a new money object that amounts to
        sum of this object and given money object
        """
        self.__assert_currency(money)

        return self.__class__(
            self.amount + money.amount, self.currency
        )

    def __sub__(self, money: Money) -> Money:
        """
        Return a new money object that amounts to
        difference of this object and given money object
        """
        self.__assert_currency(money)

        return self.__class__(
            self.amount - money.amount, self.currency
        )

    def __mul__(self, factor: (int, float)) -> Money:
        """
        Return a new money object that amounts to
        product of this object and given money object
        """
        self.__assert_operand(factor)

        return self.__class__(
            round(self.amount * factor), self.currency
        )

    def __eq__(self, money: Money) -> bool:
        """
        Check if given money object value
        and currency matches this object
        """
        if not self.currency.equals(money.currency):
            return False

        return self.amount == money.amount

    def __gt__(self, money: Money) -> bool:
        """
        Check if object amount is
        greater than given money amount
        """
        return self.__compare(money, operator.gt)

    def __ge__(self, money: Money) -> bool:
        """
        Check if object amount is greater
        or if it equals to given money amount
        """
        return self.__compare(money, operator.ge)

    def __lt__(self, money: Money) -> bool:
        """
        Check if object amount is
        less than given money amount
        """
        return self.__compare(money, operator.lt)

    def __le__(self, money: Money) -> bool:
        """
        Check if object amount is less or
        if it equals to given money amount
        """
        return self.__compare(money, operator.le)

    def __compare(self, money: Money, operator) -> bool:
        """
        Compare object amount to given money
        amount using the provided comparison operator
        """
        self.__assert_currency(money)

        return operator(self.amount, money.amount)

    def allocate(self, ratios: list) -> list[Money]:
        """
        Allocate object amount to given ratios
        and return a collection of new money objects
        """
        results = []
        fractions = []
        total = sum(ratios)
        remainder = self.amount

        if total == 0:
            raise ValueError('Sum of ratios must be greater than zero')

        """
        Share for each ratio is calculated
        and stored as a new money object
        """
        for ratio in ratios:
            if ratio < 0:
                raise ValueError('Ratio must be zero or positive')

            fraction = self.amount * ratio / total
            fraction = fraction - math.floor(fraction)
            fractions.append(fraction)

            share = self.amount * ratio // total
            results.append(self.instance(share))

            remainder = remainder - share

        """
        Distribute the remainder one by one, starting with
        the biggest fraction first until all is allocated
        """
        while remainder > 0:
            index = fractions.index(max(fractions))
            fractions[index] = 0
            results[index] += self.instance(1)
            remainder -= 1

        return results
