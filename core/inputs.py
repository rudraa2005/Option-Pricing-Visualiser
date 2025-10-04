import pandas as pd
import numpy as np
from math import erf,sqrt

def get_inputs():
    S0 = float(input("Enter Initial Stock Price:\n"))
    K = float(input("Enter Strike Price:\n"))
    r = float(input("Risk free interest rate:\n"))
    t = float(input("Enter expiration time:\n"))
    t_years = t/252
    return S0,K,r,t,t_years

def get_volatility():
    df = pd.read_csv(r"data/historical_prices.csv")

    df['Close Price'] = pd.to_numeric(df['Close Price'], errors='coerce')  
    close_price = df['Close Price'].dropna().values

    log_returns = np.log(close_price[1:]/close_price[:-1])
    vol = np.std(log_returns)
    annual_vol = vol* np.sqrt(252)
    return annual_vol

def norm_cdf(x):
    return 0.5*(1+erf(x/sqrt(2)))
