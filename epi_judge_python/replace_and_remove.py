import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    # TODO - you fill in here.
    b_count = sum([1 if c == 'b' else 0 for c in s[:size]])
    i = 0
    start = 0
    while start < size - b_count:
        while s[i] == 'b':
            i += 1
        s[start] = s[i]
        start += 1
        i += 1
    size -= b_count

    #replace a with dd
    a_count = sum([1 if c == 'a' else 0 for c in s[:size]])
    new_size = size+a_count
    size -= 1
    i = size
    size += a_count
    
    while i >=0:
        if s[i] == 'a':
            s[size] = 'd'
            s[size-1] = 'd'
            size -= 2
        else:
            s[size] = s[i]
            size -= 1
        i -= 1


    return new_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
