import requests
from typing import Dict


# Clasele din Bridge pattern
class ExchangeRateAPI:

    def __init__(self, my_url: str):
        self.url = my_url

    def get_rates(self) -> Dict[str, float]:
        data = requests.get(self.url).json()
        return data['rates']


class CurrencyConverterImplementation:

    def __init__(self, rates: Dict[str, float]):
        self.rates = rates

    def add_margin(self, _margin: float, rates: Dict[str, float]):
        for currency in rates.keys():
            rates[currency] *= (1 + _margin)
        self.rates = rates

    def convert(self, from_currency: str, to_currency: str,
                amount: float) -> float:
        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]

        # Rotunjeste la doua zecimale
        amount = round(amount * self.rates[to_currency], 2)
        return amount


class CurrencyConverterInterface:

    def __init__(self):
        self.rates = None

    def convert(self, from_currency: str, to_currency: str,
                amount: float) -> float:
        pass


class CurrencyConverterFacade(CurrencyConverterInterface):

    def __init__(self, my_url: str, my_margin: float):
        super().__init__()
        self.api = ExchangeRateAPI(my_url)
        self.rates = self.api.get_rates()
        self.decorator = CurrencyConverterDecorator(self.rates, my_margin)

    def convert(self, from_currency: str, to_currency: str,
                amount: float) -> float:
        my_converter = CurrencyConverterImplementation(self.rates)
        return self.decorator.decorate(my_converter, from_currency, to_currency,
                                       amount)


class CurrencyConverterDecorator:

    def __init__(self, rates: Dict[str, float], my_margin: float):
        self.rates = rates
        self.margin = my_margin

    def decorate(self, my_converter: CurrencyConverterImplementation,
                 from_currency: str, to_currency: str, amount: float) -> float:
        my_converter.add_margin(self.margin, self.rates)
        return my_converter.convert(from_currency.upper(), to_currency.upper(),
                                    amount)


class CurrencyConverterApp:

    def __init__(self, my_converter: CurrencyConverterInterface):
        self.converter = my_converter

    def run(self):
        print("Convertor de valută")
        print("Valute disponibile:", self.converter.rates.keys())
        from_currency = input("Introduceți valuta inițială: ")
        to_currency = input("Introduceți valuta de destinație: ")
        amount = float(input("Introduceți suma: "))

        result = self.converter.convert(from_currency.upper(), to_currency.upper(),
                                        amount)
        print(f"{amount} {from_currency.upper()} = {result} {to_currency.upper()}")


if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/EUR'
    margin = 0.05
    converter = CurrencyConverterFacade(url, margin)
    app = CurrencyConverterApp(converter)
    app.run()
