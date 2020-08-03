from test_framework import generic_test


table = {
    0:0,
    1:1,
    2:1,
    3:2,
    4:1,
    5:2,
    6:2,
    7:3
}

def count_bits(x: int) -> int:
    # TODO - you fill in here.
    count = 0
    while x:
        count += table[x&7]
        x = x >> 3
    return count


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
