# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 19:06:54 2020

@author: Mutum
"""


import os
#os.chdir("D:\Courses\EPAI\session_7")

import re
import inspect
import pytest
import session_7
from session_7 import generate_fibo

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 200, "Make your README.md file interesting! Add atleast 200 words"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session_7, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
        
def test_fourspace():
    r''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session_7)
    spaces = re.findall('\n(.+?)[a-zA-Z0-9@]', lines)
    for space in spaces:
        if len(space) % 4 > 0 and len(space) != 1: #1 in case new fn or cls start after \n
            print(space)
            return True
    return False

def test_use_ValueError():
    code_lines = inspect.getsource(session_7)
    assert "TypeError" in code_lines,"TypeError not used"
    
def test_generate_fibo_length():
    assert len(generate_fibo(5))==5,"Function not generating correct number of terms"
    
def test_generate_fibo_term():
    assert generate_fibo(5) == [0,1,1,2],"Function not generating correct terms"
    
def test_generate_fibo_term():
    with pytest.raises(TypeError) as error:
        return generate_fibo(-0.1)
    
    
def test_add_twoList_even_odd():
    a = [1,2,4,6]  # making a list of integers
    b = [3,0,5]  # making a list of integers
    assert sum([x for x in list(filter(lambda x : x %2 == 0,a)) + list(filter(lambda x : x %2 != 0,b))  ])== 20, "Expression not correct"
    
    