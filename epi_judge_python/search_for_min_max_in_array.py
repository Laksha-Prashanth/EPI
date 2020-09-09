import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max(A: List[int]) -> MinMax:
    # TODO - you fill in here.
    if len(A) < 2:
        return MinMax(A[0], A[0])

    curr_min, curr_max = A[0], A[1]
    if A[0] > A[1]:
        curr_max, curr_min = A[0], A[1]
    
    i = 2
    while i + 1 < len(A):
        winner, loser = A[i], A[i+1]
        if A[i] < A[i+1]:
            winner, loser = A[i+1], A[i]
        if winner > curr_max:
            curr_max = winner
        if loser < curr_min:
            curr_min = loser
        i += 2
    if i < len(A):
        if curr_max < A[i]:
            curr_max = A[i]
        elif curr_min > A[i]:
            curr_min = A[i]

    return MinMax(curr_min, curr_max)


def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_min_max_in_array.py',
                                       'search_for_min_max_in_array.tsv',
                                       find_min_max,
                                       res_printer=res_printer))
