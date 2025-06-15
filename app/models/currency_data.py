# Currency rate data model
# app/models/currency_data.py

EXCHANGE_RATES = {
    "USD": 1.0,
    "EUR": 0.92,
    "GBP": 0.78,
    "INR": 83.15,
    "JPY": 156.3,
}

SUPPORTED_CURRENCIES = list(EXCHANGE_RATES.keys())
