#%%
import yfinance as yf
import datetime
import pandas as pd
import os

def reader(ticker):

    ticker = str(ticker)
    now = datetime.datetime.now() + datetime.timedelta(days=1)
    start = now - datetime.timedelta(days=360)
    data = yf.download(ticker, start.date().isoformat(), now.date().isoformat(), interval="1d")
    file_name = ticker + ".csv"
    data.to_csv(file_name)
    print(data.head())
    print("-----"*5)
    print(data.tail())
    df = pd.read_csv(file_name)
    os.remove(file_name)

    return df

