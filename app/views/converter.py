# app/views/converter.py
import tkinter as tk
from tkinter import ttk
from app.services.convert_service import convert_currency
from app.models.currency_data import SUPPORTED_CURRENCIES

class ConverterView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.amount_var = tk.StringVar()
        self.from_currency = tk.StringVar(value='USD')
        self.to_currency = tk.StringVar(value='EUR')
        self.result_var = tk.StringVar()

        self.build_ui()

    def build_ui(self):
        tk.Label(self, text="Amount:").pack(pady=(20, 5))
        tk.Entry(self, textvariable=self.amount_var).pack()

        tk.Label(self, text="From:").pack(pady=(10, 5))
        from_menu = ttk.Combobox(self, textvariable=self.from_currency, values=SUPPORTED_CURRENCIES, state="readonly")
        from_menu.pack()

        tk.Label(self, text="To:").pack(pady=(10, 5))
        to_menu = ttk.Combobox(self, textvariable=self.to_currency, values=SUPPORTED_CURRENCIES, state="readonly")
        to_menu.pack()

        tk.Button(self, text="Convert", command=self.convert).pack(pady=15)

        tk.Label(self, textvariable=self.result_var, font=("Arial", 14, "bold")).pack(pady=10)

    def convert(self):
        try:
            amount = float(self.amount_var.get())
            result = convert_currency(amount, self.from_currency.get(), self.to_currency.get())
            self.result_var.set(f"{result:.2f} {self.to_currency.get()}")
        except ValueError:
            self.result_var.set("Invalid amount")
        except Exception as e:
            self.result_var.set(str(e))
