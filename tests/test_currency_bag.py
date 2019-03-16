import unittest
from money.currency_bag import CurrencyBag


class TestCurrencyBag(unittest.TestCase):
    def test_currencies_loaded(self):
        """
        Test that it can load a currency list
        """
        self.assertIsInstance(
            CurrencyBag.load_all(),
            dict)

    def test_currency_loaded(self):
        """
        Test that it can load a currency from configuration file
        """
        self.assertIsInstance(
            CurrencyBag.load('eur'),
            dict)

    def test_none_is_returned(self):
        """
        None is returned when currency is not in the configuration file
        """
        self.assertIsNone(
            CurrencyBag.load('foo'))


if __name__ == '__main__':
    unittest.main()
