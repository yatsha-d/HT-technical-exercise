import requests # to allow sending of HTTP requests
import pandas as pd # to create and use dataframes

api_key = '124fd2cccfb1ce22ea4502a0' # I signed up to ExchangeRate-API.com and got a free API key
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/GBP" # url to get latest GBP using the API key

currencies = ["AUD", "CAD", "CHF", "CNH", "EUR", "QAR", "HKD", "JPY", "NZD", "USD"] # list of currencies we want to convert to GBP

try: # lets us test if the API key is working
    response = requests.get(url)
    data = response.json()

    if data['result'] == "success": # check if the API request is successful

        rates = data['conversion_rates']
        filtered_rates = {cur: rates[cur] for cur in currencies if cur in rates} # filter ti the currencues we want
        rates_df = pd.DataFrame(list(filtered_rates.items()), columns=['Currency', 'Rate to GBP']) # prepare data for CSV

        rates_df.to_csv('Currency_rates_to_gbp.csv', index=False) # save to CSV
        print("Currency conversion rates saved to currency_rates_to_gbp.csv") # message to say the currency conversion rates were gathered successfully
    else:
        print("Failed to fetch currency rates")
except Exception as e:
    print(f"An error occurred: {e}")
    