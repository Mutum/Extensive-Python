# Sigmoid.py

from math import exp

def sigmoid(arg):
    
    """Compute sigmoid function of argument x."""
    
    result = 1/(1+exp(-arg))
    print(f'{result}')
    return result


def dif_sigmoid(arg):
    
    """Compute dirivative of sigmoid function of argument x."""
    
    def sigmoid(arg):
        return 1/(1+exp(-arg))

    result =  sigmoid(arg) * (1- sigmoid(arg))
    print(f'{result}')
    return result