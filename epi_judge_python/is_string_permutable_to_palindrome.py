from test_framework import generic_test

'''
fff
True

hello
False

edifie
False

edified
True

Edified

edifie
diefei

table{
    d: 2
    i: 2
    e: 2
    f: 1
}

'''
def can_form_palindrome(s: str) -> bool:
    '''
    >>> can_form_palindrome('fff')
    True
    >>> can_form_palindrome('edified')
    True

    '''
    table = dict()
    for character in s:
        if character not in table:
            table[character] = 0
        table[character] += 1
    
    flag = False
    for key in table:
        if table[key] %2:
            if flag:
                return False
            flag = True

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
