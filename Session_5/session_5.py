# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 15:56:48 2020

@author: Mutum
"""
import time
from math import sqrt

def time_it(fn,*args,repetitions=5,**kwargs):
    start = time.perf_counter()
    for i in range(repetitions):
        fn(*args, **kwargs)
        #print(args, kwargs)
    end = time.perf_counter()
    return (end - start) / repetitions

def squared_power_list(a, *, start=0, end=5):
    result = []
    if type(a)==int and a>0:
        for i in range(start, end+1):
            result.append(a**i)
    else:
        raise ValueError("Only positive integer greater than 0 are allowed")
    return result

#time_it(print,1,2,3,4,sep='-', end= '\n',repetitions=5)

#time_it(squared_power_list,2,start=0, end=5, repetitions=10)

# Triangle = A = ½ (length × h)  here lenght is base length
# rectangle  =  lenght * width
# square = lenght**2
# pentagon = (5 ⁄ 2) × lenght × a  , “a” is the apothem length.
# Regular hexagon = (3*sqrt(3) /2 ) * length square

def polygon_area(length, *, width=1, sides=3, apothem=None):
    if sides == 3:
        return 0.5 * length * width
    elif sides == 4 and width == 1:
        return length ** 2   # square
    elif sides == 4 and width > 1 :
        return length * width   # rectangle
    elif sides == 5:
        if apothem == None:
            raise ValueError("Need apothem value")
        else:
            return 2.5 * length * apothem  # pentagon
    elif sides == 6:
        return (3 * sqrt(3) / 2) * length ** 2
    else:
        raise ValueError("Area calculations support from triangle upto a hexagon (6 side)")

#time_it(polygon_area,15,sides =4,width = 5,repetitions=5)

# time_it(temp_converter, 100, temp_given_in = 'f', repetitons=100)
# 100 is the base temperature given to be converted

def temp_converter(temp, *, temp_given_in=None):
    if temp_given_in == None:
        raise ValueError(
            "give temperature in 'f' or 'c' for conversion in celcius or farenhiet")
    elif temp_given_in == "f":
        return ((temp - 32) * 5) / 9
    else:
        return (temp/5) * 9 + 32

#time_it(temp_converter, 100, temp_given_in = 'c', repetitions=100)

def speed_converter(speed, *, dist="km", time="min"):
    from_km = {"km": 1, "m": 1000, "ft": 3280.84, "yrd": 1093.61}
    from_hr = {"hr": 1, "min": 60, "s": 3600, "ms": 3600000, "day": 0.0416667}
    return speed * from_km[dist] / from_hr[time]


