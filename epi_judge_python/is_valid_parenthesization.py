from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    # TODO - you fill in here.
    stack = []
    for c in s:
        if c == '{' or c == '[' or c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            t = stack.pop()
            if t == '(' and c == ')':
                continue
            elif t == '{' and c == '}':
                continue
            elif t == '[' and c == ']':
                continue
            else:
                return False
    if len(stack) > 0:
        return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
