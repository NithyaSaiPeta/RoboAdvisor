import yfinance as yf
import pandas as pd

def load_price_data(tickers, start="2015-01-01"):
    print(tickers)
    data = yf.download(tickers, start=start, auto_adjust=False)
    data = data["Adj Close"]
    data = data.dropna()
    return data


def compute_returns(price_data):
    returns = price_data.pct_change().dropna()
    return returns
