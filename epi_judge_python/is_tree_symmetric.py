from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    if not tree:
        return True
    def is_symmetric_helper(left: BinaryTreeNode, right: BinaryTreeNode) -> bool:
        if not left and not right:
            return True

        if left and right:
            if left.data == right.data:
                return is_symmetric_helper(left.right, right.left) and is_symmetric_helper(left.left, right.right)
            else:
                return False
        else:
            return False
        
    return is_symmetric_helper(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
