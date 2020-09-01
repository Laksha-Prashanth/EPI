import heapq
from typing import Iterator, List

from test_framework import generic_test


def online_median(sequence: Iterator[int]) -> List[float]:
    # TODO - you fill in here.
    arr = list(sequence)
    if not arr:
        return []
    left = [-arr[0]]
    right = []
    count = 1
    result = [arr[0]]

    for e in arr[1:]:
        if e <= -left[0] or not right or e < right[0]:
            heapq.heappush(left,-e)
        else:
            heapq.heappush(right,e)
        count += 1
        if len(right) > len(left):
            heapq.heappush(left,-heapq.heappop(right))
        elif len(left) > len(right) + 1:
            heapq.heappush(right, -heapq.heappop(left))
        
        #median
        if count % 2:
            result.append(-left[0])
        else:
            result.append((-left[0]+right[0])/2)

    return result


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
