import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

'''
            5
        4       -1
    2       3   4   29
0

        1
    2       3
4
{4, -1, 5}

lca(0,,3)

lca(2,4)
5

lca(None, 4)
None

'''
def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:

    if not node1 or not node0:
        return None

    if node0 is node1:
        return node0

    parent_set = set([node0,node1])
    i = node0
    j = node1

    while i or j:
        if i:
            if i.parent in parent_set:
                return i.parent
            parent_set.add(i.parent)
            i = i.parent
        if j:
            if j.parent in parent_set:
                return j.parent
            parent_set.add(j.parent)
            j = j.parent

    return None


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'lowest_common_ancestor_close_ancestor.py',
            'lowest_common_ancestor.tsv', lca_wrapper))
