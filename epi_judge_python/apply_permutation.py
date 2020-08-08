from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    # TODO - you fill in here.
    i = 0
    while i < len(perm):
        actual = A[i]
        j = i
        while perm[j] != -1:
            goal = perm[j]
            t = A[goal]
            A[goal] = actual
            actual = t
            perm[j] = -1
            j = goal
        i += 1

    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
