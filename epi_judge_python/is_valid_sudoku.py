from typing import List

from test_framework import generic_test

def box_check_helper(sudoku: List[List[int]], x, y) -> bool:
    seen = set()
    for i in range(3):
        for j in range(3):
            element = sudoku[i+x][j+y]
            if element != 0:
                if element in seen:
                    return False
                seen.add(sudoku[i+x][j+y])
    return True

# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(sudoku: List[List[int]]) -> bool:
    # TODO - you fill in here.

    seen = set()

    #row
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] != 0:
                if sudoku[i][j] in seen:
                    return False
                seen.add(sudoku[i][j])
        seen = set()
    #column
    seen = set()
    for j in range(len(sudoku)):
        for i in range(len(sudoku[j])):
            if sudoku[i][j] != 0:
                if sudoku[i][j] in seen:
                    return False
                seen.add(sudoku[i][j])
        seen = set()
    
    #box
    for i in range(0,9,3):
        for j in range(0,9,3):
            if not box_check_helper(sudoku, i,j):
                    return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
