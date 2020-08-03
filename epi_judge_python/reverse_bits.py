from test_framework import generic_test

def reverseBit(x: int) -> int:
    y = 0
    for i in range(16):
        y = y<<1
        y = y | (x&1)
        x = x >> 1
    return y
def createLookupTable(n: int) -> dict:
    table = {}
    for i in range(n):
        table[i] = reverseBit(i)
    return table
table = createLookupTable(0b1111111111111111)


def reverse_bits(x: int) -> int:
    # TODO - you fill in here.
    result = 0
    for i in range(4):
        result = result<<16
        result = result | table[x&0b1111111111111111]
        x = x>>16
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
