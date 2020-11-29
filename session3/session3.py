
from fractions import Fraction


def encoded_from_base10(number, base, digit_map):
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module

    '''
    dict = {}
    for char in digit_map.lower():
        keys = dict.keys()
        if char in keys:
            dict[char] += 1
        else:
            dict[char] = 1

    if max(dict.values()) > 1:
        raise ValueError('characters are repeating .')

    def from_base10(n, b):       # represent a base 10 number to any base
        if b < 2:   
            raise ValueError(' base b must be >= 2')
        if n < 0:
            raise ValueError('Number n must be >= 0')
        if n == 0:
            return [0]
        digits = []
        while n > 0:
            n, m = divmod(n, b)
            digits.insert(0, m)
        return digits

    if base < 2 or base > 36:
        raise ValueError('Invalid base . : must be 2 <= base <= 36')

    sign = -1 if number < 0 else 1
    number *= sign

    digits = from_base10(number, base)

    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not long enough to encode digits")
    encoding = ''.join([digit_map[d] for d in digits])

    if sign == -1:
        encoding = '-' + encoding
    return encoding


def float_equality_testing(a, b):
    '''
        This function emulates the ISCLOSE method from the MATH module, but you can't use this function
        We are going to assume:
        - rel_tol = 1e-12
        - abs_tol = 1e-05
    '''
    abs_diff = abs(a - b)
    rel_diff = a - b if a > b else b - a
    rel_tol = 1e-12
    abs_tol = 1e-05

    if abs_diff < abs_tol or rel_diff < rel_tol:
        return True
    else:
        return False


def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point.
    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
    '''

    if isinstance(f_num, int):
        return f_num

    if isinstance(f_num, float):
        n, d = Fraction(f_num).numerator, Fraction(f_num).denominator
        if f_num >= 0:
            return n // d
        else:
            return n // d + 1


def manual_rounding_function(f_num, ndigits=None):
    '''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
    '''
    if f_num == 0:
        return f_num

    n, d = Fraction(f_num).numerator, Fraction(f_num).denominator
    return float(n // d) if f_num > 0 else float(n // d) + 1


def rounding_away_from_zero(f_num):
    '''
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't.
    Hint: use FRACTIONS and extract numerator.
    '''
    add_up = abs(f_num) + 0.5
    n, d = Fraction(add_up).numerator, Fraction(add_up).denominator
    num_int = n // d

    return copysign(num_int, fnum)
