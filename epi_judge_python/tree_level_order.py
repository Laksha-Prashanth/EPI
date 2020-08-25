from typing import List
from collections import deque

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    # TODO - you fill in here.
    if not tree:
        return []
    result = []
    q = deque()
    q.append(tree)

    while q:
        temp_q = deque()
        row = []

        while q:
            node = q.popleft()
            row.append(node.data)

            if node.left:
                temp_q.append(node.left)
            if node.right:
                temp_q.append(node.right)
        q = temp_q
        result.append(row)


    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
