import sys
from list_node import ListNode
from test_framework import generic_test



def is_linked_list_a_palindrome(L: ListNode) -> bool:
    # TODO - you fill in here.
    def palindrome_helper(L,head):
        if not L.next:
            if head is L:
                return head
            if head.data == L.data:
                return head.next
            else:
                return None
        else:
            t = palindrome_helper(L.next, head)
            if t == None:
                return None
            if t is L:
                return t.next
            if t.data == L.data:
                if not t.next:
                    return t
                return t.next
            else:
                return None

    if not L:
        return True
    if palindrome_helper(L,L):
        return True

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
