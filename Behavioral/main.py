import requests
from typing import Dict
from forex_python.converter import CurrencyRates
import math
from prettytable import PrettyTable


import tkinter as tk
from tkinter import *
import tkinter.messagebox

root = tk.Tk()

root.title("GUI : Currency Conversion")

Tops = Frame(root, bg='#E7C27D', pady=2, width=1600, height=100, relief="ridge")
Tops.grid(row=0, column=0)

headlabel = tk.Label(Tops, font=('lato black', 16, 'bold'), text='TMPS Project     :    Convertor Valutar        ',
                     bg='#E7C27D', fg='black')
headlabel.grid(row=1, column=0, sticky="we")

variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)

variable1.set("selectează")
variable2.set("selectează")


def RealTimeCurrencyConversion():
    from forex_python.converter import CurrencyRates
    conv = CurrencyRates()

    from_mcurrency = variable1.get()
    to_mcurrency = variable2.get()

    if Amount1_field.get() == "":
        tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please a valid amount.")

    elif from_mcurrency == "selecteaza" or to_mcurrency == "selecteaza":
        tkinter.messagebox.showinfo("Error !!",
                                    "Currency Not Selected.\n Please select FROM and TO Currency form menu.")

    else:
        new_amt = conv.convert(from_mcurrency, to_mcurrency, float(Amount1_field.get()))
        new_amount = float("{:.4f}".format(new_amt))
        Amount2_field.insert(0, str(new_amount))


def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)


CurrenyCode_list = ["GBP", "USD", "MDL", "RON", "DKK", "EUR"]

root.configure(background='#e6e5e5')
root.geometry("500x400")

Label_1 = Label(root, font=('lato black', 27, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=1, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Suma:  ", bg="#e6e5e5", fg="black")
label1.grid(row=2, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Valuta inițială:  ", bg="#e6e5e5", fg="black")
label1.grid(row=3, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Valuta de destinație:  ", bg="#e6e5e5", fg="black")
label1.grid(row=4, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Suma convertită:  ", bg="#e6e5e5", fg="black")
label1.grid(row=8, column=0, sticky=W)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=5, column=0, sticky=W)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=7, column=0, sticky=W)

FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list)
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list)

FromCurrency_option.grid(row=3, column=0, ipadx=4, sticky=E)
ToCurrency_option.grid(row=4, column=0, ipadx=4, sticky=E)

Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=0, ipadx=4, sticky=E)

Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=0, ipadx=4, sticky=E)

Label_9 = Button(root, font=('arial', 15, 'bold'), text=" Convertește  ", padx=2, pady=2, bg="grey", fg="black",
                 command=RealTimeCurrencyConversion)
Label_9.grid(row=6, column=0)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=9, column=0, sticky=W)

Label_9 = Button(root, font=('arial', 15, 'bold'), text=" Șterge  ", padx=2, pady=2, bg="white", fg="red",
                 command=clear_all)
Label_9.grid(row=10, column=0)

root.mainloop()


class ExchangeRateAPI:
    def __init__(self, my_url: str):
        self.url = my_url

    def get_rates(self) -> Dict[str, float]:
        data = requests.get(self.url).json()
        return data['rates']


class CurrencyConverter:
    def __init__(self, my_api: ExchangeRateAPI):
        self.rates = my_api.get_rates()

    def convert(self, my_amount: float) -> float:
        if from_currency != 'EUR':
            my_amount = my_amount / self.rates[from_currency]

        # round to two decimal places
        my_amount = round(my_amount * self.rates[to_currency], 2)
        return my_amount


if __name__ == '__main__':
    print("Bun venit la Convertor Valutar !")
    input("Apăsați orice tastă pentru a continua...")

    url = 'https://api.exchangerate-api.com/v4/latest/EUR'
    api = ExchangeRateAPI(url)
    converter = CurrencyConverter(api)

    # Lista valutelor disponibile
    c = CurrencyRates()
    currency_list = list(c.get_rates("").keys())
    currency_list.append('EUR')
    currency_list.append('MDL')
    currency_list.append('UAH')
    currency_list.append('CHW')
    currency_list.sort()

    show_currency_list = input(
        "Doriți să afișați lista de valute disponibile? (da/nu): ")
    if show_currency_list.lower() == "da":
        num_cols = 3
        num_rows = math.ceil(len(currency_list) / num_cols)
        col_width = 25

        print("Lista valutelor disponibile:")
        for i in range(num_rows):
            for j in range(num_cols):
                index = i + j * num_rows
                if index < len(currency_list):
                    print(f"{currency_list[index]:<{col_width}}", end="")
            print("")
    else:
        print("Continuăm conversia valutei...")

    from_currency = input("Introduceți valuta inițială: ")
    to_currency = input("Introduceți valuta de destinație: ")
    amount = float(input("Introduceți suma: "))

    result = converter.convert(amount)

    # Crează un tabel frumos formatat cu rezultatul conversiei valutare
    table = PrettyTable()
    table.field_names = ["Valoarea inițială", "Valuta inițială", "Valoarea convertită", "Valuta convertită"]
    table.add_row([amount, from_currency.upper(), result, to_currency.upper()])

    # Printează tabelul
    print(table)
