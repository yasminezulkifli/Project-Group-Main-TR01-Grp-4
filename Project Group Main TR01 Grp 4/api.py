from xml.dom import UserDataHandler
from forex_python.converter import CurrencyRates 
currency = CurrencyRates()
print(currency.get_rates('USD'))

import requests
import json 
api_key = "VW2YB37U2F0K0NDE"
url =f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"

function = "CURRENCY_EXCHANGE_RATE"
from_currency = "USD"

to_currency = "SGD"

to_currency = "SGD" 
"""
required
"""

response = requests.get(url)
print(response)
print(response.json())
exchange_rate = response.json()



