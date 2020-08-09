from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(matrix: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
    if not matrix:
        return []
    start = 0
    result = []
    size = len(matrix)*len(matrix[0])
    while len(result) < size:

        #->
        for j in range(start,len(matrix[0])-start):
            result.append(matrix[start][j])
        if len(result) >= size:
            break
        for i in range(start+1,len(matrix)-start):
            result.append(matrix[i][len(matrix)-1-start])
        if len(result) >= size:
            break
        for j in range(len(matrix[0])-2-start,start-1,-1):
            result.append(matrix[len(matrix)-1-start][j])
        if len(result) >= size:
            break
        for i in range(len(matrix)-2-start,start,-1):
            result.append(matrix[i][start])
        if len(result) >= size:
            break
        start += 1

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
