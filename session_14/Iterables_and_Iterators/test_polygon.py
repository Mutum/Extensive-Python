import math
import pytest
import os
import inspect

import polygon
import custom_polygon

#os.chdir("D:\Courses\EPAI\session_13\sequence_1")

from polygon import Polygon as Polygon
from custom_polygon import Polygons as Polygons

def test_use_ValueError():
    code_lines = inspect.getsource(polygon)
    assert "ValueError" in code_lines,"TypeError not used"
 
    

# testing code for polygon of 4 edges and circum radius 1

abs_tol = 0.001
rel_tol = 0.001

n = 4
R = 1
p = Polygon(n, R)

def test_interior_angle():
    assert p.interior_angle == 90, (f'actual: {p.interior_angle}, '
                                    ' expected: 90')
    
def test_area():
    assert math.isclose(p.area, 2,
                        rel_tol=abs_tol,
                        abs_tol=abs_tol), (f'actual: {p.area},'
                                           ' expected: 2.0')
def test_edge_length():
    assert math.isclose(p.edge_length, math.sqrt(2),
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.edge_length},'
                                          f' expected: {math.sqrt(2)}')
def test_perimeter():
    assert math.isclose(p.perimeter, 4 * math.sqrt(2),
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                          f' expected: {4 * math.sqrt(2)}')
def test_apothem():
    assert math.isclose(p.apothem, 0.707,
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                          ' expected: 0.707')
    