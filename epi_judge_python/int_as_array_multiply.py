from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    # TODO - you fill in here.
    if (num1[0] < 0) ^ (num2[0]<0):
        negative = True
    else:
        negative = False
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])

    num1.reverse()
    num2.reverse()

    result = [0]
    carry = 0

    for i in range(len(num1)):
        for j in range(len(num2)):
            n = num2[j]*num1[i] + carry
            while len(result) <= i+j:
                result.append(0)
            n += result[i+j]
            result[i+j] = n%10
            carry = n//10 + result[i+j]//10
        if carry:
            result.append(carry)
            carry = 0


    if negative:
        result[-1] = -result[-1]
    
    for i in result:
        if i != 0:
            return result[::-1]

    return [0]


if __name__ == '__main__':
    print(multiply([1,2,3],[9,7,8]))
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
