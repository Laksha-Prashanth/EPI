from test_framework import generic_test


def is_palindrome(s: str) -> bool:
    # TODO - you fill in here.
    start = 0
    end = len(s)-1
    while start < end:
        while start<end and not s[start].isalnum():
            start += 1
        while start<end and not s[end].isalnum():
            end -= 1
        if s[start].isalpha() or s[end].isalpha():
            if s[start].upper() != s[end].upper():
                return False
        else:
            if s[start] != s[end]:
                return False
        start += 1
        end -= 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
