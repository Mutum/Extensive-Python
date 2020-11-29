import os
os.chdir('D:\Courses\EPAI\session_12\assignment_12\calculator')

path = '/calculator'

os.chdir(os.getcwd() + path)

import pytest
import math
import calculator
from calculator import derivatives


def test():
    
    abs_tol = 0.001
    rel_tol = 0.001
    
    test_value = 25
    
    # =================  testing sin =====================
    
    assert math.isclose(calculator.sin(test_value),  -0.132 ,
                        rel_tol=abs_tol,
                        abs_tol=abs_tol),(f'actual : {calculator.sin(test_value)}',
                        f'expected : {-0.132}' )
                                          
    assert math.isclose(derivatives.sin(test_value),  0.991 ,
                        rel_tol=abs_tol,
                        abs_tol=abs_tol),(f'actual : {derivatives.sin(test_value)}',
                        f'expected : {0.991}' )
                                          
    # =================  testing cosine =====================
    
    assert math.isclose(calculator.cos(test_value),  0.991 ,
                        rel_tol=abs_tol,
                        abs_tol=abs_tol),(f'actual : {calculator.cos(test_value)}',
                        f'expected : {0.991}' )
                                          
    assert math.isclose(derivatives.cos(test_value),  0.132 ,
                        rel_tol=abs_tol,
                        abs_tol=abs_tol),(f'actual : {derivatives.cos(test_value)}',
                        f'expected : {0.132}' )
                                          
        # =================  testing exponential =====================
        
    assert math.isclose(calculator.exp(test_value),  72004899337 ,
                        rel_tol=abs_tol,
                        abs_tol=abs_tol),(f'actual : {calculator.exp(test_value)}',
                        f'expected : {72004899337}' )
                                          
    assert math.isclose(derivatives.exp(test_value),  72004899337 ,
                        rel_tol=abs_tol,
                        abs_tol=abs_tol),(f'actual : {derivatives.exp(test_value)}',
                        f'expected : {72004899337}' )
    
            # =================  testing log =====================
    assert math.isclose(calculator.log(test_value), 3.218  ,
                        rel_tol=abs_tol,
                        abs_tol=abs_tol),(f'actual : {calculator.log(test_value)}',
                        f'expected : {3.218}' )
                                          
    assert math.isclose(derivatives.log(test_value),  0.04 ,
                        rel_tol=abs_tol,
                        abs_tol=abs_tol),(f'actual : {derivatives.log(test_value)}',
                        f'expected : {0.04}' )
     # =================  testing relu =====================            
    assert math.isclose(calculator.relu(test_value),25,rel_tol=abs_tol,
                        abs_tol=abs_tol),(f'actual : {calculator.relu(test_value)}',
                        f'expected : {25}' )
                                          
    assert math.isclose(derivatives.relu(test_value),  1,
                        rel_tol=abs_tol,
                        abs_tol=abs_tol),(f'actual : {derivatives.relu(test_value)}',
                        f'expected : {1}' ) 
                                          
            # =================  testing sigmoid =====================
            
    assert math.isclose(calculator.sigmoid(test_value), 0.999  ,
                        rel_tol=abs_tol,
                        abs_tol=abs_tol),(f'actual : {calculator.sigmoid(test_value)}',
                        f'expected : {0.999}' )
                                          
    assert math.isclose(derivatives.sigmoid(test_value),  1.388794386457827062508E-11 ,
                        rel_tol=abs_tol,
                        abs_tol=abs_tol),(f'actual : {derivatives.sigmoid(test_value)}',
                        f'expected : {1.388794386457827062508E-11}' ) 
                                          
        # =================  testing Softmax =====================
        

    assert math.isclose(calculator.softmax(test_value), 1  ,
                        rel_tol=abs_tol,
                        abs_tol=abs_tol),(f'actual : {calculator.softmax(test_value)}',
                        f'expected : {1}' )
                                          
    # assert math.isclose(derivatives.softmax(test_value),  0.04 ,
    #                     rel_tol=abs_tol,
    #                     abs_tol=abs_tol),(f'actual : {derivatives.softmax(test_value)}',
    #                     f'expected : {0.04}' ) 
                                          
        # =================  testing tan =====================                                              
                                          
    assert math.isclose(calculator.tan(test_value), -0.133  ,
                        rel_tol=abs_tol,
                        abs_tol=abs_tol),(f'actual : {calculator.tan(test_value)}',
                        f'expected : {-0.133}' )
                                          
    assert math.isclose(derivatives.tan(test_value),  2.017 ,
                        rel_tol=abs_tol,
                        abs_tol=abs_tol),(f'actual : {derivatives.tan(test_value)}',
                        f'expected : {2.017}' )
