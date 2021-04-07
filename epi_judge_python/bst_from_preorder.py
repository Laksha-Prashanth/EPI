from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test

'''
            50
    20              70
10      30      60      80

preorder: 50, 20, 10, 30, 70, 60, 80
                50
    [20,10,30]  [70,60,80]
        20          70
    10      30     60   80 

time:
    N 
space:
    O(N)
    O(h)
'''
def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:
    # TODO - you fill in here.
    return None


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
