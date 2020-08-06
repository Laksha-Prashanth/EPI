from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # TODO - you fill in here.
    carry = 0
    B = list(A)
    B.reverse()
    B[0] += 1
    for i in range(len(A)):
        n = B[i]
        if carry:
            n += 1
        if n > 9:
            B[i] = 0
            carry = 1
        else:
            carry = 0
            B[i] = n

    if carry:
        B.append(1)

    return B[::-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
