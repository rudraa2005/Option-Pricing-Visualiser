'''from core.inputs import get_inputs, get_volatility, norm_cdf
from core.bsm import bsm_model
from core.payoff import call_option'''
import pandas as pd
from math import exp
import matplotlib.pyplot as plt
import sys
from pathlib import Path

backend_path = Path(__file__).parent/"core"
sys.path.insert(0,str(backend_path))

from inputs import get_inputs, get_volatility
from bsm import bsm_model
from payoff import call_option

S0, K, r,t, t_years = get_inputs()
annual_vol = get_volatility()

C = bsm_model(S0, K, r, t,t_years, annual_vol)
print(f"BSM Call Price: {C:.2f}")

df = pd.read_csv(r"data/historical_prices.csv")
prices = df['Close Price'].dropna().values

payoffs = [max(ST - K, 0) for ST in prices]
discounted_payoffs = [exp(-r*t_years)*p for p in payoffs]

print("First 10 discounted payoffs:", discounted_payoffs[:10])


plt.plot(prices, discounted_payoffs, label="Discounted Payoff")
plt.axhline(C, color='red', linestyle='--', label="BSM Price")
plt.xlabel("Stock Price")
plt.ylabel("Payoff / Price")
plt.title("Option Payoff vs Stock Price")
plt.legend()
plt.show()

# 6. Save results
df['Payoff'] = payoffs
df['Discounted_Payoff'] = discounted_payoffs
df.to_csv("payoff_results.csv", index=False)