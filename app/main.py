import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Sample exchange rates (for demonstration)
exchange_rates = {
    'USD': {'EUR': 0.85, 'GBP': 0.72, 'JPY': 110.25, 'AUD': 1.29, 'CAD': 1.21, 'CNY': 6.40, 'INR': 74.85, 'AED': 3.67,
            'PKR': 177.50},
    'EUR': {'USD': 1.18, 'GBP': 0.85, 'JPY': 130.50, 'AUD': 1.52, 'CAD': 1.42, 'CNY': 7.53, 'INR': 88.00, 'AED': 4.30,
            'PKR': 207.00},
    'GBP': {'USD': 1.39, 'EUR': 1.18, 'JPY': 153.00, 'AUD': 1.90, 'CAD': 1.70, 'CNY': 9.00, 'INR': 100.00, 'AED': 5.00,
            'PKR': 250.00},
    'JPY': {'USD': 0.0091, 'EUR': 0.0077, 'GBP': 0.0065, 'AUD': 0.012, 'CAD': 0.011, 'CNY': 0.061, 'INR': 0.73,
            'AED': 0.036, 'PKR': 1.62},
    'AUD': {'USD': 0.78, 'EUR': 0.66, 'GBP': 0.53, 'JPY': 83.00, 'CAD': 0.93, 'CNY': 4.90, 'INR': 57.00, 'AED': 2.80,
            'PKR': 140.00},
    'CAD': {'USD': 0.83, 'EUR': 0.70, 'GBP': 0.59, 'JPY': 80.00, 'AUD': 1.07, 'CNY': 5.20, 'INR': 62.00, 'AED': 3.00,
            'PKR': 150.00},
    'CNY': {'USD': 0.16, 'EUR': 0.13, 'GBP': 0.11, 'JPY': 16.40, 'AUD': 0.20, 'CAD': 0.19, 'INR': 12.00, 'AED': 0.60,
            'PKR': 30.00},
    'INR': {'USD': 0.013, 'EUR': 0.011, 'GBP': 0.010, 'JPY': 1.37, 'AUD': 0.017, 'CAD': 0.016, 'CNY': 0.083,
            'AED': 0.045, 'PKR': 0.50},
    'AED': {'USD': 0.27, 'EUR': 0.23, 'GBP': 0.20, 'JPY': 27.50, 'AUD': 0.36, 'CAD': 0.34, 'CNY': 1.80, 'INR': 22.00,
            'PKR': 110.00},
    'PKR': {'USD': 0.0056, 'EUR': 0.0048, 'GBP': 0.0040, 'JPY': 0.62, 'AUD': 0.0071, 'CAD': 0.0067, 'CNY': 0.033,
            'INR': 2.00, 'AED': 0.0091},
}


class AnimatedBackground(tk.Canvas):
    def __init__(self, parent, colors, width=400, height=350):
        super().__init__(parent, width=width, height=height, highlightthickness=0)
        self.colors = colors
        self.width = width
        self.height = height
        self.current_color = 0
        self.percent = 0
        self.rect = self.create_rectangle(0, 0, width, height, fill=colors[0], outline="")
        self.animate()

    def animate(self):
        self.percent += 0.005
        if self.percent >= 1:
            self.percent = 0
            self.current_color = (self.current_color + 1) % len(self.colors)
            next_color = self.colors[(self.current_color + 1) % len(self.colors)]
            self.itemconfig(self.rect, fill=next_color)

        # Smooth gradient transition
        r1, g1, b1 = [int(self.colors[self.current_color][i:i + 2], 16) for i in (1, 3, 5)]
        r2, g2, b2 = [int(self.colors[(self.current_color + 1) % len(self.colors)][i:i + 2], 16) for i in (1, 3, 5)]

        r = int(r1 + (r2 - r1) * self.percent)
        g = int(g1 + (g2 - g1) * self.percent)
        b = int(b1 + (b2 - b1) * self.percent)

        new_color = f"#{r:02x}{g:02x}{b:02x}"
        self.itemconfig(self.rect, fill=new_color)
        self.after(20, self.animate)


class CurrencyConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Currency Converter by Rafay")
        self.geometry("400x350")
        self.resizable(False, False)

        # Set font defaults
        self.option_add("*Font", "Poppins 10")

        # Create animated background
        self.bg_colors = ["#ee7752", "#e73c7e", "#23a6d5", "#23d5ab"]
        self.background = AnimatedBackground(self, self.bg_colors)
        self.background.pack(fill="both", expand=True)

        # Create main container
        self.container = tk.Frame(self.background, bg="white", bd=0)
        self.container.place(relx=0.5, rely=0.5, anchor="center", width=380, height=320)

        # Create inner frame for content
        self.inner_frame = tk.Frame(self.container, bg="#ffffff")
        self.inner_frame.place(relx=0.5, rely=0.5, anchor="center", width=360, height=300)

        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = tk.Label(self.inner_frame, text="Currency Converter",
                               font=("Poppins", 16, "bold"), bg="#ffffff")
        title_label.pack(pady=8)

        subtitle = tk.Label(self.inner_frame, text="Convert between 150+ currencies in real-time",
                            font=("Poppins", 9), bg="#ffffff", fg="#555555")
        subtitle.pack(pady=(0, 10))

        # Amount Entry
        amount_frame = tk.Frame(self.inner_frame, bg="#ffffff")
        amount_frame.pack(pady=8)
        tk.Label(amount_frame, text="Amount:", bg="#ffffff").pack(side=tk.LEFT, padx=(0, 5))
        self.amount_var = tk.DoubleVar(value=1.0)
        self.amount_entry = ttk.Entry(amount_frame, textvariable=self.amount_var,
                                      font=("Poppins", 12), width=12)
        self.amount_entry.pack(side=tk.LEFT)

        # Currency selectors
        currency_frame = tk.Frame(self.inner_frame, bg="#ffffff")
        currency_frame.pack(pady=10, fill="x", padx=20)

        # From currency
        from_frame = tk.Frame(currency_frame, bg="#ffffff")
        from_frame.pack(side=tk.LEFT, fill="x", expand=True)
        tk.Label(from_frame, text="From:", bg="#ffffff").pack(anchor="w")

        self.from_currency_var = tk.StringVar(value="USD")
        from_options = [
            "USD - US Dollar",
            "EUR - Euro",
            "GBP - British Pound",
            "JPY - Japanese Yen",
            "AUD - Australian Dollar",
            "CAD - Canadian Dollar",
            "CNY - Chinese Yuan",
            "INR - Indian Rupee",
            "AED - Emirati Dirham",
            "PKR - Pakistani Rupee"
        ]
        self.from_currency = ttk.Combobox(
            from_frame,
            textvariable=self.from_currency_var,
            values=from_options,
            state="readonly",
            width=18
        )
        self.from_currency.current(0)
        self.from_currency.pack(pady=5, fill="x")

        # Swap button
        swap_btn = tk.Button(currency_frame, text="↕", command=self.swap_currencies,
                             bg="#4f46e5", fg="white", bd=0, width=3, height=1,
                             activebackground="#4338ca")
        swap_btn.pack(side=tk.LEFT, padx=5, pady=20)

        # To currency
        to_frame = tk.Frame(currency_frame, bg="#ffffff")
        to_frame.pack(side=tk.LEFT, fill="x", expand=True)
        tk.Label(to_frame, text="To:", bg="#ffffff").pack(anchor="w")

        self.to_currency_var = tk.StringVar(value="EUR")
        to_options = from_options.copy()
        self.to_currency = ttk.Combobox(
            to_frame,
            textvariable=self.to_currency_var,
            values=to_options,
            state="readonly",
            width=18
        )
        self.to_currency.current(1)
        self.to_currency.pack(pady=5, fill="x")

        # Convert button
        convert_btn = tk.Button(self.inner_frame, text="Convert Currency",
                                command=self.convert, bg="#4f46e5", fg="white",
                                bd=0, padx=20, pady=5, activebackground="#4338ca")
        convert_btn.pack(pady=15)

        # Result display
        self.result_frame = tk.Frame(self.inner_frame, bg="#ffffff", bd=1)
        self.result_frame.pack(fill="x", padx=20, pady=5)

        self.result_var = tk.StringVar()
        self.result_label = tk.Label(self.result_frame, textvariable=self.result_var,
                                     font=("Poppins", 14, "bold"), bg="#ffffff")
        self.result_label.pack(pady=5)

        self.rate_var = tk.StringVar()
        self.rate_label = tk.Label(self.result_frame, textvariable=self.rate_var,
                                   font=("Poppins", 8), bg="#ffffff", fg="#555555")
        self.rate_label.pack(pady=(0, 5))

        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set(f"Last updated: {datetime.now().strftime('%H:%M:%S')}")
        status = tk.Label(self.inner_frame, textvariable=self.status_var,
                          font=("Poppins", 8), bg="#ffffff", fg="#555555")
        status.pack(side=tk.BOTTOM, pady=5)

    def swap_currencies(self):
        from_val = self.from_currency_var.get()
        to_val = self.to_currency_var.get()
        self.from_currency_var.set(to_val)
        self.to_currency_var.set(from_val)
        self.convert()

    def convert(self):
        try:
            amount = float(self.amount_var.get())
            if amount <= 0:
                messagebox.showerror("Error", "Please enter a positive amount")
                return

            from_curr = self.from_currency_var.get()[:3]
            to_curr = self.to_currency_var.get()[:3]

            if from_curr == to_curr:
                result = f"{amount:.2f} {from_curr} = {amount:.2f} {to_curr}"
                rate = f"1 {from_curr} = 1 {to_curr}"
            else:
                converted = amount * exchange_rates[from_curr][to_curr]
                result = f"{amount:.2f} {from_curr} = {converted:.2f} {to_curr}"
                rate = f"1 {from_curr} = {exchange_rates[from_curr][to_curr]:.4f} {to_curr}"

            self.result_var.set(result)
            self.rate_var.set(rate)
            self.status_var.set(f"Last updated: {datetime.now().strftime('%H:%M:%S')}")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed: {str(e)}")

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = CurrencyConverter()
    app.run()