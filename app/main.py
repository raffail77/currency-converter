# app/main.py
import tkinter as tk
from app.views.converter import ConverterView


def main():
    root = tk.Tk()
    root.title("Currency Converter")
    root.geometry("400x300")

    app = ConverterView(root)
    app.pack(expand=True, fill='both')

    root.mainloop()


if __name__ == "__main__":
    main()
