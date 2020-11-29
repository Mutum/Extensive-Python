# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 18:43:47 2020

@author: Mutum
"""
import os
#os.chdir("D:\\Courses\\EPAI\\Session_5")

import re
import inspect
import pytest
import session_5
from session_5 import *

function_list = [
    "time_it",
    "squared_power_list",
    "polygon_area",
    "temp_converter",
    "speed_converter"]

README_CONTENT_CHECK_FOR = [
    "time_it",
    "squared_power_list",
    "polygon_area",
    "temp_converter",
    "speed_converter"]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"
    
def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 200, "Make your README.md file interesting! Add atleast 200 words"

# check if all function`s descriptioin are written in README file
    
def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session_5, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_fourspace():
    r''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session_5)
    spaces = re.findall('\n(.+?)[a-zA-Z0-9@]', lines)
    for space in spaces:
        if len(space) % 4 > 0 and len(space) != 1: #1 in case new fn or cls start after \n
            print(space)
            return True
    return False

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session_5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_time_import_or_not():
    code_lines = inspect.getsource(session_5)
    assert 'time.perf_counter' in code_lines, 'time.perf_counter not used! You must use time.perf_counter for calc time'
    assert 'time' in code_lines, 'You have not imported time!'

# check if all functions are define in program code
    
def test_function_count():
    code_lines = inspect.getsource(session_5)
    all_found = True
    for func in function_list:
        if func not in code_lines:
            all_found = False
    assert all_found,"Not all functions are define"   
     
# test for function`s call 

def test_functions_call_print():
    assert type(time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitions=5)) == float,"Output must be float"

def test_functions_call_sq_power():
    assert type(time_it(squared_power_list, 2, start=0, end=5, repetitions=5) ) == float,"Output must be float"

def test_functions_call_polygon():
    assert type(time_it(polygon_area, 15, sides = 3, repetitions=10)) == float,"Output must be float"

def test_functions_call_temp_convert():
    assert type(time_it(temp_converter, 100, temp_given_in = 'f', repetitions=100)) == float,"Output must be float"

def test_functions_call_speed_convert():
    assert type(time_it(speed_converter, 100, dist='km', time='min', repetitions=200)) == float,"Output must be float"
     
     
     
def test_use_ValueError():
    code_lines = inspect.getsource(session_5)
    assert "ValueError" in code_lines,"ValueError not used"
    
def test_any_formatChange_timeit():
    code_lines = inspect.getsource(session_5)
    assert "def time_it(fn,*args,repetitions=5,**kwargs)" in code_lines,"Cannot change in time_it call format"


#@pytest.mark.xfail(reason="float is not allowed",strict=True)
def test_square_power_func_wrong_check():
    num = [-1,0,2.0]
    for a in num:
        with pytest.raises(ValueError) as error:
            return squared_power_list(a)
   # return squared_power_list(2.0)

def test_square_power_func_sum_check():
    power_2 = sum([1, 2, 4, 8, 16, 32])
    func_result = sum(squared_power_list(2))
    assert power_2 == func_result,"square power function is not correct"
 
# test on polygon function

def test_polygon_triangle_check():
    length = 5
    width = 3
    area_triangle = (1/2) * length * width
    func_area = polygon_area(length = length,width= width, sides=3, apothem=None)
    assert area_triangle == func_area,"Triangle area calculation is wrong !!"
    
def test_polygon_square_check():
    length = 5
    area_square = length ** 2
    func_area = polygon_area(length = length, sides=4, apothem=None)
    assert area_square == func_area,"Square area calculation or the logic flow is wrong!!"
    
def test_polygon_rectangle_check():
    length = 5
    width = 6
    area_rectangle = length * width
    func_area = polygon_area(length = length, width = width , sides=4, apothem=None)
    assert area_rectangle == func_area,"Rectangle area calculation or the logic flow is wrong!!"
    
def test_polygon_pentagon_apothem_missing():
    with pytest.raises(ValueError) as apothem_missing:
        return polygon_area(5,sides=5)
    
def test_polygon_pentagon_check():
    length = 5
    apothem = 3.5
    area_pentagon = 2.5 * length * apothem 
    func_area = polygon_area(length = length,sides=5, apothem= apothem)
    assert area_pentagon == func_area,"Pentagon area calculation or the logic flow is wrong!!"
    
def test_polygon_regular_hexagon_check():
    length = 5
    area_hexagon = (3 * sqrt(3) / 2) * length ** 2
    func_area = polygon_area(length = length,sides=6)
    assert area_hexagon == func_area,"Hexagon area calculation or the logic flow is wrong!!"
    
def test_polygon_sides_greater_6_check():
    sides = 7
    length = 9
    with pytest.raises(ValueError) as not_define:
        return polygon_area(length = length,sides= sides)
    
# test on temp_converter function

def test_temp_missin_temp_label():
    with pytest.raises(ValueError) as error:
        return temp_converter(25)
    
def test_fahrenhiet_to_celcius():
    assert temp_converter(32,temp_given_in="f") == 0,"32 fahrenheit is equal to 0, check your formula"
    
    
def test_celcius_to_fahrenhiet():
    assert temp_converter(0,temp_given_in="c") == 32,"32 fahrenheit is equal to 0, check your formula"
 