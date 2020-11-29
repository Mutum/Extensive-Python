# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 01:58:50 2020

@author: Mutum
"""

from ..functions.Cos import dif_cosine as cos
from ..functions.exp import dif_expo as exp
from ..functions.log import dif_log as log
from ..functions.ReLU import dif_relu as relu
from ..functions.Sigmoid import dif_sigmoid as sigmoid
from ..functions.sin import dif_sine as sin
# from package.functions.SoftMax import softmax
from ..functions.tan import dif_tan as tan
#from ..functions.tan import dif_tanh as tanh
from ..functions.SoftMax import softmax_diff as softmax


__all__ = ['cos' ,
            'exp',
            'log',
            'relu',
            'sigmoid',
            'sin',
            'softmax',
            'tan',
            'tanh' ]
