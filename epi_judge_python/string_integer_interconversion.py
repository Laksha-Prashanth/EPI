from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    # TODO - you fill in here.
    result = ""
    negative = False
    if x < 0:
        negative = True
        x = -x
    while x:
        result = chr(x%10 + ord('0'))+result
        x = x//10
    
    if negative:
        result = '-'+result

    if not result:
        return '0'
    return result


def string_to_int(s: str) -> int:
    # TODO - you fill in here.
    result = 0
    negative = False
    if s[0] == '-':
        negative = True
        s = s[1:]
    if s[0] == '+':
        s = s[1:]
    for c in s:
        result = result*10 + ord(c)-ord('0')
    
    if negative:
        result = -result
    return result


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
