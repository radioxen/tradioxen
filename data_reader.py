#%%
import yfinance as yf
import datetime
import pandas as pd
import os

def reader(ticker="TSLA", delay=0, interval="1d"):

  if interval == "1d":
    days = 500
  elif interval == "90m":
    days = 60
  elif interval == "60m":
    days = 60
  elif interval == "30m":
    days = 60
  elif interval == "15m":
    days = 30
  else:
    days = 7

  ticker = str(ticker).capitalize()
  now = datetime.datetime.now() + datetime.timedelta(days=1)
  start = now - datetime.timedelta(days=days)
  data = yf.download(ticker, start.date().isoformat(), now.date().isoformat(), interval=interval)
  file_name = ticker + ".csv"
  data.to_csv(file_name)
  df = pd.read_csv(file_name)
  if delay:
    df = df.drop(df.tail(delay).index)
  else:
    print(df.head())
    print(df.tail())
  return df, ticker




