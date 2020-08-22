from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    # TODO - you fill in here.
    head = None
    if not L1:
        return L2
    if not L2:
        return L1
    if L1.data  < L2.data:
        head = L1
    else:
        head = L2
    i = head
    while L1 and L2:
        if L1.data < L2.data:
            t = L1
            L1 = L1.next
        else:
            t = L2
            L2 = L2.next
        i.next = t
        i = i.next
    if L1:
        i.next = L1
    if L2:
        i.next = L2
    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
