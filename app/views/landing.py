# app/views/landing.py

import tkinter as tk

class LandingView(tk.Frame):
    def __init__(self, parent, on_start_callback):
        super().__init__(parent)

        tk.Label(self, text="Welcome to Currency Converter", font=("Arial", 16)).pack(pady=30)
        tk.Button(self, text="Start Converting", command=on_start_callback).pack()
