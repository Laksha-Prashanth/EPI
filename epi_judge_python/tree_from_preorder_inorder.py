from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    # TODO - you fill in here.
    if not inorder:
        return None
    if len(inorder) == 1:
        return BinaryTreeNode(inorder[0])
    
    node = BinaryTreeNode(preorder[0])
    num_left_nodes = inorder.index(preorder[0])

    node.left = binary_tree_from_preorder_inorder(preorder[1:num_left_nodes+1], inorder[:num_left_nodes])
    node.right = binary_tree_from_preorder_inorder(preorder[1+num_left_nodes:],inorder[num_left_nodes+1:])

    return node


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
