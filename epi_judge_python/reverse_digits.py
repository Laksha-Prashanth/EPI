from test_framework import generic_test


def reverse(x: int) -> int:
    # TODO - you fill in here.
    negative = False
    if x < 0:
        x = -x
        negative = True

    result = 0
    while x:
        result = result*10 + x%10
        x = x//10
    if negative:
        result = -result
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
