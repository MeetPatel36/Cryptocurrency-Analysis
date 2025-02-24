from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import os
from time import time
from time import sleep

def api_runner():

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'100',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '676af9db-3b37-4a28-9b42-ff0ceba342f1',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        #print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    df = pd.json_normalize(data['data'])
    df['timestamp'] = pd.to_datetime('now')
    df

    if not os.path.isfile(r'C:\Users\Meet Patel\Documents\Python Scripts\API.csv'):
        df.to_csv(r'C:\Users\Meet Patel\Documents\Python Scripts\API.csv', header = 'column_names')
    else:
        df.to_csv(r'C:\Users\Meet Patel\Documents\Python Scripts\API.csv', mode = 'a', header = False)


#Creating time loop:

for i in range(100):
    api_runner()
    print('API Runner Completed')
    sleep(1800) #Sleep for 30 minute
exit()
