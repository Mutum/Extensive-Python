# log.py

import math


def log(x):
    
    """Compute log value of a argument x."""
    
    result = math.log(x)
    print(f'{result}')
    return result


def dif_log(x):
    
    """Compute dirivative of log function of argument x."""
    
    result = 1/x
    print(f'{result}')
    return result
