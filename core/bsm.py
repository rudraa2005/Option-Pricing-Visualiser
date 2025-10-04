from inputs import get_volatility, norm_cdf
from math import sqrt,exp
import numpy as np

def bsm_model(S0,K,r,t,t_years,annual_vol):
    d1 = (np.log(S0/K) + (r+ ((annual_vol**2)/2))*t_years)/(annual_vol*sqrt(t_years))
    d2 = d1 - annual_vol * sqrt(t_years)   
    
    C = S0* norm_cdf(d1) - K*exp(-r*t)*norm_cdf(d2)
    return C 
