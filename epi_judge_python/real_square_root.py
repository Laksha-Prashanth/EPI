import math
from test_framework import generic_test


def square_root(x: float) -> float:
    # TODO - you fill in here.
    left = 1
    right = x
    if x < 1:
        left = 0
        right = 1


    while not math.isclose(left, right):
        root = (left+right)/2

        if root*root == x:
            return root
        elif root*root > x:
            right = root
        else:
            left = root
    return left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
