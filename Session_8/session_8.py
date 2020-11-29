# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 19:07:36 2020

@author: Mutum
"""

def fibonacci(n):
    
    '''Return nth term of fibonacci series 
      input: n --> integer
      output : nth term 
    '''
    if n<=  2:
        return 1
    else:
        return  fibonacci(n-1) + fibonacci(n-2)
    

fibonacci.__doc__

len(fibonacci.__doc__)


# Write a closure that takes a function and then check whether the function passed 
# has a docstring with more than 50 characters. 50 is stored as a free variable - 200
 
def closure_docstring_check():
    
    ''' Return a closure that check a fucntion has docstring greater than
     50 character or note
    '''
         
    x = 50  # docstring lenght to be check --> free variables
     
    def doc_func(func):
        return len(func.__doc__) > x
     
    return doc_func
     
doc = closure_docstring_check()

doc(fibonacci)

# Write a closure that gives you the next Fibonacci number - 100

def next_fibonacci():
    '''  Return a closure to generate next fibonacci number/term 
    when calling repeatedly
    '''
    n = 0 # free variable for closure---- 0th term
    
    def next():
        nonlocal n
        #print(fibonacci(n))
        n += 1      # increase term 
        return fibonacci(n)
     
    return next

f1 = next_fibonacci()


# We wrote a closure that counts how many times a function was called. 
# Write a new one that can keep a track of how many times add/mul/div functions were called, 
# and update a global dictionary variable with the counts - 250

def add(*args: int) :
    ''' Return sum of numbers
    inputs : any argument
    output : total
    '''
    return sum(args)

def mul(a,b):
    ''' Return multiplication of two numbers '''
    return a*b

def div(a,b):
    ''' Return multiplication of two numbers 
     a : numerator
     b : denominator
     
     '''
    if b == 0:
        raise ValueError('divisible by zero')
    return a/b
 

times_count_func = dict()   # global dictionary to update functions and count of function`s call


def closure(func):
    ''' Return a closure to update functioin and their fucntions`s call count in 
    global dictionary --> times_count_func
    
    Input : a function
    Output : a closure 
    '''
    cnt = 0  # free variable to capture number of functions`s call
    
    def inner(*args,**kwargs):
        nonlocal cnt
        cnt += 1
        times_count_func[func.__name__] = cnt # update fucntion and its counts 
        return func(*args,**kwargs)
    
    return inner


add_closure = closure(add)
mul_closure = closure(mul)
div_closure = closure(div)

add_closure(1,5)  
add_closure(2,8)
add_closure(1,2,3,4)

mul_closure(15,2)

div_closure(6,5)

times_count_func


# Modify above such that now we can pass in different dictionary variables
# to update different dictionaries - 250

count_dict_1 = dict()  

def closure_modify(func,counts):
    ''' Return a closure to update functioin and their fucntions`s call count in 
    global dictionary --> 
    Input : a function  and a dictionary
    Output : a closure 
    '''
    cnt = 0  # free variables 
    
    def inner(*args,**kwargs):
        nonlocal cnt
        cnt += 1
        counts[func.__name__] = cnt
        return func(*args,**kwargs)
    
    return inner

add_closure_1 = closure_modify(add,count_dict_1)

add_closure_1(1,2,3,4,5)
add_closure_1(1,2,3)     
        
mul_closure_1 = closure_modify(mul,count_dict_1)
mul_closure_1(5,6)   
mul_closure_1(5,5)
mul_closure_1(2,8)        


div_closure_1 = closure_modify(div,count_dict_1) 
div_closure_1(2,5)    
div_closure_1(8,5)  

count_dict_1






