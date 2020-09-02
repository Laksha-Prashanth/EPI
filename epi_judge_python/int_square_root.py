from test_framework import generic_test


def square_root(k: int) -> int:
    # TODO - you fill in here.
    left = 0
    right = k
    result = left
    while left <= right:
        mid = (left+right)//2
        if mid*mid <= k:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
