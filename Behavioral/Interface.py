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
    c = CurrencyRates()

    from_currency = variable1.get()
    to_currency = variable2.get()

    if Amount1_field.get() == "":
        tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please a valid amount.")

    elif from_currency == "selecteaza" or to_currency == "selecteaza":
        tkinter.messagebox.showinfo("Error !!",
                                    "Currency Not Selected.\n Please select FROM and TO Currency form menu.")

    else:
        new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
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
