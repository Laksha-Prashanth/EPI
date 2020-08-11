from test_framework import generic_test

def char_to_num(c:chr) -> int:
    if c >= '0' and c <= '9':
        return ord(c) - ord('0')
    return ord(c) - ord('A') + 10


def convert_base(num: str, b1: int, b2: int) -> str:
    # TODO - you fill in here.
    # to decimal
    negative = False
    if num[0] == '-':
        negative = True
        num = num[1:]
    if num[0] == '+':
        num = num[1:]

    decimal = 0
    power = 0
    for c in num[::-1]:
        decimal = decimal + (char_to_num(c))*(b1**power)
        power+=1
    
    result = []
    while decimal:
        rem = decimal % b2
        if rem > 9:
            result.append(chr(rem-10+ord('A')))
        else:
            result.append(rem)
        decimal = decimal//b2

    if negative:
        result.append('-')
    if not result:
        return "0"
    return "".join(str(i) for i in result[::-1])



if __name__ == '__main__':
    print(convert_base("4B5C",14,5))
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
