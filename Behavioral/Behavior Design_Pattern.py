import argparse
from abc import ABC, abstractmethod
from typing import Dict

import requests
from forex_python.converter import CurrencyRates


class ExchangeRateAPI(ABC):
    @abstractmethod
    def get_rates(self) -> Dict[str, float]:
        pass


class ExchangeRateAPIImplementation(ExchangeRateAPI):
    def __init__(self, my_url: str):
        self.url = my_url

    def get_rates(self) -> Dict[str, float]:
        data = requests.get(self.url).json()
        return data.get('rates', {})


class ExchangeRateAPIObserver(ExchangeRateAPI):
    def __init__(self, my_api: ExchangeRateAPI):
        self.api = my_api
        self.observers = set()

    def get_rates(self) -> Dict[str, float]:
        rates = self.api.get_rates()
        for observer in self.observers:
            observer.notify(rates)
        return rates

    def add_observer(self, observer):
        self.observers.add(observer)

    def remove_observer(self, observer):
        self.observers.discard(observer)


class CurrencyConverter:
    def __init__(self, my_api: ExchangeRateAPI):
        self.api = my_api
        self.rates = self.api.get_rates()

    def convert(self, from_mcurrency: str, to_mycurrency: str, my_amount: float) -> float:
        if from_mcurrency not in self.rates:
            raise ValueError(f"'{from_mcurrency}' is not a valid currency.")
        if to_mycurrency not in self.rates:
            raise ValueError(f"'{to_mycurrency}' is not a valid currency.")

        if from_mcurrency != 'EUR':
            my_amount = my_amount / self.rates[from_mcurrency]

        # round to two decimal places
        my_amount = round(my_amount * self.rates[to_mycurrency], 2)
        return my_amount


class CurrencyConverterProxy(CurrencyConverter):
    def __init__(self, my_api: ExchangeRateAPI):
        super().__init__(my_api)
        self.converter = None

    def convert(self, from_mcurrency: str, to_mycurrency: str, my_amount: float) -> float:
        if self.converter is None:
            self.converter = CurrencyConverter(self.api)

        return self.converter.convert(from_mcurrency, to_mycurrency, my_amount)


class Observer:
    @abstractmethod
    def notify(self, rates: Dict[str, float]):
        pass


class CurrencyListPrinterObserver(Observer):
    def __init__(self, my_currency_list: list):
        self.currency_list = my_currency_list

    def notify(self, rates: Dict[str, float]):
        print("Lista valutelor disponibile:")
        for my_currency in self.currency_list:
            if my_currency in rates:
                print(my_currency)


if __name__ == '__main__':
    print("Bun venit la Convertor Valutar !")
    input("Apăsați orice tastă pentru a continua...")

    parser = argparse.ArgumentParser(description='Convertor Valutar')
    parser.add_argument('--show-currencies', action='store_true', help='Afiseaza lista de valute disponibile.')
    args = parser.parse_args()

    url = 'https://api.exchangerate-api.com/v4/latest/EUR'
    api = ExchangeRateAPIObserver(ExchangeRateAPIImplementation(url))
    converter = CurrencyConverterProxy(api)

    if args.show_currencies:
        c = CurrencyRates()
        currency_list = list(c.get_rates("").keys())
        currency_list.extend(['EUR', 'MDL', 'UAH', 'CHW'])
        currency_list.sort()

        print("Lista valutelor disponibile:")
        for i, currency in enumerate(currency_list):
            if i % 8 == 0:
                print()
            if currency in api.get_rates():
                print(f"{currency:<10}", end='')
        print('\n')

        while True:
            try:
                from_currency = input("Introduceți codul valutei de pornire: ")
                to_currency = input("Introduceți codul valutei dorite: ")
                amount = float(input("Introduceți suma: "))
                converted_amount = converter.convert(from_currency.upper(), to_currency.upper(), amount)
                print(f"{amount:.2f} {from_currency.upper()} = {converted_amount:.2f} {to_currency.upper()}")
            except ValueError as e:
                print(str(e))
            except KeyboardInterrupt:
                print("\nAplicația a fost oprită.")
                break
