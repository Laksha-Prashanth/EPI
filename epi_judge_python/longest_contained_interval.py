from typing import List

from test_framework import generic_test

'''
{3, -2, 7, 9 8,1,2,0,-1,5}

visited:    {3,2,1,0,-1,-2,7,8,9}
[]
count = 6

result = 6


{-2,-1,0,1,2,3}
time:   O(N)
space:  O(N)

'''
def longest_contained_range(A: List[int]) -> int:
    # TODO - you fill in here.
    setA = set(A)
    visited = set()
    result = 0
    queue = [A[0]]
    i = 1
    '''
    {3, -2, 7, 9 8,1,2,0,-1,5}
    visited:    3, 2, 1, 0, -1, -2
    result: 0
    queue:  [-1,-3]
    count = 4
    curr = -2
    '''

    while i< len(A) and queue:

        count = 0
        while queue:
            curr = queue.pop()
            if curr in visited or curr not in setA:
                continue
            else:
                visited.add(curr)
            queue.append(curr+1)
            queue.append(curr-1)
            count += 1
        queue.append(A[i])
        i += 1
        result = max(count, result)


    return max(result,1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
