# cos.py

import math


def cos(x):
    
    """Compute cosine value of a argument x."""
    
    result = math.cos(x)
    print(f'{result}')
    return result

def dif_cosine(arg):
    
    """Compute dirivative of cosine function of argument x."""
    
    result = -math.sin(arg)
    print(f'{result}')
    return result

# from package.functions import expo

# expo.exp(12)

