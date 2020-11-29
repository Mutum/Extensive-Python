# sin.py

import math


def sin(x):
    
    """Compute sine function of argument x."""
    
    result = math.sin(x)
    print(f'{result}')
    return result


def dif_sine(x):
    
    """Compute dirivative of sine function of argument x."""
    
    result = math.cos(x)
    print(f'{result}')
    return result
