# tan.py

import math


def tan(arg):
    
    """Compute tan function of argument x."""
    
    result = math.tan(arg)
    print(f'{result}')
    return result

def dif_tan(arg):
    
    """Compute dirivative of tan function of argument x."""
    
    result = 1 / math.cos(arg)*2
    print(f'{result}')
    return result
