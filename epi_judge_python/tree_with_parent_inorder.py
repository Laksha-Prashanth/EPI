from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    # TODO - you fill in here.
    result = []
    i = tree
    prev = None
    while i:
        if prev is i.parent:
            prev = i
            #go left
            if i.left:
                i = i.left
            else:
                result.append(i.data)
                if i.right:
                    i = i.right
                else:
                    i = i.parent
        elif prev is i.left and i.left:
            result.append(i.data)
            prev = i
            if i.right:
                i = i.right
            else:
                i = i.parent
        else:
            prev = i
            i = i.parent
            

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
