# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 22:31:01 2020

@author: Mutum
"""

import pytest
import os
import inspect
import re
import time

import session9

#os.chdir("D:\Courses\EPAI\session_9")



def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session9, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_check_with_docstring():

    assert len(session9.add.__doc__) > 0, "Docstring exists"
    assert len(session9.logg.__doc__) > 0, "Docstring exists"
    assert len(session9.set_password.__doc__) > 0, "Docstring exists"
    assert len(session9.authenticate.__doc__) > 0, "Docstring exists"
    assert len(session9.timed.__doc__) > 0, "Docstring exists"
    assert len(session9.set_profiles.__doc__) > 0, "Docstring exists"
    assert len(session9.grant_access.__doc__) > 0, "Docstring exists"
    

def test_mul():
    assert session9.mul(1,0,5) == 0, "Check mul function if returning correct result"

def test_authenticate():    
    with pytest.raises(ValueError) as error:
        _ = session9.authenticate(session9.add, session9.current_password, 'pasasdcasdc'), 'incorrect login'

def test_fib_reduce():
    assert session9.fib_reduce(4) == 5, "Check fib_reduce function"

def test_get_access():
    assert session9.get_access('high') == ['a', 'b', 'c', 'd'], "Check get_access function"

def test_htmlize_complex_numbers():
    assert session9.htmlize_complex_numbers(1+2j) == '(1+2j)(<i>(1+2j)</i>)', "Check htmlize_complex_numbers function"