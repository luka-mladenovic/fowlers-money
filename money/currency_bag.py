from __future__ import annotations
import yaml
import os


class CurrencyBag:

    @staticmethod
    def load(code: str) -> Optional[dict]:
        """
        Load currency information from currencies list
        """
        currencies = __class__.load_all()

        return currencies.get(code.upper(), None)

    @staticmethod
    def load_all() -> dict:
        """
        Load currency information from the configuration file
        """
        path = os.path.join('config', 'currencies.yaml')

        with open(path, 'r') as currencies_list:
            return yaml.load(currencies_list)
