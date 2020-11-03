from typing import List

from test_framework import generic_test

'''

hello world this is hello laksha world
0       1     2   3  4      5       6

""
0

hello world
0

max: 4

{
    hello: 0
    world: 1
    ...

}

'''
def find_nearest_repetition(paragraph: List[str]) -> int:
    '''
    >>> find_nearest_repetition("hello world this is hello laksha world".split())
    4

    >>> find_nearest_repetition("".split())
    -1

    >>> find_nearest_repetition("hello world".split())
    -1
    >>> find_nearest_repetition("hello hello".split())
    1
    >>> find_nearest_repetition("hello hello world".split())
    1
    >>> find_nearest_repetition("hello world hello".split())
    1

    '''
    # TODO - you fill in here.
    table = {}
    nearest_repetition = float('inf')
    for i,word in enumerate(paragraph):
        if word in table:
            nearest_repetition = min(nearest_repetition, i-table[word])
        table[word] = i


    return nearest_repetition if nearest_repetition != float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
