import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    # TODO - you fill in here.
    i = l0
    i_length = 0
    while i and i.next:
        i = i.next
        i_length += 1
    j = l1
    j_length = 0
    while j and j.next:
        j = j.next
        j_length += 1
    
    #no overlap
    if i is not j:
        return None

    i = l0
    for _ in range(i_length - j_length):
        i = i.next
    j = l1
    for _ in range(j_length - i_length):
        j = j.next
    
    while j is not i:
        j = j.next
        i = i.next
    return j


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
