import bisect
from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    # TODO - you fill in here.
    #[1,2,3,3,4]
    #l 0
    #r 1
    #
    #m 0
    #pos -1
    left = 0
    right = len(A)-1

    position = -1

    while left <= right:
        mid = (left+right)//2
        if A[mid] < k:
            left = mid + 1
        else:
            if A[mid] == k:
                position = mid
            right = mid - 1
        
    return position


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
