# app/main.py
import tkinter as tk
from tkinter import ttk
from app.views.converter import ConverterView


def main():
    root = tk.Tk()
    root.title("Currency Converter by Rafay")
    root.geometry("400x350")
    root.configure(bg="#f0f4f8")  # Match background with converter frame

    # Use a modern theme
    style = ttk.Style()
    style.theme_use('clam')  # Options: 'clam', 'alt', 'default', 'vista'

    # Optional custom styling for ttk widgets (button, combobox, etc.)
    style.configure("TButton", font=("Segoe UI", 10), padding=6)
    style.configure("TCombobox", padding=4)
    style.configure("TEntry", padding=4)

    app = ConverterView(root)
    app.pack(expand=True, fill='both')

    root.mainloop()


if __name__ == "__main__":
    main()
