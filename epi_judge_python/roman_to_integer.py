from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    # TODO - you fill in here.
    t = {'I':1, 'V':5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i,c in enumerate(s):
        result += t[c]
        if i > 0 and t[c] > t[s[i-1]]:
            result -= t[s[i-1]]*2


    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
