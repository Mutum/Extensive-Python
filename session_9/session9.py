# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 12:57:31 2020

@author: Mutum
"""

# Write separate decorators that:
# 1. allows a function to run only on odd seconds - 100pts
# 2. log - 100pts
# 3. authenticate - 300pts
# 4. timed (n times) - 100pts
# 5. Provides privilege access (has 4 parameters, based on privileges (high, mid, low, no), gives access to all 4, 3, 2 or 1 params) - 200pts
# Write our htmlize code using inbuild singledispatch - 100pts


import random

from functools import wraps
from datetime import datetime

from functools import reduce, singledispatch
from html import escape


def odd_run(fn):

    @wraps(fn)
    def inner(*args,**kwargs):
        run_dt = datetime.utcnow().time()
        
        print(f'{run_dt}: called {fn.__name__}')
        print(run_dt.second)
        if run_dt.second %2 != 0:
            value = fn(*args,**kwargs)
            return value
        else:
            return f"Second is not odd {run_dt.second}"
    return inner


@odd_run
def oadd(a:int,b:int):
    ''' Add two integers '''
    return a+b

print(oadd(1,2))

# 2 

def logg(fn: 'func') -> 'func':
    '''
    Parameters
    ----------
    fn : 'func'
        Take a function and decorates that with execution timestamp.
    Returns
    -------
    Function
        Decorated inner function.
    '''
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print(f'{run_dt}: called {fn.__name__}')
        return result
    return inner



@logg
def mul(*args: int) -> int:
    '''
        Multiplies the input integers and returns the output.
    '''
    return reduce(lambda x, y: x*y, args)



def set_password() -> 'func':
    '''
    Takes password as input and returns a closure that can return the password when called.
    '''
    password = ''
    def inner():
        '''
        Closure function
        '''
        nonlocal password
        if password == '':
            password = 'password123' # input()
        return password
    return inner

current_password = set_password()


def authenticate(fn, current_password, user_password):
    '''
    fn : function
        Decorates an input function after successful authentifaction.
    current_password : string
        It calls set_password() function to get the password from the closure to validate against input password
    user_password : string
        Input password string.
    -------
    Output:
        
    function
        Decorated function.
    '''
    cnt = 0
    if user_password == current_password():
        def inner(*args, **kwargs):
            '''
            Closure function
            '''
            nonlocal cnt
            cnt += 1
            print(f'{fn.__name__} was called {cnt} times')
            return fn(*args, **kwargs)
        return inner
    else:
        print('You scamster!!')
        raise ValueError("Incorrect login")

def add(a:int, b:int) -> int:
    '''
    Return sum of two values
    '''
    return a + b

# Decorate add function with authentication
auth_add = authenticate(add, current_password, 'password123')


def timed(rep: int):
    '''
    Function: Decoration factory. It takes a number n as input to run the inner function n times.
    '''
    from time import perf_counter
    from functools import wraps
    
    def decorat(fn):
        '''
        Decoration function
        '''

        @wraps(fn)
        def inner(*args, **kwargs):
            '''
            Closure function that runs n times give the average execution time.
            '''
            elapsed_total = 0
            elapsed_count = 0

            for i in range(rep):
                print(f'Running iteration number {i + 1}')  
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                # elapsed = end - start
                elapsed_total += end - start
                elapsed_count += 1

            args_ = [str(a) for a in args]
            kwargs_ = ['{0}={1}'.format(k, v) for k, v in kwargs.items()]
            all_args = args_ + kwargs_
            args_str = ','.join(all_args) 

            elapsed_avg = elapsed_total / elapsed_count

            print(f'{fn.__name__}({args_str}) took {elapsed_avg} seconds')

            return result
        return inner
    return decorat


@timed(15)
def fib_reduce(n:int) -> int:
    '''
    Give nth term of fibonacci
    '''
    initial = (1, 0)
    dummy = range(n)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]), dummy, initial)
    return fib_n[0]

fib_reduce(4)


def set_profiles():
    '''
    Decorator function to define access profile dictionary and return closure function with it
    '''
    profiles = ''
    def inner():
        nonlocal profiles
        if not bool(profiles):
            profiles = {'high':['a','b','c','d'], 'mid':['b','c','d'], 'low':['c','d'], 'no':['d']}
        return profiles
    return inner

get_profiles = set_profiles()


def grant_access(get_profiles):
    '''
    Decorator factory that takes the profile dictionary from set_profiles.
    '''
    def outer(fn):
        '''
        Decoration function that finds the access profile for a given privilege based on set_profiles profile dictionary.
        '''
        def inner(*args):
            '''
            Closure function
            '''
            if len(args) > 1:
                raise ValueError("More than one privileges requested")
            profiles = get_profiles()
            if args[0] not in profiles:
                raise ValueError('Access profile does not exist')
            return fn(*args, d=profiles)
        return inner
    return outer

@grant_access(get_profiles)
def get_access(p:str, d:dict={}) -> list:
    '''
    Function that takes privilege value and returns its corresponding access profile.
    '''
    return d[p]



@singledispatch
def htmlize(a):
    '''
    It takes a value and generates html. It returns default html value escape(str(a)).
    '''
    return escape(str(a))

@htmlize.register(complex)
def htmlize_complex_numbers(a):
    '''
    Function that generates html string for complex numnber. It registers itself with htmlize.register. 
    '''
    return f'{a}(<i>{str(complex(a.real, a.imag))}</i>)'

