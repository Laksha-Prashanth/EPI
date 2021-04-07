from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils

'''
[80, 70]
            50
    20              70
10      40      60      80
result = [80, 70, 60]
(50, 3)
    (70,3)
        (80,3)
        (60, 3)
        

'''
def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    # TODO - you fill in here.
    result = []
    def helper(tree: BstNode, result: List[int], k: int) -> None:
        if not tree:
            return
        if len(result) >= k:
            return
        
        # check right
        if len(result) < k:
            helper(tree.right, result, k)
        if len(result) < k:
            result.append(tree.data)
        if len(result) < k:
            helper(tree.left, result, k)
    
    helper(tree, result, k)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
