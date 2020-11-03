from test_framework import generic_test

'''
hello world, hello world this is laksha
True

hello world, hello word this is akshal
True

hello world, laksha
False


1. hash table
    process letter      O(N)
    process magazine    O(M)
time: O(M+N)
space: O(N)

2. count number of 'a's in letter           26*O(N)
    check if magazine has >= # of 'a's      26*O(M)
time: O(M+N)
space: O(1)


'''
def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    '''
    >>> is_letter_constructible_from_magazine('hello world', 'hello world this is laksha')
    True

    >>> is_letter_constructible_from_magazine('hello world', 'hello word this is akshal')
    True

    >>> is_letter_constructible_from_magazine('hello world', 'laksha')
    False

    '''

    table = dict()
    for character in letter_text:
        if character not in table:
            table[character] = 0
        table[character] += 1

    for character in magazine_text:
        if character in table:
            table[character] -= 1
    
    for key in table:
        if table[key] > 0:
            return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
