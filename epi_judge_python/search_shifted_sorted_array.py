from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    # TODO - you fill in here.
    # [-1, 0, 1, 2, 3, 4, 5, 6]
    # [3,1,2]
    '''
    left = 0
    right = 0

    mid = 0

    pivot = 1

    '''
    left = 0
    right = len(A)-1
    pivot = 0

    while left <= right:
        mid = (left+right)//2
        
        if A[mid] <= A[right]:
            if A[mid] < A[pivot]:
                pivot = mid
            right = mid - 1
        else:
            left = mid + 1

    return pivot


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
