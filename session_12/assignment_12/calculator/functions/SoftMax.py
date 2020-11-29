# softmax.py
import numpy as np

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    result =  np.exp(x) / np.sum(np.exp(x), axis=0) 
    print(f'{result}')
    return result


def softmax_diff(s):
    """Compute derivative of softmax function."""
    jacobian_m = np.diag(s)
    for i in range(len(jacobian_m)):
        for j in range(len(jacobian_m)):
            if i == j:
                jacobian_m[i][j] = s[i] * (1-s[i])
            else: 
                jacobian_m[i][j] = -s[i]*s[j]
    return jacobian_m