from forex_python.converter import CurrencyRates, CurrencyCodes

c = CurrencyRates()
currency_codes = CurrencyCodes()

amount = int(input("Enter The Amount: "))
from_currency = input("From Currency Code: ").upper()
to_currency = input("To Currency Code: ").upper()

# Check if the entered currency codes are valid
if not currency_codes.get_currency_name(from_currency) or not currency_codes.get_currency_name(to_currency):
    print("Invalid currency code(s). Please check and try again.")
else:
    print(f"Convert {amount} {from_currency} to {to_currency}")

    result = c.convert(from_currency, to_currency, amount)

    print(f"Converted Amount Is {result}")
