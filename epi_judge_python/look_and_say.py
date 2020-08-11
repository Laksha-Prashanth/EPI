from test_framework import generic_test


def look_and_say(n: int) -> str:
    # TODO - you fill in here.
    num = "1"
    for i in range(n-1):
        result = ""
        curr = num[0]
        j = 0
        while j < len(num):
            count = 0
            while j < len(num) and num[j] == curr:
                count += 1
                j += 1
            result = result + str(count) + curr
            curr = num[j] if j < len(num) else ""
        num = result
    return num


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
