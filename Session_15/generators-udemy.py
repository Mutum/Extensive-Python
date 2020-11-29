# defining factorial

# 1 way by iterator
import math

class Factiter:
    def __init__(self,n):
        self.n = n
        self.i = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.i >= self.n:
            raise StopIteration
        else:
            self.i += 1
            return math.factorial(self.i)
        
fac = Factiter(3)

for i in fac:
    print(i)
    
next(fac) # exhuasted


# 2 way of by closure 
# this is infinite loop 

def fact():
    i = 0
    def inner():
        nonlocal i
        result = math.factorial(i)
        i += 1
        return result
    return inner
    
f = fact()

f()



#--------------------

def fib_recur(n):
    if n <= 1:
        return 1
    return fib_recur(n-1) + fib_recur(n-2)


fib = fib_recur(5)
fib

for i in range(25):
    print(fib_recur(i))
    
from timeit import timeit

timeit('fib_recur(10)',globals=globals(),number=10)
timeit('fib_recur(28)',globals=globals(),number=25)
timeit('fib_recur(29)',globals=globals(),number=29)

    # we can use memorization though,,but hang on
    
from functools import lru_cache   
@lru_cache()
def fib_recursive(n):
    if n <= 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

timeit('fib_recursive(10)',globals=globals(),number=10)
timeit('fib_recursive(28)',globals=globals(),number=25)
timeit('fib_recursive(29)',globals=globals(),number=29)

 # but still not enough if we hit max depth limit 
 
fib_recursive(20000)

# let use non-recursive way

def fib(n):
    fib_0 = 1
    fib_1 = 1
    
    for i in range(n-1):
        fib_0 , fib_1 = fib_1 , fib_0 + fib_1
    
    return fib_1    
        
class FibIter:
    def __init__(self,n):
        self.n = n
        self.i = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.i >= self.n:
            raise StopIteration
        else:
            result = fib(self.i)
        
        
        








