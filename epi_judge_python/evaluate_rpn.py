from test_framework import generic_test


def evaluate(expression: str) -> int:
    # TODO - you fill in here.
    stack = []
    for c in expression.split(','):
        if c == '+' or c == '-' or c == '*' or c == '/':
            #do something
            b = stack.pop()
            a = stack.pop()
            if c == '+':
                stack.append(a+b)
            elif c == '-':
                stack.append(a-b)
            elif c == '*':
                stack.append(a*b)
            elif c == '/':
                stack.append(a//b)
        else:
            stack.append(float(c))

    return stack.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
