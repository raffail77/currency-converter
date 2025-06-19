import unittest
import tkinter as tk
from unittest.mock import patch
from app.views.converter import ConverterView

class TestConverterView(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.converter = ConverterView(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch('app.views.converter.convert_currency')
    def test_valid_conversion(self, mock_convert):
        # Arrange
        self.converter.amount_var.set("100")
        self.converter.from_currency.set("USD")
        self.converter.to_currency.set("EUR")
        mock_convert.return_value = 90.0  # expected converted value

        # Act
        self.converter.convert()

        # Assert
        self.assertEqual(self.converter.result_var.get(), "90.00 EUR")

    def test_invalid_amount(self):
        # Arrange
        self.converter.amount_var.set("abc")  # Not a float

        # Act
        self.converter.convert()

        # Assert
        self.assertEqual(self.converter.result_var.get(), "Invalid amount")

    @patch('app.views.converter.convert_currency')
    def test_conversion_exception(self, mock_convert):
        # Arrange
        self.converter.amount_var.set("100")
        mock_convert.side_effect = Exception("Conversion Error")

        # Act
        self.converter.convert()

        # Assert
        self.assertEqual(self.converter.result_var.get(), "Conversion Error")

if __name__ == "__main__":
    unittest.main()
