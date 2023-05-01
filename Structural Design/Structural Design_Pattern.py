import requests
from typing import Dict


# --- Adapter pattern ---

class ExchangeRateAPI:
    def __init__(self, my_url: str):
        self.url = my_url

    def get_rates(self) -> Dict[str, float]:
        data = requests.get(self.url).json()
        return data['rates']


class CurrencyConverter:
    def __init__(self, api: ExchangeRateAPI):
        self.rates = api.get_rates()

    def convert(self, from_currency: str, to_currency: str, amount: float) -> float:
        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]

        # round to two decimal places
        amount = round(amount * self.rates[to_currency], 2)
        return amount


class CurrencyConverterAdapter:
    def __init__(self, my_converter: CurrencyConverter):
        self.converter = my_converter

    def convert_from_eur(self, to_currency: str, amount: float) -> float:
        return self.converter.convert('EUR', to_currency.upper(), amount)


# --- Decorator pattern ---

class CurrencyConverterDecorator:
    def __init__(self, my_converter: CurrencyConverter):
        self.converter = my_converter

    def add_margin(self, my_margin: float):
        for currency, rate in self.converter.rates.items():
            self.converter.rates[currency] = round(rate * (1 + my_margin), 4)


# --- Facade pattern ---

class CurrencyConverterFacade:
    def __init__(self, my_url: str, my_margin: float):
        self.api = ExchangeRateAPI(my_url)
        self.converter = CurrencyConverter(self.api)
        self.decorator = CurrencyConverterDecorator(self.converter)
        self.adapter = CurrencyConverterAdapter(self.converter)
        self.decorator.add_margin(my_margin)

    def convert(self, from_currency: str, to_currency: str, amount: float) -> float:
        return self.adapter.convert_from_eur(to_currency, amount)


class CurrencyConverterApp:
    def __init__(self, my_converter: CurrencyConverterFacade):
        self.converter = my_converter

    def run(self):
        print("Convertor de valută")
        print("Valute disponibile:", self.converter.converter.rates.keys())
        from_currency = input("Introduceți valuta inițială: ")
        to_currency = input("Introduceți valuta de destinație: ")
        amount = float(input("Introduceți suma: "))

        result = self.converter.convert(from_currency.upper(), to_currency.upper(), amount)
        print(f"{amount} {from_currency.upper()} = {result} {to_currency.upper()}")


if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/EUR'
    margin = 0.05
    converter = CurrencyConverterFacade(url, margin)
    app = CurrencyConverterApp(converter)
    app.run()
