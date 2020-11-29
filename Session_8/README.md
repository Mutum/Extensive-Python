# Epai_Session_8

## 1
Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable

- closure_docstring_check :
This fucntion return a closure that check whether a fuction has docstring of character 50 or not.
Here 'x' is the local scope where the inner function doc_func takes look up to


## 2o
Write a closure that gives you the next Fibonacci number
- next_fibonacci:

- First we have already define a function "fibonacci" calculating nth term of fibonacci series
- The next_fibonacci fucntion returns a closure when call gives next term of fibonacci series


## 3
We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts

-  Here the closure keeps tracks of the number of times a function is call and then update in the global dictionary "times_count_func"



## 4
Modify above such that now we can pass in different dictionary variables to update different dictionaries

Earlier in above 3rd question, the closure update only in a global dictionary
Here we change in such a way , in the closure we can pass a function and dictionary to keep tracking (# of times function is called)
