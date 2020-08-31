import heapq
from typing import Iterator, List

from test_framework import generic_test


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    # TODO - you fill in here.
    l = [i for i in sequence]
    heap = []
    heapq.heapify(heap)
    i = 0
    while i < k:
        heapq.heappush(heap, l[i])
        i += 1
    
    
    result = []

    while i < len(l):
        result.append(heapq.heappop(heap))
        heapq.heappush(heap, l[i])
        i += 1

    while heap:
        result.append(heapq.heappop(heap))

    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
