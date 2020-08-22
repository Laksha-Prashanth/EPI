from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    # TODO - you fill in here.
    dummy = ListNode(0,L)
    prev = dummy
    for _ in range(start-1):
        prev = prev.next
    
    curr = prev.next

    while start < finish and curr and curr.next:
        t = curr.next
        curr.next = t.next
        t.next = prev.next
        prev.next = t
        start += 1
    
    return dummy.next
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
