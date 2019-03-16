import unittest

from money.money import Money
from money.currency import Currency


class TestMoney(unittest.TestCase):
    def setUp(self):
        """
        Prepare default currency object for test cases
        """
        self.currency = Currency('EUR')

    def test_create_money(self):
        """
        Create new money object
        """
        for amount in [0, 10, 1000, -100]:
            with self.subTest():
                money = Money(amount, self.currency)

    def test_create_money_instance(self):
        """
        It creates a new money instance with given amount using the same currency
        """
        original = Money(10, self.currency)
        new = original.instance(100)

        self.assertEqual(self.currency, new.currency)

    def test_invalid_amount(self):
        """
        An exception is thrown when money amount is invalid
        """
        for amount in ['', None, .1, 1.10]:
            with self.subTest():
                with self.assertRaises(ValueError):
                    money = Money(amount, self.currency)

    def test_return_amount(self):
        """
        It returns money amount
        """
        money = Money(10, self.currency)
        self.assertEqual(10, money.amount)

    def test_return_currency_object(self):
        """
        It returns currecy object
        """
        money = Money(10, self.currency)
        currency = money.currency

        self.assertIsInstance(currency, Currency)

    def test_add(self):
        """
        It adds two money objects
        """
        for amount in [[10, 10, 20], [0, 0, 0], [-10, 10, 0]]:
            with self.subTest():
                money1 = Money(amount[0], self.currency)
                money2 = Money(amount[1], self.currency)
                sum = money1 + money2

                self.assertEqual(amount[2], sum.amount)

    def test_add_fail(self):
        """
        An exception is thrown when adding money with different currencies
        """
        eur = Money(0, Currency('eur'))
        usd = Money(0, Currency('usd'))
        with self.assertRaises(ValueError):
            eur + usd

    def test_subtract(self):
        """
        It subtracts two money objects
        """
        for amount in [[10, 10, 0], [0, 0, 0], [10, 20, -10]]:
            with self.subTest():
                money1 = Money(amount[0], self.currency)
                money2 = Money(amount[1], self.currency)
                difference = money1 - money2

                self.assertEqual(amount[2], difference.amount)

    def test_subtract_fail(self):
        """
        An exception is thrown when subtracting money with different currencies
        """
        eur = Money(0, Currency('eur'))
        usd = Money(0, Currency('usd'))
        with self.assertRaises(ValueError):
            eur - usd

    def test_multiply(self):
        """
        It multiplies two money objects
        """
        for amount in [[10, 10, 100], [0, 0, 0], [10, 0, 0], [-10, 20, -200], [100, 0.5, 50], [333, 1.5, 500]]:
            with self.subTest():
                money = Money(amount[0], self.currency)
                product = money * amount[1]

                self.assertEqual(amount[2], product.amount)

    def test_multiply_fail(self):
        """
        An exception is thrown when multiplying money with invalid operdan
        """
        for operand in [None, '1', '']:
            with self.subTest():
                money = Money(10, self.currency)
                with self.assertRaises(ValueError):
                    money * operand

    def test_equals(self):
        """
        It returns true when two money objects are equal
        """
        money1 = Money(0, self.currency)
        money2 = Money(0, self.currency)

        self.assertTrue(money1 == money2)

    def test_not_equals(self):
        """
        It returns false when two money objects are not equal
        """
        money1 = Money(0, self.currency)
        money2 = Money(10, self.currency)

        self.assertFalse(money1 == money2)

        money1 = Money(0, Currency('EUR'))
        money2 = Money(0, Currency('USD'))

        self.assertFalse(money1 == money2)

    def test_greater_than(self):
        """
        It returns true when money amount is greater than given money object
        """
        money1 = Money(10, self.currency)
        money2 = Money(0, self.currency)

        self.assertTrue(money1 > money2)

    def test_not_greater_than(self):
        """
        It returns false when money amount is less than given money object
        """
        money1 = Money(0, self.currency)
        money2 = Money(10, self.currency)

        self.assertFalse(money1 > money2)

        """
        An exception is thrown when comparing money objects with different currencies
        """
        money1 = Money(0, Currency('EUR'))
        money2 = Money(0, Currency('USD'))

        with self.assertRaises(ValueError):
            self.assertFalse(money1 > money2)

    def test_greater_or_equal_than(self):
        """
        It returns true when money amount is greater or equal to given money object
        """
        money1 = Money(0, self.currency)
        money2 = Money(0, self.currency)

        self.assertTrue(money1 >= money2)

    def test_not_greater_or_equal_than(self):
        """
         It returns false when money amount is less than given money object
        """
        money1 = Money(0, self.currency)
        money2 = Money(10, self.currency)

        self.assertFalse(money1 >= money2)

        """
        An exception is thrown when comparing money objects with different currencies
        """
        money1 = Money(0, Currency('EUR'))
        money2 = Money(0, Currency('USD'))

        with self.assertRaises(ValueError):
            self.assertFalse(money1 >= money2)

    def test_less_than(self):
        """
        It returns true when money amount is less than given money object
        """
        money1 = Money(0, self.currency)
        money2 = Money(10, self.currency)

        self.assertTrue(money1 < money2)

    def test_not_less_than(self):
        """
         It returns false when money amount is not less than given money object
        """
        money1 = Money(10, self.currency)
        money2 = Money(0, self.currency)

        self.assertFalse(money1 < money2)

        """
        An exception is thrown when comparing money objects with different currencies
        """
        money1 = Money(0, Currency('EUR'))
        money2 = Money(0, Currency('USD'))

        with self.assertRaises(ValueError):
            self.assertFalse(money1 < money2)

    def test_less_or_equal_than(self):
        """
        It returns true when money amount is less or equal than given money object
        """
        money1 = Money(0, self.currency)
        money2 = Money(0, self.currency)

        self.assertTrue(money1 <= money2)

    def test_not_less__or_equal_than(self):
        """
        It returns false when money amount is not less or equal than given money object
        """
        money1 = Money(10, self.currency)
        money2 = Money(0, self.currency)

        self.assertFalse(money1 <= money2)

        """
        An exception is thrown when comparing money objects with different currencies
        """
        money1 = Money(0, Currency('EUR'))
        money2 = Money(0, Currency('USD'))

        with self.assertRaises(ValueError):
            self.assertFalse(money1 <= money2)

    def test_allocation(self):
        """
        It allocates money amount to given ratios
        """
        data = [
            # amount, ratios, amount_per_ratio
            [100, [1, 1, 1], [34, 33, 33]],
            [100, [1], [100]],
            [101, [1, 1, 1], [34, 34, 33]],
            [101, [3, 7], [30, 71]],
            [101, [7, 3], [71, 30]],
            [5, [3, 7], [2, 3]],
            [5, [7, 3], [4, 1]],
            [5, [7, 3, 0], [4, 1, 0]],
            [2, [1, 1, 1], [1, 1, 0]],
            [1, [1, 1], [1, 0]],
            [-5, [7, 3], [-3, -2]],
        ]

        for amount, ratios, result in data:
            with self.subTest():
                money = Money(amount, self.currency)
                allocation = money.allocate(ratios)

                for index, money in enumerate(allocation):
                    self.assertEqual(result[index], money.amount)

    def test_allocation_fail(self):
        """
        An exception is thrown when allocation with invalid ratios
        """
        money = Money(10, self.currency)

        with self.assertRaises(ValueError):
            money.allocate([])

        with self.assertRaises(ValueError):
            money.allocate([-1])


if __name__ == '__main__':
    unittest.main()
