from core.payoff import call_option
import numpy as np

def expected_payoff(S0,r,t_years,annual_vol,n=10000):
    Z = np.random.normal(0,1,n)
    ST = S0*np.exp((r-0.5*annual_vol**2)*t_years + annual_vol*np.sqrt(t_years)*Z)
    payoffs = call_option()
    discounted = np.exp(-r*t_years) * np.mean(payoffs)
    return discounted,ST

