from xml.dom import UserDataHandler
from forex_python.converter import CurrencyRates 

import requests
import json 
api_key = "VW2YB37U2F0K0NDE"
url =f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"

function = "CURRENCY_EXCHANGE_RATE"
from_currency = "USD"
to_currency = "SGD"

def api_function():
    response = requests.get(url)
    data = response.json()
    
     #to check if the response is good to go
    if response.status_code == 200: 
        data = response.json()

        for key, value in data['Realtime Currency Exchange Rate'].items():
            if "Exchange Rate" in key: 
                exchange_rate = value 

    else: 
        print("There is an error with your request.")

api_function() 








