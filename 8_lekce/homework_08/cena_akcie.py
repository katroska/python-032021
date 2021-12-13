import yfinance as yf
import pandas as pd

csco = yf.Ticker("CSCO")
csco_df = csco.history(period="5y")
print(csco_df.describe())

csco_clone = csco_df["Close"]
