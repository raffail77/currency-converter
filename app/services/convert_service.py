# app/services/convert_service.py
from app.models.currency_data import EXCHANGE_RATES

def convert_currency(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount

    if from_currency not in EXCHANGE_RATES or to_currency not in EXCHANGE_RATES:
        raise ValueError("Unsupported currency")

    # Convert to USD first, then to target
    amount_in_usd = amount / EXCHANGE_RATES[from_currency]
    converted = amount_in_usd * EXCHANGE_RATES[to_currency]
    return converted
