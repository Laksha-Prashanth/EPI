import collections
import functools
from typing import List
from collections import deque

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


'''
[9,11] [10,12] [12,4] [1,2] [1,3] [2,5] [6,7]
4

'''

def find_max_simultaneous_events(A: List[Event]) -> int:
    # TODO - you fill in here.

    endpoints = []
    for event in A:
        endpoints.append([event[0], True])
        endpoints.append([event[1],False])
    
    endpoints.sort(key = lambda x: [x[0], not x[1]])
    count = 0
    result = 0
    for point in endpoints:
        if point[1]:
            count += 1
        else:
            count -= 1
        result = max(result, count)


    return result


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
