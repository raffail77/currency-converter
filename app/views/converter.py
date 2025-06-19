# app/views/converter.py
import tkinter as tk
from tkinter import ttk
from app.services.convert_service import convert_currency
from app.models.currency_data import SUPPORTED_CURRENCIES

class ConverterView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#f0f4f8", padx=20, pady=20)

        self.amount_var = tk.StringVar()
        self.from_currency = tk.StringVar(value='USD')
        self.to_currency = tk.StringVar(value='EUR')
        self.result_var = tk.StringVar()

        self.build_ui()

    def build_ui(self):
        # Amount Label and Entry
        tk.Label(self, text="Amount:", bg="#f0f4f8", font=("Segoe UI", 11)).pack(anchor="w", pady=(10, 2))
        ttk.Entry(self, textvariable=self.amount_var, font=("Segoe UI", 11)).pack(fill='x', pady=(0, 10))

        # From Currency
        tk.Label(self, text="From:", bg="#f0f4f8", font=("Segoe UI", 11)).pack(anchor="w", pady=(10, 2))
        from_menu = ttk.Combobox(self, textvariable=self.from_currency, values=SUPPORTED_CURRENCIES, state="readonly", font=("Segoe UI", 10))
        from_menu.pack(fill='x', pady=(0, 10))

        # To Currency
        tk.Label(self, text="To:", bg="#f0f4f8", font=("Segoe UI", 11)).pack(anchor="w", pady=(10, 2))
        to_menu = ttk.Combobox(self, textvariable=self.to_currency, values=SUPPORTED_CURRENCIES, state="readonly", font=("Segoe UI", 10))
        to_menu.pack(fill='x', pady=(0, 10))

        # Convert Button
        ttk.Button(self, text="Convert", command=self.convert).pack(pady=15)

        # Result Label
        tk.Label(self, textvariable=self.result_var, font=("Segoe UI", 14, "bold"), bg="#f0f4f8", fg="#007acc").pack(pady=(10, 0))

    def convert(self):
        try:
            amount = float(self.amount_var.get())
            result = convert_currency(amount, self.from_currency.get(), self.to_currency.get())
            self.result_var.set(f"{result:.2f} {self.to_currency.get()}")
        except ValueError:
            self.result_var.set("Invalid amount")
        except Exception as e:
            self.result_var.set(str(e))
