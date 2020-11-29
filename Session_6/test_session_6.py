# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 01:30:36 2020

@author: Mutum
"""

import os
#os.chdir("D:\Courses\EPAI\Session_6")

import re
import inspect
import pytest
import Session_6
from Session_6 import normal_func,play_card, n


function_list = [
    "normal_func",
    "play_card"
    ]

README_CONTENT_CHECK_FOR = [
    "normal_func",
    "play_card",
    "Annotation",
    "Docstrings"]

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
    functions = inspect.getmembers(Session_6, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
        
def test_fourspace():
    r''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(Session_6)
    spaces = re.findall('\n(.+?)[a-zA-Z0-9@]', lines)
    for space in spaces:
        if len(space) % 4 > 0 and len(space) != 1: #1 in case new fn or cls start after \n
            print(space)
            return True
    return False


# def test_indentations():
#     ''' Returns pass if used four spaces for each level of syntactically \
#     significant indenting.'''
#     lines = inspect.getsource(Session_6)
#     spaces = re.findall('\n +.', lines)
#     for space in spaces:
#         assert len(space) % 4 == 2, "Your script contains misplaced indentations"
#         assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_count():
    code_lines = inspect.getsource(Session_6)
    all_found = True
    for func in function_list:
        if func not in code_lines:
            all_found = False
    assert all_found,"Not all functions are define"   

def test_use_ValueError():
    code_lines = inspect.getsource(Session_6)
    assert "ValueError" in code_lines,"ValueError not used"

def test_normal_func_annotation_check():
    code_lines= normal_func.__annotations__
    assert len(code_lines) !=0,"Annotations are not added"
    
def test_normal_func_docstring_check():
    code_lines= normal_func.__doc__
    assert len(code_lines) !=0,"Docstrings are not added"

def test_normal_func_comment_check():
    assert inspect.getcomments(normal_func) is not None, "Add comments before writing fuctions for better readability"
   
def test_play_card_annotation_check():
    code_lines= play_card.__annotations__
    assert len(code_lines) !=0,"Annotations are not added"
    
def test_play_card_docstring_check():
    code_lines= play_card.__doc__
    assert len(code_lines) !=0,"Docstrings are not added"

def test_play_card_comment_check():
    assert inspect.getcomments(play_card) is not None, "Add comments before writing fuctions for better readability"
       
   #assert len(code_lines) is None,"Add comments before writing fuctions for better readability"

# inspect.getsource(normal_func.__annotations__)

# normal_func.__comment__
# print(inspect.getcomments(normal_func))

def test_normal_func_suits_check():
    
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suits = ['spades', 'clubs', 'hearts', 'diamonds','test']
    
    assert len(normal_func(vals=vals,suits=suits))==52,"52 cards are there in a play"

def test_normal_func_suits_check():
    
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suits = ['spades', 'clubs', 'hearts', 'diamonds','test']
    
    with pytest.raises(ValueError) as error:
        return normal_func(vals= vals,suits=suits)

def test_normal_func_vals_check():
    
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace','test']
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    
    with pytest.raises(ValueError) as error:
        return normal_func(vals= vals,suits=suits)
    
def test_normal_func_vals_suits_check():
    
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace','test']
    suits = ['spades', 'clubs', 'hearts', 'diamonds','test1']
    
    with pytest.raises(ValueError) as error:
        return normal_func(vals= vals,suits=suits)

def test_play_card_player_check():
    
    players = 3 # only two player allower , right !!
    cards_num = 3
    deck = n
    with pytest.raises(ValueError) as error:
        return play_card(players= players,cards_num=cards_num, deck = n)
 
def test_play_card_check():
    
    players = 2 
    cards_num = 0
    deck = n
    with pytest.raises(ValueError) as error:
        return play_card(players= players,cards_num=cards_num, deck = n)       

def test_play_card_player_check():
    
    players = 3
    cards_num = 7
    deck = n
    with pytest.raises(ValueError) as error:
        return play_card(players= players,cards_num=cards_num, deck = n)  
 
# deck of only 50 cards, for testing
deck = [('spades', '2'),
 ('spades', '3'),
 ('spades', '4'),
 ('spades', '5'),
 ('spades', '6'),
 ('spades', '7'),
 ('spades', '8'),
 ('spades', '9'),
 ('spades', '10'),
 ('spades', 'jack'),
 ('spades', 'queen'),
 ('spades', 'king'),
 ('spades', 'ace'),
 ('clubs', '2'),
 ('clubs', '3'),
 ('clubs', '4'),
 ('clubs', '5'),
 ('clubs', '6'),
 ('clubs', '7'),
 ('clubs', '8'),
 ('clubs', '9'),
 ('clubs', '10'),
 ('clubs', 'jack'),
 ('clubs', 'queen'),
 ('clubs', 'king'),
 ('clubs', 'ace'),
 ('hearts', '2'),
 ('hearts', '3'),
 ('hearts', '4'),
 ('hearts', '5'),
 ('hearts', '6'),
 ('hearts', '7'),
 ('hearts', '8'),
 ('hearts', '9'),
 ('hearts', '10'),
 ('hearts', 'jack'),
 ('hearts', 'queen'),
 ('hearts', 'king'),
 ('hearts', 'ace'),
 ('diamonds', '2'),
 ('diamonds', '3'),
 ('diamonds', '4'),
 ('diamonds', '5'),
 ('diamonds', '6'),
 ('diamonds', '7'),
 ('diamonds', '8'),
 ('diamonds', '9'),
 ('diamonds', '10'),
 ('diamonds', 'jack'),
 ('diamonds', 'queen'),
 ('diamonds', 'king')
 ]

def test_play_dec_check():
    
    players = 3
    cards_num = 7
    with pytest.raises(ValueError) as error:
        return play_card(players= players,cards_num=cards_num, deck = deck)   



