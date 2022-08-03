from xml.dom import UserDataHandler
from forex_python.converter import CurrencyRates 
currency = CurrencyRates()
print(currency.get_rates('USD'))

import requests
import json 
api_key = "VW2YB37U2F0K0NDE"
url =f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"

def api_function():
    function = "CURRENCY_EXCHANGE_RATE"
    from_currency = "USD"
    to_currency = "SGD"
    response = requests.get(url)
    exchange_rate = -1
    
     #to check if the response is good to go
    if response.status_code == 200: 
        data = response.json()

        for key, value in data['Realtime Currency Excahne Rate'].items():
            if "Exchange Rate" in key: 
                exchange_rate = value 

    else: 
        print("There is an error with your request.")

api_function() 








