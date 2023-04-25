import requests
from typing import Dict

class ExchangeRateAPI:
    def __init__(self, url: str):
        self.url = url

    def get_rates(self) -> Dict[str, float]:
        data = requests.get(self.url).json()
        return data['rates']


class CurrencyConverter:
    def __init__(self, api: ExchangeRateAPI):
        self.rates = api.get_rates()

    def convert(self, from_currency: str, to_currency: str, amount: float) -> float:
        initial_amount = amount
        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]

        # round to two decimal places
        amount = round(amount * self.rates[to_currency], 2)
        return amount


class CurrencyConverterApp:
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def run(self):
        print("Convertor de valută")
        print("Valute disponibile:", self.converter.rates.keys())
        from_currency = input("Introduceți valuta inițială: ")
        to_currency = input("Introduceți valuta de destinație: ")
        
       
        amount = float(input("Introduceți suma: "))

        result = self.converter.convert(from_currency.upper(), to_currency.upper(), amount)
        print(f"{amount} {from_currency.upper()} = {result} {to_currency.upper()}")


if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/EUR'
    api = ExchangeRateAPI(url)
    converter = CurrencyConverter(api)
    app = CurrencyConverterApp(converter)
    app.run()
