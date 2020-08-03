from test_framework import generic_test


def power(x: float, y: int) -> float:
    if y < 0:
        y = -y
        x = 1/x

    power = x
    result = 1
    while y:
        if y &1:
            result = result*power
        power = power*power
        y = y>>1

    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
