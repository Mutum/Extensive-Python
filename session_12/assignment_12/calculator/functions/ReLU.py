# ReLU.py

def relu(x):
    
    """Compute relu value of a argument x."""
    
    result = max(0,x)
    print(f'{result}')
    return result

def dif_relu(x):
    
    """Compute dirivative of relu function of argument x."""
    
    if type(x) == float or type(x) == int :
        
        if x < 0:
            print(f'{0}')
            return 0
        elif x > 0:
            print(f'{1}')
            return 1
        else:
            print(f'{0}')
            return 0
    else:
              
        raise ValueError('Input float or int')