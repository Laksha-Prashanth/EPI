from typing import List
import math

from test_framework import generic_test

'''
0+0 1+0 0+1 2+0 1+1
1+1 2.414
2+0

a+b

a+1 + b   a+2+b  a+3+b ...       a + b+1

  + 99
  + 100
'''
def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
    # TODO - you fill in here.
    i = 0
    j = 0
    result = [[0.0,0.0]]
    answer = []
    while len(result) < k:
        i_plus_1 = float(result[i][0] + 1) + result[i][1]*math.sqrt(2)
        j_plus_2 = float(result[j][0] + (result[j][1]+1)*math.sqrt(2))
        if i_plus_1 < j_plus_2:
            result.append([result[i][0]+1, result[i][1]])
        else:
            result.append([result[j][0], result[j][1]+1])

        if i_plus_1 <= j_plus_2:
            i += 1
        if j_plus_2 <= i_plus_1:
            j += 1

    return [a+b*math.sqrt(2) for a,b in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('a_b_sqrt2.py', 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
