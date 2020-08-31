from typing import List
import heapq

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
    heap = []
    heapq.heapify(heap)
    for i,element in enumerate(sorted_arrays):
        heapq.heappush(heap, [element[0],i,0])
    
    result = []
    empty = 0
    while empty < len(sorted_arrays):
        t = heapq.heappop(heap)
        result.append(t[0])
        if t[2] < len(sorted_arrays[t[1]])-1:
            a = sorted_arrays[t[1]][t[2]+1]
            heapq.heappush(heap,[a,t[1],t[2]+1])
        else:
            empty += 1
    
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
