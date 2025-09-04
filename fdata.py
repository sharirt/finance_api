import pandas_datareader.data as web
import pandas as pd
import numpy as np
import datetime as dt
import yfinance as yf

import pandas_datareader.data as web
import pandas as pd
import numpy as np
import datetime as dt
import yfinance as yf
import requests
from io import StringIO

def get_SP500(end_date=None, start_date=None, interval='1d'):
    """
    
    """
    if end_date == None:
        end_date = dt.date.today().strftime('%Y-%m-%d')
    if start_date == None:
        start_date = pd.to_datetime(end_date)-pd.DateOffset(365*5)


    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

    header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
    }

    r = requests.get(url, headers=header)

    sp500 = pd.read_html(StringIO(r.text))[0]
    
    sp500['Symbol'] = sp500['Symbol'].str.replace('.', '-')

    symbols_list = sp500['Symbol'].unique().tolist()

    df = yf.download(tickers=symbols_list,
                    start=start_date,
                    end=end_date,
                    interval=interval).stack()

    df.index.names = ['date', 'ticker']

    df.columns = df.columns.str.lower()

    return df
