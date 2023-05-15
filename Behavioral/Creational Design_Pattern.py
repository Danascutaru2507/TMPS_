import requests
from typing import Dict
from forex_python.converter import CurrencyRates
import math
from abc import ABC, abstractmethod


class ExchangeRateAPI:

    def __init__(self, my_url: str):
        self.url = my_url

    def get_rates(self) -> Dict[str, float]:
        data = requests.get(self.url).json()
        return data['rates']


class CurrencyConverter:

    def __init__(self, my_api: ExchangeRateAPI):
        self.rates = my_api.get_rates()

    def convert(self, from_currency: str, to_currency: str,
                amount: float) -> float:
        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]

        # round to two decimal places
        amount = round(amount * self.rates[to_currency], 2)
        return amount


# Factory Method pattern implementation
class CurrencyConverterFactory(ABC):

    @abstractmethod
    def create_currency_converter(self):
        pass


class CurrencyConverterFactoryMethod(CurrencyConverterFactory):

    def __init__(self, my_api: ExchangeRateAPI):
        self.api = my_api

    def create_currency_converter(self):
        return CurrencyConverter(self.api)


# Abstract Factory pattern implementation
class CurrencyConverterAbstractFactory(ABC):

    @abstractmethod
    def create_exchange_rate_api(self) -> ExchangeRateAPI:
        pass

    @abstractmethod
    def create_currency_converter(self) -> CurrencyConverter:
        pass


class ExchangeRateAPIFactoryEUROnly(CurrencyConverterAbstractFactory):

    def create_exchange_rate_api(self) -> ExchangeRateAPI:
        return ExchangeRateAPI('https://api.exchangerate-api.com/v4/latest/EUR')

    def create_currency_converter(self) -> CurrencyConverter:
        api = self.create_exchange_rate_api()
        converter = CurrencyConverter(api)
        return converter


class ExchangeRateAPIFactoryAll(CurrencyConverterAbstractFactory):

    def __init__(self, my_url: str):
        self.api_url = my_url

    def create_exchange_rate_api(self) -> ExchangeRateAPI:
        return ExchangeRateAPI(self.api_url)

    def create_currency_converter(self) -> CurrencyConverter:
        api = self.create_exchange_rate_api()
        converter = CurrencyConverter(api)
        return converter


# Singleton pattern implementation
class CurrencyRatesSingleton:
    __instance = None

    def __init__(self):
        if CurrencyRatesSingleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            CurrencyRatesSingleton.__instance = CurrencyRates()

    @staticmethod
    def get_instance():
        if not CurrencyRatesSingleton.__instance:
            CurrencyRatesSingleton()
        return CurrencyRatesSingleton.__instance


def run():
    print("Bun venit la Convertor Valutar !")
    input("Apăsați orice tastă pentru a continua...")

    show_currency_list = input(
        "Doriți să afișați lista de valute disponibile? (da/nu): ")
    if show_currency_list.lower() == "da":
        # Currency list using Singleton pattern
        c = CurrencyRatesSingleton.get_instance()
        currency_list = list(c.get_rates("").keys())
        currency_list.append('EUR')
        currency_list.append('MDL')
        currency_list.append('UAH')
        currency_list.append('CHW')
        currency_list.sort()

        num_cols = 3
        math.ceil(len(currency_list) / num_cols)
        math.floor(80 / num_cols)


class CurrencyConverterApp:

    def __init__(self, my_converter: CurrencyConverter):
        self.converter = my_converter
