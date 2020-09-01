import heapq
from typing import List

from test_framework import generic_test, test_utils


def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    # TODO - you fill in here.
    heap = []
    heapq.heappush(heap, [-A[0], 0])
    result = []
    for _ in range(k):
        curr = heapq.heappop(heap)
        result.append(-curr[0])

        if curr[1]*2+1 < len(A):
            heapq.heappush(heap, [-A[curr[1]*2+1], curr[1]*2+1])
        if curr[1]*2+2 < len(A):
            heapq.heappush(heap, [-A[curr[1]*2+2], curr[1]*2+2])

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
