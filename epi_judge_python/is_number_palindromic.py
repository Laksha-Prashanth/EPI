import math
from test_framework import generic_test


def is_palindrome_number(x: int) -> bool:
    # TODO - you fill in here.
    if x < 0:
        return False
    if x == 0:
        return True

    l = int(math.log10(x))
    while l > 0 and x:
        if x%10 != (x//(10**l))%10:
            return False
        x = x//10
        l = l-2
    return True


if __name__ == '__main__':
    print(is_palindrome_number(0))
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
