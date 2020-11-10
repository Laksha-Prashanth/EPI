import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

'''
hello world save save the union this is laksha
0       1     2    3    4   5   6   7
(save, union)
result = [2,4]
left: 2
right: 4
{
    save :  2
    union:  1
}
time: O(N)
space: O(N)
'''
def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
                
    if not paragraph or not keywords:
        return Subarray(0,0)
    left = 0
    right = 0
    words = {}
    result = [0, float('inf')]
    '''
    hello worlds this is laksha, this is
    0       1       2 3     4       5 6
    left:   3
    right:  3
    words{
        is:     1

    }
    result = [2,3]
    '''

    while right < len(paragraph):
        if paragraph[right] in keywords:
            # add to dict
            if paragraph[right] not in words:
                words[paragraph[right]] = 0
            words[paragraph[right]] += 1
        
        while left <= right and len(words) == len(keywords):
            if paragraph[left] in words:
                words[paragraph[left]] -= 1
            if paragraph[left] in words and words[paragraph[left]] == 0:
                del words[paragraph[left]]
            if result[1] - result[0] > right - left:
                result = [left, right]
            left += 1

        right += 1
        if (len(words) == len(keywords)) and (result[1] - result[0] > right - left):
            result = [left, right]
                


    return Subarray(result[0],result[1])


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
