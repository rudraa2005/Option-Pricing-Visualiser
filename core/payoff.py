import numpy as np

def call_option(ST,K):
    return np.maximum(ST-K,0)
def put_option(ST,K):
    return np.maximum(K-ST,0)
