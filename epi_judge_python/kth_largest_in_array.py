from typing import List
import random

from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    # TODO - you fill in here.
    if not A:
        return 0
    if len(A) == 1:
        return A[0]

    def partition(A, L,R):
        p = A[L]
        l,r = L+1, R
        while l <= r:
            while l<=R and A[l] < p:
                l += 1
            while r > L and A[r] > p:
                r -= 1
            if l < r:
                A[l], A[r] = A[r],A[l]
        A[L], A[r] = A[r], A[L]
        return r

    def random_partition(A,L,R):
        pivot = random.randint(L,R)
        A[L],A[pivot] = A[pivot],A[L]
        return partition(A,L,R)

    def selectHelper(A,i, L, R):
        curr = random_partition(A,L,R)
        while curr != i-1:
            if curr > i-1:
                curr = random_partition(A,L, curr-1)
            else:
                curr = random_partition(A,curr+1, R)
        return A[curr]
    
    return selectHelper(A,len(A) + 1 - k,0,len(A)-1)


if __name__ == '__main__':
    #1 3 4 5 6 7 9
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
