# ReLU.py

def relu(arg):
    return max(0,arg)

def dif_relu(arg):
    if arg < 0:
        return 0
    elif arg > 0:
        return 1
    else:
        return 0