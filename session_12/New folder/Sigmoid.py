# Sigmoid.py

from math import exp

def sigmoid(arg):
    return 1/(1+exp(-arg))

def dif_relu(arg):
    return sigmoid(arg) * (1- sigmoid(arg))