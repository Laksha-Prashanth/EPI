from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.

    def is_balanced_helper(tree: BinaryTreeNode):
        if not tree:
            return [0,True]
        left_tree = is_balanced_helper(tree.left)
        right_tree = is_balanced_helper(tree.right)

        if not left_tree[1] or not right_tree[1]:
            return [max(left_tree[0],right_tree[0])+1, False]
        if abs(left_tree[0]- right_tree[0]) > 1:
            return [max(left_tree[0], right_tree[0])+1, False]
        return [max(left_tree[0], right_tree[0])+1, True]
    return is_balanced_helper(tree)[1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
