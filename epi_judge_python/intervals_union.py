import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))

'''

'''
def union_of_intervals(intervals: List[Interval]) -> List[Interval]:
    # TODO - you fill in here.
    intervals.sort(key = lambda x: [x[0][1],not x[0][0]])

    result = []
    curr_start = intervals[0].left
    curr_end = intervals[0].right
    for interval in intervals[1:]:
        if interval.left.val < curr_end.val or (interval.left.val == curr_end.val and (interval.left.is_closed or curr_end.is_closed)):
            if curr_end.val < interval.right.val:
                curr_end = interval.right
            elif curr_end.val == interval.right.val:
                curr_end = Endpoint(curr_end.is_closed or interval.right.is_closed, curr_end.val)
        else:
            result.append(Interval(curr_start,curr_end))
            curr_start = interval.left
            curr_end = interval.right
    
    result.append(Interval(curr_start, curr_end))

    return result


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intervals_union.py',
                                       'intervals_union.tsv',
                                       union_of_intervals_wrapper))
