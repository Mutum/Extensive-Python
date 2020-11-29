# EPAI Session 3

This is the 3rd session of EPAI Program. It covers "Nummermic types" contents.
Any feedback on the code construct would be helpful


# Functions description


 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## encoded_from_base10

This function allows to represent any number(base 10) to any base and finally represent the number in their digits mapping i.e. 0-9 and a-z
Inside the fuctions:
1st , it check for duplicate in digit_map arguments .
      It lower all the character in digit_map and then check for duplicate values by counting each unique character. If any of the count is greater than 1, then ValueError is raised
2nd, functions to convert any number(base 10) to other base.
      Note that we cannot have base less than 2 or greater than 36 . Minimum is 2 as we need binary code 0 or 1 . Maximum 36 which is the total of digits 0-9 and alphabet a-z . Any base argument within this range is valid, rest gives ValueError error.
      This function at first given base representation without numeric sign ( +/-) into consideration.
3rd, In this step, we loop through out digit_map and mapped out base representation   output from 2nd step.
4th, finally our sign (+/-) has been added to 3rd output

Note the ValueError exception in the function
Note built-in methods has hex( or bin( for base representation of 2 and 16 base


   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .


## float_equality_testing

This function check for closeness or equality between two numbers. In python, the inbuilt function is isclose
There are two thing for threshold deciding the equality i.e. absolute and relative tolerance
these are the threshold rel_tol = 1e-12 and abs_tol = 1e-05
If the difference or error between two numbers is zero, then its obviously same . Rest depends on the threshold values.


 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## manual_truncation_function

This is a representative function of trunc ( truncation ) method from math module in python .
if the input is type int , then output is int . For rest it will be float.

## manual_rounding_function and rounding_away_from_zero
First function behave more of round python function
2nd function rounds away or farther than zero



 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
