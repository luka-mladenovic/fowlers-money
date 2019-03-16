import unittest
from money.currency import Currency


class TestCurrency(unittest.TestCase):
    def test_creates_currency(self):
        """
        It creates a new currency object
        """
        Currency('EUR')

    def test_fails_to_create_currency(self):
        """
        An exception is thrown when currency is invalid
        """
        with self.assertRaises(ValueError):
            Currency('foo')

    def test_return_currency_code(self):
        code = 'EUR'
        """
        It returns currency alphabetic code
        """
        currency = Currency(code)
        self.assertEqual(code, currency.code)

    def test_return_currency_name(self):
        code = 'EUR'
        """
        It returns currency name
        """
        currency = Currency(code)
        self.assertEqual('Euro', currency.name)

    def test_return_currency_iso_code(self):
        code = 'EUR'
        """
        It returns currency iso code
        """
        currency = Currency(code)
        self.assertEqual(978, currency.iso_code)

    def test_return_currency_minor_unit(self):
        code = 'EUR'
        """
        It returns currency minor unit
        """
        currency = Currency(code)
        self.assertEqual(2, currency.minor_unit)

    def test_return_currencies_equals(self):
        """
        It returns currency minor unit
        """
        currency1 = Currency('EUR')
        currency2 = Currency('EUR')

        self.assertTrue(currency1.equals(currency2))

    def test_return_currencies_not_equals(self):
        """
        It returns currency minor unit
        """
        currency1 = Currency('EUR')
        currency2 = Currency('USD')

        self.assertFalse(currency1.equals(currency2))


if __name__ == '__main__':
    unittest.main()
